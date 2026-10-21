# Prepara tus ventas con IA, llenando espacios

Manuel de León · Recursos de IA para negocios · 20 de octubre de 2026

Seis flujos (y una ruta que los junta) para llegar preparado a cada venta y dar seguimiento sin sonar
desesperado. No tienes que escribir instrucciones: eliges un número, llenas los espacios y Claude te entrega el
texto listo.

**¿Qué es una skill?** Un archivo de instrucciones que le enseña a Claude a hacer una tarea, siempre de la misma
manera. Se instala una sola vez. Si todavía no tienes Claude, entra a claude.ai o baja la app de Claude y crea
tu cuenta con tu correo.

## Qué hace

Si le dices de entrada qué necesitas («prepárame la ficha y el guion para mi cita del jueves»), va directo a eso.
Si no, te pregunta «¿Qué necesitas hoy?» y te da este menú:

1. **FICHA**: antes de una llamada o cita, ordena lo que se sabe del cliente, lo que falta saber y las
   preguntas que le vas a hacer.
2. **GUION**: qué decir en la llamada o la cita, en seis pasos, con las objeciones más probables y cómo
   contestarlas.
3. **SEGUIMIENTO**: tres mensajes de WhatsApp (día 1, 3 y 7) que traen algo útil en vez de «¿ya lo pensaste?».
4. **PROPUESTA**: tu propuesta en una sola hoja, con precio claro y cómo decir que sí.
5. **COMPETENCIA**: una tabla con los precios y lo que ofrece tu competencia, con los datos que tú traigas o los
   que estén publicados.
6. **REVISAR**: pegas tu mensaje y te señala las frases que te restan ventas, te explica por qué y te da el
   mensaje corregido.
7. **RUTA**: ficha, guion, propuesta y seguimiento, en ese orden, para un mismo cliente.

**Lo que nunca hace:** inventar datos de tu cliente o de tu competencia. Lo que no se sabe lo marca
«Por confirmar» y lo convierte en una pregunta para la cita. Si tu Claude no puede buscar en internet, te pide
que pegues lo que sabes (su página, sus reseñas, lo que te dijo por mensaje).

## Antes de empezar, ten a la mano

- Qué vendes y cuánto cuesta.
- El nombre de tu cliente y lo que te ha dicho (si es un mensaje, cópialo).
- Si tiene página, Instagram o perfil en Google Maps, el enlace.

## Instálala en Claude (app o claude.ai)

Hazlo desde la computadora (en claude.ai o en la app de escritorio). Son cinco minutos y una sola vez. Ya
instalada, pruébala también en la app del celular con la misma cuenta; si ahí no aparece, úsala desde la
computadora. ¿Solo tienes celular? Pide a alguien que te ayude a instalarla una vez desde una computadora, o usa
la opción «Sin instalar nada».

1. **Descarga el archivo** de la skill. No lo abras ni lo descomprimas:
   https://github.com/m4nueldeleon/skills/releases/download/descargas/flujos-ia-para-vender.zip
   Si usas Safari en Mac y en Descargas te aparece una carpeta en lugar del archivo `.zip`, haz clic derecho en
   la carpeta → **Comprimir**, y usa el `.zip` que se crea.
2. **Activa la ejecución de código.** En Claude, haz clic en tu nombre o tu inicial (abajo a la izquierda), entra a
   **Configuración → Capacidades** (*Settings → Capabilities*) y enciende **Ejecución de código y creación de
   archivos** (*Code execution and file creation*). Es el permiso que deja a Claude usar skills; no instala nada en
   tu computadora. Si usas Claude en una empresa, puede que esto lo tenga que activar tu administrador.
3. **Sube la skill.** Busca **Personalizar → Skills** (*Customize → Skills*) en el menú de Claude, haz clic en
   **+**, luego en **Crear skill** (*Create skill*) y en **Subir una skill** (*Upload a skill*). Elige el archivo
   que descargaste.
4. Revisa que la skill aparezca en tu lista con el interruptor **encendido**.
5. Abre un chat nuevo y escribe: `Quiero preparar una venta`. Debe aparecer el menú «¿Qué necesitas hoy?».
   Si no aparece, escribe: `Usa la skill flujos-ia-para-vender`.

Si no encuentras esas opciones, Claude pudo haber cambiado el nombre de los menús: busca «Skills» en la
configuración, o usa la opción «Sin instalar nada» de más abajo.

## Instálala en Claude Code

Si no sabes qué es Claude Code, sáltate esta parte. Si lo usas, escribe estas dos líneas dentro de Claude Code,
una por una:

```text
/plugin marketplace add m4nueldeleon/skills
/plugin install flujos-ia-para-vender@manuel-de-leon
```

Si no la reconoce enseguida, cierra Claude Code y vuelve a abrirlo. Para recibir mejoras más adelante:
`/plugin marketplace update manuel-de-leon`.

