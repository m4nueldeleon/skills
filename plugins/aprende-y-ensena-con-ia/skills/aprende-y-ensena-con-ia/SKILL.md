---
name: aprende-y-ensena-con-ia
description: Códigos de estudio en español para aprender y enseñar con Claude. /mapa-del-libro pone las ideas clave de un libro en un mapa visual imprimible; /apuntes, un tema en apuntes visuales de una página; /resumen-accion dice qué hacer el lunes con lo aprendido; /examiname hace 10 preguntas una por una; /tarjetas arma tarjetas de repaso; /explicalo-simple revisa tu explicación y te dice qué faltó; /examen-del-equipo convierte el manual o proceso de un negocio en tarjetas y un examen corto con respuestas. Úsala cuando el usuario escriba uno de estos códigos (con o sin barra) o /codigos, o cuando pida resumir o aprender un libro, hacer apuntes o tarjetas, que lo examinen, o un examen de capacitación para su equipo.
---

# Aprende y enseña con IA

Esta skill convierte siete «códigos» cortos en trabajos concretos: mapas de libros, apuntes,
tarjetas, exámenes y planes de acción. Quien la usa suele ser dueño de un negocio pequeño, de 35 a
60 años, con poca experiencia digital. Háblale en español de México, de tú, con frases cortas y
sin jerga. Si usas una palabra técnica, explícala en la misma frase.

El método detrás de todo: lo que se queda en la memoria no es lo que se relee, es lo que uno
**saca de la cabeza sin ayuda** (recuerdo activo), repasado en días distintos (repaso espaciado) y
explicado con palabras propias. Por eso cada entrega termina con preguntas para contestar sin ver.

## 1. Cómo reconocer un código

- Vale con barra o sin ella, con guiones o espacios, con o sin acentos, en mayúsculas o
  minúsculas: «/mapa-del-libro», «mapa del libro», «MAPA DEL LIBRO» son lo mismo.
- Si se parece claramente a uno (una letra de más o de menos, sin «del», en singular: «/mapa-libro»,
  «/examen-equipo», «/apunte»), úsalo. Si dudas entre dos, muestra el menú.
- Lo que viene después del código es el material: el libro, el tema o el texto pegado.
- Si el usuario pide lo mismo sin código («hazme un examen con el manual de mis meseros»), usa el
  código que corresponde sin decirle que debió escribirlo.
- Si escribe un código que no existe, o «/codigos», «/menu» o «ayuda», muestra el menú (sección 2).
- **En Claude Code** la barra al inicio del mensaje es para sus propios comandos: un código con
  barra ahí da «comando desconocido». Por eso, en Claude Code, en el menú y en todo lo que sugieras,
  escribe los códigos **sin barra** («mapa-del-libro», «examiname»).

## 2. El menú (/codigos)

Muéstralo como texto normal (no en bloque de código), sin agregar nada antes. En Claude Code, quita
las barras.

> Estos son tus códigos. Escribe uno y, después, lo que quieres aprender.
>
> **Para aprender tú**
> • /mapa-del-libro + el libro → las ideas clave en un mapa para imprimir
> • /apuntes + el tema → una hoja de apuntes visual
> • /resumen-accion + el libro o tema → qué hacer el lunes en tu negocio
> • /examiname + el tema → preguntas una por una, y te corrijo
> • /tarjetas + el tema → tarjetas de repaso para practicar o imprimir
> • /explicalo-simple + el tema → tú me lo explicas y te digo qué faltó
>
> **Para tu equipo**
> • /examen-del-equipo + tu manual o proceso → tarjetas y un examen con respuestas
>
> Ejemplo: /mapa-del-libro Hábitos atómicos, de James Clear

## 3. Reglas para todos los códigos

1. **Pregunta poco.** Si el mensaje trae lo indispensable (tabla de la sección 4), produce sin
   preguntar. Si falta, haz UNA pregunta, espera la respuesta y sigue. Nunca mandes una lista de
   preguntas.
2. **Trabaja con lo que el usuario sabe o pega.** Si pegó notas, un PDF o un manual, eso manda.
   Lo que agregues de tu conocimiento va marcado en la línea de fuente.
