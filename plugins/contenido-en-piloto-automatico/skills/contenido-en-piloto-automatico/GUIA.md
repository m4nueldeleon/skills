# Tu contenido en piloto automático

Manuel de León · Recursos de IA para negocios · 20 de octubre de 2026

Una skill para que tus ideas de contenido no se pierdan y cada lunes tengas la semana lista: qué publicar cada día,
cómo empezar el video, qué decir y qué escribir.

## Qué hace

1. **Guarda tus ideas.** Le mandas lo que se te ocurra, como te salga: una frase, un link, una captura de pantalla
   o una nota de voz que pasaste a texto. Claude la ordena y te dice para qué sirve cada una: **atraer** gente nueva,
   **nutrir** la confianza de quien ya te sigue o **vender**.
2. **Te arma la semana.** Con las mejores ideas te da, para cada día: el formato, la primera frase del video (el
   gancho), un guion corto de 30 a 60 segundos, el texto de la publicación y qué pedirle a la gente que haga.
3. **Aprende de lo que publicaste.** Le cuentas cómo te fue y la semana siguiente repite lo que funcionó.

Tú grabas y publicas. Claude planea y escribe. **No publica nada por ti ni manda mensajes.**

## Instálala

### En Claude (app de escritorio, celular o claude.ai)

1. Descarga el ZIP de la skill: https://github.com/m4nueldeleon/skills/releases/download/descargas/contenido-en-piloto-automatico.zip
   No lo descomprimas.
2. En Claude, activa **Configuración → Capacidades → Ejecución de código y creación de archivos**.
3. Abre **Personalizar → Skills**, pulsa **+**, elige **Crear skill → Subir una skill** y selecciona el ZIP.
4. Revisa que el interruptor de la skill quede encendido.

¿Prefieres que te lleve de la mano? Sigue el asistente de instalación:
https://manueldeleonm.com/recursos/contenido-en-piloto-automatico/

### En Claude Code

Escribe estos dos comandos dentro de Claude Code:

```text
/plugin marketplace add m4nueldeleon/skills
/plugin install contenido-en-piloto-automatico@manuel-de-leon
```

Confirma en el panel que se abre y escribe `/reload-plugins` (o reinicia Claude Code).

### En ChatGPT, Gemini u otra IA

Abre el archivo `SKILL.md`, copia todo su texto y pégalo en las instrucciones de un Proyecto de ChatGPT o de un Gem
de Gemini. Funciona igual, porque solo son instrucciones.

## Empieza aquí (10 minutos, una sola vez)

1. Abre una conversación nueva en Claude y escribe:

   ```text
   Quiero empezar mi banco de ideas de contenido.
   ```

2. Claude te hace 4 preguntas, una por una: qué vendes y a quién, qué quieres vender estas semanas, en qué redes
   publicas y cuántas veces por semana, y qué temas te sirven. Si no sabes cuántas veces publicar, empieza con 3.
3. Al final te entrega tu **ficha**: un bloque de texto que empieza con `=== MI BANCO DE IDEAS ===`. Toca el botón de
   copiar.
4. Abre las notas de tu celular (o un documento de Word o de Google), crea una nota llamada **Banco de ideas** y
   pega ahí la ficha. Esa nota es tu banco. Claude no la guarda por ti: la guardas tú.
5. Pon un recordatorio que se repita cada lunes (por ejemplo, a las 8:30) con este texto: **RESULTADOS y
   CALENDARIO**.

## Las palabras que entiende

| Escribe | Qué te devuelve |
|---|---|
| **IDEA** y lo que sea | Tus ideas ordenadas, listas para pegar en tu banco |
| **BANCO** | Tu banco ordenado: qué conviene grabar primero |
| **CALENDARIO** | La semana completa, con guiones y textos |
| **RESULTADOS** | Lo que funcionó y qué cambiar la semana que viene |
| **GUION 7** | El guion completo de la idea número 7 |
| **CAMBIA MIÉRCOLES** | Otra idea para el miércoles |

