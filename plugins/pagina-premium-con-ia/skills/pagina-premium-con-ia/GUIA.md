# Tu página con IA, sin cara de IA

Manuel de León · Recursos de IA para negocios · 20 de octubre de 2026

Una skill para que Claude haga o rehaga la página de tu negocio con criterio de diseñador, la revise y te diga qué
cuidar antes de publicarla.

Una *skill* es un paquete de instrucciones que le instalas a Claude (el asistente de inteligencia artificial de
Anthropic) para que haga una tarea siempre con el mismo método. Se instala una vez y después solo le escribes lo
que necesitas.

## Qué hace (y qué no)

Cuando le pides a una IA «hazme una página bonita», casi siempre sale lo mismo: degradados morados, letras que
brillan, tarjetas con emojis y frases como «Transformamos tu experiencia». Se nota a kilómetros que nadie la
pensó.

Con esta skill, Claude trabaja en otro orden:

1. Te hace **hasta 5 preguntas**, una por una: tu negocio, qué quieres que haga el cliente, qué vendes, tus
   colores o fotos y, si hace falta, qué estilo te gusta.
2. Antes de escribir código, te propone una **ficha de dirección de arte**: colores sacados de tu negocio (tu
   fachada, tu producto, tu logo), letras elegidas por una razón, el orden de las secciones en el celular y lo que
   NO va a tener.
3. Hace la **página**: pensada primero para celular, rápida, con tus datos reales y botones de WhatsApp, llamar y
   cómo llegar. Las animaciones son pocas y cada una sirve para algo.
4. La **revisa** con una lista: velocidad, celular, textos reales, botones de contacto y los rasgos típicos del
   «look de IA».
5. Antes de publicar, te da una **revisión básica** para México y EE. UU.: aviso de privacidad, términos, cookies,
   datos que pides, derechos de fotos y letras. Es orientación para llegar preparado con tu abogado (y con tu
   contador para precios e IVA); **no es asesoría legal** y no redacta tus documentos legales.

Lo que no hace: no inventa datos de tu negocio (lo que falte queda marcado como `[PENDIENTE]`), no hace sitios con
objetos 3D de estudio de diseño, no publica la página por ti y no promete ventas.

## Antes de empezar, junta esto

- Nombre del negocio, ciudad y dirección.
- Tu WhatsApp y teléfono **con lada** (México empieza con 52; EE. UU. con 1).
- Horario.
- Lo que vendes, con precios si los publicas.
- De 1 a 3 reseñas reales (por ejemplo, copiadas de Google).
- Tu logo y tus colores, si tienes. Fotos tuyas: con el celular y luz de día sirven.
- Si quieres: 2 o 3 páginas o lugares cuyo estilo te guste.

## Instálala

### En Claude (web, escritorio o celular)

La forma más fácil es el asistente de instalación: https://manueldeleonm.com/recursos/pagina-premium-con-ia/

O a mano, desde la computadora:
1. Descarga el ZIP: https://github.com/m4nueldeleon/skills/releases/download/descargas/pagina-premium-con-ia.zip
   (no lo descomprimas). Si usas Safari en Mac y el ZIP se convirtió solo en carpeta, descárgalo con Chrome, o en
   Safari ve a Configuración → General y quita la casilla «Abrir archivos seguros después de descargarlos».
2. En Claude, entra a **Configuración → Capacidades** y activa **«Ejecución de código y creación de archivos»**.
3. Ahí mismo, en **Skills**, elige **«Subir skill»** y selecciona el ZIP.
4. Abre una conversación nueva y escribe uno de los mensajes de abajo. Ya instalada en tu cuenta, también funciona
   en la app del celular.

Si tu pantalla se ve distinta, busca «Skills» dentro de Configuración. Si tu cuenta no tiene esa opción, usa la
forma «sin instalar».

### En Claude Code

Solo si ya usas Claude Code (la versión de Claude que trabaja con archivos en tu computadora). Escribe estas dos
líneas dentro de Claude Code, una por una:

```text
/plugin marketplace add m4nueldeleon/skills
/plugin install pagina-premium-con-ia@manuel-de-leon
```

En Claude Code la página queda como carpeta en tu computadora (`pagina-<negocio>/index.html`) y Claude puede correr
la revisión automática y abrirla en tu navegador.

