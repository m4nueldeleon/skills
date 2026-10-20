# Tu consejo de asesores con IA

Manuel de León · Recursos de IA para negocios · 20 de octubre de 2026

Cinco miradas que te contradicen antes de que tomes una decisión de negocio, y una arena para quedarte con
la mejor versión de un texto.

## Qué hace

Si le preguntas a la IA «¿verdad que es buena idea subir mis precios?», casi siempre te va a decir que sí.
Si le preguntas lo contrario, también. Te dice lo que quieres oír. Eso no sirve cuando hay dinero de por
medio.

Esta skill hace lo contrario. Antes de una decisión (subir precios, abrir otra sucursal, contratar a
alguien, lanzar un producto), convoca a cinco asesores. Cada uno revisa tu idea desde un ángulo distinto y
te dice, con números y razones, dónde está el hueco:

| Asesor | Lo que siempre te pregunta |
|---|---|
| 🧮 **La Contadora** | ¿Te alcanza? Hace la cuenta de cuánto ganas, cuánto arriesgas y cuántas ventas puedes perder. |
| 👤 **Tu Cliente** | ¿Y yo por qué pagaría eso? Habla como tu cliente de siempre y te dice qué notaría y a dónde se iría. |
| 📋 **La Encargada** | ¿Quién lo va a cargar? Revisa tus horas, tu equipo y lo que se va a descuidar. |
| 🔍 **El Forense** | Pasó un año y salió mal: ¿de qué murió? Te cuenta cómo fracasaría tu idea, para que lo evites. |
| 🧪 **El Probador** | ¿Cómo te lo pruebas antes de pagarlo completo? Diseña una prueba chica, con fecha y meta. |

Al final te entrega un **veredicto** (Adelante · Adelante, con condiciones · Pruébalo primero · Todavía no ·
No), el **siguiente paso para esta semana** y la **señal** que te dice si sigues o frenas.

Además trae el **modo arena**: escribe varias versiones de un mensaje (de 3 a 5, cada una con una estrategia
distinta), las califica con criterios claros, pone a las dos mejores cara a cara y te entrega la ganadora,
mejorada y lista para copiar.

## Instálala

Sigue el asistente de instalación: https://manueldeleonm.com/recursos/consejo-de-asesores/

Si prefieres hacerlo a mano:

**En Claude (app de escritorio, celular o claude.ai)**

1. Descarga el ZIP: https://github.com/m4nueldeleon/skills/releases/download/descargas/consejo-de-asesores.zip
   No lo descomprimas.
2. En Claude, entra a **Configuración → Capacidades** y enciende **Ejecución de código y creación de
   archivos**.
3. Abre **Personalizar → Skills**, toca **+**, elige **Crear skill → Subir una skill** y escoge el ZIP.
4. Revisa que el interruptor de la skill quede encendido.

**En Claude Code**

```text
/plugin marketplace add m4nueldeleon/skills
/plugin install consejo-de-asesores@manuel-de-leon
```

Confirma en el panel que se abre y escribe `/reload-plugins` (o reinicia Claude Code).

**Sin instalar nada (Claude, ChatGPT o Gemini)**