No tienes que aprenderlas de memoria: si escribes «¿qué publico esta semana?», también entiende.

## Durante la semana: apunta, no ordenes

Cada vez que se te ocurra algo, apúntalo al final de tu nota tal como venga. Por ejemplo:

- Lo que te preguntan los clientes («¿hacen factura?», «¿tienen estacionamiento?»).
- Algo que pasó en el negocio («hoy llegó una señora que…»).
- El link de un video que te gustó.
- Una captura de pantalla (guárdala en un álbum de tu celular llamado «Ideas»).
- Una nota de voz: usa el micrófono del teclado de tu celular para dictarla y que quede en texto.

No pierdas tiempo ordenándolas. El lunes lo hace Claude.

Si prefieres, también puedes mandarle a Claude «IDEA» y tu idea en el momento. Te devuelve las fichas y solo las
pegas al final de tu nota.

## Cada lunes (15 minutos)

1. Copia **toda** tu nota del banco.
2. Abre una conversación nueva en Claude y pega este mensaje, con tus datos:

   ```text
   RESULTADOS y luego CALENDARIO.

   Así me fue: [cuántas vistas, mensajes o ventas te trajo cada publicación,
   o lo que notaste. Si no publicaste alguna, dilo].

   Aquí está mi banco:
   [pega tu nota completa]
   ```

3. Claude te dice qué funcionó, te arma la semana y al final te da tu banco actualizado en un bloque. Copia ese
   bloque, borra todo lo que tenías en tu nota y pega el nuevo.
4. Revisa los **[corchetes]**: son datos que Claude no sabe y no inventa (precios, horarios, tu número de WhatsApp).
   Llénalos tú.
5. Graba todo en una sola sentada. Claude te da una lista de qué preparar y en qué orden grabar: de 40 a 60 minutos
   para toda la semana.

La primera semana no tienes resultados todavía: escribe solo **CALENDARIO** y pega tu banco.

## Si prefieres un Proyecto de Claude (opcional)

1. En Claude, crea un **Proyecto** llamado «Mi contenido».
2. Sube tu banco como archivo (cópialo en un documento y guárdalo como `banco-de-ideas.txt`).
3. Cada lunes abre una conversación **dentro del proyecto** y escribe «RESULTADOS y luego CALENDARIO» con tus
   resultados. Claude ya ve tu banco.
4. Claude no puede modificar los archivos del proyecto. Al final te da el banco actualizado: borra el archivo viejo
   del proyecto y sube el nuevo.

Si esto te parece complicado, quédate con la nota del celular. Funciona igual.

## Que se haga solo cada lunes (opcional, en computadora)

Esto es para quien ya usa Cowork (en la app de escritorio de Claude, según tu plan) o Claude Code. Si no sabes qué
es, no lo necesitas: el recordatorio del lunes funciona igual de bien.

1. Crea una carpeta llamada `contenido` **dentro de tu carpeta personal** (en Mac, la de la casita con tu nombre).
   En Mac, las tareas automáticas no pueden entrar a Documentos, Escritorio ni Descargas sin un permiso especial.
2. Pon ahí tu banco como `banco-de-ideas.md`.
3. Si quieres que también revise cómo te fue, durante la semana anota tus resultados en un archivo `resultados.md`
   en esa carpeta. La tarea lo lee y le pone al final una línea `--- procesado` con la fecha, para no contar lo
   mismo dos veces. La semana siguiente escribe tus nuevos resultados debajo de esa línea.

**Con Cowork:** entra a las tareas programadas, crea una tarea nueva **semanal, los lunes a las 9:00**, elige la
carpeta `contenido` y pega este mensaje:

```text
Usa la skill contenido-en-piloto-automatico. Es la tarea programada del lunes:
haz CALENDARIO con banco-de-ideas.md de esta carpeta (y RESULTADOS si hay
resultados.md) y guarda todo. No hay nadie para contestar preguntas.
```

Si la skill no aparece en Cowork, pega el texto completo de `SKILL.md` al inicio de ese mensaje.

