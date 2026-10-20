# Ejemplo real · Cocina Doña Lupe (negocio de ejemplo)

Conversación de prueba hecha siguiendo `SKILL.md` al pie de la letra. El negocio, el número y la cuenta son
ficticios. Resultado: `cocina-dona-lupe.html` (el video; ábrelo en el navegador). El MP4 y la hoja de contacto de
esta prueba no se incluyen para que el paquete pese menos: los generas tú con `scripts/exportar-mp4.mjs` y
`scripts/revisar.mjs`. La hoja de contacto de otro ejemplo está en `despacho-contable-rios-hoja.png`.

---

**Persona:** Hazme un video animado para mi negocio.

**Claude:** ¡Va! Te hago cinco preguntas rápidas, una por una. ¿Cómo se llama tu negocio, qué vendes y en qué ciudad
estás?

**Persona:** Cocina Doña Lupe. Vendemos comida corrida casera en Zapopan.

**Claude:** ¿Quién es tu cliente y qué problema le quitas o qué quiere lograr?

**Persona:** Gente que trabaja por la zona, en oficinas y comercios. Comen a las prisas, casi siempre algo rápido, y
quieren comer como en su casa sin gastar mucho.

**Claude:** ¿Qué quieres anunciar? Una promoción con precio y fecha, un servicio, o solo dar a conocer el negocio.
Si hay precio, dime qué incluye y las condiciones.

**Persona:** La comida corrida a 120 pesos: sopa, guisado, agua fresca y postre. Lunes a sábado de 1 a 5. También
para llevar.

**Claude:** ¿Tienes logo o colores? Si tienes logo, súbelo; si no, dime uno o dos colores que te gusten o propongo yo.

**Persona:** No tengo logo. Me gusta el naranja con gris oscuro.

**Claude:** Última: ¿cómo te contactan? Elige de 2 a 4: WhatsApp, teléfono, dirección o colonia, Instagram, horario.

**Persona:** WhatsApp 33 0000 0000, estamos en la colonia Centro de Zapopan, el horario que te dije y en Instagram
somos @cocinadonalupe.

**Claude:** *(entrega el artifact `cocina-dona-lupe.html`)*

Listo: tu video dura 17 segundos. Usé letra **directa** (Archivo Black, gruesa y fácil de leer en el celular) con
**gris oscuro y naranja terracota**, los colores que te gustan. No tienes logo, así que el nombre de tu cocina en letra
grande hace de logotipo.

| # | Escena | Texto | Seg. |
|---|---|---|---|
| 1 | Gancho | ¿Otra vez **comida rápida**? | 1.7 |
| 2 | Lo que ganas | Hoy come **como en casa** · Comida corrida casera en Zapopan | 2.4 |
| 3 | Tu marca | Cocina Doña Lupe · Comida corrida · Zapopan | 1.8 |
| 4 | Qué incluye | Sopa del día · Guisado casero · Agua fresca · Postre | 2.7 |
| 5 | Diferencia | ~~Comer a las prisas algo frío~~ → Plato **caliente**, servido al momento | 2.4 |
| 6 | Oferta | Lunes a sábado · Comida corrida **completa** · $120 por persona · De 1 a 5 pm · también para llevar | 2.8 |
| 7 | Cierre | Te esperamos **hoy** · WhatsApp, colonia, horario, Instagram · Pide por WhatsApp | 3.6 |

No puse años ni número de clientes porque no me los diste. Si tienes un dato real («desde 2009»), lo agregamos.

**Cómo grabarlo**

- **Antes:** en computadora, descarga el archivo (menú del video → Descargar) y ábrelo con doble clic; se ve grande y
  sin el chat. En el celular, grábalo ahí mismo en la app. Activa «No molestar».
- **Mac:** «Modo grabar» → Comando+Mayúsculas+5 → «Grabar parte seleccionada» → ajusta el recuadro al video → Grabar →
  toca el video → al final, botón de detener arriba.
- **Windows 11:** «Modo grabar» → Herramienta Recortes → Grabar → Nuevo → marca el área del video → Iniciar → toca el
  video → Detener.
- **iPhone:** Centro de control → Grabar pantalla → vuelve al video → «Modo grabar» → toca el video → al final, el
  punto rojo de arriba. En Fotos → Editar, recorta bordes, inicio y final.
- **Android:** panel rápido → Grabar pantalla → igual que en iPhone.

**Súbelo:** en Instagram crea un Reel con ese video, ponle música de la biblioteca de Instagram y en la descripción
escribe «Pide tu comida por WhatsApp: 33 0000 0000».

**¿Algo que cambiar?** Dímelo con tus palabras: «más lento», «quita el horario», «cambia el naranja por verde».

---

**Persona (en Claude Code):** expórtalo a MP4.

**Claude:** *(corre `scripts/revisar.mjs` → «Todo en orden», mira la hoja de contacto y luego
`scripts/exportar-mp4.mjs cocina-dona-lupe.html --calidad normal`)*

Listo: `cocina-dona-lupe.mp4`, 1080×1920, 30 cuadros por segundo, 17.4 s, 1 MB. Ya lo puedes subir tal cual.
