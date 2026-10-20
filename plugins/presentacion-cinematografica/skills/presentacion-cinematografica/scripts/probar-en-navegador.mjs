#!/usr/bin/env node
// Prueba una presentación de la skill presentacion-cinematografica en un navegador de verdad.
// Requiere Playwright (opcional; solo para Claude Code):  npm install -g playwright && npx playwright install chromium
//
// Uso:
//   node probar-en-navegador.mjs presentacion.html                 # revisa errores, que todo quepa y la navegación
//   node probar-en-navegador.mjs presentacion.html --capturas      # además guarda una imagen por lámina y una hoja de contacto
//   node probar-en-navegador.mjs presentacion.html --pdf           # además exporta el PDF (una lámina por página)
//   node probar-en-navegador.mjs presentacion.html --webkit        # además la abre en WebKit (el motor de Safari)
//   --salida <carpeta>   dónde dejar capturas, PDF y verificacion.json (por omisión, junto al archivo)
//
// Sale con código 0 si no hay errores, 1 si hay errores y 2 si falta Playwright o el archivo.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import { execSync } from 'node:child_process';

const args = process.argv.slice(2);
const archivo = args.find(a => !a.startsWith('--') && a.endsWith('.html'));
const opcion = n => args.includes(n);
const valor = n => { const i = args.indexOf(n); return i >= 0 ? args[i + 1] : undefined; };
if (!archivo || !fs.existsSync(archivo)) {
  console.error('Uso: node probar-en-navegador.mjs <presentacion.html> [--capturas] [--pdf] [--webkit] [--salida carpeta]');
  process.exit(2);
}
const ruta = path.resolve(archivo);
const base = path.basename(ruta, '.html');
const salida = path.resolve(valor('--salida') || path.join(path.dirname(ruta), base + '-prueba'));
const url = pathToFileURL(ruta).href;
const errores = [];
const avisos = [];
const bien = [];