## Sin instalar nada (también sirve en ChatGPT o Gemini)

1. Abre las instrucciones de la skill (es una página de solo texto):
   https://raw.githubusercontent.com/m4nueldeleon/skills/main/plugins/flujos-ia-para-vender/skills/flujos-ia-para-vender/SKILL.md
2. Selecciona todo (Cmd+A en Mac, Ctrl+A en Windows) y cópialo (Cmd+C o Ctrl+C).
3. Pégalo al inicio de un chat nuevo, escribe debajo `Sigue estas instrucciones y muéstrame el menú.` y envía.

Si usas Proyectos en Claude (o un GPT propio en ChatGPT), pega el texto en las instrucciones del proyecto y ya no
tendrás que copiarlo cada vez.

## Tres ejemplos para copiar

Copia el mensaje, cambia lo que está entre corchetes o los datos de ejemplo por los tuyos, y envíalo.

### 1 · Inmobiliaria: preparar una cita (ficha y guion)

```text
Tengo cita el [jueves a las 5] con [Laura Mendoza]. Quiere vender su casa en
[Zapopan] y está entrevistando a [dos] asesores. Yo soy [asesora inmobiliaria
independiente] y cobro [5 % de comisión]. Me escribió por [Facebook] y me dijo
que [ya tuvo una mala experiencia con otro asesor]. Prepárame la ficha y el
guion para la cita. Le hablo de [usted].
```

**Qué vas a recibir:** una ficha con lo que se sabe y lo que hay que preguntarle (por ejemplo, qué salió mal la
vez pasada), y un guion de seis pasos que termina con una fecha para el siguiente paso. Como Laura es una persona
y no un negocio, Claude no la busca en internet: trabaja con lo que tú le cuentas.

### 2 · Consultorio dental: seguimiento de un presupuesto (WhatsApp día 1, 3 y 7)

```text
SEGUIMIENTO
A quién: [Roberto]
Qué le coticé: [limpieza profunda y dos resinas, 4,800 pesos]
Cuándo fue: [el lunes 19 de octubre, en el consultorio]
Qué quedó pendiente: [dijo que lo iba a pensar por el precio]
Algo nuevo y cierto que le puedo dar: [aceptamos el pago en dos partes]
Trato: [de usted]
```

**Qué vas a recibir:** tres mensajes cortos con su fecha, uno para cada día, y respuestas listas por si contesta
«lo estoy pensando», «está caro» o «ahorita no». Ninguno menciona el tratamiento por WhatsApp: solo la cita.

### 3 · Tienda de ropa: revisar un mensaje antes de mandarlo

```text
REVISAR
Hola!! Somos la boutique más completa de Tlaquepaque 😊 No sé si te
interese, pero te tengo un descuentito en los vestidos de fiesta. ¿No te
gustaría pasar a verlos?
```

**Qué vas a recibir:** un semáforo (verde, amarillo o rojo), cada frase que te resta con el motivo y qué decir en
su lugar, y tu mensaje corregido, listo para copiar.

**Más ideas:** `PROPUESTA` para mandar una cotización en una hoja; `COMPETENCIA` para comparar tus precios con
los de tres negocios de tu zona (trae lo que sepas de cada uno).

## Qué esperar

- Te hace pocas preguntas, una a la vez. Si contestas «no sé», sigue y deja ese espacio marcado.
- Los mensajes salen en cuadros con botón de copiar. Revísalos y mándalos tú: la skill no manda nada.
- Puedes escribir en cualquier momento: `MENÚ`, `MÁS CORTO`, `DE USTED`, `DE TÚ`, `EN LISTA` u
  `OTRA VERSIÓN`.
- La primera vez te deja un bloque «MI NEGOCIO». Guárdalo y pégalo al empezar la próxima vez, para no repetir
  tus datos.
- Te ayuda a prepararte y a decir las cosas con claridad. No garantiza que el cliente compre: eso depende de tu
  oferta y de que sí hagas el seguimiento.

## Antes de mandar cualquier cosa

Léelo en voz alta. Cambia cualquier palabra que tú no dirías. Revisa que los precios, las fechas y los nombres
sean correctos: la skill usa lo que tú le das, y si le diste un dato equivocado, el texto lo va a repetir.

## Cuida tus datos y los de tus clientes

- No pegues cuentas bancarias, identificaciones ni expedientes médicos.
- Escribe solo lo que necesitas para la venta: nombre, qué pidió, qué le preocupa.
- La propuesta no sustituye un contrato. Si hay mucho dinero de por medio, condiciones legales o impuestos,
  revísala con tu contador o abogado.

## Enlaces oficiales

- [Usar skills en Claude (centro de ayuda)](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [Instalar skills en Claude Code](https://code.claude.com/docs/en/skills)
- [Código de esta skill en GitHub](https://github.com/m4nueldeleon/skills)
