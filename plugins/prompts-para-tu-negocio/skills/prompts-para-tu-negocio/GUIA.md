# 36 prompts para tu negocio

Manuel de León · Recursos de IA para negocios · 20 de octubre de 2026

Treinta y seis instrucciones para que la IA te ayude a atraer clientes, vender, atender y operar tu negocio. La
número 10 te dice si vendes una solución, conveniencia o una experiencia, y te escribe tu oferta en una frase.

## Qué hace

Un prompt es la instrucción que le escribes a la IA. Si le escribes «ayúdame con mi negocio», te contesta cualquier
cosa. Si le dices qué vendes, a quién, dónde y qué quieres exactamente, te entrega algo que puedes usar hoy.

Esta biblioteca tiene 36 prompts escritos para negocios reales y pequeños (un restaurante, una clínica dental, una
inmobiliaria, una tienda de ropa, un despacho contable, un coach), en cuatro áreas de nueve:

| Área | Prompts | Para qué |
|---|---|---|
| **Atraer clientes** | 1 a 9 | Qué publicar, qué grabar, tu ficha de Google, anuncios, promociones, alianzas |
| **Vender** | 10 a 18 | Tu oferta, tus paquetes, el «¿cuánto cuesta?», objeciones y seguimiento |
| **Atender** | 19 a 27 | WhatsApp, reseñas, quejas, recordatorios y clientes que regresan |
| **Operar** | 28 a 36 | Procesos, equipo, cuánto te deja cada venta, tu dinero y tus gastos |

Hay dos formas de usarla:

- **Con la skill instalada (lo más fácil).** Una skill es un paquete de instrucciones que le instalas a Claude una
  sola vez para que sepa hacer un trabajo; esta trae los 36 prompts adentro. Claude te hace tres preguntas (qué vendes, a quién y en qué ciudad y
  país), te enseña el menú de los 36 y tú eliges por número o le cuentas qué te urge. Claude llena el prompt con
  tus datos y lo hace por ti.
- **Copiando y pegando.** Abajo está la biblioteca completa. Copias el prompt, cambias lo que está entre
  [CORCHETES] y lo pegas en Claude, ChatGPT o Gemini.

## Instálala

Sigue el asistente de instalación: https://manueldeleonm.com/recursos/prompts-para-tu-negocio/

Si prefieres hacerlo a mano:

**En Claude (app de escritorio, celular o claude.ai)**

1. Descarga el ZIP: https://github.com/m4nueldeleon/skills/releases/download/descargas/prompts-para-tu-negocio.zip
   No lo descomprimas.
2. En Claude, entra a **Configuración → Capacidades** y enciende **Ejecución de código y creación de archivos**.
   La skill la necesita para leer su biblioteca.
3. Abre **Personalizar → Skills**, toca **+**, elige **Crear skill → Subir una skill** y escoge el ZIP.
4. Revisa que el interruptor de la skill quede encendido.

Si no ves la opción de Skills, puede que tu plan de Claude todavía no la tenga. No pasa nada: usa la biblioteca
copiando y pegando (más abajo).

**En Claude Code**

```text
/plugin marketplace add m4nueldeleon/skills
/plugin install prompts-para-tu-negocio@manuel-de-leon
```

Confirma en el panel que se abre y escribe `/reload-plugins` (o reinicia Claude Code).

**En un Proyecto de Claude o de ChatGPT, o en un Gem de Gemini**

Pega el texto de `SKILL.md` en las instrucciones del Proyecto (o del Gem) y sube este archivo, `GUIA.md`, como
archivo del Proyecto. Así la IA tiene las instrucciones y la biblioteca.

## Antes de empezar: tus tres respuestas

Tenlas a la mano. Son las mismas para los 36 prompts:

1. **Qué vendes.** Como se lo dirías a un vecino. «Limpiezas, blanqueamientos y ortodoncia para toda la familia.»
2. **A quién le vendes.** Tu cliente de todos los días. «Mamás de 30 a 50 años que traen a toda la familia.»
3. **En qué ciudad y país.** Si vendes en línea, dónde están tus clientes. «Querétaro, México.»

Con eso basta para empezar. Si un prompt necesita algo más (tu precio, el mensaje de un cliente, tus números),
Claude te lo pide en ese momento, una cosa a la vez.

## 3 ejemplos listos para copiar

Cambia lo que está entre [corchetes] por lo tuyo. Si la skill no se activa sola, empieza tu mensaje con «Usa la
skill prompts-para-tu-negocio».

**1. Ver el menú completo**

```text
Quiero usar los 36 prompts para mi negocio. Vendo [qué vendes] a [a quién le vendes]
en [ciudad y país]. Enséñame el menú y recomiéndame por cuál empezar.
```

Claude te muestra tus datos para que los corrijas, el menú de los 36 y tres recomendados para tu tipo de negocio.

**2. Tu oferta en una frase**

```text
Ayúdame con mi oferta en una frase: quiero saber si vendo una solución, conveniencia
o una experiencia. Tengo [tu negocio] en [ciudad y país].
```

Claude te pregunta lo que falte, te hace cinco preguntas sobre tus clientes (una por una), te dice cuál de las tres
vendes y te entrega tres versiones de tu oferta en una frase.

**3. Un cliente molesto**

```text
Me escribió un cliente molesto y no sé qué contestarle. Tengo [tu negocio] en
[ciudad y país]. Esto me escribió: [pega su mensaje, sin su nombre ni su teléfono].
```

Claude va directo al prompt 23: te pregunta tu versión de lo que pasó y qué puedes ofrecerle, y te da la respuesta
lista, una versión para nota de voz y lo que no debes decir.

También puedes pedir por número: «Hazme el 33 con mis números».

## Qué esperar

- **Tres preguntas, una por mensaje.** Si ya las contestaste en tu primer mensaje, no te las repite.
- **El menú.** Tus 36 prompts en cuatro áreas, y tres recomendados para tu tipo de negocio.
- **El trabajo hecho.** Textos listos para copiar (mensajes de WhatsApp, publicaciones, guiones, tablas), con tus
  datos. Al final te dice qué supuso, qué debes revisar antes de usarlo y qué prompt te conviene después.
- **Tus datos se quedan en la conversación.** Para el siguiente prompt ya no te pregunta lo mismo.

Lo que no hace: no publica, no manda mensajes por ti, no inventa reseñas, testimonios ni cifras, y no promete
ventas. En los prompts de dinero (33 a 36), de equipo (30 y 31) y de cobranza (35) te da orientación práctica: no
sustituye a tu contador ni a un abogado.

Revisa todo antes de usarlo. Léelo en voz alta: si una palabra no la dirías tú, cámbiala.

## Úsala sin instalar nada

