# Tu video animado hecho con Claude

Manuel de León · Recursos de IA para negocios · 20 de octubre de 2026

Contestas cinco preguntas sobre tu negocio y Claude te arma un video promocional vertical, listo para grabar y subir.

## Qué hace

Claude te pregunta qué vendes, a quién, qué quieres anunciar, tus colores y cómo te contactan. Con eso escribe un
guion corto y te entrega un video animado de 15 a 30 segundos: textos grandes que entran con movimiento, una idea por
escena y un cierre con tu WhatsApp o tu dirección. El video se reproduce ahí mismo, en Claude.

Para tenerlo como archivo de video, lo grabas con la pantalla de tu celular o de tu computadora (te explica cómo, paso
a paso) y lo subes a Instagram, TikTok o tus estados de WhatsApp. Si usas Claude Code, también te lo puede dar en
MP4 directo.

No usa fotos de banco ni inventa datos. Si no tienes fotos de tu negocio, el video es de letras y formas de color, y
así se ve profesional.

## Instálala en 3 pasos

Sigue el asistente de instalación: https://manueldeleonm.com/recursos/video-animado-de-tu-negocio/

O hazlo a mano:

1. Descarga el ZIP: https://github.com/m4nueldeleon/skills/releases/download/descargas/video-animado-de-tu-negocio.zip
   (no lo descomprimas).
2. En Claude, activa **Configuración → Capacidades → Ejecución de código y creación de archivos**.
3. Abre **Personalizar → Skills**, pulsa **+**, elige **Crear skill → Subir una skill** y selecciona el ZIP. Deja el
   interruptor encendido.

En Claude Code, escribe estos dos comandos:

```text
/plugin marketplace add m4nueldeleon/skills
/plugin install video-animado-de-tu-negocio@manuel-de-leon
```

El código de esta skill es público: https://github.com/m4nueldeleon/skills

## El prompt (sin instalar nada)

Si no quieres instalar la skill, copia este mensaje en Claude, cambia lo que está entre corchetes y mándalo:

```text
Hazme un video promocional animado de 20 segundos para mi negocio,
vertical 9:16, como una página HTML animada (artifact) que pueda
reproducir y grabar con la pantalla.

Mi negocio: [nombre, qué vendes y en qué ciudad]
Mi cliente y su problema: [a quién le vendes y qué le resuelves]
Lo que quiero anunciar: [promoción con precio, qué incluye y hasta cuándo,
o solo dar a conocer el negocio]
Colores o logo: [tus colores, o "propón tú"]
Contacto: [WhatsApp, colonia o dirección, Instagram, horario]

Cómo lo quiero:
- 6 a 8 escenas de 1 a 2.5 segundos: un gancho con una pregunta que se
  haría mi cliente, lo que gana, el nombre del negocio, qué ofrezco,
  la oferta y un cierre de 3 segundos con el contacto.
- Máximo 7 palabras por escena, letra grande y gruesa, una palabra
  resaltada con un color de acento. Lienzo de 1080×1920 que se ajuste
  a la pantalla, con el texto lejos de las orillas (abajo y a la derecha
  lo tapan los botones de Instagram).
- Entradas suaves (deslizar y aparecer), sin fotos de banco, sin emojis,
  sin inventar cifras ni reseñas.
- Botones de Reproducir, Desde el inicio y "Modo grabar", que esconde los
  botones y arranca cuando toco el video.

Después dime cómo grabarlo en mi [iPhone / Android / Mac / Windows]
y cómo subirlo a Instagram.
```

Con la skill instalada el resultado es más parejo: usa una plantilla probada que ajusta solo los textos para que
nunca se salgan de la pantalla y respeta la zona que tapan los botones de Instagram y TikTok.

## Pruébala con un mensaje real

Con la skill instalada basta con escribir «Hazme un video animado para mi negocio» y contestar sus preguntas. Si
quieres ahorrarte las preguntas, manda todo junto. Cambia lo que está entre corchetes:

**Consultorio dental**

