import { parseArgs } from 'node:util';
import path from 'node:path';
import { rm, writeFile } from 'node:fs/promises';
import sharp from 'sharp';
import { z } from 'zod';
import { archivoLocal, ffmpeg, inspeccionar, prepararSalida, publicar } from './archivos.mjs';

const esquema = z.object({
  input: z.string().min(1), image: z.string().min(1), output: z.string().min(1),
  from: z.coerce.number().finite().min(0).max(900),
  to: z.coerce.number().finite().min(0).max(900),
}).refine((dato) => dato.to > dato.from, '--to debe ser mayor que --from.');

async function insertar(opciones) {
  const entrada = await archivoLocal(opciones.input);
  const imagen = await archivoLocal(opciones.image, ['.png', '.jpg', '.jpeg', '.webp']);
  const video = await inspeccionar(entrada);
  if (opciones.to > video.duracion) throw new Error('La imagen debe aparecer dentro de la duración del video.');
  if (Math.max(video.ancho, video.alto) > 3840) throw new Error('Usa un video con resolución máxima de 3840 px.');
  const { temporal, destinos } = await prepararSalida(opciones.output, entrada, ['.mp4']);
  try {
    const ancho = Math.floor(video.ancho / 2) * 2;
    const alto = Math.floor(video.alto / 2) * 2;
    const imagenLista = path.join(temporal, 'imagen.png');
    await sharp(imagen, { limitInputPixels: 40_000_000 }).rotate().resize(ancho, alto, { fit: 'cover' }).png().toFile(imagenLista);
    const filtro = `[0:v]scale=${ancho}:${alto},setsar=1[v];[1:v]format=rgba[imagen];[v][imagen]overlay=eof_action=repeat:enable='gte(t,${opciones.from})*lt(t,${opciones.to})',format=yuv420p[final]`;
    await writeFile(path.join(temporal, 'broll.txt'), filtro);
    const final = path.join(temporal, 'final.mp4');
    await ffmpeg(['-v', 'warning', '-protocol_whitelist', 'file,pipe', '-i', entrada, '-i', imagenLista, '-filter_complex_script', 'broll.txt', '-map', '[final]', '-map', '0:a:0', '-t', String(video.duracion), '-c:v', 'libx264', '-preset', 'fast', '-crf', '20', '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', '-map_metadata', '-1', final], { cwd: temporal });
    const resultado = await inspeccionar(final);
    if (Math.abs(resultado.duracion - video.duracion) > 0.2) throw new Error('El video cambió de duración. No se publicó la salida.');
    await publicar([final], destinos);
    console.log(`Imagen insertada de ${opciones.from} a ${opciones.to} s: ${destinos[0]}`);
  } finally {
    await rm(temporal, { recursive: true, force: true });
  }
}

try {
  const { values } = parseArgs({ options: {
    input: { type: 'string' }, image: { type: 'string' }, output: { type: 'string' },
    from: { type: 'string' }, to: { type: 'string' }, help: { type: 'boolean', default: false },
  }, strict: true, allowPositionals: false });
  if (values.help) console.log('Uso: node scripts/broll.mjs --input "crudo.mp4" --image "apoyo.png" --from 3 --to 6 --output "con-imagen.mp4"\nLa imagen cubre el video durante ese intervalo y conserva su audio. Úsalo antes de generar los subtítulos.');
  else await insertar(esquema.parse(values));
} catch (error) {
  console.error(`No se pudo insertar la imagen: ${error.message}`);
  process.exitCode = 1;
}