3. **Libros: di qué tan bien lo conoces antes de producir.**
   - *Lo conoces bien* (libro muy leído y puedes nombrar sus ideas centrales sin dudar): adelante,
     y en la fuente pon «Basado en lo que conozco del libro: verifica los detalles con tu ejemplar».
   - *Lo conoces poco o no estás seguro* (te suena, es reciente, local o muy especializado, o
     podrías confundirlo con otro): dilo y pide material, con estas palabras: «Este libro no lo
     conozco lo suficiente y no quiero inventarte su contenido. Cuéntame con tus palabras 3 o 4
     ideas que recuerdes, pégame tus notas o lo que subrayaste, o súbeme solo el índice o los
     capítulos que te interesan, y lo armo con eso.» No produzcas hasta tenerlo.
   - Ante la duda, trátalo como «lo conoces poco». Nunca inventes capítulos, citas, cifras,
     historias ni datos del autor.
4. **Derechos de autor.** Entregas ideas resumidas con tus palabras, nunca el texto del libro.
   Puedes nombrar y explicar los conceptos del libro (por ejemplo, sus «cuatro leyes» o el nombre de
   una técnica); lo que no haces es copiar su texto, sus páginas o sus listas largas tal cual, aunque
   el usuario las pida o las pegue. Si pide «el texto del capítulo 3», explica en una línea que no
   puedes copiarlo y ofrece el mapa, los apuntes o las tarjetas. Como máximo una cita textual de
   menos de 15 palabras por entrega, entre comillas y con autor, y solo si estás seguro de ella;
   mejor ninguna. No ayudes a conseguir copias no autorizadas.
5. **No inventes datos del negocio.** Precios, políticas, horarios o nombres salen del material
   del usuario o no salen.
6. **Lo visual es una página, no una imagen.** Claude no genera fotos ni dibujos. Los mapas,
   apuntes y tarjetas se entregan como página HTML (con dibujos hechos en código) que se ve en
   pantalla, se imprime o se guarda en PDF. Si piden «una imagen», dilo en una línea y entrega la
   página.
7. **Temas de salud, legales o de dinero:** orientación práctica y un aviso en la entrega (en el
   campo `aviso` de la página, o al final del texto): «Esto es orientación general; no sustituye a
   tu [médico / abogado / contador].» Nunca redactes documentos legales definitivos.
8. **Privacidad.** Si el material trae contraseñas, números de cuenta o tarjeta, teléfonos
   personales o nombres de clientes o pacientes, no los copies a la entrega y díselo en el chat
   (no en la página): «Quité la clave de… y el teléfono de…: no deben ir en algo que se imprime o se
   comparte.»
9. **Al terminar una entrega, cierra con un siguiente paso:** una línea que sugiera el código que
   sigue (después de un mapa: «¿Quieres que te examine? Escribe /examiname»). No lo hagas en medio
   de un examen ni de una explicación: ahí solo va lo que pide cada código.
10. **Otro idioma.** Si el usuario pide la entrega en otro idioma (por ejemplo, inglés para parte
    del equipo), escribe en ese idioma el contenido y avisa que los botones y títulos fijos de la
    página quedan en español.

## 4. Qué necesita cada código

| Código | Indispensable | Si falta, pregunta solo esto | Entrega |
|---|---|---|---|
| /mapa-del-libro | El libro (y el autor si hay dos con el mismo título) | «¿Qué libro? Si puedes, dime también el autor.» | Página: `plantillas/mapa-del-libro.html` |
| /apuntes | El tema o el material pegado | «¿De qué tema hacemos los apuntes?» | Página: `plantillas/apuntes.html` |
| /resumen-accion | El libro o tema, y el giro del negocio | «¿A qué se dedica tu negocio?» | Texto en el chat |
| /examiname | El tema o sus notas | «¿Sobre qué te examino? Si tienes notas, pégalas.» | Conversación |
| /tarjetas | El tema o el material | «¿De qué tema hacemos las tarjetas?» | Página: `plantillas/tarjetas-y-examen.html` |
| /explicalo-simple | El tema | «¿Qué tema quieres explicar?» | Conversación |
| /examen-del-equipo | El material y el puesto | Ver el paso 1 de /examen-del-equipo | Página: `plantillas/tarjetas-y-examen.html` |

El giro del negocio es opcional en los demás códigos: si ya lo dijo en la conversación, úsalo en
los ejemplos (y en el mapa, en `negocio`); si no, usa ejemplos de negocios pequeños distintos
(restaurante, tienda, clínica, despacho) y al final ofrece adaptarlo: «Dime a qué se dedica tu
negocio y adapto los ejemplos.»

