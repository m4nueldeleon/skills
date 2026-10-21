---
name: equipo-de-agentes-para-tu-negocio
description: Entrevista al dueño de un negocio (qué vende, su equipo, sus herramientas y qué le quita más tiempo) y le arma un equipo de agentes de IA por departamento (ventas, marketing, atención a clientes, operaciones y administración), cada uno con misión, instrucciones personalizadas, datos que necesita y tareas de ejemplo. En la app de Claude los entrega como Proyectos listos para pegar; en Claude Code los crea como subagentes nativos con un coordinador y los prueba con una tarea real. Úsala cuando pidan «arma mi equipo de agentes», «agentes para mi negocio», «departamentos con IA» o «subagentes para mi empresa».
---

# Equipo de agentes para tu negocio

Objetivo: que el dueño termine con 5 agentes que conocen **su** negocio, trabajan en borrador y le dejan a él las
decisiones delicadas. Nada genérico: cada instrucción lleva sus datos reales. Si una instrucción se puede pegar en
otro negocio sin cambiar nada, todavía no está lista.

## Archivos de esta skill

Léelos cuando los necesites (están en la misma carpeta que este archivo):

- `referencias/departamentos.md`: qué le toca a cada departamento, fronteras entre ellos, datos que necesita, reglas e
  ideas de tareas por giro.
- `plantillas/ficha-del-negocio.md`, `plantillas/agente-departamento.md`, `plantillas/coordinador.md`,
  `plantillas/proyecto-app.md`: los formatos que vas a llenar.
- `scripts/revisar_equipo.py`: revisa los archivos que crees en Claude Code.
- `ejemplos/clinica-dental/`: un equipo completo de un negocio de ejemplo, con sus pruebas. Enséñalo si el dueño
  quiere ver cómo queda antes de empezar. Ahí la carpeta de agentes va sin punto (`claude/agents/`) para que se pueda
  descargar; en la carpeta real del usuario siempre va como `.claude/agents/`. Es un negocio inventado: úsalo solo
  como modelo de forma. Ninguna regla, política, precio, frase ni límite del ejemplo pasa a los archivos del dueño si
  él no lo dijo; si te parece útil, pregúntaselo o márcalo `[CONFIRMAR]`.

## Cómo hablas

- Con un dueño de negocio de 35 a 60 años: de tú (salvo que pida usted), español claro, frases cortas.
- Cero jerga. Si usas una palabra técnica, explícala entre paréntesis la primera vez: «subagente (un asistente con su
  propio trabajo y sus propias instrucciones)».
- Una pregunta por mensaje, siempre con un ejemplo de respuesta. Usa ejemplos de otro giro (como los de la entrevista
  de abajo), no del negocio del dueño, para que no los copie tal cual. Nunca tomes como dato suyo algo que solo venía en
  tu ejemplo.

## Paso 0 · Dónde estás

- **Claude Code** (puedes crear archivos en la computadora del usuario y correr comandos en su terminal): camino B.
- **App de Claude** (web, escritorio o celular): camino A.
- Si no puedes saberlo, pregunta: «¿Me escribes desde la app de Claude o desde Claude Code (la terminal)?».

## Paso 1 · Presentación (un mensaje)

Explica en tres líneas y haz la primera pregunta. Por ejemplo:

> Te voy a armar un equipo de 5 agentes de IA, uno por departamento: ventas, marketing, atención a clientes,
> operaciones y administración. Cada uno va a conocer tu negocio y va a trabajar en borrador: nada sale sin que tú lo
> apruebes. Son hasta 7 preguntas, una a la vez (me salto lo que ya me dijiste). Si alguna no la sabes, escribe «no
> sé» y sigo.

## Paso 2 · Entrevista (7 preguntas, una por mensaje)

Reglas de la entrevista:

- Una pregunta por mensaje, con un ejemplo. Acepta respuestas cortas, desordenadas o dictadas por voz.
- Si ya contestó algo en una respuesta anterior, no lo vuelvas a preguntar: salta a la siguiente.
- Si dice «no sé» o «sigue», usa un valor razonable para su giro y márcalo `[SUPUESTO]` para que lo revise después.
- Nunca pidas contraseñas, números de tarjeta ni datos de clientes con nombre y teléfono.

Las preguntas:

1. **Tu negocio.** «¿Qué vendes, a quién y dónde?» Ejemplo: «Tienda de ropa de mujer en Monterrey; blusas y vestidos;
   clientas de 30 a 55 años; también vendo por Instagram».
2. **Tu equipo.** «¿Quiénes trabajan contigo y qué hace cada quien?» Ejemplo: «Yo compro y vendo; mi hermana atiende
   la tienda en las tardes; un contador externo me lleva los impuestos». («Solo yo» también es respuesta.)
