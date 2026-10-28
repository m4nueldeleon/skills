# Ejemplos de conversación

Respuestas escritas siguiendo `SKILL.md` al pie de la letra. Negocios de ejemplo: una tienda de
ropa, el restaurante La Cazuela y una estética. Los códigos que entregan página (mapa, apuntes,
tarjetas, examen) tienen su ejemplo en los archivos `.html` de esta carpeta.

---

## 1. El menú

**Usuario:** /codigos

**Claude:**

Estos son tus códigos. Escribe uno y, después, lo que quieres aprender.

**Para aprender tú**
• /mapa-del-libro + el libro → las ideas clave en un mapa para imprimir
• /apuntes + el tema → una hoja de apuntes visual
• /resumen-accion + el libro o tema → qué hacer el lunes en tu negocio
• /examiname + el tema → preguntas una por una, y te corrijo
• /tarjetas + el tema → tarjetas de repaso para practicar o imprimir
• /explicalo-simple + el tema → tú me lo explicas y te digo qué faltó

**Para tu equipo**
• /examen-del-equipo + tu manual o proceso → tarjetas y un examen con respuestas

Ejemplo: /mapa-del-libro Hábitos atómicos, de James Clear

---

## 2. Un libro que Claude no conoce bien

**Usuario:** /mapa-del-libro El método de la tortilla, de Ramiro Sandoval

**Claude:**

> Este libro no lo conozco lo suficiente y no quiero inventarte su contenido. Cuéntame con tus
> palabras 3 o 4 ideas que recuerdes, pégame tus notas o lo que subrayaste, o súbeme solo el índice
> o los capítulos que te interesan, y lo armo con eso.

*(El libro es inventado para la prueba: la skill no produce el mapa hasta tener material.)*

---

## 3. Piden copiar un capítulo

**Usuario:** Pásame completo el capítulo 1 de Hábitos atómicos.

**Claude:**

> Eso no te lo puedo copiar: el texto del libro tiene derechos de autor. Lo que sí puedo hacer es
> explicarte sus ideas con mis palabras: escribe /mapa-del-libro Hábitos atómicos y te armo el mapa
> de una hoja, o /apuntes para una hoja de apuntes de ese capítulo.

---

## 4. /resumen-accion

**Usuario:** /resumen-accion Hábitos atómicos. Tengo una tienda de ropa.

**Claude:**

Basado en lo que conozco del libro: verifica los detalles con tu ejemplar.

**Hábitos atómicos en una frase:** los resultados grandes salen de hábitos pequeños que repites
todos los días, y es más fácil repetirlos si cambias tu entorno que si dependes de tu fuerza de voluntad.

**Tus 3 acciones para el lunes**
1. **Escribe tu hábito apilado y pégalo en la caja**: «Después de abrir la cortina, contesto los
   mensajes pendientes». Cuándo: lunes a las 10:00, al abrir. Tiempo: 5 minutos. Sabrás que lo
   hiciste si: la hoja está pegada y el lunes en la noche no quedan mensajes sin contestar de la mañana.
2. **Guarda cinco respuestas para las preguntas de siempre** (precio, tallas, envíos, horario,
   apartados) en las respuestas rápidas de WhatsApp Business. Cuándo: lunes a las 16:00. Tiempo:
   20 minutos. Sabrás que lo hiciste si: contestas una pregunta de tallas con dos toques.
3. **Pega un calendario del mes junto a la caja** y palomea cada día que mandes un mensaje a quien
   preguntó y no compró. Cuándo: lunes al cerrar. Tiempo: 5 minutos. Sabrás que lo hiciste si: el
   lunes ya tiene su primera palomita.

**Lo que todavía NO vas a hacer:** rediseñar toda la tienda o tu Instagram. Primero que estos tres
se vuelvan automáticos.

**El viernes pregúntate:** ¿cuántas palomitas tiene el calendario y cuántos de esos mensajes
terminaron en una venta o en un apartado?

¿Quieres el mapa completo del libro para imprimir? Escribe /mapa-del-libro Hábitos atómicos.

---

## 5. /examiname

**Usuario:** /examiname margen de ganancia

**Claude:** Te voy a hacer 10 preguntas, una por una. Si no sabes una, escribe *paso*. Para
terminar antes, escribe *terminar*.

**Pregunta 1 de 10**
¿Qué es el margen de ganancia, dicho con tus palabras?

**Usuario:** Lo que le gano a cada cosa que vendo

**Claude:** **A medias.** Vas bien, pero falta lo importante: el margen es la ganancia **como parte
del precio de venta**. Si vendes en $350 algo que te costó $200, ganas $150, y tu margen es
150 ÷ 350 = 42.9 %.

**Pregunta 2 de 10**
Compras una playera en $150 y la vendes en $300. ¿Qué margen tienes?

**Usuario:** 100 %

**Claude:** **No.** El 100 % es lo que le subiste al costo (150 ÷ 150). El margen se divide entre el
precio: 150 ÷ 300 = **50 %**. Es la confusión más común: se parecen, pero son dos números distintos.

**Pregunta 3 de 10**
Quieres ganar 40 % de margen con un pantalón que te cuesta $120. ¿A cuánto lo vendes?

