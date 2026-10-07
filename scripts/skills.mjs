#!/usr/bin/env node
// Uso:
//   node scripts/skills.mjs nueva <nombre> → crea plugins/<nombre>/skills/<nombre>/SKILL.md y la suma al marketplace
//   node scripts/skills.mjs validar       → revisa todas las skills y que el marketplace esté al día
//   node scripts/skills.mjs marketplace   → regenera .claude-plugin/marketplace.json y la tabla del README
//   node scripts/skills.mjs empaquetar    → crea dist/<skill>.zip (lo que se descarga desde el sitio)
//   node scripts/skills.mjs publicar      → valida, empaqueta y sube los ZIP a la release «descargas» (necesita gh)
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { execFileSync } from 'node:child_process';
import { listarSkills, validarSkill, textoMarketplace, empaquetarSkill, crearSkill, dirSkill, readmeConCatalogo } from './skills-lib.mjs';

const RAIZ = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const ARCHIVO_MARKETPLACE = path.join(RAIZ, '.claude-plugin', 'marketplace.json');
const README = path.join(RAIZ, 'README.md');

function validar() {
  const skills = listarSkills(RAIZ);
  if (!skills.length) return ['No hay skills en la carpeta plugins/.'];
  const errores = skills.flatMap(nombre => validarSkill(dirSkill(RAIZ, nombre)));
  const actual = fs.existsSync(ARCHIVO_MARKETPLACE) ? fs.readFileSync(ARCHIVO_MARKETPLACE, 'utf8') : '';
  if (actual !== textoMarketplace(RAIZ)) errores.push('El catálogo de Claude Code (.claude-plugin/marketplace.json) está desactualizado. Corre: node scripts/skills.mjs marketplace');
  const readme = fs.readFileSync(README, 'utf8');
  try {
    if (readme !== readmeConCatalogo(RAIZ, readme)) errores.push('La tabla de skills del README está desactualizada. Corre: node scripts/skills.mjs marketplace');
  } catch (error) { errores.push(error.message); }
  return errores;
}

const comandos = {
  nueva(nombre) {
    try {
      const dir = crearSkill(RAIZ, nombre ?? '');
      comandos.marketplace();
      console.log(`✔ Creada ${path.relative(RAIZ, dir)}/SKILL.md. Escribe ahí las instrucciones y corre: node scripts/skills.mjs validar`);
    } catch (error) {
      console.error(`✖ ${error.message}`);
      process.exit(1);
    }
  },
  validar() {
    const errores = validar();
    if (errores.length) {
      console.error(`✖ ${errores.length} problema(s):\n- ${errores.join('\n- ')}`);
      process.exit(1);
    }
    console.log(`✔ ${listarSkills(RAIZ).length} skills válidas y marketplace al día.`);
  },
  marketplace() {
    fs.mkdirSync(path.dirname(ARCHIVO_MARKETPLACE), { recursive: true });
    fs.writeFileSync(ARCHIVO_MARKETPLACE, textoMarketplace(RAIZ));
    fs.writeFileSync(README, readmeConCatalogo(RAIZ, fs.readFileSync(README, 'utf8')));
    console.log(`✔ Marketplace y README con ${listarSkills(RAIZ).length} skills.`);
  },
  empaquetar(salida = 'dist') {
    comandos.validar();
    const destino = path.resolve(RAIZ, salida);
    fs.mkdirSync(destino, { recursive: true });
    for (const nombre of listarSkills(RAIZ)) {
      const zip = empaquetarSkill(dirSkill(RAIZ, nombre));
      fs.writeFileSync(path.join(destino, `${nombre}.zip`), zip);
      console.log(`✔ ${nombre}.zip (${(zip.length / 1024).toFixed(1)} KB)`);
    }
  },
  // Lo mismo que hará GitHub Actions cuando el workflow esté activo. Nunca publica si validar falla.
  publicar() {
    const dist = path.join(RAIZ, 'dist');
    fs.rmSync(dist, { recursive: true, force: true });
    comandos.empaquetar('dist');
    const gh = (...args) => execFileSync('gh', args, { cwd: RAIZ, encoding: 'utf8', stdio: ['ignore', 'pipe', 'inherit'] });
    try { gh('release', 'view', 'descargas', '--json', 'name'); }
    catch { gh('release', 'create', 'descargas', '--title', 'Descargas de las skills', '--notes', 'ZIP de cada skill, listo para subir a Claude (Personalizar → Skills). Se actualiza con cada cambio en main.'); }
    const zips = fs.readdirSync(dist).filter(n => n.endsWith('.zip'));
    gh('release', 'upload', 'descargas', ...zips.map(n => path.join(dist, n)), '--clobber');
    const publicados = gh('release', 'view', 'descargas', '--json', 'assets', '-q', '.assets[].name').split('\n').filter(Boolean);
    for (const viejo of publicados.filter(n => !zips.includes(n))) gh('release', 'delete-asset', 'descargas', viejo, '-y');
    console.log(`✔ Release «descargas» con ${zips.length} ZIP.`);
  },
};

const [comando, ...argumentos] = process.argv.slice(2);
if (!comandos[comando]) {
  console.error('Uso: node scripts/skills.mjs <nueva|validar|marketplace|empaquetar|publicar>');
  process.exit(2);
}
comandos[comando](...argumentos);