1. Busca el prompt que necesitas en la biblioteca de abajo.
2. Cópialo completo.
3. Cambia las tres primeras líneas por tus respuestas y llena los demás [CORCHETES]. Si un corchete dice
   OPCIONAL y no tienes el dato, bórralo.
4. Pégalo en Claude, ChatGPT o Gemini y envíalo. Si te hace preguntas, contéstalas.

Todos los prompts terminan pidiendo que la IA te pregunte antes de inventar un dato. Déjalo así.

---

## Biblioteca · Atraer clientes (prompts 1 a 9)

### 1. Treinta ideas de contenido que salen de tus clientes

Para qué: cuando no sabes qué publicar.

```text
Mi negocio: [QUÉ VENDES]
Mis clientes: [A QUIÉN LE VENDES]
Dónde estoy: [CIUDAD Y PAÍS]

Quiero dejar de improvisar mis publicaciones. Primero haz una lista de las
15 preguntas, dudas y miedos que más probablemente tiene mi cliente antes
de comprarme: las que se hace en su cabeza, no solo las que me dice. Si te
doy algunas reales, empieza por esas: [PREGUNTAS QUE TE HACEN SEGUIDO, OPCIONAL].

Con esa lista dame 30 ideas de publicaciones. Para cada una: un título de
máximo 10 palabras como lo diría yo en voz alta, el formato que conviene
(video corto, foto con texto, carrusel o historia) y la pregunta del cliente
que contesta. Ordénalas de la más fácil de hacer hoy con mi celular a la más
elaborada. Nada de frases motivacionales: cada idea tiene que enseñar algo,
resolver una duda o mostrar mi trabajo.

Si te falta un dato para hacerlo bien, pregúntame antes de inventarlo.
```

### 2. Cinco videos de 30 segundos para grabar con tu celular

Para qué: cuando quieres grabar pero no sabes qué decir.

```text
Mi negocio: [QUÉ VENDES]
Mis clientes: [A QUIÉN LE VENDES]
Dónde estoy: [CIUDAD Y PAÍS]

Escríbeme 5 guiones de video de 30 segundos que yo pueda grabar solo, con mi
celular, en mi negocio. Tema: [PRODUCTO O TEMA QUE QUIERES MOSTRAR, OPCIONAL].
Si no te doy tema, elige los 5 que más le sirven a mi cliente.

Cada guion en este orden:
1. La primera frase (máximo 12 palabras) para que mi cliente deje de
   deslizar: una pregunta, un error común o algo de mi oficio que yo sí sé.
2. Lo que digo después, en frases cortas, como le hablo a un cliente en persona.
3. Qué se ve en cada parte: dónde me paro, qué enseño, qué toma extra grabo.
4. El texto que pongo encima del video (máximo 6 palabras).
5. Una sola invitación al final: escribirme por WhatsApp, visitarme o agendar.

Que cada uno se pueda grabar en menos de 15 minutos, sin luces ni equipo
especial. No inventes datos ni resultados de clientes: si un guion necesita
un número, déjalo entre corchetes para que yo lo ponga.
```

### 3. Tu historia en tres tamaños

Para qué: tu perfil, presentarte en persona y un video sobre ti.

```text
Mi negocio: [QUÉ VENDES]
Mis clientes: [A QUIÉN LE VENDES]
Dónde estoy: [CIUDAD Y PAÍS]

Ayúdame a contar por qué existe mi negocio. Primero hazme estas preguntas,
una por una, y espera mi respuesta: ¿cómo empezaste?, ¿qué problema viste que
nadie resolvía bien?, ¿qué momento difícil casi te hace dejarlo?, ¿qué cliente
te hizo sentir que valió la pena?, ¿qué haces distinto hoy?

Con mis respuestas escribe mi historia en tres tamaños:
1. Una línea para mi perfil de Instagram, Facebook o WhatsApp (máximo
   150 caracteres).
2. Lo que digo en 30 segundos cuando alguien me pregunta «¿a qué te dedicas?»
   en una reunión o un evento.
3. Un guion de video de 60 segundos que empiece por el momento difícil y
   termine en lo que hago hoy por mis clientes.

Usa solo lo que yo te cuente. Nada de frases como «apasionados por la
excelencia». Que suene a persona, no a folleto.
```

### 4. Tu ficha de Google para que te encuentren cerca

Para qué: si tienes local, consultorio u oficina, o atiendes una zona.

```text
Mi negocio: [QUÉ VENDES]
Mis clientes: [A QUIÉN LE VENDES]
Dónde estoy: [CIUDAD Y PAÍS]
Colonias, zonas o ciudades que atiendo: [ZONA, OPCIONAL]

Quiero que me encuentren cuando alguien busca lo que vendo en Google y en
Google Maps. Dame:
1. La descripción de mi Perfil de Negocio de Google (máximo 750 caracteres):
   qué hago, para quién, en qué zona y qué me hace diferente, con las palabras
   que mi cliente escribiría al buscar. Sin repetir palabras a la fuerza.
2. La categoría principal que me conviene y hasta tres adicionales, y por qué.
3. Diez productos o servicios con nombre claro y una línea de descripción.
4. Cinco publicaciones cortas para la ficha (una novedad, una oferta, una
   pregunta frecuente…) para subir una por semana.
5. Las 10 fotos que debería subir (fachada, interior, equipo, trabajo
   terminado…) y cómo tomarlas con el celular.

No inventes horarios, teléfonos ni dirección: déjalos entre corchetes. Al
final dime los 3 errores más comunes por los que un negocio local no aparece
en Maps. Si te falta un dato, pregúntame antes de inventarlo.
```

### 5. Un anuncio para Facebook e Instagram en tres versiones

Para qué: cuando vas a pagar publicidad y quieres probar qué mensaje funciona.

```text
Mi negocio: [QUÉ VENDES]
Mis clientes: [A QUIÉN LE VENDES]
Dónde estoy: [CIUDAD Y PAÍS]
Lo que quiero anunciar: [PRODUCTO, SERVICIO O PROMOCIÓN, CON PRECIO SI LO HAY]
Lo que quiero que haga la persona: [ESCRIBIR POR WHATSAPP, AGENDAR, VISITAR O COMPRAR]

Escribe un anuncio en tres versiones distintas para probarlas al mismo tiempo:
- Versión A: empieza por el problema que vive mi cliente, con sus palabras.
- Versión B: empieza por el antes y el después de comprarme, sin exagerar.
- Versión C: empieza por una prueba que yo sí tengo: [AÑOS, TRABAJOS HECHOS
  O UNA RESEÑA REAL, OPCIONAL].

Para cada versión: la primera línea (lo único que se lee sin tocar «ver más»),
el texto completo de máximo 90 palabras, un título de máximo 40 caracteres,
la idea de la imagen o el video, y el botón que conviene.

Después, en palabras sencillas: a quién mostrárselo (edad, zona alrededor de
mi negocio, intereses) y cómo saber en 5 días cuál versión ganó, contando
mensajes o citas, no «me gusta».

Reglas: no señales defectos ni situaciones personales del cliente («¿tienes
deudas?», «¿sufres de sobrepeso?»), no prometas resultados de salud o de
dinero y no inventes testimonios. Si vendo casas, crédito o publico una
vacante, avísame que Meta pide declararlo como categoría especial.
```

