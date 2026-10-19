import test from 'node:test';
import assert from 'node:assert/strict';
import { opcionGrafo } from '../scripts/archivos.mjs';

// ffmpeg 9 quitó -filter_complex_script; desde ffmpeg 7 el grafo en archivo va con «-/filter_complex <archivo>».
test('ffmpeg 7 o más nuevo lee el grafo con -/filter_complex', () => {
  assert.equal(opcionGrafo('ffmpeg version 9.0.2 Copyright (c) 2000-2026'), '-/filter_complex');
  assert.equal(opcionGrafo('ffmpeg version 8.1.1 Copyright (c) 2000-2026'), '-/filter_complex');
  assert.equal(opcionGrafo('ffmpeg version n7.1 Copyright (c) 2000-2024'), '-/filter_complex');
  assert.equal(opcionGrafo('ffmpeg version 7.1-full_build-www.gyan.dev'), '-/filter_complex');
});

test('ffmpeg 4 a 6 (apt de Ubuntu, Debian) conserva -filter_complex_script', () => {
  assert.equal(opcionGrafo('ffmpeg version 4.4.2-0ubuntu0.22.04.1 Copyright (c) 2000-2021'), '-filter_complex_script');
  assert.equal(opcionGrafo('ffmpeg version 6.1.1-3ubuntu5 Copyright (c) 2000-2023'), '-filter_complex_script');
});

test('compilaciones nocturnas o con fecha se tratan como nuevas', () => {
  assert.equal(opcionGrafo('ffmpeg version N-118896-g7a1b2c3 Copyright (c) 2000-2026'), '-/filter_complex');
  assert.equal(opcionGrafo('ffmpeg version 2026-03-01-git-abc123-full_build-www.gyan.dev'), '-/filter_complex');
});