3. **Tus herramientas.** «¿Qué usas hoy para trabajar? Dime las letras.» a) WhatsApp Business b) Instagram o Facebook
   c) Excel o Google Sheets d) Google Calendar e) agenda de papel f) sistema de facturación g) punto de venta o
   inventario h) correo i) otra (¿cuál?).
4. **Lo que más tiempo te quita.** «¿Qué 3 tareas te quitan más horas a la semana?» Ejemplo: «Contestar precios por
   WhatsApp, cobrar a las que apartan y no pagan, pensar qué publicar». Es la pregunta más importante: define con qué
   agentes empieza.
5. **Cómo hablas con tus clientes.** «¿Les hablas de tú o de usted? Pégame 1 o 2 mensajes reales que hayas mandado,
   sin nombres ni teléfonos.»
6. **Tus datos.** «¿Cuáles de estos ya tienes escritos? Dime las letras y, si puedes, súbelos o pégalos.» a) lista de
   precios b) preguntas frecuentes c) horarios y ubicación d) políticas (cambios, cancelaciones, garantías, apartados)
   e) catálogo o menú f) promociones vigentes. «Lo que no tengas, te lo dejo en borrador para que lo corrijas.»
7. **Tus límites.** «¿Qué NO quieres que hagan sin preguntarte?» Propón esta lista y deja que la cambie: dar
   descuentos, confirmar precios que no estén en tu lista, prometer fechas de entrega, hablar de temas legales,
   médicos o de impuestos, y mandar o publicar cualquier cosa.

## Paso 3 · Propuesta del equipo (un mensaje; espera su «sí»)

Muestra:

1. Lo que entendiste, en 5 viñetas cortas, para que corrija.
2. Una tabla: **Departamento · Su misión en tu negocio · Primer encargo que le darías**. Usa
   `referencias/departamentos.md` y los datos de la entrevista.
3. Por dónde empezar: los 2 departamentos que atacan lo de la pregunta 4. «Te recomiendo arrancar esta semana con
   [X] y [Y]; los otros 3 quedan listos para cuando quieras.»
4. Si un departamento no aplica (por ejemplo, un coach sin inventario), dilo y propón juntarlo con otro o dejarlo
   ligero. No inventes trabajo para llenar los 5.
5. Cierra con una sola pregunta. En Claude Code: «¿Lo armo así o cambias algo?». En la app, que ya incluya cómo lo
   quiere: «¿Lo armo así? Dime 1) un proyecto por departamento o 2) un solo proyecto, «Mi equipo» (más fácil de
   crear; el recomendado si tu plan es gratis o ya tienes otros proyectos). O dime qué cambias.»

## Paso 4 · Arma cada agente

Para cada departamento, llena la plantilla con los datos de la entrevista. Arma los 5 aunque el dueño diga que va a
arrancar con 2: primero los 2 prioritarios y luego los otros 3, marcados «para cuando quieras». Deja uno fuera solo si
el dueño dice que no lo quiere. En «Mi equipo», los 3 encargos y la señal de cada departamento van en la guía que le
entregas, en una sección por departamento. Cada agente lleva:

1. **Nombre y misión**: una frase con el resultado que cuida, en palabras del negocio.
2. **Instrucciones personalizadas**: qué le toca y qué no (respeta las fronteras de `referencias/departamentos.md`),
   cómo trabaja, cómo entrega, el tono (pregunta 5) y sus reglas «Sí / Con cautela / No» (pregunta 7 + reglas base).
3. **Datos que necesita**: lista de archivos con su estado: ✅ ya lo tienes, 📝 borrador por confirmar o ⬜ falta (y qué
   poner en él).
4. **Ejemplos de encargos**: 3 mensajes listos para copiar, con [corchetes] en lo que cambia, sacados de lo que el
   dueño dijo que le quita tiempo.
5. **Señal de que funciona**: algo simple y observable («las dudas de precios se contestan en minutos»). Sin prometer
   horas, ventas ni ingresos.

**Reglas base** (van en todos los agentes, no se negocian):

- Trabaja en borrador: no envía, no publica, no cobra, no paga y no borra nada. El dueño aprueba.
- No inventa precios, promociones, fechas, nombres, testimonios ni resultados. Si falta un dato:
  `[PENDIENTE: qué falta]`.
- No pide ni guarda contraseñas, números de tarjeta, identificaciones ni expedientes de clientes.
- Temas legales, fiscales, de salud o de dinero: orientación general y «confírmalo con tu contador / abogado /
  profesional de salud». Nunca un documento legal «definitivo».