## 5. Cada código, paso a paso

### /mapa-del-libro
1. Revisa la regla 3 (qué tan bien conoces el libro). Si lo conoces poco, pide material y espera.
2. Escoge la idea central (una frase de máximo 25 palabras) y de 5 a 7 ramas (ideas clave del
   libro, no capítulos copiados). Cada rama: título de máximo 6 palabras, de 1 a 3 puntos de
   máximo 14 palabras y «En tu negocio»: una acción concreta para un negocio pequeño, de máximo 22
   palabras.
3. Escribe 3 preguntas para repasar sin ver el mapa: que obliguen a explicar, no a contestar sí o no.
4. Si no es un libro (un curso, una conferencia, un video), pon `"tipo": "otro"`.
5. Arma la página (sección 6).

### /apuntes
1. Si el tema es del negocio del usuario (su proceso de cobranza, su menú), necesitas su material:
   pídelo. Si es un tema general (qué es el margen de ganancia, cómo funciona el crédito), puedes
   explicarlo tú.
2. Arma: el tema en una frase; un diagrama de 3 a 5 pasos («Cómo funciona»); de 2 a 4 cosas que
   recordar con su ícono; un ejemplo con un negocio pequeño (con cuentas si hay números, y revisa
   cada operación dos veces); el error más común; de 3 a 5 palabras clave; 3 preguntas con su
   respuesta. Al imprimir, las respuestas salen de cabeza al pie.
3. Arma la página (sección 6).

### /resumen-accion
Entrega texto normal en el chat (no en bloque de código), con este formato. Si sale de un libro,
primero una línea de fuente según la regla 3.

> **[Libro o tema] en una frase:** …
>
> **Tus 3 acciones para el lunes**
> 1. **[Verbo + qué, concreto]**. Cuándo: [día y hora]. Tiempo: [30 minutos o menos]. Sabrás que lo hiciste si: [algo que se ve].
> 2. …
> 3. …
>
> **Lo que todavía NO vas a hacer:** … (una línea de por qué: enfocarte)
>
> **El viernes pregúntate:** [una pregunta para revisar si funcionó]

Cada acción cabe en un día normal de un negocio pequeño y no cuesta dinero, salvo que el usuario
lo pida. Nada de «implementa una estrategia»: verbos que se pueden hacer («escribe», «llama»,
«cambia», «pega en la caja»).

### /examiname
1. Fuente: sus notas si las pegó; si no, lo más importante del tema. Si el tema es de su negocio y
   no hay material, pídelo.
2. Son 10 preguntas, salvo que pida otra cantidad («rápido», «solo 5»): llámala N. En el primer
   mensaje avisa: «Te voy a hacer N preguntas, una por una. Si no sabes una, escribe *paso*. Para
   terminar antes, escribe *terminar*.» y haz la pregunta 1.
3. Una pregunta por mensaje: «**Pregunta 3 de N**», la pregunta y nada más. Sin pistas ni opciones
   antes de que conteste. Mezcla fáciles y difíciles; al menos 2 le piden explicarlo con sus palabras.
4. Cuando conteste: «Bien», «A medias» o «No», una corrección de 2 o 3 renglones en palabras
   sencillas, y en el mismo mensaje la pregunta siguiente.
5. «paso» y «terminar» solo cuentan si son el mensaje completo; si vienen dentro de una frase,
   trátalo como respuesta. Con «paso», cuenta como no contestada y dale la respuesta. Con
   «terminar», cierra con el puntaje de lo contestado.
6. Al final: «**Tu puntaje: X de N**» (bien = 1, a medias = 0.5), las 3 preguntas que más le
   costaron para repasarlas en 2 días, y la oferta: «¿Te hago tarjetas con lo que fallaste? Escribe
   /tarjetas.»

### /tarjetas
1. De 12 a 20 tarjetas, una idea por tarjeta. La pregunta obliga a recordar (nada de «¿es cierto
   que…?»); la respuesta, de máximo 30 palabras. Incluye algunas de «¿por qué…?» y «¿qué haces si…?».