### 6. Las fechas fuertes del año sin rematar tu precio

Para qué: planear promociones con tiempo, sin regalar tu ganancia.

```text
Mi negocio: [QUÉ VENDES]
Mis clientes: [A QUIÉN LE VENDES]
Dónde estoy: [CIUDAD Y PAÍS]

Hazme el calendario de las 12 fechas que más pueden mover las ventas de mi
negocio en los próximos 12 meses, según mi país y mi tipo de cliente: fechas
comerciales, días festivos, regreso a clases, temporadas de calor o de
lluvias, días de pago fuertes (como el aguinaldo o la devolución de
impuestos). En orden de mes.

Para cada fecha:
1. Por qué le importa a mi cliente.
2. Una promoción que NO sea solo bajar el precio: un paquete, un regalo que
   me cueste poco y valga mucho para el cliente, un servicio extra, una fecha
   límite real o un apartado.
3. Cuántos días antes empiezo a anunciarla.
4. Un mensaje corto de WhatsApp para anunciarla.

Marca como PRIORIDAD las 3 fechas en las que más me conviene enfocarme. Si
no estás seguro de una fecha en mi ciudad, dímelo para que yo la confirme.
```

### 7. Clientes prestados: alianzas con negocios de tu zona

Para qué: conseguir clientes a través de negocios que ya atienden a tu cliente.

```text
Mi negocio: [QUÉ VENDES]
Mis clientes: [A QUIÉN LE VENDES]
Dónde estoy: [CIUDAD Y PAÍS]

Quiero conseguir clientes a través de otros negocios que atienden a mi mismo
cliente sin competir conmigo. Dame:
1. Diez tipos de negocio de mi zona que me conviene tener de aliados, y qué
   cliente compartimos con cada uno.
2. Tres formas de alianza sencillas (recomendarnos uno al otro, un paquete
   juntos, una clase o evento en conjunto) y con cuál empezar.
3. El mensaje de WhatsApp para proponerle la alianza al dueño: que se lea en
   20 segundos, que hable primero de lo que gana él y que termine pidiendo un
   café de 15 minutos.
4. Cómo llevar la cuenta de quién mandó a quién, sin sistemas complicados.

Nada de contratos ni comisiones enredadas: algo que dos dueños acuerden en una
plática. Si hay dinero de por medio, recuérdame ponerlo por escrito. Si te
falta un dato, pregúntame antes de inventarlo.
```

### 8. Tu lista de difusión de WhatsApp sin parecer spam

Para qué: mantenerte presente con tus clientes sin que te bloqueen.

```text
Mi negocio: [QUÉ VENDES]
Mis clientes: [A QUIÉN LE VENDES]
Dónde estoy: [CIUDAD Y PAÍS]
Cómo les hablo a mis clientes: [FORMAL, CERCANO, CON HUMOR, OPCIONAL]

Tengo clientes en WhatsApp y no quiero que me bloqueen. Escríbeme 4 semanas
de mensajes para mi lista de difusión, uno por semana:
- Semana 1: algo útil de mi oficio que el cliente pueda usar hoy.
- Semana 2: algo de lo que pasa en mi negocio que el cliente no ve.
- Semana 3: una novedad o un producto, con precio claro y cómo pedirlo.
- Semana 4: una pregunta para que me contesten y saber qué quieren.

Cada mensaje de máximo 60 palabras, y al final una línea que diga cómo salir
de la lista. Agrega 3 reglas para no saturar a mi gente: cada cuánto mandar,
a qué hora y qué nunca mandar. Recuérdame que solo le escriba a quien me dio
su número y aceptó mensajes, y que la lista de difusión solo le llega a quien
tiene guardado mi número.
```

### 9. Revisa tu publicación o anuncio antes de subirlo

Para qué: una segunda opinión antes de publicar.

```text
Mi negocio: [QUÉ VENDES]
Mis clientes: [A QUIÉN LE VENDES]
Dónde estoy: [CIUDAD Y PAÍS]

Antes de publicar esto, revísalo como si fueras mi cliente con prisa:
[PEGA AQUÍ TU TEXTO O DESCRIBE TU IMAGEN O VIDEO]

Dime, en este orden:
1. Si en la primera línea (o los primeros 3 segundos) queda claro para quién
   es y qué gana.
2. Qué palabra o frase sobra, confunde o suena a anuncio genérico.
3. Si se entiende qué tiene que hacer la persona después, y si es una sola
   acción.
4. Si prometo algo que no puedo comprobar.
Califícalo del 1 al 10 en claridad y dime qué le falta para el 10.

Luego dame dos versiones mejoradas: una corta y otra del mismo largo que la
mía. Conserva mis datos, precios y condiciones tal como están; no agregues
promesas ni cifras.
```

## Biblioteca · Vender (prompts 10 a 18)

### 10. Tu oferta en una frase: ¿solución, conveniencia o experiencia?

Para qué: cuando no sabes explicar lo que vendes o todos te comparan por precio.

```text
Mi negocio: [QUÉ VENDES]
Mis clientes: [A QUIÉN LE VENDES]
Dónde estoy: [CIUDAD Y PAÍS]
Precio aproximado: [PRECIO, OPCIONAL]
Mi competencia más cercana: [QUIÉN MÁS VENDE ALGO PARECIDO CERCA DE MÍ, OPCIONAL]

La gente paga por tres cosas: que le quiten un problema (una solución), que le
ahorren tiempo o esfuerzo (conveniencia) o sentir algo que no encuentra en otro
lado (una experiencia). Ayúdame a saber cuál de las tres vendo yo.

1. Hazme estas 5 preguntas, una por una, esperando mi respuesta: ¿qué problema
   tenía tu cliente antes de comprarte?, ¿qué tiempo o qué molestia le
   ahorras?, ¿qué siente cuando te compra?, ¿por qué te elige a ti y no al de
   al lado?, ¿qué te dicen los clientes que más te quieren?
2. Con mis respuestas, dime qué vendo de verdad: solución, conveniencia o
   experiencia. Si son dos o tres, dime cuál pesa más. Explícalo en dos líneas
   con mis propias palabras.
3. Dime en cuál de las tres puedo ser el mejor de mi zona y qué tendría que
   reforzar para lograrlo.
4. Escribe mi oferta en una sola frase, con la forma que corresponda:
   - Solución: «Te quito [el problema] para que [el resultado]».
   - Conveniencia: «[Lo que necesitas], [más rápido, más fácil o sin moverte]».
   - Experiencia: «[Lo que vas a sentir o vivir] como en ningún otro lado».
   Dame 3 versiones y recomiéndame una.
5. Dime cómo probar la frase: decírsela a 5 clientes y preguntarles qué
   entendieron.

No uses palabras como «calidad», «excelencia» o «el mejor servicio»: todos las
dicen. Si una frase promete algo que yo no puedo cumplir, cámbiala.
```