**Con Claude Code (Mac o Linux):** en la Terminal, escribe `which claude` y copia la ruta que te salga (algo como
`/Users/tu-nombre/.local/bin/claude`). Luego escribe `crontab -e` y agrega esta línea, cambiando `RUTA-DE-CLAUDE`
por esa ruta:

```text
0 9 * * 1 cd "$HOME/contenido" && RUTA-DE-CLAUDE -p "/contenido-en-piloto-automatico CALENDARIO. Es la tarea programada del lunes: usa banco-de-ideas.md de esta carpeta (y RESULTADOS si hay resultados.md) y guarda todo. No hay nadie para contestar preguntas." --allowedTools "Read,Write,Edit,Glob" >> "$HOME/contenido/tarea-del-lunes.log" 2>&1
```

Cada lunes a las 9:00 deja el calendario en `contenido/calendarios/semana-AAAA-MM-DD.md` y, arriba, una lista de
«Pendientes» con lo que le faltó. Solo puede leer y escribir archivos en esa carpeta; no publica nada. En Windows
se hace con el Programador de tareas; si nunca lo has usado, quédate con el recordatorio.

Importante: la computadora tiene que estar prendida a esa hora. Por eso deja el recordatorio del lunes de todos
modos.

## 3 ejemplos para copiar

**1. Tu primera vez (una clínica dental):**

```text
Quiero empezar mi banco de ideas de contenido. Tengo una clínica dental en
[tu ciudad]. Atiendo sobre todo a familias y a adultos de 40 a 60 que tienen
miedo de ir al dentista. Me escriben por WhatsApp. Publico en Facebook e
Instagram y puedo hacer 3 publicaciones por semana.
```

**2. Guardar ideas sueltas (un despacho contable):**

```text
IDEA
- todos me preguntan en marzo qué papeles necesitan para la declaración anual
- un cliente casi paga una multa por no revisar su buzón tributario
- [pega aquí el link de un video que te gustó]
- quiero explicar la diferencia entre factura y nota de venta
```

**3. Tu lunes (un restaurante):**

```text
RESULTADOS y luego CALENDARIO.
Así me fue: el video de cómo hacemos el pozole tuvo muchas vistas y 5 personas
preguntaron si hay servicio a domicilio. El de la promoción del martes casi no
lo vio nadie. El del jueves no lo publiqué.
Aquí está mi banco:
[pega tu nota completa]
```

## Qué esperar

- **Lo que sí hace:** te quita el «¿qué publico hoy?», no se te pierde ninguna idea y cada semana tienes guiones
  listos para grabar.
- **Lo que no hace:** no publica, no programa publicaciones en tus redes, no contesta mensajes y no ve tus
  estadísticas si tú no se las das.
- **Links de Instagram, TikTok o Facebook:** muchas veces Claude no puede abrirlos. Si te lo dice, pégale el texto
  de la publicación o una captura.
- **No inventa:** si falta un precio, un horario o una condición, lo deja entre [corchetes] para que lo llenes tú.
- **Resultados:** esto te ayuda a publicar con constancia. No te promete vistas, seguidores ni ventas; eso depende
  de tu negocio, tu oferta y de que grabes. Una semana dice poco: la tendencia se ve en 3 o 4 semanas.
- **Salud, dinero o temas legales:** si tienes una clínica, un despacho o vendes seguros, Claude escribe información
  general y te recuerda revisar las reglas de publicidad de tu sector. Revisa cada guion antes de publicarlo; no
  sustituye la opinión de un profesional.
- **Ideas de otras cuentas:** Claude toma la idea y la adapta a tu negocio. No copies su texto, su audio ni sus
  imágenes.
- **Datos de tus clientes:** no pongas nombres ni teléfonos en el banco. Escribe «una clienta preguntó…». Si alguien
  sale en tu video, pídele permiso.

## Enlaces oficiales

- [Código de esta skill](https://github.com/m4nueldeleon/skills)
- [Skills en Claude Code](https://code.claude.com/docs/en/skills)