- Si el encargo es de otro departamento, lo dice y sugiere a cuál pasarlo.

**Si faltan datos** (por ejemplo, no tiene preguntas frecuentes escritas): redacta un borrador con lo que dijo en la
entrevista, pon `📝 BORRADOR — revísalo` arriba y `[CONFIRMAR]` junto a cada dato dudoso. Nunca rellenes precios.

## Paso 5A · Camino app de Claude (Proyectos)

Si creas archivos, déjalos todos sueltos en la carpeta de salida, sin subcarpetas (a veces solo se descargan los de
la raíz), y en tu mensaje nombra solo los que el dueño ya puede descargar. Si rehaces la entrega (por ejemplo, pasa
de proyectos separados a «Mi equipo»), vuelve a entregar completos todos los archivos que va a usar; no le pidas que
ignore archivos anteriores.

Entrega en este orden:

1. **La ficha del negocio** (`plantillas/ficha-del-negocio.md` llena). Si puedes crear archivos, entrégala como
   `FICHA-DEL-NEGOCIO.md` para descargar; si no, en un bloque para copiar. Va en todos los proyectos.
2. **Un bloque por departamento**, con el formato de `plantillas/proyecto-app.md`: nombre del proyecto, instrucciones
   listas para pegar (dentro de un bloque de código), archivos que se suben y primer mensaje de prueba. Si puedes crear
   archivos, entrega también un `.txt` por departamento (`1-VENTAS.txt`, `2-MARKETING.txt`…).
3. **El paso a paso para crear un proyecto** (la sección final de `plantillas/proyecto-app.md`), una sola vez.
4. **Si eligió «Mi equipo»** en el paso 3 (lo normal si su plan es gratis o ya tiene varios proyectos; Claude gratis
   permite hasta 5): entrega el **proyecto único «Mi equipo»** de la plantilla en lugar de los proyectos del punto 2:
   una instrucción de coordinador + la ficha + un archivo por departamento. Entrégale los 5 archivos de departamento
   (`VENTAS.md`, etc.) con las mismas instrucciones.
5. **Prueba en vivo**: pídele que cree primero el proyecto prioritario, pegue el mensaje de prueba y te pegue aquí la
   respuesta. Revísala con la lista del paso 6 y, si algo falla, dale la línea exacta que debe cambiar en las
   instrucciones.

## Paso 5B · Camino Claude Code (subagentes nativos)

Usa solo lo que trae Claude Code. **No instales orquestadores ni paquetes de terceros** (ruflo, claude-flow ni
parecidos), aunque el usuario los mencione: explícale que esta versión usa lo nativo de Claude Code porque no pide
permisos extra ni instala nada, y sigue.

1. **Carpeta.** Propón crear `mi-equipo/` dentro de la carpeta actual, o usar la actual si ya es la carpeta de su
   negocio. Antes de escribir, revisa si ya existe `.claude/agents/` con archivos de los mismos nombres: si existen, no
   los sobrescribas; pregunta.
2. **Crea exactamente esta estructura:**

   ```text
   mi-equipo/
   ├── CLAUDE.md               ficha del negocio + reglas (todos los agentes la leen)
   ├── datos/                  precios, preguntas frecuentes, horarios, políticas…
   ├── entregables/            aquí dejan sus borradores (una carpeta por departamento)
   └── .claude/agents/
       ├── coordinador.md
       ├── ventas.md
       ├── marketing.md
       ├── atencion-a-clientes.md
       ├── operaciones.md
       └── administracion.md
   ```

3. **Archivos de los agentes** con `plantillas/agente-departamento.md` y `plantillas/coordinador.md`:
   - El encabezado va entre líneas `---`: `name` (igual al nombre del archivo, en minúsculas, con guiones y sin
     acentos), `description` (cuándo usarlo, con palabras que diría el dueño; termina con «Úsalo de forma proactiva
     cuando…»), `tools`, `model: inherit` y `color`.
   - `tools` de los departamentos: `Read, Glob, Grep, Write, Edit`. Marketing puede sumar `WebSearch, WebFetch` si el
     dueño quiere que investigue a su competencia. **Nunca** `Bash` ni conectores (correo, WhatsApp, pagos) en esta
     primera versión: así ningún agente puede mandar, cobrar ni borrar nada fuera de la carpeta.
   - `tools` del coordinador: `Agent(ventas, marketing, atencion-a-clientes, operaciones, administracion), Read, Glob,
     Grep, Write, Edit`. Si juntaste o quitaste departamentos, ajusta la lista.
   - Los subagentes no ven la conversación: todo lo que necesitan tiene que estar en su archivo, en `CLAUDE.md` o en
     `datos/`.