async function cargarPlaywright() {
  try { return await import('playwright'); } catch { /* sigue: puede estar instalado global */ }
  try {
    const raiz = execSync('npm root -g', { encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'] }).trim();
    return await import(pathToFileURL(path.join(raiz, 'playwright', 'index.mjs')).href);
  } catch { /* sin Playwright */ }
  console.error('No encontré Playwright. Instálalo con:  npm install -g playwright  y luego  npx playwright install chromium');
  process.exit(2);
}

function vigilar(pagina, etiqueta) {
  pagina.on('pageerror', e => errores.push(`${etiqueta}: error de JavaScript: ${e.message}`));
  pagina.on('console', m => { if (m.type() === 'error') errores.push(`${etiqueta}: consola: ${m.text()}`); });
  pagina.on('requestfailed', r => {
    const u = r.url();
    if (/fonts\.(googleapis|gstatic)\.com/.test(u)) avisos.push(`${etiqueta}: no cargó la tipografía en línea (sin internet o bloqueada); se usa la de respaldo.`);
    else errores.push(`${etiqueta}: no cargó ${u.slice(0, 120)}`);
  });
}

async function abrir(navegador, ancho, alto, etiqueta, destino = url) {
  const contexto = await navegador.newContext({ viewport: { width: ancho, height: alto }, acceptDownloads: true });
  const pagina = await contexto.newPage();
  vigilar(pagina, etiqueta);
  await pagina.goto(destino, { waitUntil: 'load' });
  await pagina.waitForFunction(() => window.__presentacion, null, { timeout: 8000 });
  await pagina.evaluate(() => document.fonts && document.fonts.ready);
  await pagina.waitForTimeout(400);
  return { contexto, pagina };
}

// Mide cada lámina sin animaciones: palabras, ajuste, desbordes, letra mínima y textos fuera de la lámina.
const medirTodo = () => {
  const lams = Array.from(document.querySelectorAll('#escenario > .lamina'));
  const texto = el => (el.innerText || el.textContent || '').trim();
  return lams.map((l, i) => {
    l.classList.add('medir');
    const c = l.querySelector('.contenido');
    const caja = l.getBoundingClientRect();
    const k = caja.width / 1920;
    const desborde = c ? (c.scrollHeight > c.clientHeight + 2 || c.scrollWidth > c.clientWidth + 2) : false;
    let minimo = Infinity;
    const fuera = [];
    l.querySelectorAll('h1,h2,h3,p,li,blockquote,span,figcaption').forEach(el => {
      if (el.closest('.notas') || !texto(el)) return;
      const est = getComputedStyle(el);
      if (est.display === 'none' || el.closest('[data-imagen]')) return;
      minimo = Math.min(minimo, parseFloat(est.fontSize));
      const r = el.getBoundingClientRect();
      const izq = (r.left - caja.left) / k, der = (r.right - caja.left) / k, arr = (r.top - caja.top) / k, abj = (r.bottom - caja.top) / k;
      if (izq < -2 || arr < -2 || der > 1922 || abj > 1082) fuera.push(texto(el).slice(0, 40));
    });
    l.classList.remove('medir');
    const visible = Array.from(l.querySelectorAll('h1,h2,h3,p,li,blockquote,.pie span'))
      .filter(el => !el.closest('.notas') && !el.closest('li') || el.tagName === 'LI')
      .map(texto).join(' ');
    return {
      n: i + 1,
      tipo: l.dataset.tipo || '',
      parte: l.dataset.parte || '',
      palabras: visible.split(/\s+/).filter(Boolean).length,
      pasos: l.querySelectorAll('.paso').length,
      notas: !!(l.querySelector('.notas') && texto(l.querySelector('.notas'))),
      ajuste: parseFloat(l.style.getPropertyValue('--ajuste')) || 1,
      desborde, fuera,
      letraMinima: Number.isFinite(minimo) ? Math.round(minimo) : null,
      faltas: l.querySelectorAll('mark.falta').length,
      foto: l.querySelector('[data-imagen="foto"]') ? (l.classList.contains('con-foto') ? 'con foto' : 'sin foto (se ve como frase)') : '',
      ejemplo: l.hasAttribute('data-ejemplo'),
    };
  });
};

async function probarNavegacion(pagina, total) {
  const pasosTotales = await pagina.evaluate(() => document.querySelectorAll('#escenario > .lamina .paso').length);
  const estado = () => pagina.evaluate(() => window.__presentacion.estado());
  let e = await estado();
  if (e.lamina !== 1) errores.push(`Navegación: no arrancó en la lámina 1 (arrancó en ${e.lamina}).`);
  const clics = total - 1 + pasosTotales;
  for (let i = 0; i < clics; i++) await pagina.keyboard.press('ArrowRight');
  e = await estado();
  if (e.lamina !== total || e.mostrados !== e.pasos) errores.push(`Navegación: con ${clics} clics debía terminar en la lámina ${total} completa y quedó en ${e.lamina} (${e.mostrados}/${e.pasos}).`);
  else bien.push(`Navegación: ${clics} clics recorren las ${total} láminas y sus ${pasosTotales} revelados, en orden.`);
  await pagina.keyboard.press('ArrowRight');
  e = await estado();
  if (e.lamina !== total) errores.push('Navegación: en la última lámina, → no debe hacer nada.');
  await pagina.keyboard.press('ArrowLeft');
  e = await estado();
  if (e.pasos && e.mostrados !== e.pasos - 1) errores.push('Navegación: ← no ocultó el último revelado.');
  await pagina.keyboard.press('Home');
  e = await estado();
  if (e.lamina !== 1 || e.mostrados !== 0) errores.push('Navegación: Inicio no regresó a la lámina 1.');
  await pagina.keyboard.press('ArrowLeft');
  e = await estado();
  if (e.lamina !== 1) errores.push('Navegación: ← en la lámina 1 no debe moverse.');
  await pagina.keyboard.press('g');
  const general = await pagina.evaluate(() => document.querySelectorAll('.general .item').length);
  if (general !== total) errores.push(`Vista general (G): mostró ${general} miniaturas de ${total}.`);
  else bien.push('Vista general (G): muestra todas las láminas.');
  await pagina.keyboard.press('Escape');
  await pagina.keyboard.press('n');
  const notas = await pagina.evaluate(() => document.querySelector('.panel-notas.ver') !== null);
  if (!notas) errores.push('Notas (N): el panel no se abrió.');
  await pagina.keyboard.press('n');
}

async function probarEdicion(navegador) {
  const { contexto, pagina } = await abrir(navegador, 1280, 720, 'edición');
  const indiceFoto = await pagina.evaluate(() => Array.from(document.querySelectorAll('#escenario > .lamina')).findIndex(l => l.querySelector('[data-imagen="foto"]')));
  await pagina.keyboard.press('e');
  const editables = await pagina.evaluate(() => document.querySelectorAll('[contenteditable="true"]').length);
  if (!editables) errores.push('Edición (E): no hay textos editables.');
  let conFoto = false;
  if (indiceFoto >= 0) {
    await pagina.evaluate(n => window.__presentacion.ir(n), indiceFoto + 1);
    const imagen = await pagina.screenshot({ type: 'png' });
    const [selector] = await Promise.all([pagina.waitForEvent('filechooser'), pagina.mouse.click(40, 420)]);
    await selector.setFiles({ name: 'prueba.png', mimeType: 'image/png', buffer: imagen });
    await pagina.waitForFunction(n => document.querySelectorAll('#escenario > .lamina')[n].classList.contains('con-foto'), indiceFoto, { timeout: 5000 })
      .then(() => { conFoto = true; })
      .catch(() => errores.push('Edición: la foto elegida no apareció en la lámina.'));
  }
  const [descarga] = await Promise.all([pagina.waitForEvent('download'), pagina.evaluate(() => window.__presentacion.guardarCopia())]);
  const copia = path.join(fs.mkdtempSync(path.join(os.tmpdir(), 'presentacion-')), 'copia.html');
  await descarga.saveAs(copia);
  const html = fs.readFileSync(copia, 'utf8');
  const marcado = html.replace(/<script[\s\S]*?<\/script>/gi, '').replace(/<style[\s\S]*?<\/style>/gi, '');
  if (/contenteditable|data-motor|class="[^"]*\b(actual|editando|visto)\b/.test(marcado)) errores.push('Guardar copia: la copia trae restos del modo edición.');
  if (indiceFoto >= 0 && conFoto && !/<img[^>]+src="data:image\//.test(html)) errores.push('Guardar copia: la foto no quedó incrustada.');
  await contexto.close();
  const segunda = await abrir(navegador, 1280, 720, 'copia guardada', pathToFileURL(copia).href);
  const ok = await segunda.pagina.evaluate(n => n < 0 || document.querySelectorAll('#escenario > .lamina')[n].classList.contains('con-foto'), conFoto ? indiceFoto : -1);
  if (!ok) errores.push('Copia guardada: al abrirla, la foto no aparece.');
  await segunda.contexto.close();
  bien.push(`Edición (E): ${editables} textos editables${conFoto ? ', foto agregada' : ''}; «Guardar copia» genera un archivo que abre bien.`);
}

async function capturar(navegador, total) {
  fs.mkdirSync(path.join(salida, 'capturas'), { recursive: true });
  const { contexto, pagina } = await abrir(navegador, 960, 540, 'capturas');
  const archivos = [];
  for (let n = 1; n <= total; n++) {
    await pagina.evaluate(i => window.__presentacion.ir(i), n);
    await pagina.evaluate(() => { const e = window.__presentacion.estado(); for (let i = e.mostrados; i < e.pasos; i++) window.__presentacion.siguiente(); });
    await pagina.mouse.move(5, 5);
    await pagina.evaluate(() => { document.body.classList.remove('raton'); document.querySelectorAll('[data-motor]').forEach(e => { e.style.visibility = 'hidden'; }); });
    await pagina.waitForTimeout(1500);
    const f = path.join(salida, 'capturas', `lamina-${String(n).padStart(2, '0')}.jpg`);
    await pagina.screenshot({ path: f, type: 'jpeg', quality: 82 });
    archivos.push(f);
  }
  await contexto.close();
  const columnas = total <= 4 ? 2 : 3;
  const celdas = archivos.map((f, i) => `<figure><img src="data:image/jpeg;base64,${fs.readFileSync(f).toString('base64')}"><figcaption>${i + 1}</figcaption></figure>`).join('');
  const hoja = await navegador.newPage({ viewport: { width: 1500, height: 900 } });
  await hoja.setContent(`<style>body{margin:0;padding:24px;background:#1a1a1a;font:16px system-ui;color:#ccc;display:grid;grid-template-columns:repeat(${columnas},1fr);gap:18px}figure{margin:0}img{width:100%;display:block;border-radius:6px}figcaption{margin-top:6px}</style>${celdas}`);
  await hoja.screenshot({ path: path.join(salida, 'hoja.jpg'), type: 'jpeg', quality: 80, fullPage: true });
  await hoja.close();
  bien.push(`Capturas: ${total} imágenes en ${path.basename(salida)}/capturas y la hoja de contacto ${path.basename(salida)}/hoja.jpg.`);
}

async function exportarPdf(navegador, total) {
  const { contexto, pagina } = await abrir(navegador, 1920, 1080, 'PDF');
  const f = path.join(salida, base + '.pdf');
  await pagina.emulateMedia({ media: 'print' });
  await pagina.pdf({ path: f, preferCSSPageSize: true, printBackground: true });
  await contexto.close();
  const paginas = (fs.readFileSync(f, 'latin1').match(/\/Type\s*\/Page[^s]/g) || []).length;
  if (paginas !== total) errores.push(`PDF: salieron ${paginas} páginas para ${total} láminas.`);
  else bien.push(`PDF: ${paginas} páginas, una por lámina (${(fs.statSync(f).size / 1e6).toFixed(1)} MB).`);
}

async function telefono(navegador) {
  const { contexto, pagina } = await abrir(navegador, 390, 844, 'teléfono');
  const r = await pagina.evaluate(() => { const b = document.getElementById('escenario').getBoundingClientRect(); return { x: b.left, y: b.top, w: b.width, h: b.height }; });
  if (r.x < -1 || r.y < -1 || r.x + r.w > 391 || r.y + r.h > 845) errores.push('Teléfono: la lámina se sale de la pantalla.');
  else bien.push(`Teléfono (390×844): la lámina cabe completa (${Math.round(r.w)}×${Math.round(r.h)} px; se ve mejor con el teléfono acostado).`);
  await pagina.keyboard.press('ArrowRight');
  await contexto.close();
}

async function principal() {
  const pw = await cargarPlaywright();
  const navegador = await pw.chromium.launch();
  const { contexto, pagina } = await abrir(navegador, 1920, 1080, 'Chromium');
  const total = await pagina.evaluate(() => window.__presentacion.total);
  const laminas = await pagina.evaluate(medirTodo);
  for (const l of laminas) {
    const id = `Lámina ${l.n} (${l.tipo || 'sin tipo'})`;
    if (l.ejemplo) errores.push(`${id}: es una lámina de ejemplo de la plantilla; bórrala o reescríbela.`);
    if (l.desborde) errores.push(`${id}: el texto no cabe ni achicándolo; pártela en dos láminas.`);
    if (l.fuera.length) errores.push(`${id}: texto fuera de la lámina: «${l.fuera[0]}».`);
    if (l.ajuste < 0.8) avisos.push(`${id}: se achicó al ${Math.round(l.ajuste * 100)} % para caber; mejor quítale texto.`);
    const limite = ['lista', 'pasos'].includes(l.tipo) ? 32 : 25;
    if (l.palabras > limite) avisos.push(`${id}: ${l.palabras} palabras en pantalla; una idea por lámina pide ${limite} o menos.`);
    if (l.letraMinima !== null && l.letraMinima < 28) avisos.push(`${id}: hay letra de ${l.letraMinima} px (en 1920); se leerá chica en un proyector.`);
    if (!l.notas) avisos.push(`${id}: no tiene notas de lo que se dice.`);
    if (l.faltas) avisos.push(`${id}: ${l.faltas} dato(s) por llenar (marcados en amarillo).`);
  }
  bien.push(`Medición: ${total} láminas; letra mínima ${Math.min(...laminas.map(l => l.letraMinima ?? 999))} px en lienzo de 1920.`);
  await probarNavegacion(pagina, total);
  await contexto.close();
  await probarEdicion(navegador);
  await telefono(navegador);
  if (opcion('--capturas') || opcion('--pdf')) fs.mkdirSync(salida, { recursive: true });
  if (opcion('--capturas')) await capturar(navegador, total);
  if (opcion('--pdf')) await exportarPdf(navegador, total);
  await navegador.close();
  if (opcion('--webkit')) {
    const wk = await pw.webkit.launch();
    const p = await abrir(wk, 1440, 900, 'WebKit (Safari)');
    for (let i = 0; i < 4; i++) await p.pagina.keyboard.press('ArrowRight');
    const e = await p.pagina.evaluate(() => window.__presentacion.estado());
    bien.push(`WebKit (Safari): abre y navega (quedó en la lámina ${e.lamina}).`);
    await wk.close();
  }
  const reporte = { archivo: path.basename(ruta), fecha: new Date().toISOString(), total, errores: [...new Set(errores)], avisos: [...new Set(avisos)], bien, laminas };
  if (opcion('--capturas') || opcion('--pdf')) fs.writeFileSync(path.join(salida, 'verificacion.json'), JSON.stringify(reporte, null, 2));
  console.log(`\nPrueba en navegador · ${path.basename(ruta)} · ${total} láminas\n`);
  bien.forEach(t => console.log('  ✔ ' + t));
  reporte.avisos.forEach(t => console.log('  ⚠ ' + t));
  reporte.errores.forEach(t => console.log('  ✖ ' + t));
  console.log(reporte.errores.length ? `\n${reporte.errores.length} error(es): corrígelos antes de entregar.` : '\nSin errores.');
  process.exit(reporte.errores.length ? 1 : 0);
}

principal().catch(e => { console.error('La prueba se detuvo:', e.message); process.exit(1); });
