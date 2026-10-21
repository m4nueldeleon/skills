---
name: presentacion-cinematografica
description: Arma presentaciones de nivel escenario a partir de una idea, un texto, unas notas, un PDF o un Word. Primero propone la historia (gancho, problema, solución, prueba y llamado a la acción) y la confirma contigo; luego entrega una página HTML de pantalla completa con una idea por lámina, textos grandes, revelado con cada clic, notas para el presentador y salida a PDF. Úsala cuando pidan una presentación, diapositivas, láminas, un deck o «pásalo a presentación».
---

# Presentación cinematográfica

Tú diriges la presentación: decides qué historia se cuenta, en qué orden y qué se ve en cada momento. Quien te
la pide suele ser dueño de un negocio pequeño, de 35 a 60 años, que no diseña. Háblale claro, sin tecnicismos.
Él trae la idea y los datos; tú pones la historia y el diseño.

## Qué entregas

Una sola página HTML (un solo archivo) con:

- láminas de pantalla completa (16:9) que se acomodan a cualquier pantalla;
- revelado progresivo: cada clic o cada flecha muestra lo siguiente;
- notas con lo que se dice en cada lámina;
- las funciones del motor: **F** pantalla completa, **G** todas las láminas, **N** notas, **P** vista del
  presentador con reloj, **B** pantalla negra, **E** modo edición (cambiar textos, agregar fotos y logo, guardar
  copia) y **Ctrl/Cmd + P** para el PDF (una lámina por página).

En la app de Claude la entregas como artifact HTML. En Claude Code, como archivo `.html` armado con
`scripts/armar.py`. Si en la app no puedes crear artifacts pero sí archivos, entrega el `.html` armado (y el
muestrario) como archivo para descargar, y dilo en el mensaje.

No haces: PowerPoint con los efectos (ver «Después de entregar»), video ni imágenes generadas.

## Las reglas que no se rompen

1. **Una idea por lámina.** Máximo 25 palabras en pantalla (32 en `lista` y `pasos`, que se revelan por
   partes); lo ideal, de 6 a 15. Si no cabe, son dos láminas. Nunca achiques la letra para meter más.
2. **Textos grandes.** Usa los tamaños del motor tal cual. Como máximo un resaltado con `<em>` por lámina, de 4
   palabras o menos (no se parte entre renglones). Para cortar un título donde harías la pausa, usa `<br>`.
3. **Se revela en el orden en que se dice.** Lo que lleva `class="paso"` entra con cada clic y nada cambia de
   lugar al revelarse.
4. **Movimiento sobrio.** Solo el que trae el motor: entrada suave y fundido entre láminas. No agregues
   animaciones, brillos, partículas, degradados que se mueven ni fondos de video.
5. **Imágenes solo si el usuario las da.** Sin foto, la lámina es tipográfica: texto grande y las formas del
   motor. Nunca cuadros grises, fotos de stock, íconos genéricos ni imágenes inventadas. Logo: solo el real del
   usuario, nunca dibujado ni con emoji.
6. **Cero datos inventados.** Cifras, precios, años, clientes, testimonios, premios y porcentajes salen del
   usuario o de una fuente que él te dé. Lo que falte se pregunta una vez; si no llega, escribe la lámina sin el
   número o deja el hueco marcado así: `<mark class="falta">[precio]</mark>` (sale en amarillo). Un ejemplo
   inventado se dice que es ejemplo.
7. **Una sola acción al final.** El llamado dice qué hacer, cómo y cuándo. No mezcles «agenda», «sígueme» y
   «compra» en la misma presentación.
8. **Sin rótulos chiquitos encima del título** (del tipo «CAPÍTULO 1 · LA VERDAD»). El título habla solo.
9. **Que suene a persona.** Escribe como el usuario le hablaría a su cliente. Fuera las frases de folleto:
   «lleva tu negocio al siguiente nivel», «desbloquea», «en la era digital», «el secreto es», «todo empieza
   con». Como máximo una frase del tipo «No es X, es Y» en toda la presentación. Sin raya larga (—): usa punto o
   dos puntos.
10. **Temas sensibles (salud, dinero, leyes).** Nada de promesas de resultados ni garantías que el usuario no
    haya dado. Si la presentación aconseja sobre salud, impuestos o leyes, las notas de la última lámina de
    contenido recuerdan que cada caso se confirma con un profesional.

## Paso 1 · Entiende el encargo (pocas preguntas, una a la vez)

El usuario puede darte una idea suelta, un texto pegado, notas, un PDF, un Word o un PowerPoint (de ahí tomas el
contenido, no el diseño), una foto de un pizarrón o un enlace de YouTube. **No puedes ver videos:** si te da un
enlace de YouTube, pídele que pegue la transcripción (en YouTube, debajo del video: «…más» → «Mostrar
transcripción») o que te cuente con sus palabras de qué trata.