### Sin instalar nada

Abre las instrucciones en
https://github.com/m4nueldeleon/skills/blob/main/plugins/pagina-premium-con-ia/skills/pagina-premium-con-ia/SKILL.md,
copia todo el texto, pégalo en una conversación nueva de Claude y, abajo, escribe tu mensaje. Funciona, pero con
menos herramientas: Claude revisa a mano (sin el programa de revisión) y, en la parte legal, te da los temas y las
preguntas para tu abogado sin la lista detallada.

## Prueba con estos mensajes (copia, cambia lo que está entre [corchetes] y pega)

**1. Hacer tu página desde cero**

```text
Hazme la página de mi negocio sin que se vea hecha por IA.
Negocio: [qué es y cómo se llama], en [ciudad].
Quiero que los clientes [me escriban por WhatsApp / llamen / agenden / vengan al local].
Mi WhatsApp: [52 en México o 1 en EE. UU. + tu número a 10 dígitos]. Dirección: [calle, número, colonia].
Horario: [días y horas].
Lo que vendo: [productos o servicios, con precio si lo publicas].
Reseñas reales: [pega 1 a 3].
Colores o estilo: [los de tu logo o fachada, o «tú propón»].
```

**2. Rehacer o revisar una página que se ve «de IA»**

```text
Revisa mi página y dime qué la hace ver de plantilla o hecha por IA.
Aquí está: [link de tu página, o adjunta capturas del celular de arriba a abajo, o el archivo].
Dame los 5 problemas más importantes en el orden en que los ve un cliente
y después rehazla conservando mis textos, precios y fotos.
```

**3. Revisar antes de publicar**

```text
Antes de publicar mi página, haz la revisión básica para publicar.
Mis clientes están en [México / Estados Unidos / los dos].
Mi página [tiene / no tiene] formulario, [cobra o recibe anticipos / no cobra]
y [usa / no usa] Google Analytics o el píxel de Facebook.
Dame el semáforo, el inventario de datos y las preguntas para mi abogado.
```

## Qué esperar

- Antes del código, una ficha corta para que digas «así» o «cambia esto».
- La página aparece junto al chat (en la app se llama *artifact*). Para bajarla: menú de la página → Descargar.
  Si en esa vista previa alguna letra o foto no carga, ábrela en tu navegador: ahí sí se ve completa. Si no aparece
  junto al chat, Claude te deja el archivo de la página para descargar: en la computadora ábrelo con doble clic; en
  el celular, tócalo, descárgalo y ábrelo con tu navegador (si no abre, mírala en una computadora).
- Una tabla de revisión con ✅ listo, ⚠️ revisar y ❌ falta, y una lista corta de lo que te toca a ti (fotos, datos
  pendientes, la revisión con tu abogado).
- Si no tienes fotos, la página deja marcos que dicen exactamente qué foto tomar. No pone fotos de banco ni
  imágenes generadas que parezcan tu negocio.

En la carpeta `ejemplos/` hay un caso completo con un negocio de ejemplo (una panadería inventada): la página «con
cara de IA», su revisión, la ficha de dirección de arte y la página rehecha, con capturas.

## Cómo publicarla

Tu página es un solo archivo. Puedes subirlo con tu proveedor actual de hosting (donde vive tu sitio o tu dominio)
o, para empezar, con un servicio que tenga plan gratuito, como Netlify, Cloudflare Pages o GitHub Pages. Pídele a
Claude el paso a paso del que elijas. Antes, haz la revisión del mensaje 3.

## Antes de mandarla al mundo

Los botones solo funcionan de verdad cuando la página está en internet. Súbela primero a una dirección de prueba
(Claude te dice cómo) y ábrela en tu celular. Haz 5 pruebas: ¿se entiende qué vendes en 5 segundos? ¿El botón de
WhatsApp abre con tu número? ¿«Llamar» marca? ¿«Cómo llegar» abre el mapa en tu local? ¿Carga rápido con datos
móviles? Y revisa que cada precio, horario y reseña sea real. Que se vea bien no significa que sea cierto.

## Enlaces oficiales

- Código de esta skill: https://github.com/m4nueldeleon/skills
- Instalar skills en Claude Code: https://code.claude.com/docs/en/skills