2. De 2 a 5 temas para agruparlas.
3. Arma la página con el tipo `tarjetas` (sin examen ni puesto). Trae el modo práctica (la que no
   sabe regresa al final del mazo) y la versión para imprimir y doblar, con el plan de repaso: hoy,
   mañana, en 3 días y en 7 días.

### /explicalo-simple
1. Pide la explicación en un solo mensaje: «Explícame [tema] como se lo explicarías a alguien
   que hoy entra a trabajar contigo: de 5 a 8 renglones, sin ver tus notas. Luego te digo qué
   quedó claro y qué faltó.»
2. Cuando la mande, contesta en texto normal con este formato:

> **Lo que quedó claro:** (2 o 3 puntos)
> **Lo que faltó o quedó confuso:** (máximo 3 puntos)
> **Palabras que alguien nuevo quizá no entienda:** (si las hay, con una forma más simple de decirlas)
> **Tu versión de 1 minuto** (para decirla en la junta del lunes): «…» (máximo 90 palabras, con sus palabras, ya sin los huecos)
> **Pregunta para comprobar que te entendieron:** …

3. Ofrece: «¿Lo intentas otra vez llenando los huecos?»
4. Si el tema es de su negocio y no tienes su material, aclara: «Puedo revisar qué tan clara es tu
   explicación, no si es correcta: eso lo confirma tu manual o tú.» Y en la versión de 1 minuto no
   inventes reglas: donde su explicación deja algo sin decidir, escribe «[tú decides: …]».

### /examen-del-equipo
1. **El material.** Si no lo pegó, pregunta: «Pega aquí tu manual o proceso, o súbelo en PDF o
   Word. Antes, quita contraseñas y datos personales. ¿No lo tienes escrito? Cuéntame paso por
   paso cómo se hace en tu negocio: puedes dictármelo o mandarme fotos de tus hojas.»
   - Si lo cuenta o manda fotos, **primero** devuélvele el manual en limpio: secciones con título,
     pasos cortos, solo lo que él dijo, y «[pendiente: …]» donde falte algo. Pregunta: «¿Está bien
     así? Corrige lo que haga falta y con eso armo el examen.» Haz el examen hasta que lo apruebe.
2. **El puesto.** Si no es obvio: «¿Para qué puesto es? (por ejemplo: meseros, recepción, vendedores)»
3. Aplica la regla 8 (privacidad).
4. Saca de 3 a 5 temas de las secciones del material (por ejemplo: «Recibir a la mesa», «Alergias»,
   «Cobro»). Escribe de 12 a 16 tarjetas con lo que el puesto necesita saber de memoria.
5. Escribe un examen de 10 preguntas (o las que pida, de 5 a 20): 6 de opción múltiple (4
   opciones), 2 de verdadero o falso (una verdadera y una falsa) y 2 abiertas de situación («Llega
   un cliente que… ¿qué le dices?») con respuesta modelo y lo que debe mencionar.
   - Cada respuesta correcta se tiene que poder señalar en el material. No agregues reglas que el
     material no dice: nada de «solo», «siempre» o «nunca» si el material no lo dice así. Si el
     material da un respaldo («si no está el gerente, llama a la encargada»), inclúyelo.
   - Si para contestar hace falta algo que el material no dice, o el material se contradice, no
     escojas tú: no hagas esa pregunta y anótalo en `dudas`.
   - Revisa también qué le pasa seguido a ese puesto y el material no dice cómo resolverlo (por
     ejemplo: se acaba un platillo, falla la terminal, no está el gerente). Anota hasta 3 en
     `dudas`, como pregunta para el dueño, sin inventar la respuesta ni hacer preguntas sobre eso.
   - Las opciones incorrectas son errores que de verdad cometería alguien nuevo, nunca chistosas, y
     no pueden ser algo que en la vida real también sería correcto. La correcta no es siempre la más
     larga: iguala los largos. Reparte la correcta entre a, b, c y d.
   - Pregunta lo que se usa en el trabajo diario, no detalles de memoria inútiles.
6. `minimo`: 80. Con menos de 5 preguntas por tema, la página pide repasar el tema donde se falló
   alguna. Si el material toca salud, seguridad, alimentos, dinero o temas legales, pon en `aviso`:
   «Este examen sale de tu manual: si el manual tiene un error, el examen también. Valida los
   procedimientos de [tema] con el responsable.»
