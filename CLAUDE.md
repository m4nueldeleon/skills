# CLAUDE.md — Skills públicas de Manuel de León

Repositorio **público** `m4nueldeleon/skills`. Regla de la casa: **toda skill que se entrega a personas
(recursos de reels, clases, lead magnets) vive aquí**, la haga quien la haga del equipo. Si una skill aparece
en `manueldeleonm.com/recursos`, tiene que estar en este repositorio: el sitio no la publica si no está.

## Cómo está armado

- Cada skill es un plugin de Claude Code: `plugins/<nombre>/skills/<nombre>/SKILL.md` (el nombre va dos
  veces a propósito: así cada instalación carga solo esa skill).
- `.claude-plugin/marketplace.json` es el catálogo que lee Claude Code (`/plugin marketplace add m4nueldeleon/skills`,
  `/plugin install <nombre>@manuel-de-leon`). **No se edita a mano**: lo genera el script, igual que la tabla del README.
- Los ZIP viven en la release `descargas` → `https://github.com/m4nueldeleon/skills/releases/download/descargas/<nombre>.zip`.
  Los sube `node scripts/skills.mjs publicar` (valida antes y se niega si algo falla). Cuando se active el workflow
  «Validar y publicar skills» (pendiente: el token de `gh` necesita el permiso `workflow`), GitHub lo hará solo en
  cada push a `main`; mientras tanto, **córrelo tú después de cada push**.
- Sin `version` en el marketplace a propósito: quien instaló recibe cada mejora con `/plugin marketplace update`.

## Crear una skill nueva (paso a paso)

1. `git pull --rebase origin main`
2. `node scripts/skills.mjs nueva <nombre>` — minúsculas, números y guiones (`respuestas-whatsapp`).
3. Escribe `plugins/<nombre>/skills/<nombre>/SKILL.md`: en `description`, qué hace y cuándo usarla (es lo que
   Claude lee para decidir usarla); abajo, las instrucciones. Puedes sumar `GUIA.md`, `scripts/`, ejemplos.
4. `node scripts/skills.mjs validar` — debe decir «✔ … skills válidas». Si falla, el mensaje dice qué corregir.
5. Pruébala de verdad: `claude plugin validate .` y, en una sesión de Claude Code,
   `/plugin marketplace add ./` + `/plugin install <nombre>@manuel-de-leon`.
6. Commit y push a `main`:
   ```bash
   git add plugins/<nombre> .claude-plugin/marketplace.json README.md
   git commit -m "feat: skill <nombre>"
   git push origin main
   ```
7. Publica los ZIP: `node scripts/skills.mjs publicar` (necesita `gh` con sesión). Abre el ZIP de la release para
   confirmar.
8. Para mostrarla en `/recursos`, sigue la sección «Recurso de tipo skill» del `CLAUDE.md` del sitio
   (`m4nueldeleon/manueldeleonm-website`).

Para editar una skill: cambia sus archivos y repite los pasos 4, 6 y 7 (sin el 7, el ZIP queda viejo). Después, en el sitio, corre
`npm run skills:sincronizar` para que la página use la versión nueva.

## Reglas (el repositorio es público)

- Nunca credenciales, tokens, `.env`, datos de alumnos o clientes, auditorías privadas ni cifras internas de
  Sinergéticos. El validador busca patrones de llaves y archivos prohibidos, pero no adivina datos de negocio:
  revisa tú.
- No prometas resultados, ingresos ni «pasar detectores». Tono de Manuel: directo, realista, paso a paso para
  personas de 35 a 60 años con poca experiencia digital.
- No renombres ni borres una skill publicada sin hablar con Manuel: rompe instalaciones existentes (se resuelve
  con el mapa `renames` del marketplace).
- Skills internas con información confidencial **no** van aquí; esas se quedan en repos privados.

## Comandos

```bash
node scripts/skills.mjs nueva <nombre>   # crea la carpeta y la suma al catálogo
node scripts/skills.mjs validar          # revisa todo (también lo corre GitHub)
node scripts/skills.mjs marketplace      # regenera marketplace.json y la tabla del README
node scripts/skills.mjs empaquetar       # crea dist/<nombre>.zip (valida antes)
node scripts/skills.mjs publicar         # valida, empaqueta y sube los ZIP a la release «descargas»
node --test scripts/*.test.mjs           # pruebas del motor
```
