# Tu editor de Reels con IA

**Manuel de León · Recurso gratuito de la comunidad**

Convierte una grabación tuya en un video con menos pausas, audio más uniforme y subtítulos grandes. La IA te ayuda a elegir qué decir primero; los scripts hacen la edición y exportan un MP4.

## Empieza por aquí

1. Instala la skill en Claude Code con el asistente de https://manueldeleonm.com/recursos/editor-de-reels-con-ia/ (dos comandos), o descomprime esta carpeta en una computadora.
2. Abre Claude Code (o Codex u otro asistente que pueda leer archivos y ejecutar programas en tu equipo) en la carpeta donde está tu video.
3. Coloca una copia de tu video en esa carpeta y pega este mensaje:

> Lee SKILL.md y ayúdame a editar mi video. Comprueba qué herramientas faltan y configúralas. Transcribe lo que digo, corrige los subtítulos y encuentra un buen inicio usando una frase real del video. Quiero un Reel vertical, con pausas recortadas, audio más uniforme y subtítulos fáciles de leer. Usa fondo desenfocado si hace falta para conservar el encuadre. Conserva mi original y entrégame una copia MP4. Antes de terminar, revisa el video y dime qué requiere un ajuste manual.

Puedes descargar el paquete desde el teléfono. **La edición de este paquete se ejecuta en una computadora**, dentro de tu asistente. No es un editor que funcione dentro de la página web ni una aplicación móvil.

## Qué incluye

| Función | Cómo funciona |
|---|---|
| Recortar pausas | Detecta silencios por volumen del audio y conserva un pequeño margen para respirar. |
| Ordenar el video | El asistente puede crear un plan con los fragmentos y el orden que necesitas. |
| Elegir un buen inicio | El asistente analiza tu transcripción, cita la frase y explica su elección. No hay una puntuación que garantice viralidad. |
| Audio más uniforme | Normaliza volumen. Puedes activar una reducción ligera de ruido constante. |
| Subtítulos grandes | Usa tu transcripción con tiempos y los ajusta a los cortes. Exporta el video con texto visible y también un archivo SRT editable. |
| Formato para redes | Vertical 9:16 u horizontal 16:9, en calidad estándar o Full HD. |
| Movimiento | Acercamiento suave opcional de hasta 3.5 %. |
| Fondo desenfocado | Adapta el formato manteniendo el contenido completo sobre un fondo borroso. |
| Imágenes de apoyo | Un segundo script inserta una imagen que tú proporciones. Puedes pedírsela a una herramienta de IA disponible en tu cuenta. |

Los scripts funcionan localmente y no llevan claves ni cuentas incluidas. La instalación descarga dependencias; una transcripción local descarga su modelo la primera vez. Si usas un asistente o un generador de imágenes de pago, se aplica tu propio plan o tus créditos.

## Instalación para tu asistente

Se necesitan **Node.js 22 o posterior** y **FFmpeg con ffprobe**. Para transcribir localmente también puedes instalar Python y Whisper. Si tu asistente ya tiene otra transcripción con tiempos, puede convertirla al formato de `examples/transcripcion.json`.

Comprueba las herramientas:

```bash
node --version
ffmpeg -version
ffprobe -version
```

Instala las dependencias desde esta carpeta:

```bash
npm ci
```

