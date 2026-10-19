import { spawn } from 'node:child_process';
import { constants } from 'node:fs';
import { copyFile, lstat, mkdir, mkdtemp, readFile, realpath, rm } from 'node:fs/promises';
import path from 'node:path';

const LIMITE_SALIDA = 4 * 1024 * 1024;
const LIMITE_JSON = 10 * 1024 * 1024;
const EXTENSIONES_VIDEO = ['.mp4', '.mov', '.m4v', '.mkv', '.webm', '.avi'];

export function ejecutar(programa, argumentos, opciones = {}) {
  return new Promise((resolver, rechazar) => {
    const proceso = spawn(programa, argumentos, { shell: false, windowsHide: true, ...opciones });
    let salida = '';
    let error = '';
    const reloj = setTimeout(() => proceso.kill('SIGTERM'), 30 * 60 * 1000);
    proceso.stdout.on('data', (dato) => { salida = (salida + dato).slice(-LIMITE_SALIDA); });
    proceso.stderr.on('data', (dato) => { error = (error + dato).slice(-LIMITE_SALIDA); });
    proceso.on('error', (causa) => {
      clearTimeout(reloj);
      rechazar(new Error(`No se pudo iniciar ${programa}. Comprueba su instalación. ${causa.message}`));
    });
    proceso.on('close', (codigo) => {
      clearTimeout(reloj);
      if (codigo !== 0) return rechazar(new Error(`${programa} no terminó correctamente (${codigo}).\n${error.slice(-5000)}`));
      resolver({ salida, error });
    });
  });
}

export async function archivoLocal(nombre, extensiones = EXTENSIONES_VIDEO) {
  if (!nombre || /[\x00-\x1f]/u.test(nombre)) throw new Error('Indica una ruta local válida.');
  const ruta = await realpath(path.resolve(nombre));
  const datos = await lstat(ruta);
  if (!datos.isFile() || !extensiones.includes(path.extname(ruta).toLowerCase())) {
    throw new Error(`Archivo no compatible: ${path.basename(ruta)}. Usa ${extensiones.join(', ')}.`);
  }
  return ruta;
}

export async function leerJson(nombre, esquema) {
  const ruta = await archivoLocal(nombre, ['.json']);
  if ((await lstat(ruta)).size > LIMITE_JSON) throw new Error('El JSON supera el límite de 10 MB.');
  return esquema.parse(JSON.parse(await readFile(ruta, 'utf8')));
}

async function asegurarNuevo(nombre) {
  try { await lstat(nombre); } catch (error) {
    if (error.code === 'ENOENT') return;
    throw error;
  }
  throw new Error(`Ya existe ${nombre}. Elige otro nombre; no se sobrescriben archivos.`);
}

export async function prepararSalida(nombre, entrada, sufijos = ['.mp4', '.srt', '.plan.json']) {
  if (!nombre || /[\x00-\x1f]/u.test(nombre)) throw new Error('Indica --output con una ruta local.');
  const ruta = path.resolve(nombre);
  if (path.extname(ruta).toLowerCase() !== '.mp4') throw new Error('La salida debe terminar en .mp4.');
  await mkdir(path.dirname(ruta), { recursive: true });
  const directorio = await realpath(path.dirname(ruta));
  const base = path.basename(ruta).slice(0, -4);
  const destinos = sufijos.map((sufijo) => path.join(directorio, base + sufijo));
  for (const destino of destinos) {
    if (destino === entrada) throw new Error('El original y la salida deben ser archivos diferentes.');
    await asegurarNuevo(destino);
  }
  return { destinos, temporal: await mkdtemp(path.join(directorio, '.edicion-')) };
}

export async function publicar(temporales, destinos) {
  const creados = [];
  try {
    for (const [indice, origen] of temporales.entries()) {
      await copyFile(origen, destinos[indice], constants.COPYFILE_EXCL);
      creados.push(destinos[indice]);
    }
  } catch (error) {
    await Promise.all(creados.map((archivo) => rm(archivo, { force: true })));
    throw error;
  }
}

export async function inspeccionar(entrada) {
  const { salida } = await ejecutar('ffprobe', ['-v', 'error', '-protocol_whitelist', 'file,pipe', '-show_streams', '-show_format', '-of', 'json', entrada]);
  const datos = JSON.parse(salida);
  const duracion = Number(datos.format?.duration);
  const video = datos.streams?.find((pista) => pista.codec_type === 'video');
  const audio = datos.streams?.find((pista) => pista.codec_type === 'audio');
  if (!video || !audio || !Number.isFinite(duracion) || duracion <= 0 || duracion > 900) {
    throw new Error('Se necesita un video con audio de entre 0 y 900 segundos. Divide las grabaciones largas.');
  }
  return { duracion, ancho: Number(video.width), alto: Number(video.height) };
}

export const ffmpeg = (args, opciones) => ejecutar('ffmpeg', ['-hide_banner', '-nostdin', '-n', ...args], opciones);

/**
 * Opción para pasar el grafo de filtros desde un archivo. ffmpeg 9 quitó -filter_complex_script; desde ffmpeg 7 se
 * usa «-/filter_complex <archivo>». Las versiones 4 a 6 (apt de Ubuntu y Debian) solo entienden la vieja. Una
 * compilación nocturna o con fecha en vez de número se trata como nueva.
 */
export function opcionGrafo(versionTexto) {
  const numero = /ffmpeg version n?(\d+)[.-]/.exec(versionTexto ?? '');
  if (!numero) return '-/filter_complex';
  const mayor = Number(numero[1]);
  return mayor >= 7 ? '-/filter_complex' : '-filter_complex_script';
}

let grafo;
export async function argGrafo() {
  grafo ??= ejecutar('ffmpeg', ['-hide_banner', '-version']).then(({ salida }) => opcionGrafo(salida));
  return grafo;
}