*(… sigue hasta la 10. Al final:)*

**Claude:** **Tu puntaje: 6.5 de 10**

Repasa en 2 días estas tres, que fueron las que más te costaron:
1. La diferencia entre margen y aumento sobre el costo.
2. Cómo sacar el precio para un margen exacto: costo ÷ (1 − margen).
3. Por qué el margen se calcula sin IVA.

¿Te hago tarjetas con lo que fallaste? Escribe /tarjetas.

---

## 6. /explicalo-simple (sin manual a la mano)

**Usuario:** /explicalo-simple cómo atender una queja en el restaurante

**Claude:**

> Explícame cómo atender una queja en el restaurante como se lo explicarías a alguien que hoy entra a
> trabajar contigo: de 5 a 8 renglones, sin ver tus notas. Luego te digo qué quedó claro y qué faltó.

**Usuario:** Pues que no se pelee con el cliente, que le pida una disculpa y que le diga al gerente.
Y que si es la comida se la cambiamos. Y que no le haga descuentos porque eso no le toca.

**Claude:**

**Lo que quedó claro:**
- No discutir con el cliente y disculparse.
- Ofrecer cambiar el platillo cuando la queja es de la comida.
- El mesero no hace descuentos.

**Lo que faltó o quedó confuso:**
- El primer paso: escuchar completo, sin interrumpir, antes de contestar.
- Cuándo llamar al gerente: tal como lo dijiste, suena a que siempre. Decide si es siempre o solo
  en ciertos casos, y dilo igual cada vez.

**Palabras que alguien nuevo quizá no entienda:** ninguna; lo dijiste claro.

**Tu versión de 1 minuto** (para decirla en la junta del lunes): «Si un cliente se queja, primero lo
escuchas completo, sin interrumpir. Le pides una disculpa y no discutes. Si es la comida, le
ofreces cambiar el platillo. Tú no haces descuentos. Y llamas al gerente [tú decides: siempre, o
solo si el cliente sigue molesto o pide un descuento].»

**Pregunta para comprobar que te entendieron:** «Si un cliente te dice que su carne llegó fría,
¿qué es lo primero que haces?»

Puedo revisar qué tan clara es tu explicación, no si es correcta: eso lo confirma tu manual o tú.
¿Lo intentas otra vez llenando los huecos?

---

## 7. Piden «una imagen»

**Usuario:** hazme una imagen con el mapa de ese libro

**Claude:**

> No hago fotos ni dibujos, pero te lo armo como página visual que puedes imprimir, guardar en PDF o
> capturar con el celular.

*(Y entrega el mapa, como en `mapa-del-libro-habitos-atomicos.html`.)*

---

## 8. Lo que acompaña al examen del equipo

Después de entregar `examen-del-equipo-restaurante.html` (hecho con el manual de
`entrada-manual-meseros.md`), en el chat:

> Listo: 16 tarjetas y un examen de 10 preguntas, sacados de tu manual del mesero.
>
> - Quité la clave de la tablet y el teléfono de la encargada: no deben ir en algo que se imprime
>   o se comparte.
> - Tu manual no deja claras dos cosas: si en grupos de 8 o más se sugiere propina (en «Cobro» dice
>   que no y en «Grupos» que sí) y qué hacer si falla la terminal. Resuelve estas dudas y te lo
>   rearmo sin el recuadro. No se lo compartas a tu equipo antes de eso.
> - Esta semana: día 1 entrega las tarjetas; días 2 a 6, cinco minutos al empezar el turno; día 7,
>   el examen impreso, sin la hoja de respuestas. El tema donde fallen alguna pregunta se repasa y
>   se repite en 2 días.
> - Para imprimir: todo va en el mismo archivo. En «Versión para imprimir» salen primero las
>   tarjetas, luego el examen y al final la hoja de respuestas. El día 1 imprime solo las hojas de
>   tarjetas; el día 7, quita la palomita de «Incluir la hoja de respuestas».
> - Por enlace o WhatsApp sirve para practicar, pero no es un examen de verdad: al calificar se ven
>   las respuestas y no se guarda nada. Es para saber qué repasar, no para calificar a nadie.

---

## 9. El manual no está escrito

**Usuario:** /examen-del-equipo tengo una estética y quiero examinar a las chicas de recepción, pero
no tengo nada escrito

**Claude:**

> Va. Cuéntame paso por paso cómo se hace en tu estética: cómo contestan el teléfono, cómo
> agendan, qué hacen cuando llega una clienta y cómo cobran. Puedes dictármelo con el micrófono o
> mandarme fotos de tus hojas.

**Usuario:** *(dicta durante dos minutos cómo agendan, confirman y cobran)*

**Claude:** devuelve primero el manual en limpio, con secciones («Contestar», «Agendar»,
«Confirmar», «Cobrar»), pasos cortos y lo que faltó marcado como «[pendiente: ¿qué hacen si la
clienta llega más de 15 minutos tarde?]», y pregunta:

> ¿Está bien así? Corrige lo que haga falta y con eso armo el examen.

*(El examen se arma hasta que la dueña lo aprueba.)*
