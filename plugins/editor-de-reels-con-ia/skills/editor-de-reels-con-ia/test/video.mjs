import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { mkdtemp, readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import sharp from 'sharp';
import { ejecutar, ffmpeg, inspeccionar } from '../scripts/archivos.mjs';

const temporal = await mkdtemp(path.join(os.tmpdir(), 'prueba-editor-'));
const entrada = path.join(temporal, 'crudo con espacios.mp4');
const hash = async (archivo) => createHash('sha256').update(await readFile(archivo)).digest('hex');
const node = (archivo, args) => ejecutar(process.execPath, [archivo, ...args]);

try {
  await ffmpeg(['-v', 'error', '-f', 'lavfi', '-i', 'testsrc2=size=640x360:rate=30:duration=6', '-f', 'lavfi', '-i', "aevalsrc='if(between(t,0.5,1.8)+between(t,3.5,5.5),0.15*sin(2*PI*440*t),0)':s=48000:d=6", '-c:v', 'libx264', '-preset', 'ultrafast', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-shortest', entrada]);
  const original = await hash(entrada);
  const baseArgs = ['--input', entrada, '--transcript', 'examples/transcripcion.json'];
  const vertical = path.join(temporal, 'vertical.mp4');
  await node('scripts/editar.mjs', [...baseArgs, '--output', vertical, '--motion', '--noise-reduction']);
  const v = await inspeccionar(vertical);
  assert.deepEqual([v.ancho, v.alto], [720, 1280]);
  assert.ok(v.duracion < 5 && v.duracion > 3, `Duración tras corte: ${v.duracion}`);
  const srt = await readFile(vertical.replace('.mp4', '.srt'), 'utf8');
  assert.match(srt, /Tu tiempo vale más/);
  assert.match(srt, /Empieza con una tarea repetitiva/);
  const audio = await ffmpeg(['-v', 'info', '-i', vertical, '-af', 'volumedetect', '-f', 'null', '-']);
  const pico = Number(audio.error.match(/max_volume:\s*([-\d.]+) dB/u)?.[1]);
  assert.ok(Number.isFinite(pico) && pico < 0, `Pico de audio: ${pico}`);
  const horizontal = path.join(temporal, 'horizontal.mp4');
  await node('scripts/editar.mjs', [...baseArgs, '--output', horizontal, '--format', 'horizontal', '--framing', 'crop', '--plan', 'examples/plan.json', '--keep-silence']);
  const h = await inspeccionar(horizontal);
  assert.deepEqual([h.ancho, h.alto], [1280, 720]);
  const plan = JSON.parse(await readFile(horizontal.replace('.mp4', '.plan.json'), 'utf8'));
  assert.match(plan.captions[0].text, /Empieza/);
  await assert.rejects(node('scripts/editar.mjs', [...baseArgs, '--output', entrada]), /Ya existe|diferentes/u);
  await assert.rejects(node('scripts/editar.mjs', [...baseArgs, '--output', vertical]), /Ya existe/u);
  await assert.rejects(node('scripts/editar.mjs', [...baseArgs, '--output', path.join(temporal, 'invalido.mp4'), '--threshold=1;touch']), /number|NaN/u);
  const imagen = path.join(temporal, 'apoyo.png');
  await sharp({ create: { width: 640, height: 360, channels: 3, background: '#C1FF33' } }).png().toFile(imagen);
  const broll = path.join(temporal, 'broll.mp4');
  await node('scripts/broll.mjs', ['--input', entrada, '--image', imagen, '--from', '2', '--to', '3', '--output', broll]);
  const b = await inspeccionar(broll);
  assert.ok(Math.abs(b.duracion - 6) < 0.2);
  assert.equal(await hash(entrada), original);
  const resumen = { ok: true, vertical: v, horizontal: h, broll: b, audio_peak_db: pico, raw_unchanged: true, overwrite_rejected: true, unsafe_option_rejected: true };
  await writeFile(path.join(temporal, 'resultado.json'), JSON.stringify(resumen, null, 2));
  console.log(JSON.stringify({ ...resumen, artifacts: temporal }, null, 2));
} catch (error) {
  console.error(`Falló prueba funcional; artefactos en ${temporal}`);
  throw error;
}