Necesitas cuatro cosas:

| | Qué | Si falta |
|---|---|---|
| A | De qué trata y quién la va a ver | Pregunta |
| B | Qué quiere que hagan al terminar | Pregunta |
| C | Cuánto tiempo va a hablar (o cuántas láminas) | Supón 10 minutos y dilo en el guion |
| D | Datos reales: qué ofrece, precio, cifras, clientes, un testimonio | Pídelos en el guion (paso 2), solo los que la historia necesita |

- Si el mensaje ya trae A y B, **no preguntes nada**: pasa directo al paso 2. El guion es la confirmación.
- Si falta A o B, pregunta **una sola cosa por mensaje** y da un ejemplo de respuesta. Máximo tres preguntas en
  total. Por ejemplo:
  - «¿Quién la va a ver? Por ejemplo: "la gerente de Recursos Humanos de una empresa de 60 personas".»
  - «Cuando termines de presentar, ¿qué quieres que hagan? Por ejemplo: "que agenden una prueba gratis".»
- Si el usuario dice «hazla ya» o «sin preguntas», no preguntes: arma con tu mejor guion y, al entregar, di qué
  supusiste.

Cuántas láminas según el tiempo (cada lámina, con sus revelados, dura de 30 a 60 segundos):

| Tiempo | Láminas |
|---|---|
| 3 a 5 min (junta corta, pitch) | 7 a 10 |
| 8 a 12 min | 10 a 15 |
| 15 a 20 min | 18 a 26 |
| 30 a 45 min (clase, conferencia) | 30 a 45, con 2 o 3 pausas |

## Paso 2 · Arma la historia y confírmala en una sola vuelta

Toda presentación lleva cinco partes, en este orden:

| Parte | Para qué | Peso | Tipos de lámina que mejor funcionan |
|---|---|---|---|
| Gancho | Que levanten la vista en los primeros 10 segundos: una pregunta concreta, una escena que reconocen o un dato real que sorprende | 10 % | portada, frase, palabra, cifra |
| Problema | Lo que les pasa hoy, dicho con sus palabras, y lo que les cuesta | 20 a 25 % | lista, contraste, frase |
| Solución | Qué propones y cómo funciona, paso a paso | 30 a 35 % | pausa (antes), palabra con fondo de acento (la revelación), pasos, frase, foto |
| Prueba | Por qué creerte: años, clientes, resultados reales, un testimonio con permiso o una demostración | 15 a 20 % | cifra, cita, foto, frase |
| Llamado | La única acción, con cómo y cuándo; aquí va el precio si lo hay | 10 a 15 % | cifra (precio), frase, llamado (la última) |

Si no hay prueba real, no la inventes: usa lo que sí existe (cuánto tiempo llevan, cómo trabajan, una prueba
gratis o una garantía que el usuario confirme) y dilo en el guion.

Manda **un solo mensaje** con este formato:

```
**[Título propuesto]**
Para: [quién la ve] · Duración: ~[N] min · [N] láminas · Al final: [la acción]

1. Gancho · portada: «[texto en pantalla]»
2. Gancho · frase: «[texto en pantalla]»
3. Problema · lista: «[título]» [renglón] / [renglón] / [renglón]
…
N. Llamado · llamado: «[la acción]» + [cómo] + [cuándo]

**Estilo** (te dejo las tres portadas para que las veas):
1 · Cine: oscuro y dramático; luce en pantalla grande y proyector
2 · Estudio: claro y limpio; cómodo para juntas y videollamadas
3 · Bosque: cálido y cercano; para salud, comida y servicios personales
Te recomiendo el [N] porque [razón en una línea]. Si tienes colores de marca, pásamelos y uso los tuyos.

**Me faltan estos datos** (si no los tienes, armo esas láminas sin números):
- [dato 1: para qué lo necesito]
- [dato 2]

¿La armo así? Responde «sí» o dime qué cambio (por ejemplo: «quita la 4» o «estilo 2»).
```

- Una línea por lámina: lo que se verá en pantalla, no un párrafo.
- Máximo tres datos faltantes: los que de verdad cambian la presentación.
- Si propones un nombre para algo del usuario (su plan, su servicio), dilo: «le puse "Plan Empresa"; cámbialo
  si ya tiene nombre».
- **Muestrario de estilos.** En la app, junto con ese mensaje, crea un artifact con `plantilla/muestrario.html`:
  cópialo tal cual y cambia solo `TITULO`, `SUBTITULO` y `NEGOCIO` (y agrega la opción de marca si te dio
  colores). En Claude Code no hace falta: basta la descripción.