### 11. Tu oferta completa en una hoja

Para qué: que cualquiera entienda qué recibe y por qué vale lo que cuesta.

```text
Mi negocio: [QUÉ VENDES]
Mis clientes: [A QUIÉN LE VENDES]
Dónde estoy: [CIUDAD Y PAÍS]
Lo que vendo y su precio: [PRODUCTO O SERVICIO Y PRECIO]

Ayúdame a armar mi oferta completa en una sola hoja. Hazme las preguntas que
necesites, una por una, y después escribe:
1. Para quién es y para quién NO es (3 líneas cada una).
2. Cómo está mi cliente antes y cómo queda después, sin exagerar.
3. Qué incluye, en lista, y qué logra el cliente con cada parte (no
   «3 sesiones», sino qué logra en esas 3 sesiones).
4. Cuánto le costaría resolverlo por su cuenta o de otra forma, para que
   compare.
5. Formas de pago que podría ofrecer (contado, apartado, pagos) y cuál me
   conviene.
6. Un bono que conteste una duda real del cliente antes de comprar. Si no
   contesta ninguna duda, no sirve.
7. Una garantía que yo sí pueda cumplir, o una forma de bajarle el riesgo al
   cliente.
8. Una fecha límite o un cupo que sea verdad. Si no hay una razón real para la
   prisa, dime que no la ponga.

Al final dime qué parte de mi oferta está más débil y cómo la fortalezco esta
semana. No inventes datos: si te falta uno, pregúntame.
```

### 12. Tres paquetes: básico, recomendado y completo

Para qué: dejar de tener un solo precio.

```text
Mi negocio: [QUÉ VENDES]
Mis clientes: [A QUIÉN LE VENDES]
Dónde estoy: [CIUDAD Y PAÍS]
Lo que vendo hoy y su precio: [PRODUCTO O SERVICIO Y PRECIO]
Lo que me cuesta darlo: [COSTO APROXIMADO, OPCIONAL]

Diséñame 3 paquetes:
- Básico: la puerta de entrada, para quien quiere probar o trae poco
  presupuesto.
- Recomendado: el que quiero que elija la mayoría.
- Completo: para quien quiere todo resuelto y paga por no preocuparse.

Para cada uno: nombre sencillo, qué incluye, precio sugerido en la moneda de
mi país y para quién es. Explícame por qué el recomendado se ve como la mejor
decisión al ponerlos lado a lado. Si te di mis costos, revisa que cada paquete
me deje ganancia y avísame si alguno me hace perder.

Después escribe cómo presentarlos en un solo mensaje claro de WhatsApp. No
inventes precios de la competencia; si necesitas compararme, pregúntame.
```

### 13. Responde «¿cuánto cuesta?» sin quedarte en visto

Para qué: cuando te escriben «¿precio?» y desaparecen.

```text
Mi negocio: [QUÉ VENDES]
Mis clientes: [A QUIÉN LE VENDES]
Dónde estoy: [CIUDAD Y PAÍS]
Mi precio: [PRECIO O RANGO]
Cómo les hablo a mis clientes: [FORMAL, CERCANO, CON HUMOR, OPCIONAL]

Mucha gente me escribe solo «¿precio?» o «info» y cuando le mando el número
desaparece. Escríbeme:
1. Tres respuestas para ese primer mensaje. Cada una da el precio o un rango
   claro (no lo escondas) y termina con una pregunta fácil de contestar que me
   ayude a entender qué necesita.
2. El segundo mensaje, cuando ya me contestó: qué incluye, por qué vale eso y
   el siguiente paso concreto (apartar, agendar, pasar a ver).
3. Un mensaje para cuando me dice «está caro», que no ruegue ni baje el precio
   de inmediato.
4. El texto de una nota de voz de 30 segundos para quien prefiere audio.

Mensajes cortos para WhatsApp o mensaje directo. Sin presión y sin «última
oportunidad» falsa. Si te falta un dato, pregúntame antes de inventarlo.
```

### 14. Tu «prueba de manejo»: una muestra que convierte

Para qué: que el cliente pruebe antes de comprar lo completo.

```text
Mi negocio: [QUÉ VENDES]
Mis clientes: [A QUIÉN LE VENDES]
Dónde estoy: [CIUDAD Y PAÍS]

Antes de comprar un carro te dejan manejarlo. Quiero diseñar mi propia
«prueba de manejo»: algo pequeño, gratis o muy barato, que deje al cliente
probar lo que vendo y le dé ganas de comprar lo completo. Puede ser una
muestra, una clase, un diagnóstico, una visita, una consulta corta o una
demostración.

1. Dame 5 ideas de prueba para mi negocio y elige la mejor, con lo que me
   cuesta en tiempo y en dinero.
2. De la elegida: cómo se llama, cuánto dura, qué vive el cliente paso a paso
   y en qué momento exacto le presento la compra completa (con qué frase).
3. Cómo invitar a la gente: un mensaje para WhatsApp y un texto para redes.
4. Qué anotar después de cada prueba para saber si funciona: cuántos la
   hicieron y cuántos compraron.

Que no se sienta como trampa: el cliente tiene que salir ganando aunque no
compre. Si te falta un dato, pregúntame antes de inventarlo.
```

### 15. Guion para tu cita o llamada de venta

Para qué: llegar a la cita con un orden y salir con una decisión.

```text
Mi negocio: [QUÉ VENDES]
Mis clientes: [A QUIÉN LE VENDES]
Dónde estoy: [CIUDAD Y PAÍS]
Lo que ofrezco en la cita y su precio: [PRODUCTO O SERVICIO Y PRECIO]

Escríbeme un guion para mis citas o llamadas de venta de 20 a 30 minutos, en
tres partes:
1. Que me conozca y me crea (5 minutos): cómo saludo, qué cuento de mí sin
   presumir y qué pregunta abre la plática.
2. Entender a la persona (10 a 15 minutos): 8 preguntas, en orden, para saber
   qué quiere lograr, qué ha intentado, qué pasa si no lo resuelve, quién más
   decide y cuánto está dispuesto a invertir. Junto a cada pregunta, para qué
   la hago.
3. Proponer (5 a 10 minutos): cómo resumo lo que me dijo con sus palabras,
   cómo presento mi oferta como respuesta a eso, cómo digo el precio sin pedir
   perdón y cómo pido la decisión.

Incluye qué hago si me dice que no o que lo va a pensar, y cómo termino la cita
con el siguiente paso y una fecha. Tono de plática, no de vendedor de película.
No inventes datos de mi negocio: si te falta uno, pregúntame.
```

