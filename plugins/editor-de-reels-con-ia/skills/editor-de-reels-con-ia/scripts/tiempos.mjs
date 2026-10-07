import { z } from 'zod';

const tiempo = z.number().finite().min(0).max(900);
export const intervalo = z.object({ start: tiempo, end: tiempo }).refine((dato) => dato.end > dato.start, 'end debe ser mayor que start.');
const palabra = z.object({ start: tiempo, end: tiempo, word: z.string().trim().min(1).max(100) });
const segmento = z.object({ start: tiempo, end: tiempo, text: z.string().trim().min(1).max(2000), words: z.array(palabra).max(500).optional() });
export const esquemaTranscripcion = z.object({ segments: z.array(segmento).min(1).max(2000) });
export const esquemaPlan = z.object({ segments: z.array(intervalo).min(1).max(120) });

export function silenciosDesdeLog(log, duracion) {
  const eventos = [...log.matchAll(/silence_(start|end):\s*([0-9.]+)/g)];
  let comienzo = null;
  const silencios = [];
  for (const evento of eventos) {
    const instante = Math.min(duracion, Number(evento[2]));
    if (evento[1] === 'start') comienzo = instante;
    if (evento[1] === 'end' && comienzo !== null) {
      silencios.push({ start: comienzo, end: instante });
      comienzo = null;
    }
  }
  if (comienzo !== null) silencios.push({ start: comienzo, end: duracion });
  return silencios;
}

function restarIntervalo(segmentos, corte) {
  return segmentos.flatMap((tramo) => {
    if (corte.end <= tramo.start || corte.start >= tramo.end) return [tramo];
    return [
      { start: tramo.start, end: Math.min(tramo.end, corte.start) },
      { start: Math.max(tramo.start, corte.end), end: tramo.end },
    ].filter((pieza) => pieza.end - pieza.start >= 0.08);
  });
}

export function crearMapa(seleccion, silencios, margen, duracion = Infinity) {
  const cortes = silencios.map((s) => ({ start: s.start <= 0 ? 0 : s.start + margen, end: s.end >= duracion ? duracion : s.end - margen }))
    .filter((s) => s.end > s.start);
  const tramos = seleccion.flatMap((tramo) => cortes.reduce(restarIntervalo, [tramo]))
    .map((tramo) => ({ start: Math.round(tramo.start * 30) / 30, end: Math.round(tramo.end * 30) / 30 }))
    .filter((tramo) => tramo.end - tramo.start >= 0.08);
  if (!tramos.length) throw new Error('Solo se detectó silencio. Revisa el audio o usa --keep-silence.');
  if (tramos.length > 240) throw new Error('Hay más de 240 cortes. Divide el video o aumenta --pause.');
  let reloj = 0;
  return tramos.map((tramo) => {
    const nuevo = { ...tramo, output_start: reloj, output_end: reloj + tramo.end - tramo.start };
    reloj = nuevo.output_end;
    return nuevo;
  });
}

export function validarTranscripcion(transcripcion, duracion) {
  let anterior = -1;
  for (const segmento of transcripcion.segments) {
    if (segmento.end <= segmento.start || segmento.start < anterior || segmento.end > duracion + 0.25) {
      throw new Error('Los segmentos deben estar ordenados, sin traslaparse y dentro del video.');
    }
    anterior = segmento.end;
    let palabraAnterior = segmento.start - 0.05;
    for (const palabra of segmento.words ?? []) {
      if (palabra.end <= palabra.start || palabra.start < palabraAnterior - 0.05 || palabra.end > segmento.end + 0.25) {
        throw new Error('Revisa los tiempos de las palabras en la transcripción.');
      }
      palabraAnterior = palabra.end;
    }
  }
}

function unidadesSubtitulos(segmento) {
  if (segmento.words?.length) return segmento.words.map((p) => ({ start: p.start, end: p.end, text: p.word }));
  return [{ start: segmento.start, end: segmento.end, text: segmento.text }];
}

export function adaptarSubtitulos(transcripcion, mapa) {
  const unidades = transcripcion.segments.flatMap(unidadesSubtitulos);
  const grupos = mapa.flatMap((tramo) => {
    const visibles = unidades.flatMap((unidad) => {
      const start = Math.max(unidad.start, tramo.start);
      const end = Math.min(unidad.end, tramo.end);
      if (end - start < 0.04) return [];
      return [{ text: unidad.text, start: tramo.output_start + start - tramo.start, end: tramo.output_start + end - tramo.start }];
    });
    return agrupar(visibles);
  });
  return grupos.map((grupo, indice) => ({
    ...grupo,
    end: Math.min(grupo.end, grupos[indice + 1]?.start ?? Infinity),
  })).filter((grupo) => grupo.end - grupo.start >= 0.01);
}

function agrupar(unidades) {
  return unidades.reduce((grupos, unidad) => {
    const anterior = grupos.at(-1);
    if (anterior && anterior.text.length + unidad.text.length < 42 && unidad.end - anterior.start < 2.2 && unidad.start - anterior.end < 0.25) {
      return [...grupos.slice(0, -1), { ...anterior, text: `${anterior.text} ${unidad.text}`, end: unidad.end }];
    }
    return [...grupos, unidad];
  }, []);
}

function marca(segundos) {
  const ms = Math.round(segundos * 1000);
  const parte = (numero, ancho = 2) => String(numero).padStart(ancho, '0');
  return `${parte(Math.floor(ms / 3600000))}:${parte(Math.floor(ms / 60000) % 60)}:${parte(Math.floor(ms / 1000) % 60)},${parte(ms % 1000, 3)}`;
}

export const crearSrt = (subtitulos) => subtitulos.map((s, i) => `${i + 1}\n${marca(s.start)} --> ${marca(s.end)}\n${s.text}\n`).join('\n');