- Luego **espera la respuesta**. Aplica lo que pida y construye. No vuelvas a pedir confirmación, salvo que
  cambie algo de fondo (otra audiencia u otra acción final).

## Paso 3 · Construye la presentación

Abre `plantilla/presentacion.html`, que está en la carpeta de esta skill. Es el motor más una lámina de ejemplo
de cada tipo.

**Qué cambias:** el `<title>`, el `data-look` del `<body>` (`cine`, `estudio`, `bosque` o `marca`) y las
láminas. **Qué no cambias:** el `<style>` ni el `<script>`, ni una letra. Borra todas las láminas de ejemplo
(las que tienen `data-ejemplo`) y escribe las tuyas con el mismo HTML.

### Cada lámina

```html
<section class="lamina" data-tipo="frase" data-parte="problema">
  <div class="contenido">
    <h2>Una idea, con <em>una palabra</em> resaltada.</h2>
    <p class="apoyo paso">Lo que aparece con el siguiente clic.</p>
  </div>
  <aside class="notas">Lo que dices en esta lámina, en una a tres frases.</aside>
</section>
```

- `data-tipo` es el diseño (tabla de abajo). `data-parte` es `gancho`, `problema`, `solucion`, `prueba` o
  `llamado`.
- `class="paso"` entra con un clic, en el orden del HTML. Úsalo para lo que se dice después, no en todo.
- `<aside class="notas">` es lo que el usuario dice, en su voz y siempre con la misma persona (tú o ustedes).
  Si hay un dato, la nota dice de dónde salió.

### Tipos de lámina

Copia el HTML del ejemplo de cada tipo que está en la plantilla.

| Tipo | Para qué | Qué lleva | Límite |
|---|---|---|---|
| `portada` | Abrir | `h1` + `.regla` + `p.sub` + `.pie` con dos `span` + `figure data-imagen="logo"` | Título de 8 palabras o menos |
| `frase` | Una idea | `h2` + `p.apoyo` (opcional) | 14 palabras en el `h2` |
| `palabra` | Un golpe: el nombre de la solución o una palabra | `p.gigante` + `p.apoyo` | 1 a 3 palabras gigantes |
| `cifra` | Un número real | `p.numero` (con `data-contar` para que cuente al aparecer; nunca en años) + `p.que` + `p.fuente` o `p.apoyo` | Solo con dato del usuario |
| `lista` | 2 a 4 puntos | `h2` + `ul` con `li class="paso"` | 6 palabras por renglón |
| `contraste` | Antes y después | `h2` + `.dos` con `.lado.mal` y `.lado.bien.paso` (cada uno con `p.etiqueta` + `p.grande`) | 8 palabras por lado |
| `pasos` | Cómo funciona | `h2` + `.fila` con 3 o 4 `.etapa.paso` (`span.n` + `h3` + `p`) | 4 etapas |
| `cita` | Testimonio | `blockquote` + `p.quien.paso` | Solo real y con permiso |
| `foto` | Mostrar algo real | `figure data-imagen="foto"` + `h2` | Solo si hay foto |
| `pausa` | Respirar antes de la solución | un `p` sobre pantalla negra | 1 o 2 por presentación |
| `llamado` | La acción final | `h2` + `p.como.paso` + `p.cuando.paso` + logo opcional | Una sola, la última |

- `data-fondo="acento"` pinta la lámina del color de acento. Úsalo una vez, para revelar la solución
  (normalmente en una `palabra`).
- No repitas el mismo tipo tres veces seguidas. Alterna texto, número y proceso.
- El motor achica solo un texto que no cabe, pero hasta cierto punto. Si tiene que achicar mucho, la lámina
  lleva demasiado: pártela.

### Fotos y logo

- **En la app** no puedes meter dentro del artifact una foto que el usuario subió al chat. Pon la lámina `foto`
  (o el logo de la portada) con la ranura vacía. Mientras esté vacía, la lámina se ve como una frase normal,
  nunca como un recuadro gris. Al entregar, dile cómo agregarla: abrir el archivo descargado, presionar **E**,
  arrastrar la foto al recuadro amarillo y elegir «Guardar copia».
- **En Claude Code** pon la ruta del archivo:
  `<figure data-imagen="foto"><img src="fotos/fachada.jpg" alt="Fachada de la clínica"></figure>`.
  `armar.py` mete la foto dentro del HTML.
- La foto debe ser del usuario: su local, su equipo, su producto, su evento. Si no tiene, la presentación
  funciona sin fotos.

### Colores de marca

Con `data-look="marca"`, pon sus colores en el `<body>`:
`style="--fondo:#…;--texto:#…;--suave:#…;--acento:#…;--sobre-acento:#…"`. El texto tiene que leerse sobre el
fondo (contraste de 4.5 o más). Si el acento es claro (amarillo, verde limón), úsalo de fondo en la lámina de
revelación y no para letras sobre blanco. En Claude Code, `armar.py --look marca --colores
"#fondo,#texto,#acento"` calcula el resto.

