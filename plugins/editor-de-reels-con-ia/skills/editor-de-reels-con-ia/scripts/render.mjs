import path from 'node:path';
import { writeFile } from 'node:fs/promises';
import { argGrafo, ffmpeg } from './archivos.mjs';

export function filtroFormato(ancho, alto, encuadre, entrada = '[cortado]', salida = '[formato]') {
  const escala = `scale=${ancho}:${alto}:force_original_aspect_ratio=decrease:force_divisible_by=2`;
  if (encuadre === 'crop') return `${entrada}scale=${ancho}:${alto}:force_original_aspect_ratio=increase,crop=${ancho}:${alto},setsar=1${salida}`;
  return `${entrada}split=2[fondo][frente];[fondo]scale=${ancho}:${alto}:force_original_aspect_ratio=increase,crop=${ancho}:${alto},gblur=sigma=25[borroso];[frente]${escala},setsar=1[contenido];[borroso][contenido]overlay=(W-w)/2:(H-h)/2,setsar=1${salida}`;
}

function filtroCortes(mapa) {
  const v = mapa.map((_, i) => `[sv${i}]`).join('');
  const a = mapa.map((_, i) => `[sa${i}]`).join('');
  const origenes = mapa.length === 1 ? '[0:v]fps=30[sv0];[0:a]anull[sa0]' : `[0:v]fps=30,split=${mapa.length}${v};[0:a]asplit=${mapa.length}${a}`;
  const tramos = mapa.map((tramo, i) => {
    const duracion = tramo.end - tramo.start;
    return `[sv${i}]trim=start=${tramo.start}:end=${tramo.end},setpts=PTS-STARTPTS[v${i}];[sa${i}]atrim=start=${tramo.start}:end=${tramo.end},asetpts=PTS-STARTPTS,afade=t=in:d=0.012,afade=t=out:st=${Math.max(0, duracion - 0.012)}:d=0.012[a${i}]`;
  });
  const unir = mapa.map((_, i) => `[v${i}][a${i}]`).join('');
  return `${origenes};${tramos.join(';')};${unir}concat=n=${mapa.length}:v=1:a=1[cortado][sonido]`;
}

export async function renderizar({ entrada, mapa, capa, ancho, alto, opciones, temporal }) {
  const movimiento = opciones.motion ? `zoompan=z='1+0.035*min(on/180,1)':x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2':d=1:s=${ancho}x${alto}:fps=30` : 'null';
  const limpieza = opciones['noise-reduction'] ? 'afftdn=nf=-25,' : '';
  const grafo = `${filtroCortes(mapa)};${filtroFormato(ancho, alto, opciones.framing)};[formato]${movimiento}[movimiento];[movimiento][1:v]overlay=eof_action=pass:shortest=0,format=yuv420p[v];[sonido]${limpieza}loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000[a]`;
  await writeFile(path.join(temporal, 'filtros.txt'), grafo);
  const final = path.join(temporal, 'final.mp4');
  await ffmpeg(['-v', 'warning', '-protocol_whitelist', 'file,pipe', '-i', entrada, '-i', capa, await argGrafo(), 'filtros.txt', '-map', '[v]', '-map', '[a]', '-t', String(mapa.at(-1).output_end), '-c:v', 'libx264', '-preset', 'fast', '-crf', '20', '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', '-map_metadata', '-1', final], { cwd: temporal });
  return final;
}
