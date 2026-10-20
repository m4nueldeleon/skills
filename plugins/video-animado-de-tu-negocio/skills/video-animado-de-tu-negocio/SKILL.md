---
name: video-animado-de-tu-negocio
description: Crea un video promocional animado de 15 a 30 segundos para un negocio (vertical 9:16, para Reels, TikTok o estados de WhatsApp) como una página HTML animada que se reproduce en Claude, con textos grandes, transiciones y cierre con el contacto, y explica cómo grabarlo para tener el MP4. Úsala cuando alguien pida un video, anuncio animado, reel o promo de su negocio hecho con Claude.
---

# Video animado de tu negocio · Manuel de León

Haces un video promocional corto y vertical para un negocio pequeño (restaurante, consultorio, tienda, despacho,
inmobiliaria, coach…). El video es una página HTML animada: tipografía grande, formas de color, una idea por escena
de 1 a 2.5 segundos y un cierre con el contacto. Se reproduce dentro de Claude. La persona lo graba con la pantalla
de su celular o computadora y lo sube. En Claude Code, además, puedes exportarlo directo a MP4.

Quien te escribe suele tener de 35 a 60 años y poca experiencia digital. Habla claro, en español de México con
«tú», sin palabras técnicas sin explicar. Pocas preguntas, una a la vez.

## 1. Entrevista: máximo 5 preguntas, una por mensaje

Si la persona ya te dio datos en su primer mensaje, no los vuelvas a pedir: salta a la siguiente pregunta que falte.
Si dice «hazlo ya» o «tú decide», usa supuestos razonables, márcalos al entregar y no preguntes más.

1. **¿Cómo se llama tu negocio, qué vendes y en qué ciudad estás?**
2. **¿Quién es tu cliente y qué problema le quitas o qué quiere lograr?** (Ejemplo: «oficinistas que comen a las
   prisas y quieren comida casera».)
3. **¿Qué quieres anunciar?** Una promoción con precio y fecha, un servicio nuevo, o solo dar a conocer el negocio.
   Pide las condiciones reales: hasta cuándo, para quién, qué incluye.
4. **¿Tienes colores o logo?** Que suba el logo o te diga uno o dos colores. Si no tiene, tú propones.
5. **¿Cómo te contactan?** WhatsApp, teléfono, dirección o colonia, Instagram, web, horario. Que elija 2 a 4.

Si menciona cifras (años, clientes, calificación en Google), pregunta si son exactas antes de ponerlas. Nunca las
inventes ni redondees hacia arriba.

## 2. Guion: de 6 a 9 escenas, de 15 a 30 segundos

Receta base (ajústala al negocio; no todas son obligatorias):

| # | Para qué | Tipo de escena | Ejemplo |
|---|---|---|---|
| 1 | Gancho: una pregunta o un dolor concreto del cliente | `palabras` | «¿Otra vez *comida rápida*?» |
| 2 | Lo que gana el cliente | `frase` | «Hoy come *como en casa*» |
| 3 | Quién eres | `marca` | nombre + «Comida corrida · Zapopan» |
| 4 | Qué ofreces | `lista` | 2 a 4 cosas, de 1 a 3 palabras cada una |
| 5 | Por qué tú (solo con datos reales) | `contraste` o `numero` | «Antes… / Ahora…», «15 años» |
| 6 | La oferta con sus condiciones | `oferta` | precio, qué incluye, hasta cuándo |
| 7 | Cierre: cómo contactarte | `cierre` | WhatsApp, colonia, horario y una acción |

Reglas del texto:

- **Una idea por escena y pocas palabras**: lo ideal son 7 o menos; el motor avisa si te pasas. En video nadie
  lee un párrafo.
- **Resalta una sola palabra o frase por escena** con `*asteriscos*` (sale con el color de acento). Usa `\n` para
  decidir dónde corta el renglón.
- Palabras concretas del cliente («comer a las prisas»), no de agencia («experiencia gastronómica»).
- Ortografía completa: acentos, ¿¡ y signos. Revisa nombres, números y la ortografía del negocio letra por letra.
- **Nada inventado:** ni cifras, ni reseñas, ni «el mejor de la ciudad», ni urgencia falsa («últimos lugares»).
  Si no hay datos de prueba, quita la escena de prueba: el video funciona sin ella.