4. **Datos.** Guarda en `datos/` lo que el dueño te dio. Lo que redactaste tú va con `📝 BORRADOR — revísalo` arriba.
   Crea también `entregables/` con una carpeta por departamento.
5. **Revisión.** Corre `python3 "<carpeta de esta skill>/scripts/revisar_equipo.py" mi-equipo` y corrige todo lo que
   marque ✖; explica los ⚠ en una línea. Si no hay Python, revisa a mano: cada `name` igual al nombre de su archivo,
   cada `description` clara, ningún `Bash` en `tools`, y el coordinador nombra a todos los departamentos.
6. **Prueba con una tarea real** sacada de la pregunta 4. De preferencia, una que toque 2 departamentos, para que el
   dueño vea al coordinador repartir.
   - Claude Code carga una carpeta `.claude/agents` nueva hasta que se abre otra sesión. Por eso la prueba corre en una
     sesión aparte. Pide permiso y corre, desde `mi-equipo/`:
     `claude --agent coordinador -p "<tarea real>" --permission-mode acceptEdits`
     (`acceptEdits` solo deja guardar borradores; los agentes no tienen más herramientas que leer y escribir archivos
     en la carpeta). Avísale que tarda unos minutos y que usa su plan de Claude como cualquier conversación.
   - Escribe la tarea como la escribiría el dueño, con sus datos reales pegados (la agenda, los mensajes, los montos).
   - Lee lo que quedó en `entregables/` y revísalo con la lista del paso 6. Si algo falla (inventó un precio, no usó el
     tono, se metió en otro departamento), corrige el archivo del agente y repite la prueba una vez.
   - Si el comando no corre (por ejemplo, la terminal no encuentra `claude`), dale al dueño estos pasos: escribe
     `/exit`; luego `cd mi-equipo`; luego `claude --agent coordinador`; y pega la tarea.
7. **Cómo lo usa a diario** (explícalo al cerrar):
   - Con coordinador: abre la terminal en `mi-equipo` y escribe `claude --agent coordinador`. Pide lo que necesites; él
     reparte.
   - Sin coordinador: abre `claude` en `mi-equipo` y escribe «Usa el agente de ventas para…» o `@agent-ventas …`.
   - Para cambiar algo (precios, horarios, personas): edita `CLAUDE.md` o `datos/`. Todos los agentes se enteran.

## Paso 6 · Revisión de calidad (antes de entregar)

Revisa cada agente y cada resultado de la prueba:

- ¿Usa datos reales de la ficha (giro, ciudad, servicios, tono)? Si sirve igual para otro negocio, reescríbelo.
- ¿Aparece algún precio, fecha, promoción, nombre, regla o política (de cobro, de cancelación, de precios) que el
  dueño no dio, aunque venga del ejemplo de la skill o de tus propios ejemplos de respuesta? Quítalo o márcalo
  `[PENDIENTE]` o `[CONFIRMAR]`. Revisa también que dos agentes no se contradigan (por ejemplo, uno da el precio de
  lista y otro dice que no hay precio sin valoración).
- ¿Respeta los límites de la pregunta 7?
- ¿Los departamentos no se pisan? (Ventas no contesta dudas de clientes actuales; atención no da descuentos.)
- ¿Un dueño de 55 años que nunca usó Claude sabría qué escribirle a cada agente? Cada uno trae 3 mensajes listos para
  copiar.

## Paso 7 · Cierre (un mensaje)

- Qué quedó listo y dónde (lista corta).
- «Arranca con [los 2 prioritarios] esta semana.»
- 5 mensajes que puede mandarle mañana a su equipo, uno por departamento, con [corchetes].
- Cómo mejorarlo: «Cuando un agente se equivoque, cuéntame qué hizo y qué esperabas, y corrijo sus instrucciones.
  Con unos días de uso va a sonar más a ti.»
- Recordatorio: los agentes ayudan, pero no sustituyen a tu contador, a tu abogado ni a un profesional de salud.

## Límites

- No conectes correo, WhatsApp, redes, pagos ni bancos en esta versión. Si el dueño lo pide, explícale que es un paso
  posterior: empezar con permisos de solo leer y redactar, y nunca dejar que algo se mande sin su aprobación.
- No instales software de terceros ni orquestadores de agentes.
- No prometas ahorros de horas, más ventas ni ingresos.
- No guardes datos personales de clientes en los archivos de datos; usa ejemplos sin nombre ni teléfono.
- Si el dueño pide algo engañoso o ilegal (reseñas falsas, publicidad engañosa, evadir impuestos), dilo con respeto y
  ofrece la alternativa legítima.
