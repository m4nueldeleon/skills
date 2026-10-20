#!/usr/bin/env node
// revisar.mjs — revisa un video animado antes de entregarlo.
//   node scripts/revisar.mjs mi-video.html [--hoja hoja.png]
// Comprueba: que abra sin errores, que cada escena termine de aparecer, que ningún texto se salga de la
// pantalla ni de la zona segura de Reels/TikTok, tamaño mínimo de letra y contraste. Guarda una «hoja de
// contacto» (una foto por escena) para mirarla antes de entregar. Sale con código 1 si hay problemas.
import { writeFileSync } from "node:fs";
import path from "node:path";
import { abrirNavegador, abrirVideo, servirCarpeta, urlDe, ZONA_SEGURA, ANCHO, ALTO } from "./lib/navegador.mjs";

const LETRA_MINIMA = 40; // px sobre 1080 de ancho (≈ 14 pt en un celular)

function argumentos(argv) {
  const pos = [], op = {};
  for (let i = 0; i < argv.length; i++) {
    if (argv[i].startsWith("--")) { op[argv[i].slice(2)] = argv[i + 1]; i++; } else pos.push(argv[i]);
  }
  if (!pos[0]) {
    console.error("Uso: node scripts/revisar.mjs <video.html> [--hoja hoja-de-contacto.png]");
    process.exit(2);
  }
  const html = path.resolve(pos[0]);
  return { html, hoja: path.resolve(op.hoja || html.replace(/\.html?$/i, "") + "-hoja.png") };
}

/** Corre dentro de la página: mide los textos visibles en el cuadro actual. */
function medirCuadro({ zona, ancho, alto, minimo }) {
  const problemas = [];
  const visibles = [...document.querySelectorAll(".escena")].filter((e) => e.style.display === "block");
  for (const escena of visibles) {
    const cont = escena.querySelector(".contenido");
    if (cont && cont.scrollHeight > cont.clientHeight + 2) problemas.push("el texto no cabe a lo alto");
    const hojas = [...escena.querySelectorAll(".contenido *")].filter((e) =>
      [...e.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim()));
    for (const e of hojas) {
      const r = e.getBoundingClientRect();
      if (!r.width || !r.height) continue;
      const tam = parseFloat(getComputedStyle(e).fontSize);
      const texto = e.textContent.trim().slice(0, 40);
      if (tam < minimo) problemas.push(`letra de ${tam.toFixed(0)} px en «${texto}» (mínimo ${minimo})`);
      if (r.left < -1 || r.right > ancho + 1 || r.top < -1 || r.bottom > alto + 1) problemas.push(`«${texto}» se sale de la pantalla`);
      else if (r.left < zona.izq - 2 || r.right > ancho - zona.der + 2 || r.top < zona.arriba - 2 || r.bottom > alto - zona.abajo + 2) {
        problemas.push(`«${texto}» queda fuera de la zona segura (lo pueden tapar los botones de la app)`);
      }
    }
  }
  return [...new Set(problemas)];
}

async function hojaDeContacto(nav, fotos, info, destino) {
  const celdas = fotos.map((f, i) => {
    const e = info.escenas[i];
    return `<figure><img src="data:image/jpeg;base64,${f}"><figcaption>${e.n}. ${e.tipo} · ${e.inicio.toFixed(1)}–${e.fin.toFixed(1)} s</figcaption></figure>`;
  }).join("");
  const columnas = Math.min(5, fotos.length);
  const html = `<!doctype html><meta charset="utf-8"><style>
    body{margin:0;padding:24px;background:#111;color:#ddd;font:15px system-ui,sans-serif}
    .g{display:grid;grid-template-columns:repeat(${columnas},216px);gap:16px}
    figure{margin:0} img{width:216px;height:384px;display:block;border-radius:6px;box-shadow:0 0 0 1px #333}
    figcaption{margin-top:6px}</style><div class="g">${celdas}</div>`;
  const ctx = await nav.newContext({ viewport: { width: 48 + columnas * 232, height: 400 }, deviceScaleFactor: 1 });
  const p = await ctx.newPage();
  await p.setContent(html);
  await p.screenshot({ path: destino, fullPage: true });
  await ctx.close();
}

async function main() {
  const o = argumentos(process.argv.slice(2));
  const carpeta = path.dirname(o.html);
  const srv = await servirCarpeta(carpeta);
  const nav = await abrirNavegador();
  let problemas = 0;
  try {
    const { page, errores, avisosRed, info } = await abrirVideo(nav, urlDe(srv, o.html, carpeta));
    if (!info) throw new Error("La página no expone window.VIDEO_INFO: ¿se cambió el motor de la plantilla?");
    console.log(`\nRevisión de ${path.basename(o.html)}`);
    console.log(`  Duración: ${info.duracion.toFixed(1)} s · ${info.escenas.length} escenas · tipografía: ${info.fuentes}`);
    console.log(`  Contraste: texto ${info.contraste.texto}:1 · acento ${info.contraste.acento}:1${info.contraste.resaltadoConMarcador ? " (el acento se usa como marcador)" : ""}`);
    for (const e of errores) { console.log(`  ✖ ${e}`); problemas++; }
    for (const a of avisosRed) console.log(`  · ${a}`);
    for (const a of info.avisos) { console.log(`  ✖ ${a}`); problemas++; }

    const fotos = [];
    for (const e of info.escenas) {
      await page.evaluate((t) => window.seek(t), e.heroe);
      const encontrados = await page.evaluate(medirCuadro, { zona: ZONA_SEGURA, ancho: ANCHO, alto: ALTO, minimo: LETRA_MINIMA });
      const buf = await page.screenshot({ type: "jpeg", quality: 82 });
      fotos.push(buf.toString("base64"));
      const marca = encontrados.length ? "✖" : "✔";
      console.log(`  ${marca} Escena ${e.n} (${e.tipo}, ${e.inicio.toFixed(1)}–${e.fin.toFixed(1)} s, entra con ${e.entrada})`);
      for (const p of encontrados) { console.log(`      - ${p}`); problemas++; }
    }
    // Recorre todo el video cada cuarto de segundo: ningún cuadro debe lanzar errores.
    const yaVistos = errores.length;
    for (let t = 0; t <= info.duracion; t += 0.25) await page.evaluate((x) => window.seek(x), t);
    for (const e of errores.slice(yaVistos)) { console.log(`  ✖ Al reproducir: ${e}`); problemas++; }

    await hojaDeContacto(nav, fotos, info, o.hoja);
    console.log(`  Hoja de contacto: ${o.hoja}`);
  } finally {
    await nav.close().catch(() => {});
    srv.close();
  }
  console.log(problemas ? `\n${problemas} problema(s): corrígelos antes de entregar.\n` : "\nTodo en orden.\n");
  process.exit(problemas ? 1 : 0);
}

main().catch((e) => { console.error(`\nrevisar: ${e.message}\n`); process.exit(1); });