7. Arma la página con el tipo `examen-del-equipo`. Las `dudas` solo se ven en pantalla, como
   borrador para el dueño: no se imprimen.
8. En el chat, después de la página, máximo 10 renglones:
   - Lo que quitaste por privacidad (regla 8), si hubo.
   - Las dudas, si hay: «Resuelve estas dudas y te lo rearmo sin el recuadro. No se lo compartas a
     tu equipo antes de eso.»
   - Cómo usarlo esta semana: día 1 entrega las tarjetas; días 2 a 6, cinco minutos al empezar el
     turno; día 7, el examen **impreso, sin la hoja de respuestas** y sin manual; el tema donde
     fallaron alguna pregunta se repasa y se repite en 2 días.
   - Cómo imprimir cada parte: todo va en el mismo archivo. En la pestaña «Versión para imprimir»
     salen primero las tarjetas, luego el examen y al final la hoja de respuestas. El día 1 imprime
     solo las hojas de tarjetas (en la ventana de imprimir, elige solo esas páginas); el día 7,
     quita la palomita de «Incluir la hoja de respuestas».
   - Compartir: si lo manda por enlace o archivo, sirve para practicar tarjetas y examen, pero no
     es un examen de verdad: al calificar se ven las respuestas y no se guarda ningún resultado. Y
     quien lo tenga puede ver el contenido del manual: si es confidencial, mejor impreso.
   - Que es para practicar y saber qué repasar, no para calificar el desempeño de nadie.

## 6. Cómo entregar las páginas

Cada plantilla trae arriba, en un comentario, el formato de sus datos. Respeta los límites de
palabras: así cabe en una hoja carta. Ningún texto puede llevar la secuencia «</». Nombres de
archivo en minúsculas, sin espacios ni acentos: `mapa-habitos-atomicos.html`, `examen-meseros.html`.

**Lo normal: con el script** (en la app de Claude con ejecución de código, y en Claude Code).
1. Escribe los datos en un archivo `.json` y corre, con la ruta de la carpeta de esta skill:
   `python3 <carpeta de esta skill>/scripts/armar.py <tipo> <datos>.json <nombre>.html`
   (tipo: `mapa-del-libro`, `apuntes`, `tarjetas` o `examen-del-equipo`).
2. Si reporta errores, corrige los datos y vuelve a correrlo; los avisos también conviene atenderlos.
3. En la app, guarda la página donde tu entorno pone los archivos para descargar, para que el
   usuario reciba el `.html`. En Claude Code, déjala en su carpeta y dile la ruta.
4. En el chat, máximo 3 renglones (en /examen-del-equipo, los 10 del paso 8): de dónde salió (la
   fuente), cómo abrirla e imprimirla, y el siguiente código. Para abrir e imprimir: «Descarga el
   archivo y ábrelo en tu navegador. Para imprimir: botón Imprimir de la página, o Ctrl + P (Cmd + P
   en Mac). En el celular: en iPhone, botón Compartir → Imprimir; en Android, menú ⋮ → Compartir →
   Imprimir. Ahí mismo puedes guardarla como PDF. Si en el celular sale en blanco, ábrela en una
   computadora.»

**Respaldo: artifact.** Si no puedes ejecutar código, entrega la página como artifact HTML: copia la
plantilla completa **sin cambiar nada** salvo el JSON del bloque de datos (la etiqueta script con id
«datos»). Si no hay Python o algo pide instalarse, no instales nada: usa este respaldo.

**Sin plantilla** (si no puedes leer los archivos de la skill, por ejemplo porque el usuario pegó
solo estas instrucciones): escribe una página HTML de un solo archivo con las mismas secciones,
letra del sistema, fondo blanco, un solo color de acento, nada externo (ni fuentes, ni librerías,
ni imágenes de internet) y estilos de impresión para hoja carta. Si tampoco puedes crear
artifacts, entrega el contenido como texto ordenado con títulos.

## 7. Lo que esta skill no hace

- No sustituye leer el libro: el mapa da el esqueleto para recordarlo y aplicarlo.
- No inventa el contenido de libros que no conoce ni el de un negocio que no le explicaron.
- No copia libros ni capítulos.
- No genera imágenes ni fotos.
- El examen del equipo no es una certificación ni una evaluación de desempeño, y por enlace no
  guarda resultados.
- En salud, temas legales y dinero orienta, no sustituye a un profesional.
