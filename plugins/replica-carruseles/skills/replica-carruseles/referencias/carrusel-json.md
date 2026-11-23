# Formato de `carrusel.json`

`scripts/carrusel.py` lee este archivo y arma las láminas. Las rutas de fotos y logo son relativas a la carpeta donde
está el JSON. Ejemplo completo: `ejemplos/consultorio-dental/carrusel.json`.

```json
{
  "marca": {
    "nombre": "Panadería La Espiga",
    "usuario": "@laespiga.pan",
    "colores": { "principal": "#B4432B", "acento": "#F2B705" },
    "logo": "logo.png"
  },
  "estilo": "claro",
  "fuentes": { "titulo": "archivo", "texto": "inter" },
  "diseno": { "alineacion": "izquierda", "mayusculas": false, "acento_modo": "color", "tamano_titulo": "normal" },
  "numerar": true,
  "laminas": [
    { "tipo": "portada", "titulo": "Estás *guardando* mal el pan", "subtitulo": "3 trucos para que dure más", "foto": "fotos/pan.jpg" },
    { "tipo": "texto", "titulo": "El plástico lo *ablanda*", "texto": "La humedad se queda adentro y la corteza se pone chiclosa." },
    { "tipo": "texto", "numero": "01", "titulo": "Guárdalo en *tela*", "texto": "Una bolsa de tela deja respirar la corteza." },
    { "tipo": "foto", "numero": "02", "foto": "fotos/rebanado.jpg", "enfoque": "arriba", "titulo": "Rebánalo al *momento*", "texto": "Entero se seca más lento." },
    { "tipo": "lista", "titulo": "Guárdala para *mañana*", "items": ["Bolsa de tela", { "texto": "Rebanar al momento", "nota": "Entero dura más" }, "Congela lo que sobre"] },
    { "tipo": "cierre", "titulo": "¿Pasas por el tuyo *hoy*?", "texto": "Horneamos a las 7 de la mañana.", "accion": "Escríbenos PAN por mensaje", "foto": "fotos/fachada.jpg" }
  ],
  "caption": "Primera línea de 125 caracteres o menos.\n\nDos o tres renglones con las palabras que busca tu cliente.\n\nLa acción.",
  "hashtags": ["#panaderia", "#panartesanal", "#pangdl"],
  "credito": "@cuenta-que-te-inspiro"
}
```

## Campos generales

| Campo | Obligatorio | Qué es |
|---|---|---|
| `marca.colores.principal` | Sí (si falta, usa azul marino y avisa) | Color de la marca en hexadecimal (`#0E7C7B`) |
| `marca.colores.acento` | No | Segundo color para la palabra clave. Si no hay, se usa el principal |
| `marca.usuario` | Recomendado | El @ que va al pie de cada lámina y en el cierre |
| `marca.nombre` | Recomendado | Va en el cierre, debajo del @ |
| `marca.logo` | No | PNG (mejor con fondo transparente); va arriba del cierre si el cierre no tiene foto |
| `estilo` | No (claro) | `claro`, `oscuro` o `foto` |
| `fuentes.titulo` / `fuentes.texto` | No | `archivo`, `inter`, `montserrat`, `oswald` (solo titular) o la ruta a un `.ttf` de la marca |
| `diseno.alineacion` | No | `izquierda` (por omisión) o `centro` |
| `diseno.mayusculas` | No | Titulares en mayúsculas (por omisión solo en el estilo `foto`) |
| `diseno.acento_modo` | No | `color` (la palabra en color) o `resaltado` (caja de color detrás; por omisión en `foto`) |
| `diseno.tamano_titulo` | No | `compacto`, `normal` o `grande` |
| `diseno.fondo` | No | Color de fondo distinto (el script cuida que la letra se siga leyendo) |
| `numerar` | No (`true`) | Pone «3/9» al pie de cada lámina |
| `caption` | Recomendado | Texto de la publicación; sale en `caption.txt` |
| `hashtags` | Recomendado | De 3 a 5; si alguno no trae `#`, se lo pone |
| `credito` | No | Si la persona quiere dar crédito: sale como «Inspirado en @…» en `caption.txt`, nunca en las láminas |

## Tipos de lámina

En el texto, lo que va entre `*asteriscos*` es la palabra clave (va en color o resaltada). Usa una por lámina. Un
salto de renglón forzado se escribe `\n`.

| Tipo | Campos | Para qué |
|---|---|---|
| `portada` | `titulo` (obligatorio), `subtitulo`, `foto`, `enfoque` | La primera lámina. Con foto: arriba en `claro`/`oscuro`, a sangre con franja en `foto` |
| `texto` | `titulo`, `texto`, `numero` | Una idea. Con `numero` («01») todas arrancan a la misma altura y se leen como serie |
| `lista` | `titulo`, `items` (2 a 6: texto o `{texto, nota}`) | El resumen que se guarda |
| `foto` | `foto` (obligatorio), `titulo`, `texto`, `numero`, `enfoque` | Una foto real con su idea. Si la foto no existe, se dibuja como `texto` y avisa |
| `cierre` | `titulo` (obligatorio), `texto`, `accion`, `foto` | La acción. Cambia de colores a propósito para que se note. Con `foto`, la pone en círculo |

`enfoque` decide qué parte de la foto se conserva al recortarla: `centro` (por omisión), `arriba`, `abajo`,
`izquierda`, `derecha`, o `[x, y]` entre 0 y 1 (por ejemplo `[0.5, 0.3]`).

## Cómo se corre

```bash
python3 scripts/carrusel.py carrusel.json                  # PNG en laminas/ junto al JSON
python3 scripts/carrusel.py carrusel.json --salida otra/   # en otra carpeta
python3 scripts/carrusel.py carrusel.json --estilo oscuro  # probar otro estilo sin tocar el JSON
python3 scripts/carrusel.py carrusel.json --html           # además, vista previa carrusel.html
```

Salida: `01.png`, `02.png`… (1080 × 1350), `revision.jpg` (todas juntas en chiquito) y `caption.txt`.

Código de salida: `0` todo bien · `1` algún texto no cupo ni con la letra más chica (recórtalo) · `2` el JSON tiene un
error (el mensaje dice cuál).

Lo que el script hace solo: baja la letra si un texto no cabe (hasta un mínimo legible), empareja los renglones de los
titulares, evita palabras sueltas al final, cuida el contraste de los colores, quita emojis y cambia los signos que la
tipografía no tiene. Si no hay Pillow, intenta instalarla con `pip`; si no puede, deja `carrusel.html` como vista
previa.

Pruebas del motor: `python3 -m unittest scripts/test_carrusel.py`.
