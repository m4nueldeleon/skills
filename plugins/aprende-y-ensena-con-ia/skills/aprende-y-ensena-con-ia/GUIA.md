# Aprende y enseña con IA

Manuel de León · Recursos de IA para negocios · 20 de octubre de 2026

Siete códigos para estudiar un libro, entender un tema y capacitar a tu equipo con Claude.

## Qué hace

Escribes un código, y después lo que quieres aprender, y Claude te entrega algo que puedes usar
ese mismo día:

| Escribe | Y recibes |
|---|---|
| `/mapa-del-libro` + el libro | Las ideas clave del libro en un mapa de una hoja, con cómo aplicarlas en tu negocio |
| `/apuntes` + el tema | Una hoja de apuntes visual: diagrama, lo que hay que recordar, un ejemplo y preguntas |
| `/resumen-accion` + el libro o tema | Tres acciones concretas para el lunes |
| `/examiname` + el tema | 10 preguntas, una por una; contestas sin ver y te corrige |
| `/tarjetas` + el tema | Tarjetas de repaso para practicar en pantalla o imprimir y doblar |
| `/explicalo-simple` + el tema | Tú lo explicas con tus palabras y te dice qué faltó |
| `/examen-del-equipo` + tu manual | Tarjetas y un examen con hoja de respuestas para tu equipo |

¿Se te olvidaron? Escribe `/codigos` y te muestra el menú.

Los mapas, apuntes, tarjetas y exámenes salen como una página (un archivo que se abre en el
navegador) que puedes ver, imprimir o guardar en PDF. Claude no hace fotos ni dibujos: arma una
página con texto, recuadros y flechas. Así se ven los tres ejemplos de esta carpeta:

- [Mapa de un libro](ejemplos/vista-previa/mapa-del-libro-habitos-atomicos-escritorio.jpg) · [abrir la página](ejemplos/mapa-del-libro-habitos-atomicos.html)
- [Apuntes de un tema](ejemplos/vista-previa/apuntes-margen-de-ganancia-escritorio.jpg) · [abrir la página](ejemplos/apuntes-margen-de-ganancia.html)
- [Examen del equipo: tarjetas](ejemplos/vista-previa/examen-del-equipo-restaurante-tarjeta-volteada.jpg) y [examen calificado](ejemplos/vista-previa/examen-del-equipo-restaurante-examen-calificado.jpg) · [abrir la página](ejemplos/examen-del-equipo-restaurante.html)

## Por qué funciona

Releer y subrayar se siente bien, pero se olvida rápido. Lo que se queda es lo que sacas de la
cabeza sin ver, repasado en días distintos y explicado con tus palabras. Por eso cada código
termina con preguntas para contestar sin ver, y las tarjetas traen un plan: hoy, mañana, en 3 días
y en 7 días.

## Seis palabras que vas a leer

- **Skill:** un paquete de instrucciones que le enseña a Claude a hacer una tarea siempre igual.
- **ZIP:** un archivo comprimido, que guarda una carpeta adentro. Así se descarga esta skill.
- **Descomprimir:** abrir el ZIP para que vuelva a ser carpeta. Para subir la skill **no** lo descomprimas.
- **Ejecución de código:** un permiso de Claude para crear archivos. Las skills lo necesitan.
- **Proyecto:** un espacio de Claude donde guardas instrucciones que se usan en todas sus conversaciones.
- **Claude Code:** la versión de Claude que se usa en la computadora, escribiendo en una ventana de
  texto. Si no sabes qué es, no lo necesitas: usa la app.

## Antes de empezar

- Una cuenta de Claude. Funciona en todos los planes, también el gratuito; en el gratuito hay un
  límite de mensajes, y un examen grande puede gastar varios.
- En la app o en claude.ai: entra a **Configuración → Capacidades** y activa **Ejecución de código
  y creación de archivos** (en inglés: *Settings → Capabilities → Code execution and file creation*).

## Instálala en Claude (app o web)

1. Descarga el ZIP de la skill:
   https://github.com/m4nueldeleon/skills/releases/download/descargas/aprende-y-ensena-con-ia.zip
   No lo descomprimas. En Mac, Safari a veces lo descomprime solo: si en Descargas te aparece una
   carpeta en vez del ZIP, dale clic derecho → **Comprimir** y usa el archivo `.zip` que se crea.
2. En Claude, entra a **Personalizar → Habilidades** (en inglés: *Customize → Skills*).
3. Toca el botón **+** y elige **Cargar una habilidad** (*Upload a skill*).
4. Escoge el ZIP. La skill aparece en tu lista: revisa que esté encendida.
5. Abre un chat nuevo y escribe `/codigos`. Si te muestra el menú, quedó lista.

Los nombres de los menús a veces cambian. Si no los encuentras, busca «skills» en la ayuda
oficial de Claude (enlace al final).

## Instálala en Claude Code

En una sesión de Claude Code escribe:

```text
/plugin marketplace add m4nueldeleon/skills
/plugin install aprende-y-ensena-con-ia@manuel-de-leon
```

En Claude Code, la barra al inicio del mensaje es para sus propios comandos: un código con barra da
«comando desconocido». Ahí escribe los códigos **sin la barra**: `codigos` para ver el menú,
`mapa-del-libro Hábitos atómicos`, o `examen-del-equipo` y pegas el manual. Las páginas se guardan
como archivo `.html` en tu carpeta: ábrelo con doble clic.