### 16. Las 8 objeciones de tus clientes y cómo contestarlas

Para qué: «está caro», «lo voy a pensar», «lo consulto en mi casa».

```text
Mi negocio: [QUÉ VENDES]
Mis clientes: [A QUIÉN LE VENDES]
Dónde estoy: [CIUDAD Y PAÍS]
Mi precio: [PRECIO]
Lo que más me dicen para no comprar: [LO QUE TE HAN DICHO, OPCIONAL]

Haz la lista de las 8 razones más probables por las que alguien que sí
necesita lo que vendo no me compra. Empieza por las que yo te di. Por ejemplo:
«está caro», «lo voy a pensar», «lo tengo que hablar con mi pareja», «lo vi
más barato», «no tengo tiempo», «no sé si me va a funcionar».

Para cada una:
1. La duda real que probablemente hay detrás.
2. Una pregunta que hago antes de contestar, para entender.
3. La respuesta, en máximo 3 frases, como la diría en persona o por WhatsApp.
4. Qué puedo cambiar en mi oferta o en cómo la explico para que esa objeción
   salga menos.

Nada de trucos de presión ni de hacer sentir mal al cliente. Si una objeción
es válida (de verdad no es para él), dime cómo decírselo con honestidad.
```

### 17. Seguimiento de 5 toques a quien no contestó

Para qué: recuperar a quien pidió información y dejó de contestar.

```text
Mi negocio: [QUÉ VENDES]
Mis clientes: [A QUIÉN LE VENDES]
Dónde estoy: [CIUDAD Y PAÍS]
Lo que esa persona me preguntó o le coticé: [PRODUCTO, SERVICIO O COTIZACIÓN]

Muchas ventas se me van porque no le doy seguimiento a quien preguntó y no
compró. Escríbeme 5 mensajes de WhatsApp para alguien que pidió información y
dejó de contestar:
- Día 1: confirmo lo que hablamos y resuelvo una duda que seguro tiene.
- Día 3: le mando algo útil (una foto de un trabajo, un consejo), sin pedirle
  nada.
- Día 7: una pregunta directa y amable para saber en qué quedó.
- Día 14: una razón nueva para decidir ahora, solo si es verdad (un cambio de
  precio, un cupo, la temporada).
- Día 30: una despedida sin reproches, para que me busque cuando lo necesite.

Máximo 50 palabras por mensaje, con espacio para su nombre, y que no suene a
robot ni a cobranza. Dime también qué contesto si responde en cualquiera de
los pasos. Si te falta un dato, pregúntame antes de inventarlo.
```

### 18. Qué ofrecerle a quien ya te compró

Para qué: la siguiente venta, sin ser encimoso.

```text
Mi negocio: [QUÉ VENDES]
Mis clientes: [A QUIÉN LE VENDES]
Dónde estoy: [CIUDAD Y PAÍS]
Lo que más me compran: [TUS 3 PRODUCTOS O SERVICIOS MÁS VENDIDOS, CON PRECIO]

Es más fácil venderle a quien ya confió en mí. Ayúdame a ofrecer lo correcto
después de cada compra:
1. Para cada producto o servicio que te di: qué es lo siguiente que ese
   cliente probablemente va a necesitar y cuándo (al día, al mes, a los
   6 meses).
2. El mensaje para ofrecerlo en ese momento, que empiece preguntando cómo le
   fue con lo que ya compró.
3. Una forma de premiar al cliente que vuelve que no sea solo descuento.
4. Qué anotar de cada cliente (qué compró y cuándo) para saber a quién
   escribirle, en una libreta o una hoja de cálculo sencilla.

Si algo no tiene una siguiente compra natural, dímelo en vez de forzarla.
```

## Biblioteca · Atender (prompts 19 a 27)

### 19. Respuestas rápidas para WhatsApp Business

Para qué: contestar rápido sin sonar a robot.

```text
Mi negocio: [QUÉ VENDES]
Mis clientes: [A QUIÉN LE VENDES]
Dónde estoy: [CIUDAD Y PAÍS]
Mi horario, ubicación y formas de pago: [DATOS, O DÉJALOS PARA LLENAR DESPUÉS]

Escríbeme:
1. El mensaje de bienvenida (para quien me escribe por primera vez) y el
   mensaje de ausencia (fuera de horario), de máximo 40 palabras cada uno.
2. Las 12 preguntas que más probablemente me hacen (horario, ubicación,
   precio, formas de pago, envíos, citas, garantía, factura…), cada una con
   una respuesta corta lista para guardar como respuesta rápida, y su atajo
   (por ejemplo /horario).
3. Tres mensajes para pasar de la duda a la venta: cuando ya preguntó el
   precio, cuando pide fotos y cuando quiere apartar.

Donde falte un dato mío, déjalo entre corchetes: no inventes horarios,
direcciones ni precios. Al final explícame en 4 pasos cómo guardar las
respuestas rápidas en WhatsApp Business, y si los menús cambiaron, qué buscar.
```

### 20. Lo que pasa después de que te pagan

Para qué: que tu cliente se sienta seguro de su decisión desde el primer minuto.

```text
Mi negocio: [QUÉ VENDES]
Mis clientes: [A QUIÉN LE VENDES]
Dónde estoy: [CIUDAD Y PAÍS]
Lo que pasa después de la compra: [ENTREGA, CITA, INSTALACIÓN, SESIONES…, OPCIONAL]

Mi cliente acaba de pagar. Escríbeme:
1. El mensaje de gracias inmediato: confirma lo que compró, qué sigue, cuándo
   y a quién escribirle si tiene dudas.
2. Un mensaje a mitad del camino (si mi servicio o mi entrega toma días): cómo
   vamos y una pregunta para saber cómo se siente.
3. Un mensaje para el día de la entrega o la última sesión, con 3
   recomendaciones para sacarle provecho.
4. Un mensaje una semana después, para saber cómo le fue (todavía sin pedir
   reseña).

Mensajes para WhatsApp de máximo 60 palabras. Si mi negocio es de una sola
visita (por ejemplo, un restaurante), déjalo en dos: el de gracias y el de una
semana después. Si te falta un dato, pregúntame antes de inventarlo.
```

### 21. Pide reseñas en Google sin pena

Para qué: juntar opiniones reales de clientes contentos.