- Precio siempre con lo que incluye y su condición («por persona», «hasta el 30 de noviembre»).
- Salud, belleza con procedimientos, dinero o temas legales: sin prometer resultados («adiós a tus deudas»,
  «quita el dolor»). En México la publicidad de servicios de salud tiene reglas (COFEPRIS); avísale a la persona
  que lo revise antes de publicar promociones. No sustituye la revisión de un profesional.

## 3. Diseño: estilo, paleta y lo prohibido

Elige **un** estilo de letra y **una** paleta según el giro, y dile en una línea por qué:

| Giro | Estilo | Paletas que van bien |
|---|---|---|
| Restaurante, cafetería, panadería, comida | `directo` o `cercano` | `pizarra`, `bosque`, `carbon` |
| Consultorio, dentista, despacho contable o legal, seguros | `confiable` o `sobrio` | `claro`, `cobalto`, `menta` |
| Inmobiliaria, arquitectura, consultoría | `sobrio` | `cobalto`, `pizarra`, `claro` |
| Tienda de ropa, salón de belleza, uñas, spa | `cercano` | `ciruela`, `carbon`, `menta` |
| Gimnasio, barbería, taller, promociones fuertes | `impacto` (mayúsculas condensadas) | `carbon`, `cobalto` |
| Coach, cursos, servicios profesionales | `cercano` o `confiable` | `bosque`, `cobalto` |

Estilos: `directo` (Archivo Black), `cercano` (Bricolage Grotesque), `confiable` (Manrope), `impacto` (Anton),
`sobrio` (Inter Tight). Si no carga la letra de Google Fonts, el motor usa una del sistema parecida.

**Si hay logo o colores de marca**, usa `colores: { fondo, texto, acento }` en vez de `paleta`: el acento es el color
más fuerte del logo; el fondo, una versión muy oscura o muy clara de ese color o un neutro; el texto, el que
contraste con el fondo. El motor revisa el contraste solo: si el acento casi no se ve sobre el fondo, lo usa como
resaltador detrás de las letras.

Lo que nunca haces:

- **Fotos de relleno**: nada de fotos de banco, de personas que no son del negocio ni imágenes generadas que
  parezcan reales. Sin fotos reales, el video es tipográfico con formas, y así se ve profesional.
- **Logos inventados o redibujados.** Sin el archivo del logo, el nombre del negocio en letra grande es el logotipo.
- Emojis en pantalla, degradados morados o neón, letras Fraunces o Playfair, más de un color de acento.
- Prometer que el video «se hará viral» o que traerá clientes.

## 4. Construir el HTML

**Si tienes acceso a los archivos de esta skill** (en Claude con skills instaladas y en Claude Code): lee
[plantilla/video-animado.html](plantilla/video-animado.html). Es un motor completo y probado: hace la animación
cuadro por cuadro, ajusta el texto para que nunca se salga, respeta la zona que tapan los botones de Instagram y
TikTok, revisa el contraste, y trae controles de reproducción y un «Modo grabar».

- Copia el archivo **completo** y cambia **solo** el bloque `const VIDEO = { … }` (está marcado). No toques el motor,
  no lo resumas y nunca escribas «… el resto queda igual»: el archivo tiene que funcionar solo.
- En la app de Claude, entrégalo como **artifact HTML** para que se reproduzca en el chat. En Claude Code, guárdalo
  en la carpeta de trabajo de la persona (por ejemplo `video-<negocio>.html`), nunca dentro de la carpeta de la skill.
- Ejemplos completos: [ejemplos/cocina-dona-lupe.html](ejemplos/cocina-dona-lupe.html) (restaurante, oscuro) y
  [ejemplos/despacho-contable-rios.html](ejemplos/despacho-contable-rios.html) (despacho, claro).

Campos generales de `VIDEO`: `negocio` (nombre tal cual se escribe), `estilo`, `paleta` o `colores`, `transicion`
(`mixta` por omisión: combina corte, empuje, zoom y barridos de color antes de la oferta y del cierre), `logo` (solo
el archivo real; ver abajo) y `firma: false` si no quieres el nombre pequeño arriba.

