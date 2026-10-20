# Fotos de producto con IA

Manuel de León · Recursos de IA para negocios · 20 de octubre de 2026

Quince códigos que convierten la foto de celular de tu producto en foto de estudio, póster, oferta o flyer.

## Qué hace (y qué no)

Le mandas a Claude la foto de tu producto y un código, por ejemplo `/estudio`. Claude revisa tu foto, describe tu
producto con todo detalle y te entrega **el texto exacto** (el «prompt») para pegarlo en ChatGPT o en Gemini junto
con tu foto. ChatGPT o Gemini hacen la imagen.

Lo que no hace:
- **Claude no hace la foto.** La hace ChatGPT o Gemini con el texto que Claude te da.
- **Los códigos no vienen en ChatGPT ni en Gemini.** Si escribes «/estudio» en un chat normal, no pasa nada.
  Funcionan aquí, con esta skill, o en tu propio GPT o Gem (te explico cómo crearlo más abajo).
- **No promete que nadie note que es IA.** Promete algo más útil: que tu producto se vea como es.

## Antes de empezar: toma bien la foto

La IA mejora la luz y el fondo, pero no adivina tu etiqueta. Con una buena foto de celular basta:

1. Ponte junto a una ventana, de día. Apaga el flash.
2. Limpia el producto (huellas, polvo, gotas).
3. La etiqueta, de frente a la cámara. El producto completo, sin cortarlo.
4. Toma la foto a la altura del producto, sin usar el zoom.
5. Toca la pantalla sobre la etiqueta para enfocar. Revisa que las letras se lean.

Para `/vistas`, toma también una foto de atrás y otra de lado.

## Los 15 códigos

| Código | Te da |
|---|---|
| `/estudio` | Foto publicitaria de estudio, fondo de un color |
| `/catalogo` | Fondo blanco para tienda en línea y catálogo de WhatsApp |
| `/escena` | Tu producto con los ingredientes o materiales de los que está hecho |
| `/en-uso` | Tu producto usándose en su lugar real |
| `/menu` | Tu platillo listo para menú o apps de entrega, con la misma porción |
| `/poster-limpio` | Póster minimalista con un título corto |
| `/oferta` | Tu producto grande con el precio de tu promoción |
| `/flyer-limpio` | Flyer sencillo con horario, dirección y WhatsApp |
| `/temporada` | Versión para Día de Muertos, Navidad, Día de las Madres… |
| `/vistas` | 4 vistas de tu producto en una sola lámina |
| `/despiece` | Las partes o ingredientes separados, flotando en orden |
| `/anatomia` | Diagrama con etiquetas que señalan cada parte |
| `/angulo-imposible` | Tu producto visto desde el suelo o desde arriba |
| `/surrealista` | Una escena imposible, con tu producto intacto |
| `/con-persona` | Tú sosteniendo tu producto |

Además: `/video` (opcional, solo si tu plan de ChatGPT o Gemini hace video), `/corregir` (cuando la IA cambió tu
producto) y `/otro-formato` (la misma imagen en otra medida).

**Empieza por estos tres:** `/estudio`, `/poster-limpio` y `/oferta`.

## Cómo instalarla

### En Claude (app de celular, escritorio o claude.ai)

Sigue el asistente de instalación: https://manueldeleonm.com/recursos/fotos-de-producto-con-ia/

Si prefieres hacerlo a mano:
1. Descarga el archivo: https://github.com/m4nueldeleon/skills/releases/download/descargas/fotos-de-producto-con-ia.zip
2. En Claude, entra a **Configuración → Capacidades → Skills**.
3. Toca **Subir skill** y elige el archivo que descargaste (no lo abras ni lo descomprimas).
4. Revisa que quede activada.

Si no ves la sección Skills, activa en esa misma pantalla la opción de ejecución de código y creación de archivos.
Los nombres de los menús pueden cambiar con el tiempo.

### En Claude Code

```text
/plugin marketplace add m4nueldeleon/skills
/plugin install fotos-de-producto-con-ia@manuel-de-leon
```

### Sin instalar nada

