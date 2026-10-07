// Motor del repo de skills: leer y validar cada skill, generar el marketplace de Claude Code
// y empaquetar cada skill en un ZIP determinista (mismos archivos = mismos bytes).
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';

export const MARKETPLACE = 'manuel-de-leon';
const NOMBRE_VALIDO = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;
const MAX_DESCRIPCION = 1024;
const MAX_BYTES_SKILL = 25e6;
const IGNORAR = new Set(['node_modules', '__pycache__', 'dist']);
const ARCHIVO_PROHIBIDO = /^(?:\.env.*|.*\.pem|.*\.key|id_rsa.*|credentials.*\.json)$/i;
const SECRETOS = [
  /sk-ant-[A-Za-z0-9_-]{20,}/, /\bsk-[A-Za-z0-9]{32,}/, /AKIA[0-9A-Z]{16}/, /\bgh[pousr]_[A-Za-z0-9]{30,}/,
  /xox[baprs]-[A-Za-z0-9-]{10,}/, /-----BEGIN [A-Z ]*PRIVATE KEY-----/, /AIza[0-9A-Za-z_-]{35}/,
  /eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,}/,
];

// Cada skill es un plugin de Claude Code: plugins/<nombre>/skills/<nombre>/SKILL.md.
// Así cada instalación carga solo su skill (Claude Code descubre la carpeta skills/ de cada plugin).
export const dirSkill = (raiz, nombre) => path.join(raiz, 'plugins', nombre, 'skills', nombre);

export function listarSkills(raiz) {
  const dir = path.join(raiz, 'plugins');
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir, { withFileTypes: true })
    .filter(e => e.isDirectory() && !e.name.startsWith('.'))
    .map(e => e.name)
    .sort();
}

