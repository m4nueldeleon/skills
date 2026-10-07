import { writeFile } from 'node:fs/promises';
import path from 'node:path';
import sharp from 'sharp';
import { ffmpeg } from './archivos.mjs';

const escapar = (texto) => texto.replace(/[&<>"']/g, (caracter) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&apos;' })[caracter]);

function lineasTexto(texto, maximo) {
  return texto.toUpperCase().split(/\s+/u).reduce((lineas, palabra) => {
    const anterior = lineas.at(-1);
    if (anterior && anterior.length + palabra.length < maximo) return [...lineas.slice(0, -1), `${anterior} ${palabra}`];
    return [...lineas, palabra];
  }, []);
}

async function dibujar(texto, ancho, alto, destino) {
  const lineas = lineasTexto(texto, ancho > alto ? 38 : 25);
  if (lineas.length > 3) throw new Error('Un subtítulo supera 3 líneas. Genera tiempos por palabra o divide el segmento del JSON.');
  const fuente = Math.round(ancho * (ancho > alto ? 0.038 : 0.057));
  const y = Math.round(alto * (ancho > alto ? 0.76 : 0.62));
  const tspan = lineas.map((linea, i) => `<tspan x="50%" y="${y + i * fuente * 1.3}">${escapar(linea)}</tspan>`).join('');
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${ancho}" height="${alto}"><text font-family="Arial,Helvetica,sans-serif" font-weight="900" font-size="${fuente}" text-anchor="middle" fill="#FFFFFF" stroke="#111315" stroke-width="${fuente * 0.14}" stroke-linejoin="round" paint-order="stroke fill">${tspan}</text><rect x="${ancho * 0.43}" y="${y + lineas.length * fuente * 1.3}" width="${ancho * 0.14}" height="${Math.max(3, fuente * 0.1)}" rx="3" fill="#C1FF33"/></svg>`;
  await sharp(Buffer.from(svg)).png().toFile(destino);
}

export async function crearCapa(subtitulos, duracion, ancho, alto, temporal) {
  const vacio = path.join(temporal, 'vacio.png');
  await sharp({ create: { width: ancho, height: alto, channels: 4, background: '#00000000' } }).png().toFile(vacio);
  const entradas = [];
  let reloj = 0;
  const agregar = (archivo, duracion) => {
    if (duracion > 0.001) entradas.push(`file '${archivo}'\nduration ${duracion.toFixed(6)}`);
  };
  for (const [indice, subtitulo] of subtitulos.entries()) {
    if (subtitulo.start < reloj - 0.000001 || subtitulo.end > duracion + 0.000001) {
      throw new Error('Los subtítulos se traslapan o exceden la duración del video.');
    }
    agregar('vacio.png', subtitulo.start - reloj);
    const nombre = `sub-${String(indice).padStart(5, '0')}.png`;
    await dibujar(subtitulo.text, ancho, alto, path.join(temporal, nombre));
    agregar(nombre, subtitulo.end - subtitulo.start);
    reloj = subtitulo.end;
  }
  agregar('vacio.png', duracion - reloj);
  entradas.push("file 'vacio.png'");
  await writeFile(path.join(temporal, 'subtitulos.txt'), entradas.join('\n'));
  await ffmpeg(['-v', 'error', '-f', 'concat', '-safe', '1', '-i', 'subtitulos.txt', '-t', String(duracion), '-vf', 'fps=30', '-c:v', 'qtrle', '-pix_fmt', 'argb', 'subtitulos.mov'], { cwd: temporal });
  return path.join(temporal, 'subtitulos.mov');
}
