# Adiós a perder horas en PowerPoint

Manuel de León · Recursos de IA para negocios · 20 de octubre de 2026

Una skill para que Claude convierta tu idea en una presentación de nivel escenario, lista para proyectar.

## Qué hace

1. Le das una idea, un texto, tus notas, un PDF o un Word.
2. Claude te propone la historia en este orden: gancho, problema, solución, prueba y llamado a la acción. Te
   enseña tres estilos para elegir.
3. Tú respondes «sí» o le dices qué cambia.
4. Te entrega la presentación: pantalla completa, una idea por lámina, letra grande, cada clic revela lo
   siguiente, notas de lo que vas a decir y salida a PDF.

Lo que no hace: no inventa cifras ni testimonios (si te falta un dato, te lo pide o lo deja marcado en
amarillo), no pone fotos de relleno y no hace un PowerPoint con efectos.

## Empieza por aquí

Antes de pedirla, ten a la mano tres cosas:

- **Quién la va a ver.** No es lo mismo un cliente, tu equipo o una sala de 200 personas.
- **Qué quieres que hagan al final.** Una sola cosa: agendar, comprar, probar, firmar.
- **Tus datos reales:** precio, desde cuándo trabajas, cuántos clientes, un comentario de un cliente con su
  permiso.

Con eso Claude trabaja bien. Sin eso, la presentación queda bonita pero vacía.

## Instálala

### En la app de Claude (web, escritorio o celular)

1. Descarga el ZIP (no lo descomprimas):
   https://github.com/m4nueldeleon/skills/releases/download/descargas/presentacion-cinematografica.zip
2. En Claude abre Configuración (Settings) → Capacidades (Capabilities) y activa la ejecución de código y
   creación de archivos.
3. En esa misma página, en Skills, elige subir una skill y selecciona el ZIP.

Si no ves la opción de Skills, revisa que tu plan de Claude la incluya. Asistente paso a paso:
https://manueldeleonm.com/recursos/presentacion-cinematografica/

### En Claude Code

```text
/plugin marketplace add m4nueldeleon/skills
/plugin install presentacion-cinematografica@manuel-de-leon
```

Opcional, para que Claude pruebe la presentación en un navegador antes de entregártela:
`npm install -g playwright` y luego `npx playwright install chromium`. Sin esto la skill funciona igual.

### Sin instalar nada

Adjunta en una conversación los archivos `SKILL.md` y `plantilla/presentacion.html` de la skill y pídele a
Claude que los siga. Funciona, pero instalada es más cómodo.

## Prueba con estos mensajes

Copia uno, cambia lo que está entre corchetes y mándalo.

**1. Una idea suelta (restaurante)**

```text
Usa la skill presentacion-cinematografica.
Tengo un restaurante de comida casera y quiero ofrecer comidas para oficinas.
Lo voy a presentar en 5 minutos a los gerentes de [3 empresas cercanas].
Al final quiero que me pidan una semana de prueba.
Mis datos reales: [precio por comida], abrimos en [año], servimos [número] comidas al día.
```

**2. Un documento que ya tienes (despacho contable)**

```text
Usa la skill presentacion-cinematografica.
Te adjunto el PDF con los servicios de mi despacho contable.
Hazme una presentación de 10 minutos para dueños de negocio, en una plática de [la cámara de comercio].
Al final quiero que agenden un diagnóstico gratis de 30 minutos.
```

**3. Tus notas para una junta (inmobiliaria)**

```text
Usa la skill presentacion-cinematografica.
Estas son mis notas para la junta del lunes con mis [6] asesores:
[pega tus notas tal como las tengas]
Quiero 8 láminas, estilo claro, y que al final cada uno se comprometa a [su meta de la semana].
```

Si tienes un video de YouTube con el tema, Claude no puede verlo: pega su transcripción (en YouTube, debajo del
video: «…más» → «Mostrar transcripción»).

## Qué esperar

1. Si no dijiste para quién es o qué quieres que hagan, Claude te pregunta, una cosa a la vez.
2. Te manda el guion: una línea por lámina, tres estilos para elegir y los datos que le faltan. Contestas «sí» o
   lo que cambias («quita la 4», «estilo 2»).
3. Te entrega la presentación. En la app aparece junto a la conversación y la puedes recorrer ahí mismo.

Todo toma unos minutos, no segundos: la historia se confirma contigo antes de diseñar.

## Cómo presentarla

Descarga el archivo (en la app, con el botón de descarga de la presentación), ábrelo con Chrome, Edge o Safari y
presiona **F** para verla en pantalla completa.

| Tecla | Qué hace |
|---|---|
| → · espacio · clic | Lo siguiente (revela o pasa de lámina) |
| ← | Regresar |
| F | Pantalla completa |
| G | Ver todas las láminas |
| N | Ver lo que vas a decir (para ensayar) |
| P | Tus notas y un reloj en otra ventana |
| B | Pantalla negra para hacer una pausa |
| E | Editar textos y agregar fotos |
| 5 y Enter | Ir a la lámina 5 |

Si presentas por Zoom o Meet, presiona **P**, comparte solo la ventana de la presentación y deja tus notas en la
otra.

## Cómo pasarla a PDF

En Chrome o Edge: Ctrl + P (Cmd + P en Mac) → destino «Guardar como PDF» → márgenes «Ninguno» → Guardar. Sale
una lámina por página, con todo a la vista. Safari no respeta bien el tamaño de página: para el PDF usa Chrome o
Edge.

## Cómo poner tus fotos y tu logo

1. Abre el archivo descargado en tu navegador.
2. Presiona **E**. Los recuadros amarillos son los lugares para una foto o tu logo.
3. Arrastra tu foto al recuadro, o haz clic en él para elegirla.
4. Haz clic en «Guardar copia». Se descarga un archivo nuevo con tus fotos adentro: usa ese.

Ahí mismo puedes corregir cualquier texto. Si quieres una lámina para una foto que no está, pídesela a Claude:
«agrega una lámina para la foto de mi local». Mientras no pongas la foto, esa lámina se ve como una frase y nunca
como un cuadro vacío.

## ¿Y si necesito PowerPoint?

Para compartirla, manda el PDF. Si tu equipo trabaja en PowerPoint o Google Slides, pídele a Claude una versión
`.pptx`: se puede editar ahí, pero pierde el revelado con cada clic y parte del diseño.

## Antes de presentarla

- Lee cada número en voz alta: ¿es tuyo y está al día? Lo que está en amarillo es un dato que falta.
- Ensaya una vez con **N** o **P** y mide el tiempo.
- Ábrela en la pantalla o el proyector donde vas a presentar.

## Enlaces oficiales

- Código de esta skill: https://github.com/m4nueldeleon/skills
- Skills en Claude Code: https://code.claude.com/docs/en/skills
- Ayuda de Claude: https://support.claude.com