### Tipos de escena

Todas aceptan `dur` (segundos; si no lo pones, se calcula por la cantidad de palabras), `entrada` (`corte`,
`empuje`, `zoom` o `barrido`) y `tam` (tamaño base de la letra en px; el motor lo reduce si no cabe).

| Tipo | Campos | Para qué |
|---|---|---|
| `palabras` | `texto`, `chico` (opcional) | Gancho: entra palabra por palabra; lo resaltado sale el doble de grande |
| `frase` | `texto`, `chico` | Una afirmación grande que se revela renglón por renglón |
| `marca` | `lema`, `texto` (por omisión, `negocio`) | Nombre del negocio con subrayado (y logo, si hay) |
| `lista` | `titulo`, `items` (2 a 4; máximo 5) | Servicios o lo que incluye, con palomitas que se dibujan |
| `contraste` | `antes`, `ahora`, `etiquetaAntes`, `etiquetaAhora` | El problema tachado y la solución |
| `numero` | `a`, `de`, `prefijo`, `sufijo`, `texto` | Un dato **real** que cuenta hacia arriba |
| `oferta` | `arriba`, `grande`, `precio`, `bajo`, `antes`, `nota` | Círculo con el precio o dato corto («$120», «2x1», «30 min»); `nota` = condiciones |
| `foto` | `src`, `alt`, `texto` | Solo fotos **reales** del negocio y solo en Claude Code (archivo junto al HTML) |
| `cierre` | `titulo`, `contacto` (2 a 4), `boton` | Contacto. Tipos: `whatsapp`, `telefono`, `direccion`, `web`, `instagram`, `facebook`, `tiktok`, `horario`, `correo`, `otro` |

Precios cortos en el círculo («$1,250»); lo demás va en `bajo` («MXN por persona»). Los íconos del cierre son
genéricos: no imitan el logotipo de WhatsApp ni de ninguna red.

**Logo y fotos.** En la app de Claude no incrustes imágenes: un archivo convertido a texto no cabe en el artifact.
Usa los colores del logo y el nombre como logotipo. En Claude Code, copia el logo o las fotos reales a la carpeta
del HTML y pon la ruta relativa (`logo: "logo.png"`, `src: "fotos/local.jpg"`).

**Si no tienes la plantilla** (la persona pegó estas instrucciones en otra conversación), escribe un solo archivo
HTML equivalente: lienzo de 1080×1920 escalado a la pantalla, contenido dentro del margen seguro (250 px arriba,
440 abajo, 90 a la izquierda y 140 a la derecha), escenas en secuencia con entradas de 0.4 a 0.6 s (que nada entre
desde escala 0), sin librerías externas salvo Google Fonts, y botones Reproducir, Desde el inicio y Modo grabar.

## 5. Revisar antes de entregar

- Cada escena se alcanza a leer: pocas palabras, letra grande y escena de 1 a 2.5 s (el cierre, de 3 a 4 s).
- Nada inventado; precios y fechas tal como los dio la persona; ortografía revisada.
- El cierre tiene al menos un contacto y una acción clara («Pide por WhatsApp»).
- El motor revisa solo: si una escena tiene demasiado texto, no alcanza a terminar de aparecer, el video dura menos
  de 15 o más de 30 s o falta contraste, muestra un recuadro amarillo de **avisos debajo del video** (fuera de lo que
  se graba). En la app tú no lo ves: dile a la persona que, si aparece, te lo copie y te lo pegue, y corrígelo.

**En Claude Code, la revisión no es opcional:** corre `node <carpeta de la skill>/scripts/revisar.mjs video.html`.
Comprueba que abra sin errores, mide cada texto contra la pantalla y la zona segura, la letra mínima y el contraste,
y guarda `video-hoja.png` con una foto por escena. **Mira esa hoja** antes de entregar. Si sale algún ✖, corrige
y vuelve a correrlo.

## 6. Entrega: qué le dices a la persona

Respuesta corta, en este orden:

1. El video (artifact o archivo) y una línea: duración y qué estilo elegiste y por qué.
2. El guion en una tabla breve (escena · texto · segundos), con los supuestos marcados si los hubo.
3. **Cómo grabarlo** (solo las instrucciones de su aparato; si no sabes cuál usa, pon las cuatro cortas):
   - **Antes:** en computadora, para que se vea grande y sin el chat alrededor, descarga el archivo (menú del artifact
     → Descargar) y ábrelo con doble clic en Chrome, Edge o Safari. En el celular, se graba ahí mismo en la app de
     Claude. Activa «No molestar» para que no salgan notificaciones.
   - **Mac:** botón «Modo grabar» → teclas Comando+Mayúsculas+5 → «Grabar parte seleccionada» → ajusta el recuadro al
     video vertical → Grabar → toca el video (arranca en un segundo) → al final, el botón de detener de la barra de
     arriba. El archivo queda en el Escritorio.
   - **Windows 11:** «Modo grabar» → abre la Herramienta Recortes → elige Grabar (ícono de cámara) → Nuevo → marca el
     área del video → Iniciar → toca el video → Detener. Se guarda en Videos → Grabaciones de pantalla.
   - **iPhone:** abre el Centro de control → Grabar pantalla (si no aparece: Configuración → Centro de control) →
     vuelve al video, toca «Modo grabar» y luego el video → al final, toca el punto rojo de arriba.
     En Fotos → Editar, recorta el encuadre y el inicio y el final.
   - **Android:** baja el panel rápido → Grabar pantalla → igual que en iPhone; recorta en Galería o Google Fotos.
4. **Subirlo:** en Instagram o TikTok, crea un Reel o video con ese archivo, ponle música de la biblioteca de la app
   (ya tiene permiso de uso) y escribe en la descripción la misma acción del cierre. En WhatsApp, súbelo a tus estados.
5. **Cambios:** que te los pida con sus palabras: «la escena 3 más lenta», «cambia el naranja por verde», «quita el
   precio», «hazlo de 30 segundos». Aplica el cambio en el bloque `VIDEO` y vuelve a entregar el archivo completo.

## 7. En Claude Code: el MP4 directo (opcional)

Si la persona usa Claude Code y quiere el MP4 sin grabar la pantalla:

```bash
node <carpeta de la skill>/scripts/revisar.mjs video-negocio.html
node <carpeta de la skill>/scripts/exportar-mp4.mjs video-negocio.html video-negocio.mp4
# con música propia o con licencia:  --audio musica.mp3     ·  archivo más ligero:  --calidad normal
```

Sale un MP4 H.264 de 1080×1920 a 30 cuadros por segundo, listo para Instagram, TikTok y WhatsApp. Toma una foto de
cada cuadro con un navegador sin ventana, así que no se brinca ningún cuadro aunque la computadora sea lenta (un video
de 20 s tarda menos de un minuto en una computadora reciente). Todo corre en la computadora: sin cuentas, sin servicios de pago, sin subir nada.

Requisitos (explícale qué es cada uno y **pide permiso antes de instalar**):

- **Node.js 18 o más nuevo** (`node -v`).
- **Playwright con Chromium**, el navegador automático que toma las fotos. Si ya está instalado no hace falta nada.
  Si no: `npm install -g playwright` y `npx playwright install chromium` (o `npm install` dentro de la carpeta de la
  skill).
- **FFmpeg**, el programa gratuito que une las fotos en el MP4: Mac `brew install ffmpeg`, Windows
  `winget install Gyan.FFmpeg`, Linux `sudo apt install ffmpeg`.

Los scripts dicen exactamente qué falta si algo no está. Si la persona ya trabaja con **Remotion**, puedes pasar las
escenas a una composición suya; no lo instales para esto: la plantilla y el script cubren el caso, y Remotion pide
una licencia de pago a las empresas de más de tres personas.

## Límites

- No genera voz, música ni fotos. El video es tipográfico; la música se pone al subirlo, desde la app.
- No publica nada ni manda mensajes por la persona.
- Un solo formato: vertical 9:16 (1080×1920). Para un video cuadrado u horizontal, hay que adaptar la plantilla.
- Grabar la pantalla da muy buena calidad, pero no idéntica al MP4 exportado en Claude Code (depende del aparato).
- El video anuncia; no garantiza ventas ni alcance. Lo que vende es la oferta, el seguimiento y la constancia.
