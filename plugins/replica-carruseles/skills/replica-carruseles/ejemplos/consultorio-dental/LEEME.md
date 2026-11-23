# Ejemplo: un consultorio dental

Un carrusel completo hecho con esta skill para un consultorio dental genérico. No hay personas, testimonios ni cifras
inventadas: «Tu Consultorio Dental» y `@tuconsultorio.ejemplo` son nombres de ejemplo.

- **Pedido:** «Mi carrusel del día para mi consultorio: algo que haga que la gente que no ha venido en años agende su
  revisión.»
- **Forma:** «señales» (`referencias/estructuras.md`, número 1): portada → por qué importa → 5 señales numeradas →
  resumen para guardar → cierre.
- **Gancho:** fórmula de negación («No esperes a que te *duela* la muela»), con un dolor que el paciente reconoce.
- **Estilo:** `claro`, con el color del consultorio en la palabra clave y en los números; el cierre cambia a fondo de
  color para que la acción se note.
- **La foto** de la lámina 7 está hecha con IA, solo para este ejemplo. En tus carruseles usa fotos reales de tu
  negocio.

## Archivos

- `carrusel.json`: lo que escribe Claude.
- `fotos/consultorio.jpg`: la foto de la lámina 7.
- `laminas/01.png` a `09.png`: las láminas listas para subir (1080 × 1350).
- `laminas/revision.jpg`: todas juntas en chiquito.
- `laminas/caption.txt`: el texto de la publicación con sus hashtags.

Para volver a armarlo: `python3 scripts/carrusel.py ejemplos/consultorio-dental/carrusel.json`

Los mismos textos en los tres estilos base: `../estilos/los-tres-estilos.jpg` (se arman con `../estilos/estilos.json` y
`--estilo claro`, `--estilo oscuro` o `--estilo foto`).