```text
Hazme un video animado para mi consultorio dental [Sonrisa Norte] en
[Monterrey]. Atiendo a familias que tienen miedo de ir al dentista.
Quiero anunciar [limpieza dental a $450, hasta el 30 de noviembre].
Mis colores son [azul marino y blanco]. Contacto: WhatsApp [número],
[colonia], horario [lunes a sábado de 9 a 7].
```

**Tienda de ropa**

```text
Hazme un video animado para mi tienda [Lola Boutique] en [Houston]:
vendo [vestidos de fiesta para mamá e hija]. Quiero anunciar
[20 % de descuento en la segunda prenda este fin de semana].
Me gustan el [rosa y el negro]. Me encuentran en Instagram [@usuario]
y por WhatsApp [número].
```

**Inmobiliaria**

```text
Hazme un video animado para [Casas del Sur], asesoría para comprar casa
en [Mérida]. Mis clientes son parejas que quieren dejar de rentar y no
saben si les alcanza el crédito. Quiero anunciar [una primera asesoría
sin costo de 30 minutos]. No tengo logo: propón tú los colores.
Contacto: WhatsApp [número] y [colonia].
```

## Cómo grabarlo y tener tu video

En computadora, para que se vea grande y sin el chat alrededor, descarga el archivo (en el menú del video,
**Descargar**) y ábrelo con doble clic: se abre en tu navegador. En el celular, grábalo ahí mismo, en la app de
Claude. En los dos casos activa **No molestar** para que no salgan notificaciones en la grabación.

- **Mac:** toca **Modo grabar** → presiona Comando+Mayúsculas+5 → **Grabar parte seleccionada** → ajusta el
  recuadro al video → **Grabar** → toca el video (arranca en un segundo) → al terminar, toca el botón de detener en
  la barra de arriba. El video queda en tu Escritorio.
- **Windows 11:** toca **Modo grabar** → abre la **Herramienta Recortes** → elige **Grabar** (ícono de cámara) →
  **Nuevo** → marca el área del video → **Iniciar** → toca el video → **Detener**. Queda en Videos → Grabaciones de
  pantalla.
- **iPhone:** abre el Centro de control → **Grabar pantalla** (si no aparece, agrégalo en Configuración → Centro de
  control) → vuelve al video, toca **Modo grabar** y luego el video → al terminar, toca el punto rojo de arriba. En
  Fotos → Editar, recorta los bordes y quita el inicio y el final.
- **Android:** baja el panel rápido → **Grabar pantalla** → lo mismo que en iPhone. Recorta en Galería o Google Fotos.

## Súbelo

En Instagram o TikTok crea un Reel o un video con ese archivo. Ponle música desde la biblioteca de la app (esa
música ya tiene permiso de uso) y escribe en la descripción la misma acción del cierre, por ejemplo «Escríbenos por
WhatsApp». En WhatsApp, súbelo a tus estados.

¿Quieres cambiar algo? Díselo a Claude con tus palabras: «la escena 3 más lenta», «cambia el naranja por verde»,
«quita el precio», «hazlo de 30 segundos». Si debajo del video aparece un recuadro amarillo de **avisos**, cópialo y
pégaselo a Claude: le dice qué corregir.

## ¿Usas Claude Code? Tu MP4 sin grabar la pantalla

En Claude Code, pídele «expórtalo a MP4». La skill trae dos programas: uno revisa el video (que ningún texto se
salga, que se alcance a leer, que no haya errores) y otro lo convierte en un MP4 de 1080×1920 listo para subir. Todo
corre en tu computadora, gratis y sin cuentas. Necesitas Node.js, Playwright con su navegador Chromium y FFmpeg;
Claude te dice cuál falta y te pide permiso antes de instalar nada. También puede ponerle tu música si tienes el
archivo y el derecho de usarla.

## Qué esperar

La primera versión sale en uno o dos minutos y casi siempre pide uno o dos ajustes: un texto, un color, una escena
más lenta. El video no trae voz ni música. Revisa precios, fechas y tu número antes de publicar: es tu anuncio.

Un video bien hecho ayuda a que te vean, pero no vende solo. Lo que vende es una oferta clara, contestar rápido y dar
seguimiento a quien te escribe.

## Enlaces oficiales

- [Usar skills en Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- [Instalar skills en Claude Code](https://code.claude.com/docs/en/skills)
