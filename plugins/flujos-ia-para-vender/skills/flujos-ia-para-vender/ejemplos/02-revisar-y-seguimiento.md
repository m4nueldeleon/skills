# Ejemplo 2 · REVISAR un mensaje y armar un SEGUIMIENTO

> **Negocios de ejemplo (ficticios).** Nombres, personas y cifras son inventados para mostrar cómo funciona la
> skill; cualquier parecido con un negocio real es coincidencia. Conversaciones simuladas en la app de Claude, sin
> búsqueda web. Hoy es martes 20 de octubre de 2026.

## A · Inmobiliaria: un asesor le escribe a un comprador

### Tú

REVISAR
Buenas tardes Sr. Ramírez, perdón que lo moleste otra vez 🙏. Nada más para ver si ya pensó lo de la casa de Valle Real. Somos la inmobiliaria líder en Zapopan con más de 15 años de experiencia y los mejores precios. Le puedo conseguir que el dueño se la deje más barata. ¡¡ÚLTIMA OPORTUNIDAD, ya hay otros interesados!! ¿No le interesaría ir a verla otra vez? ¿Le marco? Cualquier cosa me avisa.

### Claude

**Semáforo: ROJO** — el mensaje tiene 7 frenos. Supuse que lo que quieres es que acepte volver a ver la casa.

1. «perdón que lo moleste otra vez 🙏»
   Freno 1 · Pedir perdón por vender. Gastas el arranque en pedir permiso y lo importante llega después.
   Mejor: «Le escribo por la casa de Valle Real.»
2. «Nada más para ver si ya pensó lo de la casa»
   Freno 2 · Escribir sin traer nada. Le pides una respuesta sin darle un motivo nuevo para darla.
   Mejor: contarle algo que cambió (ver la pregunta de abajo).
3. «Somos la inmobiliaria líder en Zapopan con más de 15 años de experiencia y los mejores precios»
   Freno 8 · Hablar de ti antes que de él. Ya lo conoce; ahora le importa la casa. «Líder» y «los mejores
   precios» además no los puede comprobar.
   Mejor: quitarlo de este mensaje. Los 15 años guárdalos para cuando te pregunte por qué contigo.
4. «Le puedo conseguir que el dueño se la deje más barata»
   Freno 5 · Bajar el precio sin que te lo pidan. Y además no depende de ti: si el dueño no acepta, quedas mal.
   Mejor: no mencionar precio hasta que él lo pregunte.
5. «¡¡ÚLTIMA OPORTUNIDAD, ya hay otros interesados!!»
   Freno 7 · Presionar. Las mayúsculas y los signos se leen como grito.
   Mejor: depende de si es cierto (te pregunto abajo).
6. «¿No le interesaría ir a verla otra vez?»
   Freno 9 · Pregunta que invita al «no».
   Mejor: proponer un día y una hora concretos.
7. «Cualquier cosa me avisa»
   Freno 3 · Dejar el siguiente paso en el aire.
   Mejor: que el mensaje termine con una sola pregunta que se conteste en una línea.

**Forma:** ✔ lleva su nombre · ✘ tiene 2 preguntas (deja una) · ✘ en el celular pasa de 6 renglones · ✘ no queda
claro qué sigue · ✔ sin enlaces ni palabras raras

Antes de darte el mensaje corregido, una pregunta: ¿es cierto que hay otras personas interesadas en la casa?

### Tú

Sí hay otra pareja que la vio el sábado, pero todavía no han hecho oferta. Lo de los 15 años es cierto. El dueño no me ha dicho que la baje.

### Claude

Entonces lo de la otra pareja se queda, dicho tal cual, y lo del precio se va. Este es tu mensaje, corregido:

```text
Buenas tardes, Sr. Ramírez. Le escribo por la casa de Valle Real: el sábado la visitó otra pareja. Todavía no hay oferta, pero quería que lo supiera. ¿Le parece si la vemos de nuevo el [día] a las [hora]? Si no le acomoda, dígame qué día sí.
```

Pon en `[día]` y `[hora]` un horario que sí tengas libre. Quedó en unas 50 palabras (el original tenía unas 70).

Si no contesta en dos días, escribe 3 y armamos el seguimiento.

## B · Consultorio: un mensaje que ya está bien

### Tú

REVISAR
Hola, Paty. Te confirmo tu cita de mañana miércoles 21 a las 11 en el consultorio de la colonia Del Valle. ¿Sigue en pie? Si necesitas cambiarla, dime hoy y te busco otro horario.

### Claude

**Semáforo: VERDE** — mándalo así.

**Forma:** ✔ lleva su nombre · ✔ una sola pregunta · ✔ se lee sin bajar · ✔ queda claro qué sigue · ✔ sin enlaces
ni palabras raras

Bien hecho también: habla de la cita y no menciona el tratamiento. En WhatsApp eso cuida a Paty si alguien más ve su
teléfono.

## C · Consultorio dental: seguimiento de un presupuesto

### Tú