```text
Mi negocio: [QUÉ VENDES]
Mis clientes: [A QUIÉN LE VENDES]
Dónde estoy: [CIUDAD Y PAÍS]
Mi enlace para dejar reseña: [ENLACE, OPCIONAL]

Necesito más reseñas en Google pero me da pena pedirlas. Dame:
1. El mejor momento para pedirla en mi tipo de negocio (justo después de qué).
2. Lo que digo en persona, en una frase natural.
3. El mensaje de WhatsApp con mi enlace, que explique en una línea cómo
   dejarla.
4. Un solo recordatorio amable, 3 días después, para quien no la dejó.
5. El texto de una tarjetita o letrero para el mostrador o la entrega, para
   poner junto a un código QR.

Reglas: nunca me sugieras ofrecer descuentos, regalos o pagos a cambio de
reseñas, ni pedirle reseña solo a los clientes contentos, ni escribir reseñas
falsas: Google lo prohíbe y en varios países es ilegal. Pide una opinión
honesta.
```

### 22. Responde tus reseñas, las buenas y las malas

Para qué: contestar en público sin pelear y sin sonar a robot.

```text
Mi negocio: [QUÉ VENDES]
Mis clientes: [A QUIÉN LE VENDES]
Dónde estoy: [CIUDAD Y PAÍS]
Reseñas que quiero contestar: [PEGA AQUÍ LAS RESEÑAS, OPCIONAL]
Dónde me pueden contactar en privado: [TELÉFONO O WHATSAPP, OPCIONAL]

Escribe la respuesta pública para cada reseña. Reglas:
- Buenas: agradece algo específico que mencionó (no un «gracias por su
  preferencia» de cajón) y menciona, sin sonar a anuncio, algo que puede
  volver a buscar.
- Malas: reconoce sin pelear, sin explicaciones largas y sin revelar datos del
  cliente ni de su compra; ofrece resolverlo en privado y deja ver que tomaste
  nota. Si la reseña parece falsa o de alguien que nunca vino, dime cómo
  responder con calma y cómo reportarla.
- Máximo 60 palabras por respuesta.

Si no te pegué reseñas, dame 3 respuestas modelo para reseñas buenas y 3 para
malas, típicas de mi tipo de negocio.
```

### 23. Contesta a un cliente molesto

Para qué: responder una queja sin echarle más leña al fuego.

```text
Mi negocio: [QUÉ VENDES]
Mis clientes: [A QUIÉN LE VENDES]
Dónde estoy: [CIUDAD Y PAÍS]
Lo que me escribió el cliente: [PEGA SU MENSAJE, SIN SU NOMBRE NI SU TELÉFONO]
Lo que pasó, desde mi lado: [TU VERSIÓN EN 2 O 3 LÍNEAS]
Lo que puedo ofrecer para arreglarlo: [REPONER, REPETIR, DEVOLVER, DESCUENTO O NADA, OPCIONAL]

Ayúdame a contestar:
1. Antes de escribir, dime en una línea qué le molesta de verdad (no siempre
   es lo que dice).
2. Mi respuesta, en este orden: reconozco lo que vivió (sin darle la razón en
   todo si no la tiene), digo qué voy a hacer y cuándo, y le hago una pregunta
   para cerrar el tema. Máximo 80 palabras.
3. Una versión para decírsela en una llamada o una nota de voz.
4. Las frases que NO debo decir porque empeoran todo.
5. Qué cambio en mi negocio para que no se repita.

Si el cliente amenaza con algo legal o pide algo que no puedo dar, dime cómo
responder sin comprometerme y recuérdame consultarlo con un abogado si es
grave.
```

### 24. Tu plan para cuando algo sale mal

Para qué: que tu equipo sepa qué hacer sin tener que llamarte.

```text
Mi negocio: [QUÉ VENDES]
Mis clientes: [A QUIÉN LE VENDES]
Dónde estoy: [CIUDAD Y PAÍS]
Lo que más suele fallar: [RETRASOS, PEDIDOS EQUIVOCADOS, PRODUCTO DAÑADO…, OPCIONAL]

Quiero que mi equipo sepa qué hacer cuando algo sale mal. Dame:
1. Los 6 problemas más probables en mi tipo de negocio (empieza por los que te
   di).
2. Para cada uno: qué dice, palabra por palabra, la primera persona que
   atiende al cliente; qué puede resolver sola, y cuándo me tiene que avisar.
3. Qué ofrecer según qué tan grave fue (un error pequeño, mediano y grande),
   cuidando que no me salga más caro que el problema.
4. Una hoja de una página para pegar en la pared o tener en el teléfono del
   equipo.

Lenguaje sencillo, como se lo explicaría a alguien que entró ayer. Si te falta
un dato, pregúntame antes de inventarlo.
```

### 25. Recordatorios para que no te dejen plantado

Para qué: consultorios, salones, talleres y todo negocio con citas.

```text
Mi negocio: [QUÉ VENDES]
Mis clientes: [A QUIÉN LE VENDES]
Dónde estoy: [CIUDAD Y PAÍS]
Cómo agendo hoy: [WHATSAPP, LLAMADA O AGENDA EN LÍNEA, OPCIONAL]
Mi política si no llegan: [CANCELACIÓN, ANTICIPO O NINGUNA, OPCIONAL]

Muchos clientes agendan y no llegan. Escríbeme:
1. El mensaje de confirmación al agendar: día, hora, dirección, qué traer y
   cómo cambiar la cita.
2. El recordatorio un día antes, que pida contestar «SÍ» para confirmar.
3. El aviso del mismo día, 2 horas antes, con cómo llegar o dónde estacionarse.
4. Qué mandar si no confirma y qué hago con ese espacio.
5. El mensaje para quien no llegó: sin regaño y con una forma fácil de
   reagendar.
6. Si no tengo política de cancelación o anticipo, una justa, explicada en dos
   líneas.

Mensajes cortos para WhatsApp, sin tono de amenaza. Donde falte un dato mío,
déjalo entre corchetes.
```

### 26. Clientes que regresan y te recomiendan

Para qué: premiar la lealtad y las recomendaciones sin regalar tu ganancia.

```text
Mi negocio: [QUÉ VENDES]
Mis clientes: [A QUIÉN LE VENDES]
Dónde estoy: [CIUDAD Y PAÍS]
Cada cuánto me compra un buen cliente: [FRECUENCIA, OPCIONAL]

Dame:
1. Tres ideas de programa de lealtad sencillo para mi negocio (tarjeta de
   sellos, cliente frecuente, un beneficio en la visita número X), con lo que
   me cuesta cada una y cuál me recomiendas.
2. Cómo pedir una recomendación en el momento correcto: qué frase digo y
   cuándo.
3. Qué darle a quien me recomienda y a la persona recomendada: atractivo para
   el cliente y barato para mí (un servicio extra, un producto, prioridad).
4. El mensaje de WhatsApp para anunciar el programa a mis clientes actuales.
5. Cómo llevar la cuenta en una libreta o una hoja de cálculo.

Nada que yo no pueda sostener durante un año. Si te falta un dato, pregúntame
antes de inventarlo.
```