## Sin instalar nada

Abre el archivo de instrucciones en
https://github.com/m4nueldeleon/skills/blob/main/plugins/aprende-y-ensena-con-ia/skills/aprende-y-ensena-con-ia/SKILL.md,
copia todo su texto y pégalo al inicio de una conversación (o en las instrucciones de un Proyecto
de Claude). Luego escribe tus códigos. Así Claude no tiene las plantillas, y las páginas pueden salir
más sencillas que en los ejemplos. En ChatGPT o Gemini suele entender los códigos, pero lo visual
puede salir solo como texto.

## Cómo se escribe un código

- Escríbelo al inicio de tu mensaje y, después, lo que quieres: `/apuntes qué es el flujo de efectivo`.
- Si al escribir la barra la app te muestra una lista, no le hagas caso y sigue escribiendo. También
  funciona sin barra: `apuntes: qué es el flujo de efectivo`.
- Si Claude no reconoce el código, empieza tu mensaje así: «Usa la skill aprende-y-ensena-con-ia:»
  y después el código.

## Tres ejemplos para copiar

Cambia lo que está entre corchetes.

**1. Un libro en un mapa**

```text
/mapa-del-libro [nombre del libro], de [autor]. Tengo [tu negocio: una tienda de ropa, una
clínica dental, una inmobiliaria…].
```

Si Claude conoce bien el libro, te arma el mapa y te pide que verifiques los detalles con tu
ejemplar. Si no lo conoce bien, te lo dice y te pide que le cuentes 3 o 4 ideas que recuerdes, tus
notas o el índice. Así no te inventa nada.

**2. Un tema en apuntes**

```text
/apuntes [el tema que quieres entender: margen de ganancia, cómo contestar una reseña negativa,
qué es el punto de equilibrio]. Tengo [tu negocio].
```

Imprímelo. Tapa la parte de abajo con otra hoja, contesta las preguntas y luego gira la hoja: las
respuestas están de cabeza al pie.

**3. El manual de tu negocio convertido en examen para tu equipo**

```text
/examen-del-equipo Tengo [tu negocio]. Es para [el puesto: meseros, recepción, vendedores].
Este es mi manual (ya le quité contraseñas y datos personales):
[pega aquí tu manual, tu proceso o tu guion de ventas]
```

¿No tienes el manual escrito? Escribe el código y cuéntale paso por paso cómo se hace (puedes
dictarlo con el micrófono o mandarle fotos de tus hojas). Primero te devuelve el manual en limpio
para que lo revises; con tu visto bueno arma el examen.

Recibes tarjetas para repasar, un examen de 10 preguntas y la hoja de respuestas con la
calificación por tema. Si tu manual se contradice o le falta algo, Claude no inventa la respuesta:
deja fuera esas preguntas, te lo señala en un recuadro que solo ves tú en pantalla (no se imprime)
y te lo rearma cuando lo resuelvas.

Para probar los demás: `/resumen-accion [el libro] Tengo [tu negocio]`, `/examiname [el tema]`,
`/tarjetas [el tema]` y `/explicalo-simple [el tema]`.

## Qué esperar

- **Un mapa no sustituye al libro.** Te da el esqueleto para recordarlo y aplicarlo; los detalles
  están en el libro.
- **No copia libros.** Resume ideas con sus palabras. Si le pides el texto de un capítulo, te ofrece
  el mapa o los apuntes en su lugar. Usa tu propio ejemplar.
- **Revisa antes de usarlo.** Sobre todo el examen del equipo: si tu manual tiene un error, el
  examen también. En temas de salud, seguridad, dinero o legales, valídalo con el responsable o con
  un profesional.
- **El examen es para practicar,** para saber qué repasar, no para calificar el trabajo de nadie.
  El tema donde fallen alguna pregunta se repasa y se repite en 2 días.
- **Cómo te llega:** como un archivo para descargar. Ábrelo en tu navegador. Para imprimir, usa el
  botón «Imprimir o guardar en PDF» de la página, o Ctrl + P (en Mac, Cmd + P). En el celular: en
  iPhone, botón Compartir → Imprimir; en Android, menú ⋮ → Compartir → Imprimir. Ahí mismo puedes
  guardarlo como PDF. Si en el celular se ve en blanco, ábrelo en una computadora.
- **Para tu equipo:** el día 7, el examen va **impreso y sin la hoja de respuestas**. Si mandas la
  página por enlace o por WhatsApp, sirve para practicar, pero no es un examen de verdad: al
  calificar se ven las respuestas y no se guarda ningún resultado. Además, quien la tenga puede ver
  el contenido de tu manual: si es confidencial, mejor impreso.

## Cuida tus datos

Antes de pegar un manual, quita contraseñas, números de cuenta, teléfonos personales y nombres de
clientes o pacientes. La skill le pide a Claude no copiarlos y avisarte si se te pasó alguno, pero
revísalo tú: es más seguro no pegarlos.

## Enlaces oficiales

- [Cómo usar skills en Claude (ayuda oficial)](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- [Skills en Claude Code](https://code.claude.com/docs/en/skills)
- El código de esta skill es público: https://github.com/m4nueldeleon/skills