SEGUIMIENTO
A quién: Roberto
Qué le coticé: limpieza profunda y dos resinas, 4,800 pesos
Cuándo fue: el lunes 19 de octubre, en el consultorio
Qué quedó pendiente: dijo que lo iba a pensar por el precio
Algo nuevo y cierto que le puedo dar: aceptamos el pago en dos partes
Trato: de usted

### Claude

Con esto armo los tres. Una pregunta antes, para que el mensaje del día 3 traiga algo concreto: ¿qué horarios
libres tiene para su cita en los próximos días?

### Tú

El jueves 29 a las 10 de la mañana y el viernes 30 a las 5 de la tarde.

### Claude

## Seguimiento · Roberto

Ninguno de los mensajes menciona el tratamiento, solo su presupuesto y su cita: por WhatsApp otra persona puede
ver ese chat.

**Día 1 · hoy, martes 20 de octubre · Lo que quedó**

```text
Roberto, buenas tardes. Gracias por venir ayer al consultorio. Le comento algo que puede ayudarle con lo del presupuesto: se puede pagar en dos partes. ¿Quiere que le explique cómo quedarían los pagos?
```

Por qué funciona: contesta justo la duda que se llevó (el precio) y le pide algo fácil: un «sí».

**Día 3 · jueves 22 de octubre · Algo que le sirve**

```text
Roberto, buenos días. Para que lo tenga a la mano: tengo lugar para su cita el jueves 29 a las 10 de la mañana o el viernes 30 a las 5 de la tarde. ¿Le aparto alguno de los dos?
```

Por qué funciona: le quita el trabajo de buscar horario; contestar le toma una palabra.

**Día 7 · lunes 26 de octubre · Puerta abierta**

```text
Roberto, buenas tardes. Si prefiere dejar su presupuesto para más adelante, lo entiendo. Cuando quiera retomarlo, me escribe por aquí y le busco lugar. ¿Lo dejamos para otro momento?
```

Por qué funciona: le da permiso de decir que no sin quedar mal, y así le cuesta menos contestar. Después de este,
ya no se le escribe.

### Si le contesta...

- «Lo estoy pensando»
  ```text
  Claro, Roberto, tómese su tiempo. Para ayudarle: ¿lo que más le pesa es el monto o el momento?
  ```
- «Está caro»
  ```text
  Lo entiendo, Roberto. Por eso le comenté lo de las dos partes: serían dos pagos de [monto de cada pago]. ¿Se lo dejo así para su cita?
  ```
  Pon el monto real de cada pago; no supuse que fueran mitades iguales.
- «Ahorita no»
  ```text
  Muy bien, Roberto, gracias por decirme. ¿Le parece si le escribo a principios de [mes] para ver si ya le acomoda?
  ```
- «Sí, ¿cómo le hago?»
  ```text
  Qué gusto, Roberto. Le aparto el [día] a las [hora]. El primer pago se hace [cómo se paga: en el consultorio, por transferencia...]. ¿Se lo confirmo?
  ```

### Para que no se te olvide

Pon un recordatorio en tu celular para el jueves 22 y el lunes 26. En WhatsApp Business puedes ponerle a este chat
una etiqueta como «Seguimiento». Si Roberto contesta antes, ya no mandes los que faltan: respóndele a lo que dijo.

## D · Tienda de ropa: el mensaje del ejemplo 3 de la GUIA

### Tú

REVISAR
Hola!! Somos la boutique más completa de Tlaquepaque 😊 No sé si te interese, pero te tengo un descuentito en los vestidos de fiesta. ¿No te gustaría pasar a verlos?

### Claude

**Semáforo: ROJO** — es corto, pero trae 4 frenos y no lleva el nombre de la clienta. Supuse que se lo mandas a
alguien que ya te había comprado o preguntado.

1. «Somos la boutique más completa de Tlaquepaque»
   Freno 8 · Hablar de ti antes que de ella. Y «la más completa» no lo puede comprobar.
   Mejor: empezar por lo que a ella le sirve: los vestidos que llegaron.
2. «No sé si te interese»
   Freno 6 · Sonar inseguro. Si tú dudas que le interese, ella también.
   Mejor: decir por qué te acordaste de ella (algo que te haya contado).
3. «te tengo un descuentito»
   Freno 4 · Hacer chiquito lo que vendes, y freno 5 · ofrecer descuento sin que lo pida.
   Mejor: si es una promoción real de la tienda, dila con su tamaño y su fecha; si no, quítala.
4. «¿No te gustaría pasar a verlos?»
   Freno 9 · Pregunta que invita al «no».
   Mejor: proponer algo concreto que se conteste fácil.

**Forma:** ✘ no lleva su nombre · ✔ una sola pregunta · ✔ se lee sin bajar · ✘ no queda claro qué sigue · ✔ sin
enlaces ni palabras raras. Un detalle: con un signo de admiración basta.

**Tu mensaje, corregido:**

```text
Hola, [nombre]. Ya llegaron los vestidos de fiesta y me acordé de [lo que te contó: su boda en diciembre]. ¿Te aparto unos en tu talla para que te los midas el [día]?
```

Si la promoción es real, agrega al final: «Esta semana tienen [descuento] hasta el [fecha].»