Abre la lista de códigos (https://github.com/m4nueldeleon/skills/blob/main/plugins/fotos-de-producto-con-ia/skills/fotos-de-producto-con-ia/CODIGOS.md), copia el prompt del código que quieras, cambia lo que está entre [corchetes] y pégalo en ChatGPT
o Gemini con tu foto.

### Tu propio GPT o Gem (para escribir solo «/estudio»)

Sigue los pasos de https://github.com/m4nueldeleon/skills/blob/main/plugins/fotos-de-producto-con-ia/skills/fotos-de-producto-con-ia/GPT-Y-GEM.md. Lo creas una vez y desde ahí, en tu GPT o tu Gem, subes la foto, escribes el código y te
entrega la imagen. O pídeselo a Claude: «Ayúdame a crear mi GPT de fotos de producto».

## Cómo subir la foto en ChatGPT o Gemini

**En el celular:**
1. Abre ChatGPT o Gemini y empieza un chat nuevo.
2. Toca el **+** que está junto a la caja de texto.
3. Elige **Fotos** (o **Galería**) y selecciona la foto de tu producto.
4. Deja el dedo sobre la caja de texto, toca **Pegar** y envía.

**En la computadora:** arrastra la foto a la ventana del chat (o usa el **+**), pega el texto con Ctrl+V (o
Cmd+V en Mac) y presiona Enter.

Para guardar la imagen: deja el dedo sobre ella y toca **Guardar** (o el ícono de descarga).

Un producto por chat. Si cambias de producto, abre un chat nuevo para que no se mezclen.

## Prueba con estos mensajes

Sube tu foto a Claude y copia uno de estos (cambia lo que está entre [corchetes]):

**1. Panadería: foto para el catálogo**
```text
/estudio Tengo una panadería en [tu ciudad]. Te mando la foto de mi [pan: concha de chocolate]. La quiero para mi catálogo de WhatsApp.
```

**2. Tienda de ropa: promoción**
```text
/oferta Vendo [blusas bordadas] en [tu ciudad]. La oferta es [2 blusas por $650] hasta [el domingo 2 de noviembre]. Me piden por WhatsApp al [tu número]. Te mando la foto.
```

**3. Clínica dental: flyer (sirve para servicios)**
```text
/flyer-limpio Tengo una clínica dental. Te mando la foto de mi consultorio. Título: [Limpieza dental en 40 minutos]. Datos: [lunes a sábado, 9 a 7], [tu dirección], [WhatsApp tu número].
```

Claude te puede hacer una o dos preguntas. Contesta lo que sepas; lo demás lo decide con buen gusto y te lo dice.

## Qué esperar

- Claude te entrega el texto en un recuadro con botón **Copiar**, los pasos para pegarlo y una lista corta para
  revisar la imagen.
- ChatGPT o Gemini tardan uno o dos minutos en hacer cada imagen. Las versiones gratuitas tienen un límite de
  imágenes por día.
- A veces la IA cambia una letra de tu etiqueta o el color de la tapa. Para eso está `/corregir`: Claude ya te lo
  deja escrito.
- El mismo texto da una imagen distinta cada vez. Si no te gustó, pide «hazla otra vez» en el mismo chat.
- La medida puede salir un poco distinta a la que pediste. Recórtala con el editor de fotos de tu celular.

## Antes de publicar

Compara la imagen con tu producto real, de verdad, uno al lado del otro:

- ¿La etiqueta dice exactamente lo mismo, letra por letra?
- ¿Misma forma, color, tapa y contenido?
- ¿El texto del diseño (precio, horario, teléfono) está bien escrito?
- ¿Apareció algo que tu producto no tiene (un ingrediente, un sello, una pieza)?
- Si salen personas: ¿manos con cinco dedos y la cara igual a la real?

Si algo no coincide, no la publiques así. Tu cliente va a recibir el producto real, no la foto. Si la red social
te pregunta si la imagen se hizo con IA, contesta con la verdad.

En México, la publicidad que exagera o cambia lo que vendes puede considerarse engañosa ante Profeco; en Estados
Unidos, ante la FTC. Esto es orientación práctica, no asesoría legal.

## Enlaces oficiales

- [Código de esta skill (público)](https://github.com/m4nueldeleon/skills)
- [Instalar skills en Claude Code](https://code.claude.com/docs/en/skills)