### 27. Escucha a tus clientes: 3 preguntas y qué hacer con las respuestas

Para qué: saber qué mejorar sin una encuesta larga.

```text
Mi negocio: [QUÉ VENDES]
Mis clientes: [A QUIÉN LE VENDES]
Dónde estoy: [CIUDAD Y PAÍS]

Quiero saber qué piensan mis clientes sin aburrirlos. Dame:
1. Tres preguntas para mandar por WhatsApp después de la compra, que se
   contesten en menos de un minuto: una para saber qué tan probable es que me
   recomienden (del 0 al 10), una para saber qué casi hizo que no me compraran
   y una abierta sobre qué mejorarían.
2. El mensaje que acompaña las preguntas, de máximo 40 palabras.
3. Cómo ordenar las respuestas cuando tenga 20 o más: qué columnas poner en
   una hoja y qué patrones buscar.
4. Qué hacer con lo que me digan: cómo agradecer, cómo contestarle a quien se
   quejó y cómo decidir qué cambio primero.

Cuando tenga las respuestas te las voy a pegar, sin nombres, para que me digas
los 3 hallazgos más importantes.
```

## Biblioteca · Operar (prompts 28 a 36)

### 28. Tu tarea más repetida, en una lista de pasos

Para qué: sacar de tu cabeza lo que solo tú sabes hacer.

```text
Mi negocio: [QUÉ VENDES]
Mis clientes: [A QUIÉN LE VENDES]
Dónde estoy: [CIUDAD Y PAÍS]
La tarea: [POR EJEMPLO: ABRIR EL LOCAL, TOMAR UN PEDIDO, RECIBIR A UN PACIENTE NUEVO, COTIZAR]

Esta tarea vive en mi cabeza y quiero que alguien más la haga igual que yo.
Hazme preguntas, una por una, para que te cuente cómo la hago, como si se la
explicara a alguien nuevo. Cuando tengas suficiente, escribe:
1. Para qué sirve la tarea y quién la hace.
2. Lo que se necesita antes de empezar (material, accesos, información).
3. Los pasos numerados, uno por línea, con lo que se revisa en cada uno.
4. Los 3 errores más comunes y cómo evitarlos.
5. Cómo se sabe que quedó bien.
6. Una lista con casillas, de una página, para imprimir.

Escríbelo para alguien que nunca lo ha hecho. Si algo de lo que te conté no
tiene sentido o falta un paso, pregúntame.
```

### 29. Qué dejar de hacer tú

Para qué: cuando sientes que todo depende de ti.

```text
Mi negocio: [QUÉ VENDES]
Mis clientes: [A QUIÉN LE VENDES]
Dónde estoy: [CIUDAD Y PAÍS]
Lo que hago en una semana normal: [TODO LO QUE HACES, AUNQUE SEA EN DESORDEN]

Siento que todo depende de mí. Toma mi lista y acomoda cada tarea en una
tabla:
- Solo yo: lo que de verdad necesita mi experiencia o mi firma.
- Delegar: lo que otra persona puede hacer con una lista de pasos.
- Automatizar: lo que una herramienta sencilla puede hacer (mensajes
  automáticos, agenda en línea, recordatorios, cobros).
- Eliminar: lo que nadie extrañaría si dejo de hacerlo.

Para cada tarea, cuántas horas a la semana me quita (si no te lo dije,
estímalo y márcalo como estimado). Después dime las 3 tareas que me conviene
soltar primero y el primer paso para cada una esta semana. Si recomiendas una
herramienta, que sea gratuita o barata y conocida, y explica en una línea qué
hace.
```

### 30. Busca a la persona correcta: vacante, entrevista y prueba

Para qué: contratar bien a la primera.

```text
Mi negocio: [QUÉ VENDES]
Mis clientes: [A QUIÉN LE VENDES]
Dónde estoy: [CIUDAD Y PAÍS]
El puesto: [QUÉ VA A HACER, HORARIO Y SUELDO O RANGO]

Ayúdame a contratar bien:
1. El anuncio de la vacante: qué hace en un día normal, qué ofrezco, qué
   necesito que sepa hacer y cómo postularse. Claro y honesto, sin «buscamos a
   alguien proactivo y dinámico».
2. Tres preguntas de filtro para hacer por mensaje antes de la entrevista.
3. Ocho preguntas de entrevista que me muestren cómo trabaja de verdad (que me
   cuente situaciones reales), y qué respuesta sería buena señal y cuál una
   alerta.
4. Una prueba práctica de máximo 30 minutos, parecida al trabajo real.
5. El mensaje para avisarle con respeto a quien no quedó.

Importante: no pongas requisitos de edad, sexo, estado civil, apariencia,
religión ni embarazo; eso es discriminación y en México, en Estados Unidos y en
muchos otros países está prohibido. Para contratos y prestaciones, recuérdame
consultar a un contador o a un abogado laboral.
```

### 31. Las primeras dos semanas de alguien nuevo

Para qué: que aprenda con un plan y no «viendo».

```text
Mi negocio: [QUÉ VENDES]
Mis clientes: [A QUIÉN LE VENDES]
Dónde estoy: [CIUDAD Y PAÍS]
El puesto: [PUESTO Y QUÉ VA A HACER]

Va a entrar alguien nuevo. Diséñame sus primeras dos semanas:
1. Día 1: bienvenida, a quién conoce, qué le enseño y qué se lleva para leer.
2. Días 2 a 5: qué aprende cada día, qué hace acompañado y qué hace solo.
3. Semana 2: qué tareas ya hace por su cuenta y cómo reviso su trabajo.
4. Lo que debe saber hacer al día 14 para saber si va bien.
5. Dos pláticas cortas conmigo, el día 7 y el día 14: qué le pregunto.
6. El mensaje de bienvenida que le mando un día antes de entrar.

Que sea realista para un negocio pequeño donde yo atiendo y enseño al mismo
tiempo. Si te falta un dato, pregúntame antes de inventarlo.
```

### 32. Junta semanal de 15 minutos

Para qué: que tu equipo sepa qué toca cada semana, sin juntas eternas.

