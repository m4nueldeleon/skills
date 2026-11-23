# Tu carrusel del día, sin copiar

Manuel de León · Recursos de IA para negocios · 23 de noviembre de 2026

Una skill para que subas un carrusel al día a Instagram y Facebook. Buscas carruseles que ya funcionan en tu giro,
Claude toma su receta (el orden, el ritmo y el estilo) y le pone tu sazón: tu voz, tu cliente, tus colores y tus
fotos. Te entrega las imágenes listas para subir y el texto de la publicación.

**Roba la receta, ponle tu sazón.** Nunca copia el texto ni las fotos de nadie.

## Seis palabras que vas a leer

- **Carrusel:** una publicación con varias imágenes que se pasan con el dedo. Cada imagen es una **lámina**.
- **Portada:** la primera lámina. Su frase grande es el **gancho**: lo que hace que la gente se detenga.
- **Skill:** un paquete de instrucciones que le enseña a Claude a hacer una tarea siempre igual.
- **ZIP:** un archivo comprimido que guarda una carpeta adentro. Así se descarga la skill. **No lo abras.**
- **Cowork:** el modo de Claude que trabaja en una carpeta de tu computadora y te deja ahí los archivos.
- **Ficha de marca (`MI-MARCA.md`):** un archivo con lo básico de tu negocio. Claude lo lee antes de escribir.

## Qué necesitas

- Una cuenta de Claude con **plan de pago (Pro o superior)** para usar Cowork.
- La **app de escritorio de Claude** en tu computadora (Mac o Windows), abierta y con internet. Se baja en
  https://claude.com/download
- Instagram en tu celular. Para publicar también en Facebook, tu Instagram y tu página de Facebook conectados.
- Opcional: tu logo y de 3 a 10 fotos reales de tu negocio.

¿Plan gratis? Puede funcionar en el chat normal de claude.ai (sin Cowork); si no te aparece la sección de skills,
necesitas un plan de pago.

## Instálala (una sola vez, 5 minutos)

1. **Descarga la skill:**
   https://github.com/m4nueldeleon/skills/releases/download/descargas/replica-carruseles.zip
   No le des doble clic ni la descomprimas.
   - **En Mac con Safari:** a veces el ZIP se abre solo y en Descargas te aparece una carpeta. Si pasa, dale clic
     derecho a la carpeta → **«Comprimir»** y usa el `.zip` que se crea.
   - **En Windows:** si se descomprimió, clic derecho a la carpeta → **Enviar a → Carpeta comprimida (en zip)**.
2. **Revisa que Claude pueda crear archivos.** En Claude entra a **Configuración → Capacidades** y deja prendida
   **«Ejecución de código y creación de archivos»**. Casi siempre ya viene prendida.
3. **Sube la skill.** En la barra de la izquierda entra a **Personalizar → Skills**, toca **«+»** y elige
   **«Subir Skill»**. Arrastra el ZIP a la ventana (o búscalo en tu computadora).
4. **Revisa que quede activada:** el interruptor a la derecha de «replica-carruseles» debe estar prendido.

Si en tu pantalla algo se llama un poco distinto («Personalización», «Subir una Skill»), es lo mismo: la app cambia
sus nombres de vez en cuando.

## Prepara tu carpeta (una sola vez)

En tu computadora crea una carpeta llamada **Carruseles** (por ejemplo, en tu Escritorio). Mete ahí:

- `MI-MARCA.md`, si ya la tienes (por ejemplo, la que armaste en la clase). Si no, Claude te la hace.
- Tu logo con el nombre `logo.png`.
- Tus fotos reales del negocio.
- Las capturas de los carruseles que te gustaron: `referencia-1.png`, `referencia-2.png`…

Es mejor darle a Claude una carpeta solo para esto que darle acceso a toda tu computadora.

## Úsala en Cowork

1. Abre la app de Claude. **Si ves el botón «Cowork», dale clic. Si no lo ves, ya tienes la versión nueva:** pídelo
   directo en el chat.
2. En la caja del mensaje toca **«Trabajar en una carpeta»** y elige tu carpeta **Carruseles**.
3. Escribe lo que quieres (abajo tienes ejemplos). También puedes escribir **`/`** y escoger la skill de la lista.
4. Si Claude te pide permiso para algo, revisa qué es y toca **«Permitir»**.
5. Al terminar, tus láminas quedan en la carpeta (`carruseles/fecha-tema/laminas/01.png`, `02.png`…) y también las
   ves junto a la conversación para revisarlas.

La primera vez, si no tienes `MI-MARCA.md`, Claude te hace siete preguntas en un solo mensaje. Contesta como te salga;
lo que no sepas, sáltalo.

## Úsala en el chat de claude.ai (sin Cowork)

1. Abre un **chat normal** (en el modo incógnito Claude no crea archivos).
2. Adjunta tu `MI-MARCA.md`, tus fotos y las capturas del carrusel que te gustó.
3. Pide tu carrusel. Las láminas te salen en la conversación para descargarlas una por una.

Consejo: si usas mucho el chat, crea un **Proyecto** en Claude y sube ahí tu `MI-MARCA.md` y tu logo para no
adjuntarlos cada vez.

## Qué pedirle (copia y cambia lo de los corchetes)

```text
Hazme mi ficha de marca.
```

```text
Mi carrusel del día. En la carpeta están las capturas de un carrusel que me gustó
(referencia-1 a referencia-4). Hazme el mío para [mi negocio], sobre [tema].
```

```text
Investiga carruseles de mi giro: soy [dentista en Guadalajara]. Guíame para encontrar
10 que funcionen y hazme el calendario de 7 días.
```

