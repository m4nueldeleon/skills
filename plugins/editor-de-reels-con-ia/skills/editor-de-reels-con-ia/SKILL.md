---
name: editor-de-reels-con-ia
description: Edita en la computadora una grabación propia y la deja lista como Reel. Recorta pausas, ordena las tomas, elige el inicio con una frase que sí se dijo, empareja el volumen, pone subtítulos sincronizados y exporta un MP4 vertical u horizontal con su SRT, sin tocar el original. Necesita Claude Code (u otro asistente que ejecute programas) con Node.js y FFmpeg. Úsala cuando digan «usa la skill editor-de-reels-con-ia», «ayúdame a editar mi video», «recorta las pausas», «ponle subtítulos a mi video» o «hazme un reel con esta grabación». NO usar para videos animados sin grabación (→ video-animado-de-tu-negocio) ni para publicar el video.
---

# Editor de Reels con IA · Manuel de León

Ayuda a una persona sin experiencia técnica a convertir su grabación en un MP4 revisable. Empieza leyendo [README.md](README.md) para instalación, comandos y límites. Ejecuta los scripts desde la carpeta de esta skill.

## Flujo de edición

1. Localiza el archivo proporcionado, inspecciona video y audio, y comprueba Node.js, FFmpeg, ffprobe y las dependencias del paquete. El usuario debe trabajar en un asistente con ejecución local; descargar el ZIP en el teléfono no ejecuta el editor.
   - Si el video viene de un iPhone, pide que lo pase desde la app Archivos o por cable: elegido desde Fotos, el teléfono puede entregar una copia de menor resolución.
   - Si `ffprobe` muestra que el audio no empieza en 0 (`start_time`), avísalo y revisa con cuidado que la voz vaya con los labios en el MP4 final.
2. Obtén una transcripción con tiempos del original. Si tienes una herramienta de transcripción, úsala y adapta su resultado al formato de [examples/transcripcion.json](examples/transcripcion.json). Como alternativa, configura Whisper local siguiendo el README. Prioriza tiempos por palabra para subtítulos cortos. Revisa los nombres y cifras en el audio; no presentes una transcripción automática como verificada.
3. Propón hasta tres posibles inicios basados en frases que sí se dicen. Para cada uno registra la cita exacta, sus tiempos y el motivo: problema concreto, contraste, resultado demostrable o pregunta que el propio video responde. Elige el que sirva al objetivo del usuario. No inventes números ni prometas que será viral.
4. Si conviene reordenar o excluir repeticiones, crea un plan usando tiempos del original. El formato está en [examples/plan.json](examples/plan.json). El primer fragmento será el inicio. Evita volver a incluir el mismo gancho por accidente. Revisa con audio las tomas repetidas: la transcripción puede ocultarlas.
5. Ejecuta `scripts/editar.mjs` con transcripción y salida nueva. Por omisión usa vertical, fondo desenfocado y calidad estándar. Añade `--motion` si un acercamiento suave ayuda al contenido. Usa `--noise-reduction` solo para ruido constante; no prometas restaurar una grabación saturada.
6. Inspecciona el MP4 final y una muestra de sus subtítulos. Escucha los cortes y confirma rostro, encuadre, texto, duración y audio. Si tienes transcripción disponible, vuelve a transcribir los fragmentos donde eliminaste repeticiones. Entrega MP4, SRT e informe con cualquier limitación pendiente.
   - Una pausa de más de medio segundo entre frases se siente como que el video se cae. Si la oyes, exporta de nuevo con `--pause 0.4` y confirma que no se coma palabras suaves.
   - Que ninguna frase se oiga dos veces: si subiste una frase al inicio, quítala de su lugar original en el plan.

## Invariantes del motor

- Los silencios se detectan con `silencedetect` sobre audio real. Los tiempos de palabras se usan para subtítulos y decisiones editoriales; no sustituyen la medición de pausas.
- Los fragmentos se ajustan a fotogramas de 30 fps. Un mapa une tiempos originales y finales; subtítulos y otros eventos posteriores deben usar esa nueva línea temporal.
- Los cortes de audio llevan fades de 12 ms para reducir clics. Se normaliza a un objetivo de −16 LUFS con techo de pico verdadero de −1.5 dB; es un objetivo del filtro, no una medición garantizada de cada archivo exportado.
- Los subtítulos se dibujan como PNG transparente y una capa de video. No se requiere `libass`. El texto del JSON se trata como texto, nunca como comandos.
- El crudo no se sobrescribe. Todos los destinos deben ser nuevos. Si algo falla, informa el error y corrige la causa; no ocultes un paso fallido.

## Imágenes y acabado opcional

Para imágenes de apoyo, parte de una imagen del usuario o genera una con la herramienta disponible y sus propios créditos. Usa una escena que explique lo que está diciendo y registra en qué segundo debe aparecer. Cada imagen va de 2 a 4 segundos, mientras la voz la explica: menos de un segundo se ve como un destello. El script `scripts/broll.mjs` inserta PNG/JPEG/WebP sobre el crudo, conserva el audio y no cambia su duración. Edita después para colocar subtítulos encima.

El desenfoque disponible es del fondo al adaptar el formato. El zoom es un acercamiento suave; no hay seguimiento automático del rostro, enfoque óptico, eliminación semántica de muletillas ni generación de imágenes incorporada en los scripts. Si el usuario pide esas funciones, explica qué herramienta o trabajo adicional haría falta y usa solo los accesos que tenga disponibles.

## Entrega

Ofrece un resumen sencillo: duración anterior y final, cambios que se hicieron, nombre de los archivos y qué revisar. La edición usa material y cuentas del usuario. Esta skill no publica videos ni manda mensajes por sí sola.
