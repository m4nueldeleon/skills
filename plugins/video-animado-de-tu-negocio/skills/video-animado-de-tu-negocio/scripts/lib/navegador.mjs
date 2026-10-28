// navegador.mjs — piezas comunes de revisar.mjs y exportar-mp4.mjs.
// Busca Playwright, sirve la carpeta del video en 127.0.0.1 y abre la página en Chromium sin ventana.
// Contrato de la página (lo cumple plantilla/video-animado.html):
//   window.DURACION (segundos) · window.seek(t) · window.LISTO (promesa) · window.VIDEO_INFO (avisos y escenas)
import { createServer } from "node:http";
import { createRequire } from "node:module";
import { execSync } from "node:child_process";
import { createReadStream, existsSync, statSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const AQUI = path.dirname(fileURLToPath(import.meta.url));
const SKILL = path.resolve(AQUI, "..", "..");
export const ANCHO = 1080;
export const ALTO = 1920;
// Zona que no tapan los botones ni el texto de Reels/TikTok (px sobre 1080×1920).
export const ZONA_SEGURA = { arriba: 230, abajo: 420, izq: 80, der: 130 };

const MIME = {
  ".html": "text/html; charset=utf-8", ".js": "text/javascript", ".mjs": "text/javascript", ".css": "text/css",
  ".json": "application/json", ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp",
  ".svg": "image/svg+xml", ".gif": "image/gif", ".woff2": "font/woff2", ".woff": "font/woff", ".ttf": "font/ttf", ".otf": "font/otf",
};

export function cargarPlaywright() {
  const lugares = [path.join(SKILL, "node_modules") + path.sep, process.cwd() + path.sep];
  try { lugares.push(execSync("npm root -g", { stdio: ["ignore", "pipe", "ignore"] }).toString().trim() + path.sep); } catch { /* sin npm global */ }
  for (const lugar of lugares) {
    for (const nombre of ["playwright", "@playwright/test"]) {
      try { return createRequire(lugar)(nombre); } catch { /* sigue buscando */ }
    }
  }
  throw new Error(
    "No encuentro Playwright (el navegador automático que toma las fotos del video).\n" +
    `  Instálalo una vez dentro de la carpeta de la skill:\n    cd "${SKILL}"\n    npm install\n    npx playwright install chromium`
  );
}

export async function abrirNavegador() {
  const pw = cargarPlaywright();
  try {
    return await pw.chromium.launch({ headless: true });
  } catch (e) {
    if (/Executable doesn't exist|browserType\.launch/i.test(e.message)) {
      throw new Error("Playwright está instalado pero falta su Chromium. Ejecuta:\n    npx playwright install chromium");
    }
    throw e;
  }
}

/** Sirve solo la carpeta del video (las fotos o el logo van junto al .html). */
export function servirCarpeta(carpeta) {
  const raiz = path.resolve(carpeta);
  return new Promise((resolve, reject) => {
    const srv = createServer((req, res) => {
      try {
        const rel = decodeURIComponent(new URL(req.url, "http://localhost").pathname);
        const abs = path.resolve(raiz, "." + rel);
        if (abs !== raiz && !abs.startsWith(raiz + path.sep)) { res.writeHead(403).end(); return; }
        if (!existsSync(abs) || !statSync(abs).isFile()) { res.writeHead(404).end(); return; }
        res.writeHead(200, { "Content-Type": MIME[path.extname(abs).toLowerCase()] || "application/octet-stream", "Cache-Control": "no-store" });
        createReadStream(abs).pipe(res);
      } catch (e) {
        res.writeHead(500).end(String(e));
      }
    });
    srv.on("error", reject);
    srv.listen(0, "127.0.0.1", () => resolve(srv));
  });
}

export function urlDe(srv, archivo, carpeta) {
  const rel = path.relative(carpeta, archivo).split(path.sep).map(encodeURIComponent).join("/");
  return `http://127.0.0.1:${srv.address().port}/${rel}?exportar=1`;
}

/** Abre la página a 1080×1920 exactos y espera a que esté lista. Devuelve la página y los problemas vistos. */
export async function abrirVideo(nav, url) {
  const ctx = await nav.newContext({ viewport: { width: ANCHO, height: ALTO }, deviceScaleFactor: 1 });
  const page = await ctx.newPage();
  const errores = [];
  const avisosRed = [];
  page.on("pageerror", (e) => errores.push(`Error de JavaScript: ${e.message}`));
  page.on("console", (m) => { if (m.type() === "error") errores.push(`Consola: ${m.text()}`); });
  page.on("requestfailed", (r) => {
    const destino = /fonts\.(googleapis|gstatic)\.com/.test(r.url()) ? avisosRed : errores;
    destino.push(`No cargó ${r.url()} (${r.failure()?.errorText || "sin detalle"})`);
  });
  page.on("response", (r) => { if (r.status() >= 400) errores.push(`HTTP ${r.status()}: ${r.url()}`); });
  // «load» espera a Google Fonts: sin internet (o con la red bloqueada) nunca llega. Se abre con «domcontentloaded»
  // y se le da un tiempo razonable a que cargue todo (fotos, logo, letras); si no, se sigue con la letra de respaldo.
  await page.goto(url, { waitUntil: "domcontentloaded", timeout: 30000 });
  await page.waitForLoadState("load", { timeout: 12000 }).catch(async () => {
    avisosRed.push("La página no terminó de cargar en 12 s (¿sin internet?): sigo con la letra de respaldo.");
    // Corta lo que sigue colgado (la hoja de Google Fonts): si no, las capturas se quedan esperando la letra.
    await page.evaluate(() => window.stop());
  });
  const ok = await page.waitForFunction(() => typeof window.seek === "function" && window.DURACION > 0, null, { timeout: 15000 })
    .then(() => true, () => false);
  if (!ok) throw new Error(`La página no cumple el contrato (window.seek y window.DURACION).\n  ${errores.join("\n  ")}`);
  await page.evaluate(() => Promise.race([window.LISTO, new Promise((r) => setTimeout(r, 15000))]));
  const info = await page.evaluate(() => window.VIDEO_INFO || null);
  return { ctx, page, errores, avisosRed, info };
}

export function rutaFfmpeg() {
  const candidatos = [process.env.FFMPEG, "ffmpeg", "/opt/homebrew/bin/ffmpeg", "/usr/local/bin/ffmpeg", "/usr/bin/ffmpeg"].filter(Boolean);
  for (const c of candidatos) {
    try { execSync(`"${c}" -version`, { stdio: "ignore" }); return c; } catch { /* siguiente */ }
  }
  return null;
}

export const COMO_INSTALAR_FFMPEG =
  "Falta FFmpeg (el programa gratuito que arma el MP4). Instálalo una vez:\n" +
  "  Mac:      brew install ffmpeg        (si no tienes Homebrew: https://brew.sh)\n" +
  "  Windows:  winget install Gyan.FFmpeg  (y abre una terminal nueva)\n" +
  "  Linux:    sudo apt install ffmpeg";
