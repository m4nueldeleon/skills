import test from 'node:test';
import assert from 'node:assert/strict';
import { adaptarSubtitulos, crearMapa, esquemaPlan, esquemaTranscripcion, silenciosDesdeLog, validarTranscripcion } from '../scripts/tiempos.mjs';

test('recorta pausas conservando respiración y reordena un gancho', () => {
  const silencios = silenciosDesdeLog('silence_start: 1\nsilence_end: 3\nsilence_start: 5', 6);
  assert.deepEqual(silencios, [{ start: 1, end: 3 }, { start: 5, end: 6 }]);
  const mapa = crearMapa([{ start: 3, end: 6 }, { start: 0, end: 1 }], silencios, 0.1, 6);
  assert.equal(mapa[0].start, 3);
  assert.ok(Math.abs(mapa[0].end - 5.1) < 0.001);
  assert.ok(Math.abs(mapa[1].output_start - 2.1) < 0.001);
});

test('subtítulos siguen el orden del video editado y no el del crudo', () => {
  const texto = { segments: [{ start: 0, end: 1, text: 'primero' }, { start: 3, end: 4, text: 'gancho' }] };
  const mapa = crearMapa([{ start: 3, end: 4 }, { start: 0, end: 1 }], [], 0);
  assert.deepEqual(adaptarSubtitulos(texto, mapa), [{ text: 'gancho', start: 0, end: 1 }, { text: 'primero', start: 1, end: 2 }]);
});

test('rechaza JSONs con números imposibles o texto fuera de tiempo', () => {
  assert.throws(() => esquemaPlan.parse({ segments: [{ start: 5, end: 1 }] }));
  assert.throws(() => esquemaTranscripcion.parse({ segments: [{ start: -1, end: 1, text: 'hola' }] }));
  assert.throws(() => validarTranscripcion({ segments: [{ start: 0, end: 20, text: 'hola' }] }, 10));
});

test('un video de puro silencio pide revisar el audio', () => {
  assert.throws(() => crearMapa([{ start: 0, end: 6 }], [{ start: 0, end: 6 }], 0));
});

test('tolera palabras Whisper solapadas sin acumular desfase en los subtítulos', () => {
  const texto = { segments: [{ start: 0, end: 2, text: 'Tres frases.', words: [
    { start: 0, end: 1, word: 'Esta primera frase ocupa un subtítulo completo.' },
    { start: 0.96, end: 1.5, word: 'Esta segunda frase también ocupa otro subtítulo.' },
    { start: 1.46, end: 2, word: 'Esta tercera frase termina exactamente al final.' },
  ] }] };
  validarTranscripcion(texto, 2);
  const mapa = crearMapa([{ start: 0, end: 2 }], [], 0);
  const subtitulos = adaptarSubtitulos(texto, mapa);
  assert.equal(subtitulos.length, 3);
  let reloj = 0;
  let duracionCapa = 0;
  for (const subtitulo of subtitulos) {
    assert.ok(subtitulo.start >= reloj);
    duracionCapa += Math.max(0, subtitulo.start - reloj) + subtitulo.end - subtitulo.start;
    reloj = subtitulo.end;
  }
  assert.ok(Math.abs(duracionCapa - 2) < 0.000001);
});