// Frontmatter YAML sencillo: `clave: valor` en una línea, o bloques `>` / `|` con sangría.
function parsearFrontmatter(texto) {
  const datos = {};
  const lineas = texto.split('\n');
  for (let i = 0; i < lineas.length; i++) {
    const m = lineas[i].match(/^([A-Za-z][\w-]*):\s*(.*)$/);
    if (!m) continue;
    let valor = m[2].trim();
    if (valor === '>' || valor === '|') {
      const bloque = [];
      while (i + 1 < lineas.length && /^\s+\S/.test(lineas[i + 1])) bloque.push(lineas[++i].trim());
      valor = bloque.join(valor === '>' ? ' ' : '\n');
    }
    datos[m[1]] = valor.replace(/^(['"])(.*)\1$/, '$2');
  }
  return datos;
}

export function leerSkill(dir) {
  const archivo = path.join(dir, 'SKILL.md');
  const texto = fs.readFileSync(archivo, 'utf8').replace(/\r\n/g, '\n');
  const m = texto.match(/^---\n([\s\S]*?)\n---\n?/);
  return {
    nombre: path.basename(dir),
    frontmatter: m ? parsearFrontmatter(m[1]) : {},
    cuerpo: (m ? texto.slice(m[0].length) : texto).trim(),
  };
}

// Archivos que viajan en la skill, con ruta relativa POSIX, ordenados.
export function archivosDeSkill(dir) {
  const salida = [];
  const recorrer = (actual, relativo) => {
    for (const e of fs.readdirSync(actual, { withFileTypes: true })) {
      if (e.name.startsWith('.') || IGNORAR.has(e.name) || e.isSymbolicLink()) continue;
      const ruta = relativo ? `${relativo}/${e.name}` : e.name;
      if (e.isDirectory()) recorrer(path.join(actual, e.name), ruta);
      else if (e.isFile()) salida.push(ruta);
    }
  };
  recorrer(dir, '');
  return salida.sort();
}

function archivosOcultosProhibidos(dir) {
  const hallados = [];
  const recorrer = actual => {
    for (const e of fs.readdirSync(actual, { withFileTypes: true })) {
      if (IGNORAR.has(e.name)) continue;
      if (e.isDirectory()) recorrer(path.join(actual, e.name));
      else if (ARCHIVO_PROHIBIDO.test(e.name)) hallados.push(path.relative(dir, path.join(actual, e.name)));
    }
  };
  recorrer(dir);
  return hallados;
}

export function validarSkill(dir) {
  const nombre = path.basename(dir);
  const errores = [];
  if (!NOMBRE_VALIDO.test(nombre) || nombre.length > 64) errores.push(`Nombre inválido «${nombre}»: usa minúsculas, números y guiones (máximo 64).`);
  const contenedor = path.dirname(dir);
  const vecinas = fs.existsSync(contenedor) ? fs.readdirSync(contenedor).filter(n => !n.startsWith('.') && n !== nombre) : [];
  if (vecinas.length) errores.push(`plugins/${nombre}/skills/ solo debe contener la carpeta ${nombre} (sobra: ${vecinas.join(', ')}).`);
  if (!fs.existsSync(path.join(dir, 'SKILL.md'))) return [...errores, `Falta SKILL.md en plugins/${nombre}/skills/${nombre}/.`];
  const { frontmatter, cuerpo } = leerSkill(dir);
  if (frontmatter.name !== nombre) errores.push(`El name del SKILL.md («${frontmatter.name ?? ''}») no coincide con la carpeta «${nombre}».`);
  if (!frontmatter.description) errores.push(`Falta la descripción en el SKILL.md de ${nombre}.`);
  else if (frontmatter.description.length > MAX_DESCRIPCION) errores.push(`La descripción de ${nombre} pasa de ${MAX_DESCRIPCION} caracteres.`);
  if (!cuerpo) errores.push(`El SKILL.md de ${nombre} no tiene instrucciones.`);
  for (const f of archivosOcultosProhibidos(dir)) errores.push(`Archivo prohibido en ${nombre}: ${f} (nunca subas credenciales).`);
  let total = 0;
  for (const rel of archivosDeSkill(dir)) {
    const ruta = path.join(dir, rel);
    const tam = fs.statSync(ruta).size;
    total += tam;
    if (tam > 2e6) continue;
    const texto = fs.readFileSync(ruta, 'utf8');
    if (SECRETOS.some(p => p.test(texto))) errores.push(`Posible secreto en ${nombre}/${rel}: quítalo antes de publicar.`);
  }
  if (total > MAX_BYTES_SKILL) errores.push(`La skill ${nombre} pesa ${(total / 1e6).toFixed(1)} MB; el máximo es 25 MB.`);
  return errores;
}

export function generarMarketplace(raiz) {
  return {
    name: MARKETPLACE,
    owner: { name: 'Manuel de León' },
    metadata: { description: 'Skills gratuitas de Manuel de León para usar la IA en tu negocio. Guía paso a paso en https://manueldeleonm.com/recursos/' },
    plugins: listarSkills(raiz).map(nombre => ({
      name: nombre,
      description: leerSkill(dirSkill(raiz, nombre)).frontmatter.description || '',
      source: `./plugins/${nombre}`,
      strict: false,
    })),
  };
}

export function crearSkill(raiz, nombre) {
  if (!NOMBRE_VALIDO.test(nombre) || nombre.length > 64) throw new Error(`Nombre inválido «${nombre}»: usa minúsculas, números y guiones.`);
  const dir = dirSkill(raiz, nombre);
  if (fs.existsSync(path.join(raiz, 'plugins', nombre))) throw new Error(`Ya existe plugins/${nombre}.`);
  fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(path.join(dir, 'SKILL.md'), `---\nname: ${nombre}\ndescription: Qué hace esta skill y cuándo usarla, en una o dos frases concretas.\n---\n\n# ${nombre}\n\nInstrucciones paso a paso para Claude.\n`);
  return dir;
}

export const textoMarketplace = raiz => `${JSON.stringify(generarMarketplace(raiz), null, 2)}\n`;

// Catálogo del README, entre marcas: se regenera con las skills para que nunca quede viejo.
export const REPO = 'm4nueldeleon/skills';
export const URL_ZIP = nombre => `https://github.com/${REPO}/releases/download/descargas/${nombre}.zip`;
const MARCA_INICIO = '<!-- catalogo:inicio -->';
const MARCA_FIN = '<!-- catalogo:fin -->';

export function textoCatalogo(raiz) {
  const filas = listarSkills(raiz).map(nombre => {
    const descripcion = (leerSkill(dirSkill(raiz, nombre)).frontmatter.description || '').replace(/\|/g, '\\|');
    return `| **${nombre}** | ${descripcion} | [ZIP](${URL_ZIP(nombre)}) · [archivos](plugins/${nombre}/skills/${nombre}) |`;
  });
  return [MARCA_INICIO, '| Skill | Qué hace | Descarga |', '|---|---|---|', ...filas, MARCA_FIN].join('\n');
}

export function readmeConCatalogo(raiz, readme) {
  const i = readme.indexOf(MARCA_INICIO);
  const f = readme.indexOf(MARCA_FIN);
  if (i < 0 || f < i) throw new Error(`El README necesita las marcas ${MARCA_INICIO} y ${MARCA_FIN}.`);
  return readme.slice(0, i) + textoCatalogo(raiz) + readme.slice(f + MARCA_FIN.length);
}

// ── ZIP determinista: fecha fija (1-ene-1980), orden alfabético, permisos 644/755, nombres UTF-8. ──
const TABLA_CRC = Array.from({ length: 256 }, (_, n) => {
  let c = n;
  for (let k = 0; k < 8; k++) c = c & 1 ? 0xedb88320 ^ (c >>> 1) : c >>> 1;
  return c >>> 0;
});
function crc32(buf) {
  let c = 0xffffffff;
  for (const byte of buf) c = TABLA_CRC[(c ^ byte) & 0xff] ^ (c >>> 8);
  return (c ^ 0xffffffff) >>> 0;
}
const FECHA_DOS = (0 << 9) | (1 << 5) | 1;

function entradasZip(dir) {
  const carpeta = path.basename(dir);
  const directorios = new Set([`${carpeta}/`]);
  const archivos = archivosDeSkill(dir);
  for (const rel of archivos) {
    const partes = rel.split('/');
    for (let i = 1; i < partes.length; i++) directorios.add(`${carpeta}/${partes.slice(0, i).join('/')}/`);
  }
  const entradas = [...directorios].map(nombre => ({ nombre, datos: Buffer.alloc(0), modo: 0o40755 }));
  for (const rel of archivos) {
    const ruta = path.join(dir, rel);
    const ejecutable = (fs.statSync(ruta).mode & 0o111) !== 0;
    entradas.push({ nombre: `${carpeta}/${rel}`, datos: fs.readFileSync(ruta), modo: ejecutable ? 0o100755 : 0o100644 });
  }
  return entradas.sort((a, b) => (a.nombre < b.nombre ? -1 : a.nombre > b.nombre ? 1 : 0));
}

export function empaquetarSkill(dir) {
  const locales = [];
  const central = [];
  let desplazamiento = 0;
  for (const { nombre, datos, modo } of entradasZip(dir)) {
    const nombreBuf = Buffer.from(nombre, 'utf8');
    const comprimido = datos.length ? zlib.deflateRawSync(datos, { level: 9 }) : datos;
    const metodo = datos.length && comprimido.length < datos.length ? 8 : 0;
    const cuerpo = metodo === 8 ? comprimido : datos;
    const crc = crc32(datos);
    const local = Buffer.alloc(30);
    local.writeUInt32LE(0x04034b50, 0); local.writeUInt16LE(20, 4); local.writeUInt16LE(0x0800, 6);
    local.writeUInt16LE(metodo, 8); local.writeUInt16LE(0, 10); local.writeUInt16LE(FECHA_DOS, 12);
    local.writeUInt32LE(crc, 14); local.writeUInt32LE(cuerpo.length, 18); local.writeUInt32LE(datos.length, 22);
    local.writeUInt16LE(nombreBuf.length, 26); local.writeUInt16LE(0, 28);
    const cabecera = Buffer.alloc(46);
    cabecera.writeUInt32LE(0x02014b50, 0); cabecera.writeUInt16LE((3 << 8) | 20, 4); cabecera.writeUInt16LE(20, 6);
    cabecera.writeUInt16LE(0x0800, 8); cabecera.writeUInt16LE(metodo, 10); cabecera.writeUInt16LE(0, 12);
    cabecera.writeUInt16LE(FECHA_DOS, 14); cabecera.writeUInt32LE(crc, 16); cabecera.writeUInt32LE(cuerpo.length, 20);
    cabecera.writeUInt32LE(datos.length, 24); cabecera.writeUInt16LE(nombreBuf.length, 28);
    cabecera.writeUInt32LE(((modo << 16) | (nombre.endsWith('/') ? 0x10 : 0)) >>> 0, 38);
    cabecera.writeUInt32LE(desplazamiento, 42);
    locales.push(local, nombreBuf, cuerpo);
    central.push(cabecera, nombreBuf);
    desplazamiento += local.length + nombreBuf.length + cuerpo.length;
  }
  const directorio = Buffer.concat(central);
  const fin = Buffer.alloc(22);
  const total = central.length / 2;
  fin.writeUInt32LE(0x06054b50, 0); fin.writeUInt16LE(total, 8); fin.writeUInt16LE(total, 10);
  fin.writeUInt32LE(directorio.length, 12); fin.writeUInt32LE(desplazamiento, 16);
  return Buffer.concat([...locales, directorio, fin]);
}