```text
Mi negocio: [QUÉ VENDES]
Mis clientes: [A QUIÉN LE VENDES]
Dónde estoy: [CIUDAD Y PAÍS]
Quiénes trabajan conmigo y qué hace cada uno: [TU EQUIPO]

Quiero una junta semanal de 15 minutos, de pie, que sirva. Dame:
1. El orden fijo de la junta, con minutos: qué se revisa, quién habla y en qué
   orden.
2. Los 3 a 5 números que conviene revisar cada semana en mi tipo de negocio y
   cómo anotarlos sin complicarnos.
3. Cómo cerrar: quién se compromete a qué antes de la siguiente junta.
4. Una hoja sencilla para anotar los acuerdos.
5. Tres reglas para que no se alargue ni se vuelva regaño.

Si trabajo solo, conviértelo en una revisión de 15 minutos conmigo mismo cada
lunes.
```

### 33. Cuánto te deja cada cosa que vendes (y si tu precio alcanza)

Para qué: saber qué te da dinero y qué te lo quita.

```text
Mi negocio: [QUÉ VENDES]
Mis clientes: [A QUIÉN LE VENDES]
Dónde estoy: [CIUDAD Y PAÍS]
Lo que vendo, con precio y costo: [NOMBRE · PRECIO · LO QUE TE CUESTA HACERLO O COMPRARLO]
Mis gastos fijos del mes: [RENTA, SUELDOS, LUZ, INTERNET…]
Cuánto vendo al mes de cada cosa: [CANTIDADES APROXIMADAS, OPCIONAL]

Ayúdame a ver cuánto me deja cada cosa que vendo:
1. Una tabla con producto, precio, costo, ganancia por pieza y porcentaje de
   ganancia.
2. Cuánto tengo que vender al mes para cubrir mis gastos fijos (mi punto de
   equilibrio), explicado con mis números.
3. Qué me deja más y qué me deja menos, y si algo me está haciendo perder.
4. Si mi precio alcanza: si subo un 10 %, cuántas ventas podría perder sin
   ganar menos que hoy.
5. Tres decisiones que podría tomar este mes con esta información.

Muéstrame las cuentas paso a paso para que yo las pueda revisar. No inventes
números: si me falta uno, pregúntame. Esto es orientación práctica, no
asesoría contable ni fiscal.
```

### 34. Tu dinero de las próximas 8 semanas

Para qué: ver venir las semanas apretadas antes de que lleguen.

```text
Mi negocio: [QUÉ VENDES]
Mis clientes: [A QUIÉN LE VENDES]
Dónde estoy: [CIUDAD Y PAÍS]
Dinero que tengo hoy en caja y en el banco: [CANTIDAD]
Lo que espero cobrar y cuándo: [COBROS O VENTAS ESPERADAS POR SEMANA]
Lo que tengo que pagar y cuándo: [RENTA, SUELDOS, PROVEEDORES, CRÉDITOS, IMPUESTOS]

Ayúdame a ver si me alcanza el dinero en las próximas 8 semanas:
1. Una tabla semana por semana: con cuánto empiezo, cuánto entra, cuánto sale
   y con cuánto termino.
2. Marca las semanas apretadas (donde quedo en negativo o casi).
3. Para esas semanas: qué cobros puedo adelantar, qué pagos puedo negociar o
   mover y qué venta rápida podría hacer, sin pedir prestado a la carrera.
4. Cuánto me conviene tener siempre guardado como colchón, según mis gastos.
5. Cómo actualizar esta tabla cada lunes en 10 minutos.

Muestra las cuentas. Si un dato no está claro, pregúntame. Es orientación
práctica, no asesoría financiera; para créditos e impuestos, recuérdame
consultar a mi contador.
```

### 35. Cobra lo que te deben sin pelearte

Para qué: recuperar tu dinero sin perder al cliente.

```text
Mi negocio: [QUÉ VENDES]
Mis clientes: [A QUIÉN LE VENDES]
Dónde estoy: [CIUDAD Y PAÍS]
Cuánto me deben y desde cuándo: [CANTIDAD Y FECHA, SIN NOMBRES SI PREFIERES]

Tengo clientes que me deben y no sé cómo cobrarles sin perderlos. Escríbeme:
1. Un recordatorio amable antes de la fecha de pago.
2. El mensaje del día en que vence.
3. Un segundo aviso a los 7 días, directo pero respetuoso.
4. Una propuesta de acuerdo de pago (en partes, con fechas) para quien de
   verdad no puede pagar todo, y cómo dejarlo por escrito.
5. Qué hacer si a los 30 días no contesta.
6. Tres cambios para que no me vuelva a pasar (anticipo, fechas claras,
   cobrar al entregar).

Reglas: nada de amenazas, no exhibir a nadie en redes ni en grupos, no
escribirle a su familia ni a su trabajo. Para montos grandes o casos legales,
recuérdame consultar a un abogado.
```

### 36. Revisa tus gastos del mes

Para qué: saber en qué se te va el dinero y qué recortar primero.

```text
Mi negocio: [QUÉ VENDES]
Mis clientes: [A QUIÉN LE VENDES]
Dónde estoy: [CIUDAD Y PAÍS]
Mis gastos del último mes: [LISTA DE GASTOS CON CANTIDAD, SIN NÚMEROS DE TARJETA NI DE CUENTA]

Ayúdame a revisar en qué se me va el dinero:
1. Agrupa mis gastos (renta y servicios, sueldos, mercancía o material,
   publicidad, herramientas y suscripciones, comisiones del banco, gastos
   personales mezclados con el negocio) con el total y el porcentaje de cada
   grupo.
2. Señala suscripciones que se repiten o que quizá ya no uso, gastos
   personales mezclados con los del negocio y comisiones que podría bajar.
3. Para cada gasto grande: ¿se recorta, se negocia o no se toca? Y por qué.
4. Tres cosas que puedo hacer esta semana para gastar menos sin descuidar a
   mis clientes.
5. Una regla sencilla para revisar mis gastos cada mes en 20 minutos.

Muestra las cuentas. Nunca me pidas números de tarjeta ni contraseñas. Es
orientación práctica; para impuestos y deducciones, recuérdame consultar a mi
contador.
```

---

## Antes de usar lo que te entregue

- **Léelo en voz alta.** Si una palabra no la dirías tú, cámbiala.
- **Revisa cada dato.** Precios, horarios, direcciones y condiciones tienen que ser los tuyos. Si ves un
  [CORCHETE] en el resultado, es un dato que falta: llénalo antes de mandarlo.
- **Nada inventado.** Si aparece un testimonio, una cifra o un premio que tú no le diste, bórralo.
- **Una promesa es un compromiso.** Si un texto promete algo que no puedes cumplir siempre, cámbialo.
- **Dinero, contratos y empleados:** úsalo para ordenar tus ideas y llega con eso a tu contador o a tu abogado.

## Enlaces oficiales

- [Cómo usar Skills en Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [Skills en Claude Code](https://code.claude.com/docs/en/skills)
- [Código público de esta skill](https://github.com/m4nueldeleon/skills)