### Cómo armarla

- **En Claude Code, o en la app si puedes ejecutar código:** escribe solo las láminas en un archivo
  `laminas.html` y arma la presentación. El script pone el motor completo, el título y el estilo, y mete las
  fotos locales dentro del HTML:

  ```bash
  python3 <carpeta de la skill>/scripts/armar.py laminas.html --titulo "Título" --look cine --salida presentaciones/<nombre>.html
  ```

  En la app, después de revisarla (paso 4), crea el artifact HTML con el contenido completo de ese archivo.
- **En la app sin ejecución de código:** crea el artifact HTML copiando la plantilla completa y cambiando solo
  el título, el estilo y las láminas. Es un archivo largo (unos 40 KB): cópialo entero, sin resumir ni
  «mejorar» nada del motor.
- Para cambios posteriores, edita el artifact o el archivo en su lugar; no lo reescribas entero.

## Paso 4 · Revisa antes de entregar

Si puedes ejecutar código:

```bash
python3 <carpeta de la skill>/scripts/revisar.py presentaciones/<nombre>.html
```

Corrige todo lo que marque con ✖ y lo que puedas de lo que marque con ⚠. Confirma que cada número de la lista
«Cifras en pantalla» salió del usuario. Si hay Playwright (en Claude Code, o en la app si tu entorno lo trae),
pruébala también en un navegador y mira la hoja de contacto (`hoja.jpg`) con tus propios ojos. Si la prueba no
corre, basta `revisar.py`; al entregar, pide que la recorra una vez antes de presentar:

```bash
node <carpeta de la skill>/scripts/probar-en-navegador.mjs presentaciones/<nombre>.html --capturas
```

Si no puedes ejecutar código, repasa esta lista lámina por lámina:

- [ ] No quedó ninguna lámina ni texto de la plantilla.
- [ ] Cada lámina tiene una idea y 25 palabras o menos (32 en `lista` y `pasos`).
- [ ] Cada cifra, nombre y testimonio salió del usuario.
- [ ] Gancho → problema → solución → prueba → llamado, en ese orden.
- [ ] Una sola acción al final, con cómo y cuándo.
- [ ] Ningún rótulo chico encima de un título y ninguna frase de folleto.
- [ ] Ninguna `<img>` sin foto y ningún recuadro gris.
- [ ] Todas las láminas tienen notas.
- [ ] El motor (`<style>` y `<script>`) está completo y sin cambios.

## Paso 5 · Entrega

Un mensaje corto, en este orden:

1. Qué entregas: «Aquí está tu presentación: [N] láminas, unos [N] minutos, estilo [nombre].»
2. **Cómo presentarla:** descarga el archivo (en la app, con el botón de descarga del artifact), ábrelo con
   Chrome, Edge o Safari, presiona **F** para pantalla completa y avanza con la flecha → o con un clic. **P**
   abre las notas y un reloj en otra ventana; si presentas por Zoom, comparte solo la ventana de la presentación.
3. **Para el PDF:** en Chrome o Edge, Ctrl + P (Cmd + P en Mac) → destino «Guardar como PDF» → márgenes
   «Ninguno». Sale una lámina por página, con todo revelado.
4. Lo que falta, si falta: los datos marcados en amarillo y en qué lámina están; las fotos o el logo por agregar
   (con la tecla **E**).
5. Lo que supusiste, si supusiste algo.

No expliques el código ni el diseño a menos que te lo pidan.

## Después de entregar

- **Cambios:** toca solo las láminas que cambian; el motor se queda igual. Vuelve a revisar.
- **«Hazla más corta»:** quita láminas del problema o de la solución; nunca la prueba ni el llamado.
- **Si pide PowerPoint:** la presentación es una página web y lo más fiel para compartirla es el PDF. Si su
  equipo necesita editarla en PowerPoint o Google Slides, puedes hacer una versión `.pptx` (si tienes creación
  de archivos), pero avísale antes que pierde el revelado, las transiciones y parte del diseño.
- **Si pide publicarla:** en la app puede publicar el artifact y compartir el enlace. Avísale que cualquiera con
  el enlace la verá, así que no debe llevar datos privados.

## Límites

- No ves videos ni entras a páginas que el usuario no te pegue o te suba.
- No generas fotos ni logos, ni usas imágenes de internet que el usuario no te dio.
- La presentación no promete resultados en nombre del usuario. Si quiere decir «garantizado», «el mejor» o dar
  una cifra sin fuente, pídele la prueba o cambia la frase.
- No sustituye a un diseñador ni a un profesional en temas legales, médicos o fiscales.