Abre las instrucciones de la skill
(https://github.com/m4nueldeleon/skills/blob/main/plugins/consejo-de-asesores/skills/consejo-de-asesores/SKILL.md),
copia todo el texto y pégalo al inicio de una conversación, o en las instrucciones de un Proyecto (Claude o
ChatGPT) o de un Gem (Gemini). Son solo instrucciones, no necesita programas. Si las pegas en una
conversación, valen solo para esa conversación; en un Proyecto o un Gem, se quedan guardadas.

## Cómo se usa: dos frases

- Para una decisión, empieza tu mensaje con **«Convoca al consejo:»** y cuenta lo que estás pensando hacer.
- Para un texto, empieza con **«Arena:»** y di qué necesitas escribir.

Si la skill no se activa sola, empieza con «Usa la skill consejo-de-asesores».

Mientras más números le des (aunque sean aproximados), mejor trabaja el consejo. Si no los sabes, contesta
«no sé»: trabaja con supuestos y te los marca.

## 3 ejemplos listos para copiar

Cambia lo que está entre [corchetes] por lo tuyo.

**1. Subir precios**

```text
Convoca al consejo: tengo [una taquería] en [Guadalajara]. Estoy pensando en subir
[la orden de tacos de 75 a 85 pesos]. Vendo como [1,800 órdenes al mes] y de cada
venta me quedan como [26 pesos] después de pagar lo que me cuesta. La competencia
cobra [70]. La otra opción es [dejar el precio igual].
```

**2. Abrir otra sucursal o contratar**

```text
Convoca al consejo: tengo [una clínica dental] en [San Antonio] desde hace [5 años].
Estoy pensando en [abrir una segunda clínica en otra zona / contratar a otra
doctora]. Me costaría [cuánto al mes y cuánto para empezar]. Hoy vendo [cuánto al
mes] y me quedan [cuánto] libres. Tengo ahorrado [cuánto]. Tengo que decidir antes
de [fecha].
```

**3. Arena para un mensaje**

```text
Arena: necesito un mensaje de WhatsApp para [clientes que pidieron cotización y no
contestaron] de mi [inmobiliaria]. Quiero que [me contesten si siguen buscando casa].
Esto me dio la IA y no me convence: [pega aquí el texto].
```

## Qué puedes escribir después

| Escribe | Y pasa esto |
|---|---|
| **otra ronda** + un dato nuevo | El consejo vuelve a revisar con ese dato y te dice si cambia el veredicto |
| **pregúntale a [la Contadora]** | Ese asesor te explica más a fondo y te hace 2 preguntas |
| **más duro** | Cada asesor te da su objeción más fuerte, sin suavizar |
| **arena** | Si tu siguiente paso es escribir algo, pone a competir versiones de ese texto |
| **resumen para mi socio** | Cinco líneas para mandar por WhatsApp |
| **otra arena** | Versiones nuevas con estrategias que no se usaron |
| **más corta** | Recorta la ganadora sin perder lo importante |

## Qué esperar

- Puede hacerte hasta tres preguntas antes de empezar, una por una. Si tu primer mensaje ya trae lo
  necesario, empieza de una vez.
- Te va a contradecir. Es a propósito. Si todo te suena demasiado cómodo, escribe «más duro».
- Una respuesta del consejo se lee en dos o tres minutos.
- **¿Por qué la arena hace de 3 a 5 versiones y no 100?** Cada versión gasta parte del uso de tu cuenta de
  Claude, y los planes tienen un límite cada cierto número de horas y por semana. Cien versiones te acaban
  ese uso y tardan mucho. Además, después de 4 o 5 versiones bien distintas, las nuevas se parecen entre sí.
  Lo que hace ganar no es la cantidad: es que las versiones sean de verdad distintas y que los criterios estén
  claros desde antes.

## Antes de decidir

El consejo trabaja con lo que tú le cuentas: si los números están mal, el veredicto también. Son cinco
miradas de la misma IA; ayudan a ver lo que no estabas viendo, pero no adivinan el futuro ni garantizan
ventas. La decisión es tuya.

Si tu decisión toca impuestos, contratos, despidos, créditos o temas legales, úsalo para ordenar tus ideas y
llévalo después con tu contador o tu abogado. La Contadora del consejo no sustituye a tu contador.

Y el mejor juez de un mensaje no es la IA: son tus clientes. Si dudas entre dos versiones, manda una a la
mitad de tus clientes y la otra a la otra mitad, y quédate con la que más respuestas te traiga.

## Enlaces oficiales

- [Código de esta skill (público)](https://github.com/m4nueldeleon/skills)
- [Instalar skills en Claude Code](https://code.claude.com/docs/en/skills)