```text
Hazlo en estilo oscuro · Usa la portada número 2 · La lámina 4 tiene mucho texto, recórtala
```

```text
Así me fue con el carrusel del martes a los 7 días: [guardados], [compartidos],
[comentarios], [cuentas alcanzadas que no me seguían]. ¿Qué repito en el siguiente?
```

## Qué te entrega

- Las láminas en imagen: `01.png`, `02.png`… de 1080 × 1350 (el tamaño vertical de Instagram).
- `revision.jpg`: todas juntas en chiquito, para ver si la portada se entiende de un vistazo.
- El texto de la publicación con 3 a 5 hashtags (`caption.txt`), listo para copiar.
- Dos portadas de repuesto por si quieres cambiar el gancho.

Antes de entregarte, Claude revisa: que el gancho se entienda en 2 segundos, que se vea como tu marca y no como la
referencia, una idea por lámina, letra que se lea en el celular, y que no haya cifras, testimonios ni promesas que no
puedas respaldar.

## Publícalo en Instagram y Facebook a la vez

1. **Pasa las láminas a tu celular.** En Mac con iPhone, por AirDrop. También puedes subirlas a tu Google Drive o
   iCloud y guardarlas desde ahí en tus fotos.
2. En la app de Instagram toca **«+»** y elige la opción para hacer una publicación (el nombre cambia según tu
   versión de la app; es la de foto, no la de historia ni la de video).
3. Toca el ícono para escoger varias fotos (suele verse como cuadritos encimados) y elige las láminas **en
   orden**: 01, 02, 03… Instagram acepta hasta 20.
4. Pega el texto de la publicación.
5. Antes de compartir, busca **«Compartir también en…»** y prende tu página de Facebook. Esto solo está en la app
   del celular. Si no te aparece (o no aparece para carruseles en tu versión), primero conecta tu Instagram con tu
   Facebook en el Centro de cuentas; si aun así no sale, sube las mismas láminas en Facebook como publicación de
   varias fotos.
6. Comparte.

## Mide para que el siguiente salga mejor

Con una cuenta profesional, en tu publicación toca **«Ver estadísticas»** a las 48 horas y a los 7 días. Fíjate en:

- **Guardados:** la gente lo quiere para después. Es la mejor señal de un carrusel útil.
- **Compartidos:** se lo mandaron a alguien.
- **Comentarios** que hablan del tema.
- **Cuentas alcanzadas que no te seguían:** gente nueva que te conoció.

Cuéntaselo a Claude. El siguiente carrusel repite lo que funcionó y cambia una sola cosa. Un carrusel solo no dice
mucho: compara al menos cinco.

## Cómo encontrar carruseles que funcionan (15 minutos)

1. En Instagram toca **«Buscar»** (la lupa) y escribe lo que buscaría tu cliente: «cómo quitar el sarro», «pastel para
   baby shower».
2. Toca **«Sin personalizar»** para ver lo que funciona en tu giro y no solo lo que te gusta a ti.
3. Los carruseles tienen en la esquina el ícono de cuadritos encimados.
4. **La regla del 3×:** entra al perfil, mira sus últimas 9 a 12 publicaciones y fíjate en los Me gusta de la de en
   medio. Si el carrusel tiene 3 veces eso o más, pegó. Ese se estudia.
5. Toma captura de la portada, 2 o 3 láminas de adentro y los Me gusta. Junta 10 de cuentas distintas y dáselas a
   Claude.

## Las reglas de la casa

- **Se toma la receta:** el orden de las láminas, el ritmo, la forma del gancho y el estilo.
- **Nunca se toma:** su texto, sus fotos, su logo, sus clientes ni sus cifras.
- **Dar crédito es opcional** («Inspirado en @cuenta» en el texto), pero no te salva de copiar: Instagram dejó de
  recomendar las cuentas que vuelven a subir trabajo ajeno, aunque pongan el crédito.
- **Nada inventado:** ni testimonios, ni clientes, ni cifras, ni promesas de resultados.
- Nadie puede prometerte que un carrusel se haga viral. Lo que sí funciona es publicar seguido, medir y repetir lo que
  le sirve a tu cliente.

## Si algo falla

| Pasa | Qué hacer |
|---|---|
| No aparece «Skills» o se ve gris | Prende «Ejecución de código y creación de archivos» (paso 2) |
| Error al subir el ZIP | Bájalo de nuevo y súbelo sin abrirlo. Si se volvió carpeta, comprímela (paso 1) |
| Claude no usa la skill | Revisa que esté activada; escribe `/` y escógela, o dile «usa la skill replica-carruseles» |
| No encuentra tus archivos | La app de escritorio tiene que estar abierta y la carpeta conectada |
| No puede abrir la liga de Instagram | Mándale capturas: Instagram pide iniciar sesión |
| Te dio un archivo `.html` en vez de imágenes | No pudo dibujar las imágenes esta vez: pídeselo otra vez en una conversación nueva |
| Una lámina tiene mucho texto | Dile «recorta la lámina 4» |

## Instálala en Claude Code (opcional)

Si usas Claude Code, escribe dentro de él:

```text
/plugin marketplace add m4nueldeleon/skills
/plugin install replica-carruseles@manuel-de-leon
```

El código de esta skill es público: https://github.com/m4nueldeleon/skills

## Créditos

- Idea de «robar como un artista»: Austin Kleon, *Roba como un artista* (2012).
- Tipografías Archivo, Inter, Montserrat y Oswald, con licencia SIL Open Font License (incluidas en `fuentes/`).
- La foto del consultorio del ejemplo está hecha con IA, solo para el ejemplo. En tus carruseles usa fotos reales de tu
  negocio.
