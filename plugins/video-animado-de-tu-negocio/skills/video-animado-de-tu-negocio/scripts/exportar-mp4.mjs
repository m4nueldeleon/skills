#!/usr/bin/env node
// exportar-mp4.mjs — convierte el video animado (HTML) en un MP4 vertical 1080×1920 listo para subir.
//   node scripts/exportar-mp4.mjs mi-video.html [salida.mp4] [--fps 30] [--audio musica.mp3] [--calidad alta|normal]
// Toma una foto por cuadro con Chromium (Playwright) usando window.seek(t) —así no se brinca ningún cuadro
// aunque la computadora sea lenta— y FFmpeg las une en H.264. Todo corre en tu computadora: sin servicios
// de pago, sin cuentas, sin subir nada.
// Requisitos: Node 18+, Playwright con Chromium y FFmpeg (el script dice cómo instalarlos si faltan).
import { spawn, execFileSync } from "node:child_process";
import { mkdtempSync, rmSync, existsSync, statSync } from "node:fs";
import { writeFile } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { abrirNavegador, abrirVideo, servirCarpeta, urlDe, rutaFfmpeg, COMO_INSTALAR_FFMPEG } from "./lib/navegador.mjs";

function argumentos(argv) {
  const pos = [], op = {};
  for (let i = 0; i < argv.length; i++) {
    if (argv[i].startsWith("--")) { op[argv[i].slice(2)] = argv[i + 1]; i++; } else pos.push(argv[i]);
  }
  if (!pos[0]) {
    console.error("Uso: node scripts/exportar-mp4.mjs <video.html> [salida.mp4] [--fps 30] [--audio musica.mp3] [--calidad alta|normal]");
    process.exit(2);
  }
  const html = path.resolve(pos[0]);
  if (!existsSync(html)) throw new Error(`No existe ${html}`);
  const salida = path.resolve(pos[1] || html.replace(/\.html?$/i, "") + ".mp4");
  if (salida === html) throw new Error("La salida no puede ser el mismo archivo HTML.");
  const fps = Number(op.fps || 30);
  if (![24, 25, 30, 60].includes(fps)) throw new Error("--fps debe ser 24, 25, 30 o 60.");
  const audio = op.audio ? path.resolve(op.audio) : null;
  if (audio && !existsSync(audio)) throw new Error(`No encuentro el audio ${audio}`);
  return { html, salida, fps, audio, crf: op.calidad === "normal" ? "23" : "18" };
}

function correr(bin, args) {
  return new Promise((resolve, reject) => {
    const p = spawn(bin, args, { stdio: ["ignore", "ignore", "pipe"] });
    let err = "";
    p.stderr.on("data", (d) => { err = (err + d).slice(-4000); });
    p.on("error", reject);
    p.on("close", (code) => (code === 0 ? resolve() : reject(new Error(`FFmpeg terminó con error ${code}:\n${err}`))));
  });
}

async function capturar(nav, url, dir, fps, trabajadores) {
  const primera = await abrirVideo(nav, url);
  if (primera.errores.length) throw new Error(`La página tiene errores; corrígelos antes de exportar:\n  ${primera.errores.join("\n  ")}`);
  if (primera.info?.fuentes === "respaldo") console.log("  Aviso: no cargó la tipografía de Google Fonts (¿sin internet?). El MP4 saldrá con la letra de respaldo.");
  const duracion = await primera.page.evaluate(() => window.DURACION);
  const total = Math.round(duracion * fps);
  const paginas = [primera];
  const n = Math.min(trabajadores, Math.max(1, Math.floor(total / 30)));
  for (let i = 1; i < n; i++) paginas.push(await abrirVideo(nav, url));
  const tramo = Math.ceil(total / n);
  let hechos = 0;
  await Promise.all(paginas.map(async ({ page }, w) => {
    const cdp = await page.context().newCDPSession(page);
    for (let f = w * tramo; f < Math.min(total, (w + 1) * tramo); f++) {
      await page.evaluate((t) => window.seek(t), f / fps);
      const { data } = await cdp.send("Page.captureScreenshot", { format: "png", optimizeForSpeed: true });
      await writeFile(path.join(dir, `f${String(f).padStart(5, "0")}.png`), Buffer.from(data, "base64"));
      hechos++;
      if (hechos % fps === 0) process.stdout.write(`\r  Capturando cuadros: ${hechos}/${total}`);
    }
  }));
  process.stdout.write(`\r  Capturando cuadros: ${total}/${total}\n`);
  for (const p of paginas) {
    const tarde = p.errores.filter(Boolean);
    if (tarde.length) throw new Error(`Hubo errores al recorrer el video:\n  ${tarde.join("\n  ")}`);
    await p.ctx.close();
  }
  return { duracion, total };
}

async function main() {
  const o = argumentos(process.argv.slice(2));
  const ffmpeg = rutaFfmpeg();
  if (!ffmpeg) throw new Error(COMO_INSTALAR_FFMPEG);
  const carpeta = path.dirname(o.html);
  const dir = mkdtempSync(path.join(os.tmpdir(), "video-animado-"));
  const srv = await servirCarpeta(carpeta);
  const nav = await abrirNavegador();
  const t0 = Date.now();
  try {
    console.log(`\nExportando ${path.basename(o.html)} a MP4 (1080×1920, ${o.fps} cuadros por segundo)`);
    const { duracion } = await capturar(nav, urlDe(srv, o.html, carpeta), dir, o.fps, Math.max(1, Math.min(4, os.cpus().length - 1)));
    const args = ["-y", "-loglevel", "error", "-framerate", String(o.fps), "-i", path.join(dir, "f%05d.png")];
    if (o.audio) args.push("-i", o.audio);
    args.push(
      "-vf", "scale=out_color_matrix=bt709:out_range=tv,format=yuv420p",
      "-c:v", "libx264", "-preset", "medium", "-crf", o.crf, "-pix_fmt", "yuv420p", "-r", String(o.fps),
      "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-color_range", "tv"
    );
    if (o.audio) {
      const fin = Math.max(0, duracion - 1.2).toFixed(2);
      args.push("-map", "0:v:0", "-map", "1:a:0", "-c:a", "aac", "-b:a", "192k",
        "-af", `afade=t=in:st=0:d=0.3,afade=t=out:st=${fin}:d=1.2`);
    }
    args.push("-t", duracion.toFixed(3), "-movflags", "+faststart", o.salida);
    console.log("  Uniendo cuadros con FFmpeg…");
    await correr(ffmpeg, args);
  } finally {
    await nav.close().catch(() => {});
    srv.close();
    rmSync(dir, { recursive: true, force: true });
  }
  const mb = (statSync(o.salida).size / 1e6).toFixed(1);
  let detalle = "";
  try {
    const ffprobe = ffmpeg.replace(/ffmpeg(\.exe)?$/, "ffprobe$1");
    detalle = execFileSync(ffprobe, ["-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height,r_frame_rate:format=duration",
      "-of", "default=noprint_wrappers=1:nokey=0", o.salida]).toString().trim().replace(/\n/g, " · ");
  } catch { /* ffprobe es opcional */ }
  console.log(`  Listo en ${((Date.now() - t0) / 1000).toFixed(0)} s → ${o.salida} (${mb} MB)${detalle ? `\n  ${detalle}` : ""}\n`);
}

main().catch((e) => { console.error(`\nexportar-mp4: ${e.message}\n`); process.exit(1); });
