// Pruebas del motor del repo de skills: validación, marketplace y ZIP determinista.
import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { leerSkill, validarSkill, generarMarketplace, empaquetarSkill, listarSkills, crearSkill, dirSkill, readmeConCatalogo, MARKETPLACE } from './skills-lib.mjs';

function repoTemporal(skills) {
  const raiz = fs.mkdtempSync(path.join(os.tmpdir(), 'skills-'));
  for (const [nombre, archivos] of Object.entries(skills)) {
    for (const [ruta, contenido] of Object.entries(archivos)) {
      const destino = path.join(raiz, 'plugins', nombre, 'skills', nombre, ruta);
      fs.mkdirSync(path.dirname(destino), { recursive: true });
      fs.writeFileSync(destino, contenido);
    }
  }
  return raiz;
}
const skillMd = (name, description = 'Hace algo útil y concreto para tu negocio.') => `---\nname: ${name}\ndescription: ${description}\n---\n\n# Título\n\nInstrucciones.\n`;

test('leerSkill separa el frontmatter del cuerpo', () => {
  const raiz = repoTemporal({ 'mi-skill': { 'SKILL.md': skillMd('mi-skill') } });
  const s = leerSkill(dirSkill(raiz, 'mi-skill'));
  assert.equal(s.nombre, 'mi-skill');
  assert.equal(s.frontmatter.name, 'mi-skill');
  assert.match(s.frontmatter.description, /útil/);
  assert.match(s.cuerpo, /^# Título/);
});

test('validarSkill acepta una skill correcta', () => {
  const raiz = repoTemporal({ 'mi-skill': { 'SKILL.md': skillMd('mi-skill'), 'GUIA.md': '# Guía' } });
  assert.deepEqual(validarSkill(dirSkill(raiz, 'mi-skill')), []);
});

test('validarSkill rechaza nombre distinto a la carpeta, sin descripción o con mayúsculas', () => {
  const raiz = repoTemporal({
    'otra': { 'SKILL.md': skillMd('mi-skill') },
    'vacia': { 'SKILL.md': '---\nname: vacia\n---\n\nTexto' },
    'Mayus': { 'SKILL.md': skillMd('Mayus') },
    'sin-skill': { 'GUIA.md': '# nada' },
  });
  assert.match(validarSkill(dirSkill(raiz, 'otra')).join(' '), /no coincide con la carpeta/);
  assert.match(validarSkill(dirSkill(raiz, 'vacia')).join(' '), /Falta la descripción/);
  assert.match(validarSkill(dirSkill(raiz, 'Mayus')).join(' '), /Nombre inválido/);
  assert.match(validarSkill(dirSkill(raiz, 'sin-skill')).join(' '), /Falta SKILL\.md/);
});

test('validarSkill detecta secretos y archivos prohibidos', () => {
  const raiz = repoTemporal({ 'fuga': {
    'SKILL.md': skillMd('fuga'),
    'config.js': 'const clave = "sk-ant-api03-AbCdEfGhIjKlMnOpQrStUvWxYz0123456789";',
    '.env': 'TOKEN=1',
  } });
  const errores = validarSkill(dirSkill(raiz, 'fuga')).join(' ');
  assert.match(errores, /Posible secreto/);
  assert.match(errores, /Archivo prohibido/);
});

test('generarMarketplace crea un plugin por skill, ordenado, con la descripción del SKILL.md', () => {
  const raiz = repoTemporal({ 'zeta': { 'SKILL.md': skillMd('zeta', 'Z.') }, 'alfa': { 'SKILL.md': skillMd('alfa', 'A.') } });
  const m = generarMarketplace(raiz);
  assert.equal(m.name, MARKETPLACE);
  assert.deepEqual(m.plugins.map(p => p.name), ['alfa', 'zeta']);
  assert.deepEqual(m.plugins[0], { name: 'alfa', description: 'A.', source: './plugins/alfa', strict: false });
});

test('listarSkills ignora archivos sueltos y carpetas ocultas', () => {
  const raiz = repoTemporal({ 'una': { 'SKILL.md': skillMd('una') } });
  fs.writeFileSync(path.join(raiz, 'plugins', 'LEEME.md'), 'x');
  fs.mkdirSync(path.join(raiz, 'plugins', '.oculta'));
  assert.deepEqual(listarSkills(raiz), ['una']);
});

test('empaquetarSkill produce exactamente los mismos bytes en dos corridas', () => {
  const raiz = repoTemporal({ 'mi-skill': { 'SKILL.md': skillMd('mi-skill'), 'scripts/a.mjs': 'export const a = 1;\n', 'GUIA.md': '# Guía\n' } });
  const dir = dirSkill(raiz, 'mi-skill');
  const a = empaquetarSkill(dir);
  fs.utimesSync(path.join(dir, 'GUIA.md'), new Date(2030, 0, 1), new Date(2030, 0, 1));
  const b = empaquetarSkill(dir);
  assert.ok(a.equals(b), 'el ZIP debe ser determinista aunque cambie la fecha de los archivos');
});

test('el ZIP lleva la carpeta de la skill en la raíz, omite basura y lo abre unzip', () => {
  const raiz = repoTemporal({ 'mi-skill': {
    'SKILL.md': skillMd('mi-skill'), 'scripts/a.mjs': 'export const a = 1;\n',
    '.DS_Store': 'x', 'node_modules/dep/index.js': 'x',
  } });
  const zip = path.join(raiz, 'mi-skill.zip');
  fs.writeFileSync(zip, empaquetarSkill(dirSkill(raiz, 'mi-skill')));
  const lista = execFileSync('unzip', ['-Z1', zip], { encoding: 'utf8' }).trim().split('\n');
  assert.deepEqual(lista, ['mi-skill/', 'mi-skill/SKILL.md', 'mi-skill/scripts/', 'mi-skill/scripts/a.mjs']);
  const salida = fs.mkdtempSync(path.join(os.tmpdir(), 'unzip-'));
  execFileSync('unzip', ['-q', zip, '-d', salida]);
  assert.equal(fs.readFileSync(path.join(salida, 'mi-skill', 'scripts', 'a.mjs'), 'utf8'), 'export const a = 1;\n');
});

test('validarSkill exige que la carpeta del plugin tenga solo su propia skill', () => {
  const raiz = repoTemporal({ 'una': { 'SKILL.md': skillMd('una') } });
  fs.mkdirSync(path.join(raiz, 'plugins', 'una', 'skills', 'intrusa'));
  assert.match(validarSkill(dirSkill(raiz, 'una')).join(' '), /solo debe contener/);
});

test('crearSkill arma la carpeta con un SKILL.md válido y se niega a pisar una existente', () => {
  const raiz = repoTemporal({});
  fs.mkdirSync(path.join(raiz, 'plugins'), { recursive: true });
  crearSkill(raiz, 'mi-nueva-skill');
  assert.deepEqual(validarSkill(dirSkill(raiz, 'mi-nueva-skill')), []);
  assert.throws(() => crearSkill(raiz, 'mi-nueva-skill'), /Ya existe/);
  assert.throws(() => crearSkill(raiz, 'Con Espacios'), /Nombre inválido/);
});

test('readmeConCatalogo reemplaza solo lo que está entre las marcas', () => {
  const raiz = repoTemporal({ 'una': { 'SKILL.md': skillMd('una', 'Hace una cosa | con barra.') } });
  const readme = 'Antes\n<!-- catalogo:inicio -->\nviejo\n<!-- catalogo:fin -->\nDespués\n';
  const nuevo = readmeConCatalogo(raiz, readme);
  assert.match(nuevo, /^Antes\n<!-- catalogo:inicio -->\n\| Skill/);
  assert.match(nuevo, /\*\*una\*\* \| Hace una cosa \\\| con barra\./);
  assert.match(nuevo, /releases\/download\/descargas\/una\.zip/);
  assert.match(nuevo, /<!-- catalogo:fin -->\nDespués\n$/);
  assert.equal(readmeConCatalogo(raiz, nuevo), nuevo);
  assert.throws(() => readmeConCatalogo(raiz, 'sin marcas'), /marcas/);
});

test('acepta descripciones YAML en bloque (>- y |) y rechaza lo que Claude no deja subir', () => {
  const raiz = repoTemporal({
    'plegada': { 'SKILL.md': '---\nname: plegada\ndescription: >-\n  Primera línea\n  y segunda.\n---\n\nCuerpo' },
    'mi-claude': { 'SKILL.md': skillMd('mi-claude') },
    'con-xml': { 'SKILL.md': skillMd('con-xml', 'Usa <tag> raro.') },
  });
  assert.equal(leerSkill(dirSkill(raiz, 'plegada')).frontmatter.description, 'Primera línea y segunda.');
  assert.deepEqual(validarSkill(dirSkill(raiz, 'plegada')), []);
  assert.match(validarSkill(dirSkill(raiz, 'mi-claude')).join(' '), /«claude» o «anthropic»/);
  assert.match(validarSkill(dirSkill(raiz, 'con-xml')).join(' '), /etiquetas/);
});
