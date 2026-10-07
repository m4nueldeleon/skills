import { parseArgs } from 'node:util';
import path from 'node:path';
import { rm, writeFile } from 'node:fs/promises';
import { z } from 'zod';
import { archivoLocal, ffmpeg, inspeccionar, leerJson, prepararSalida, publicar } from './archivos.mjs';
import { adaptarSubtitulos, crearMapa, crearSrt, esquemaPlan, esquemaTranscripcion, silenciosDesdeLog, validarTranscripcion } from './tiempos.mjs';
import { crearCapa } from './subtitulos.mjs';
import { renderizar } from './render.mjs';

const definiciones = {
  input: { type: 'string' }, transcript: { type: 'string' }, output: { type: 'string' },
  plan: { type: 'string' }, format: { type: 'string', default: 'vertical' },
  quality: { type: 'string', default: 'standard' }, framing: { type: 'string', default: 'blur' },
  threshold: { type: 'string', default: '-35' }, pause: { type: 'string', default: '0.55' },
  padding: { type: 'string', default: '0.12' }, from: { type: 'string', default: '0' },
  to: { type: 'string' }, motion: { type: 'boolean', default: false },
  'keep-silence': { type: 'boolean', default: false }, 'noise-reduction': { type: 'boolean', default: false },
  help: { type: 'boolean', default: false },
};
const numero = (min, max) => z.coerce.number().finite().min(min).max(max);
const esquema = z.object({
  input: z.string().min(1), transcript: z.string().min(1), output: z.string().min(1),
  plan: z.string().optional(), format: z.enum(['vertical', 'horizontal']),
  quality: z.enum(['standard', 'hd']), framing: z.enum(['blur', 'crop']),
  threshold: numero(-60, -15), pause: numero(0.2, 5), padding: numero(0, 0.5),
  from: numero(0, 900), to: numero(0, 900).optional(), motion: z.boolean(),
  'keep-silence': z.boolean(), 'noise-reduction': z.boolean(), help: z.boolean(),
});

function ayuda() {
  console.log('Uso: node scripts/editar.mjs --input "crudo.mp4" --transcript "crudo.json" --output "salida/reel.mp4"\nOpciones: --format vertical|horizontal --quality standard|hd --framing blur|crop --motion --noise-reduction --keep-silence --from 0 --to 60 --plan plan.json --threshold=-35 --pause 0.55 --padding 0.12\nLee README.md antes de la primera edición.');
}

function seleccionTemporal(opciones, plan, duracion) {
  if (plan && (opciones.from !== 0 || opciones.to !== undefined)) throw new Error('Usa --plan o --from/--to, sin combinarlos.');
  const seleccion = plan?.segments ?? [{ start: opciones.from, end: opciones.to ?? duracion }];
  if (seleccion.some((s) => s.end > duracion + 0.001 || s.end - s.start < 0.1)) throw new Error('La selección debe estar dentro del video y cada tramo durar al menos 0.1 s.');
  if (seleccion.reduce((total, s) => total + s.end - s.start, 0) > 900) throw new Error('La selección supera 15 minutos.');
  return seleccion;
}

async function editar(opciones) {
  const entrada = await archivoLocal(opciones.input);
  const datos = await inspeccionar(entrada);
  const transcripcion = await leerJson(opciones.transcript, esquemaTranscripcion);
  validarTranscripcion(transcripcion, datos.duracion);
  const plan = opciones.plan ? await leerJson(opciones.plan, esquemaPlan) : null;
  const seleccion = seleccionTemporal(opciones, plan, datos.duracion);
  const { temporal, destinos } = await prepararSalida(opciones.output, entrada);
  try {
    console.log('1/4 · Midiendo pausas del audio…');
    const analisis = opciones['keep-silence'] ? { error: '' } : await ffmpeg(['-v', 'info', '-protocol_whitelist', 'file,pipe', '-i', entrada, '-map', '0:a:0', '-af', `silencedetect=noise=${opciones.threshold}dB:d=${opciones.pause}`, '-f', 'null', '-']);
    const silencios = silenciosDesdeLog(analisis.error, datos.duracion);
    const mapa = crearMapa(seleccion, silencios, opciones.padding, datos.duracion);
    const duracionFinal = mapa.at(-1).output_end;
    const subtitulos = adaptarSubtitulos(transcripcion, mapa);
    if (!subtitulos.length) throw new Error('La selección no contiene subtítulos. Revisa sus tiempos.');
    const base = opciones.quality === 'hd' ? [1080, 1920] : [720, 1280];
    const [ancho, alto] = opciones.format === 'horizontal' ? [...base].reverse() : base;
    console.log('2/4 · Preparando subtítulos con los tiempos nuevos…');
    const capa = await crearCapa(subtitulos, duracionFinal, ancho, alto, temporal);
    console.log('3/4 · Exportando video, encuadre y audio…');
    const final = await renderizar({ entrada, mapa, capa, ancho, alto, opciones, temporal });
    console.log('4/4 · Verificando la exportación…');
    const resultado = await inspeccionar(final);
    if (resultado.ancho !== ancho || resultado.alto !== alto || Math.abs(resultado.duracion - duracionFinal) > 0.2) throw new Error('La exportación no pasó la verificación de tamaño o duración.');
    const srt = path.join(temporal, 'final.srt');
    const informe = path.join(temporal, 'final.plan.json');
    await writeFile(srt, crearSrt(subtitulos));
    await writeFile(informe, JSON.stringify({ version: 1, source_duration: datos.duracion, output_duration: resultado.duracion, size: { width: ancho, height: alto }, options: { format: opciones.format, framing: opciones.framing, motion: opciones.motion, silence_threshold_db: opciones.threshold, loudness_target_lufs: -16 }, silence_intervals: silencios, timeline: mapa, captions: subtitulos }, null, 2));
    await publicar([final, srt, informe], destinos);
    console.log(`Exportado: ${destinos[0]}\nOriginal: ${datos.duracion.toFixed(2)} s · Final: ${resultado.duracion.toFixed(2)} s\nRevisa el video completo antes de publicarlo.`);
  } finally {
    await rm(temporal, { recursive: true, force: true });
  }
}

try {
  const { values } = parseArgs({ options: definiciones, strict: true, allowPositionals: false });
  if (values.help) ayuda();
  else await editar(esquema.parse(values));
} catch (error) {
  console.error(`No se completó la edición: ${error.message}`);
  process.exitCode = 1;
}