FFmpeg: en macOS con Homebrew, `brew install ffmpeg`. En Windows y Linux sigue las opciones de la [página oficial de descarga](https://ffmpeg.org/download.html). Node.js se descarga desde [nodejs.org](https://nodejs.org/). Después de instalar, abre de nuevo tu terminal.

## Transcribe tu video

El editor necesita un JSON con el texto y sus tiempos. No basta con pegar un párrafo: sin tiempos no puede colocar los subtítulos.

Una opción local es [Whisper](https://github.com/openai/whisper). Configúralo en un entorno de Python separado. Ejemplo para macOS/Linux con Python 3.11:

```bash
python3.11 -m venv .venv
.venv/bin/python -m pip install -U openai-whisper
.venv/bin/whisper "crudo.mp4" --model base --language Spanish --word_timestamps True --output_format json --output_dir transcripciones
```

En Windows, los ejecutables del entorno están en `.venv\Scripts\python.exe` y `.venv\Scripts\whisper.exe`. Tu asistente puede adaptar la instalación. Un modelo mayor puede mejorar el texto y tardar más; empieza por un fragmento corto.

**Revisa nombres, cantidades y frases antes de editar.** La transcripción puede equivocarse. Si corriges un texto con tiempos por palabra, corrige también `words`, porque esos son los textos que aparecerán en pantalla.

## Exporta tu primer Reel

```bash
node scripts/editar.mjs --input "crudo.mp4" --transcript "transcripciones/crudo.json" --output "salida/reel.mp4"
```

Obtendrás tres archivos:

- `reel.mp4`: video vertical con subtítulos y audio procesado.
- `reel.srt`: subtítulos con los tiempos de la edición final.
- `reel.plan.json`: cortes y relación entre los tiempos originales y los nuevos.

El original permanece intacto. Si el nombre de salida ya existe, el programa pide otro nombre.

### Opciones útiles

| Lo que quieres | Agrega al comando |
|---|---|
| Un acercamiento suave | `--motion` |
| Reducir ruido de fondo constante | `--noise-reduction` |
| Full HD: 1080 × 1920 | `--quality hd` |
| Horizontal: 1280 × 720 | `--format horizontal` |
| Horizontal Full HD: 1920 × 1080 | `--format horizontal --quality hd` |
| Llenar la pantalla con recorte central | `--framing crop` |
| Conservar las pausas | `--keep-silence` |
| Tomar del segundo 12 al 55 | `--from 12 --to 55` |
| Quitar solo pausas de 1 segundo o más | `--pause 1` |
| Detectar como silencio solo audio más bajo | `--threshold=-45` |

El encuadre predeterminado conserva la imagen sobre fondo desenfocado. El recorte central puede cortar rostros laterales o texto; revisa antes de publicar. El script no sigue automáticamente a las personas.

### Pon primero la frase que engancha

Pide al asistente un `plan.json` con los tiempos **del video original**. Puedes reordenar fragmentos y excluir tomas repetidas. `examples/plan.json` muestra el formato; sus tiempos son de ejemplo y deben cambiarse para tu video.

```bash
node scripts/editar.mjs --input "crudo.mp4" --transcript "transcripciones/crudo.json" --plan "plan.json" --output "salida/reel-con-gancho.mp4"
```

El plan usa segundos decimales. Cada entrada tiene `start` y `end`; el orden de las entradas determina el orden del video. No combines `--plan` con `--from` o `--to`.

### Añade una imagen de apoyo

Usa una imagen propia o una que puedas utilizar. Si la generas con IA, pide una escena concreta que explique tu idea. La generación ocurre con la herramienta disponible en tu cuenta; este paquete no genera imágenes por sí solo.

```bash
node scripts/broll.mjs --input "crudo.mp4" --image "apoyo.png" --from 3 --to 6 --output "crudo-con-imagen.mp4"
node scripts/editar.mjs --input "crudo-con-imagen.mp4" --transcript "transcripciones/crudo.json" --output "salida/reel-con-apoyo.mp4"
```

La imagen cubre la pantalla del segundo 3 al 6 y conserva tu voz. Se inserta **antes** de generar subtítulos para que el texto siga visible. Los tiempos de tu transcripción no cambian en ese paso.

## Revisa antes de publicar

- Escucha el principio, cada corte y el final. Si corta respiraciones o palabras suaves, prueba `--threshold=-45` o `--keep-silence`.
- Comprueba nombres, precios, cifras y que los subtítulos coincidan con lo que se oye.
- Verifica que el rostro y las partes importantes quepan en el encuadre.
- Mira el video con el volumen habitual de tu teléfono.
- Asegúrate de tener permiso para utilizar el video y las imágenes.

La reducción de ruido es ligera: no reconstruye una voz saturada ni elimina todas las conversaciones de fondo. Las pausas se detectan por volumen, no por significado; la música constante puede impedir detectarlas. El asistente debe revisar las tomas repetidas porque el script no reconoce errores de discurso. El zoom es un movimiento visual, no cambia el foco óptico de la cámara.

## Si algo falla

| Mensaje o problema | Qué hacer |
|---|---|
| No se pudo iniciar ffmpeg o ffprobe | Instala FFmpeg y vuelve a abrir la terminal. |
| Ya existe el archivo | Elige otro nombre de salida. |
| Solo se detectó silencio | Revisa si hay voz audible o prueba `--keep-silence`. |
| Un subtítulo supera 3 líneas | Pide tiempos por palabra o divide ese segmento del JSON. |
| Los segmentos deben estar ordenados | Corrige los tiempos de la transcripción original; el reordenamiento se hace en el plan. |
| El render tarda demasiado | Prueba un fragmento de 30–60 segundos y calidad estándar. |

Admite videos con audio de hasta 15 minutos; conviene dividir grabaciones largas. El motor finaliza una operación que exceda 30 minutos. El resultado visual depende de la fuente y de las fuentes tipográficas del equipo. Verificado en macOS; Windows y Linux requieren tener los mismos programas disponibles en la terminal.

Para verificar la instalación:

```bash
npm test
npm run test:video
```

La segunda prueba genera un video sintético corto, prueba ambas orientaciones, subtítulos, b-roll y protección del original. Guarda los ejemplos y un informe en una carpeta temporal cuya ruta aparece al terminar. Puedes borrar esa carpeta después de revisarla.

Implementación basada en operaciones documentadas de [FFmpeg](https://ffmpeg.org/ffmpeg-filters.html) y en el formato de transcripción de [Whisper](https://github.com/openai/whisper). Esta edición pública incluye su propio código y no requiere cuentas de Manuel de León.
