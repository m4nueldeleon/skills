# Ejemplo 5 · Claude Code: la tarea del lunes, sin nadie enfrente

> **Negocio de ejemplo (ficticio):** Boutique Alma, la misma de los ejemplos anteriores.
>
> **Cómo se produjo:** Claude Code con la skill instalada como plugin local y solo permiso para leer y escribir
> archivos en la carpeta. Es la misma orden que corre la tarea programada de la GUIA; para la prueba se le dijo la
> fecha («hoy es lunes 2 de noviembre de 2026»), porque la corrida se hizo antes. Los archivos de abajo son los que
> Claude escribió, copiados tal cual.

## La carpeta antes de correr

- `banco-de-ideas.md`: el banco que dejó el ejemplo 3 (la semana del 26 de octubre ya planeada).
- `resultados.md`: lo que la dueña anotó durante la semana.

## La orden (la misma de la tarea programada)

```text
/contenido-en-piloto-automatico CALENDARIO. Es la tarea programada del lunes (hoy es lunes 2 de noviembre de 2026): usa banco-de-ideas.md de esta carpeta y guarda todo. No hay nadie para contestar preguntas.
```

## Lo que respondió Claude al terminar

Dejé armado el calendario de la semana del lunes 2 al domingo 8 de noviembre y actualicé el banco.

**Resultados de la semana pasada**
- **Ganadora:** el pantalón del martes (#02). Tuvo 4,200 vistas, 31 compartidos, 60 comentarios y 22 seguidoras nuevas.
- **Los demás:** el vestido del lunes (#01) tuvo 1,850 vistas y 3 seguidoras nuevas. Los apartados del sábado (#09) trajeron 6 mensajes y 2 apartados.
- **Sin publicar:** lo del jueves (#04) no salió y volvió a «nueva».
- Con una sola semana hay pocos datos. La tendencia se ve en 3 o 4 semanas.

**Calendario**

| Día | Objetivo | Formato | Idea |
|---|---|---|---|
| Lunes 2 | Atraer | Reel mostrando | #10, «3 señales de que sí es su talla», Parte 2 del pantalón ganador (idea nueva, secuela de #02) |
| Martes 3 | Atraer | Carrusel | #07, 4 looks para una boda de día, con prendas y fotos propias de la tienda |
| Jueves 5 | Nutrir | Reel mostrando | #08, cómo medirse con una cinta |
| Sábado 7 | Vender | Reel mostrando | #06, vestidos de otoño, verde olivo |

El ajuste para esta semana: 3 de las 4 piezas son reels mostrando, porque el pantalón fue el que más se compartió.

**Pendientes (también están al inicio del archivo)**
- **Datos que faltan:** el precio, las tallas disponibles y la tela de los vestidos (#06).
- **Buen Fin:** no pude verificar la fecha de 2026 porque no tengo búsqueda web. Si cae pronto, hay que sumarla o cambiar la pieza del sábado.
- **Día de Muertos:** no lo usé, porque no encaja con una pieza de ropa.
- **Por confirmar en la ficha:** los días de publicación y las palabras que usted usa en el tono.
- **Verificar antes de publicar:** la frase «el que se va primero» del #06 debe ser cierta.
- **Tema repetido:** Tallas sale dos veces (#10 y #08). Si prefiere variar, #04 (Detrás del mostrador, en Historias) puede sustituir a #08.
- **Sin usar:** #03 y #05 siguen en el banco como `nueva`.

**Archivos**
- `calendarios/semana-2026-11-02.md`: el calendario completo, con guiones, captions y la lista de grabación en una sola sentada.
- `banco-de-ideas.md`: resultados anotados, estados al día, idea #10 creada y la semana agregada en `--- SEMANAS ---`.
- `resultados.md`: agregué la línea `--- procesado 2026-11-02 ---`.

El próximo lunes escribe RESULTADOS (cómo te fue) y luego CALENDARIO.

## `resultados.md` después de correr

Claude solo agregó la última línea, para no contar lo mismo dos veces:

```text
# Cómo me fue

Semana del 26 de octubre:
- Vestido del lunes: 1,850 vistas, 9 compartidos, 3 seguidoras nuevas.
- Pantalón del martes: 4,200 vistas, 31 compartidos, 60 comentarios, 22 seguidoras nuevas.
- Lo del jueves no lo publiqué.
- Apartados del sábado: 980 vistas, 6 me escribieron APARTAR y 2 apartaron.

--- procesado 2026-11-02 ---
```

## Lo que cambió en `banco-de-ideas.md`

Ninguna idea se borró: cambiaron estados y resultados, entró la idea #10 y se anotó la semana.

```diff
--- banco-de-ideas.md (antes)
+++ banco-de-ideas.md (después)
@@ -8 +8 @@
-ACTUALIZADO: 2026-10-20
+ACTUALIZADO: 2026-11-02
@@ -12 +12 @@
-    ATRAER · Reel hablado a cámara · Tema: Looks de otoño · Fuerza 4/5 (real · fácil · oferta · propia) · en calendario sem. 26-oct
+    ATRAER · Reel hablado a cámara · Tema: Looks de otoño · Fuerza 4/5 (real · fácil · oferta · propia) · publicada 26-oct
@@ -15 +15 @@
-    Resultado:
+    Resultado: 1,850 vistas · 9 compartidos · 3 seguidoras nuevas
@@ -18 +18 @@
-    ATRAER · Reel mostrando · Tema: Tallas y cómo le queda · Fuerza 3/5 (real · fácil · propia) · en calendario sem. 26-oct
+    ATRAER · Reel mostrando · Tema: Tallas y cómo le queda · Fuerza 3/5 (real · fácil · propia) · publicada 27-oct
@@ -21 +21 @@
-    Resultado:
+    Resultado: 4,200 vistas · 31 compartidos · 60 comentarios · 22 seguidoras nuevas (la mejor de la semana)
@@ -30 +30 @@
-    NUTRIR · Historias · Tema: Detrás del mostrador · Fuerza 3/5 (real · fácil · propia) · en calendario sem. 26-oct
+    NUTRIR · Historias · Tema: Detrás del mostrador · Fuerza 3/5 (real · fácil · propia) · nueva
@@ -42 +42 @@
-    VENDER · Reel mostrando · Tema: Looks de otoño · Fuerza 3/5 (fácil · oferta · propia) · nueva
+    VENDER · Reel mostrando · Tema: Looks de otoño · Fuerza 3/5 (fácil · oferta · propia) · en calendario sem. 02-nov
@@ -48 +48 @@
-    ATRAER · Carrusel · Tema: Looks de otoño · Fuerza 2/5 (fácil · oferta) · nueva
+    ATRAER · Carrusel · Tema: Looks de otoño · Fuerza 2/5 (fácil · oferta) · en calendario sem. 02-nov
@@ -54 +54 @@
-    NUTRIR · Reel mostrando · Tema: Tallas y cómo le queda · Fuerza 4/5 (real · fácil · oferta · propia) · nueva
+    NUTRIR · Reel mostrando · Tema: Tallas y cómo le queda · Fuerza 4/5 (real · fácil · oferta · propia) · en calendario sem. 02-nov
@@ -60 +60 @@
-    VENDER · Historias · Tema: Apartados y Navidad · Fuerza 4/5 (real · fácil · oferta · propia) · en calendario sem. 26-oct
+    VENDER · Historias · Tema: Apartados y Navidad · Fuerza 4/5 (real · fácil · oferta · propia) · publicada 31-oct
@@ -62,0 +63,6 @@
+    Resultado: 980 vistas · 6 escribieron APARTAR · 2 apartaron
+
+#10 · 3 señales de que sí es su talla (Parte 2 del pantalón)
+    ATRAER · Reel mostrando · Tema: Tallas y cómo le queda · Fuerza 4/5 (real · fácil · propia · secuela) · en calendario sem. 02-nov
+    Origen: secuela de #02
+    Cómo lo adapto: tres señales para saber si un pantalón le queda justo sin bajar de talla; mismo tema que el pantalón que más se compartió.
@@ -66 +72,2 @@
-Sem. 26-oct: #01 lun · #02 mar · #04 jue · #09 sáb
+Sem. 26-oct: #01 lun · #02 mar · #04 jue (no publicada) · #09 sáb
+Sem. 02-nov: #10 lun · #07 mar · #08 jue · #06 sáb
```

## `calendarios/semana-2026-11-02.md` (el archivo que dejó)

# Calendario · Semana del lunes 2 al domingo 8 de noviembre de 2026
Boutique Alma · Instagram y Facebook · 4 piezas · lunes, martes, jueves, sábado

## Pendientes
- **Resultados procesados** de la semana del 26-oct (ya anotados en el banco). Lo del jueves (#04) no se publicó y volvió a «nueva».
- **Ganadora de la semana pasada:** el pantalón del martes (#02): 4,200 vistas, 31 compartidos, 60 comentarios y 22 seguidoras nuevas, la mejor de las 3 publicadas. Por eso hoy abre la semana su Parte 2 (#10).
- **Pocos datos:** una semana dice poco; la tendencia se ve en 3 o 4 semanas. Ajuste para esta semana: los reels mostrando prendas y cómo les queda (el pantalón) fueron lo que más compartieron; hagamos 3 de las 4 piezas así.
- **Fechas especiales:** 1 y 2 de noviembre (Día de Muertos) ya pasaron o son hoy y no encajan con una pieza de ropa; no las usé. **El Buen Fin 2026 no pude verificarlo** (no tengo búsqueda web): confirme la fecha. Si cae en los próximos 7 días o poco después, avíseme y se agrega una pieza o se cambia la del sábado.
- **Faltan datos:** [precio] y [tallas disponibles] de los vestidos (#06). Confirmar días de publicación (siguen «por confirmar») y palabras que usted sí usa en el TONO.
- Permiso: no se muestra a ninguna clienta sin su permiso.

---

LUNES 2 · ATRAER · Reel mostrando · idea #10 (Parte 2 del pantalón)
Idea: tres señales de que un pantalón le queda justo y no necesita bajar de talla (Parte 2 del reel del pantalón que más se compartió).
Gancho (primera frase, dicha y escrita en pantalla): «Si su pantalón le marca así, no es que usted esté mal: es la talla.»
Guion (unos 40 segundos):
  [0–3 s]   Se dice: «Si su pantalón le marca así, no es que usted esté mal: es la talla.»   Se ve: pantalón apretado en la cadera, en primer plano, con una mano señalando la marca.
  [3–15 s]  Se dice: mucha gente compra una talla menos pensando que así se ve mejor, y termina incómoda todo el día.   Se ve: el mismo pantalón al sentarse, la tela jalando.
  [15–35 s] Se dice: tres señales de que sí es su talla: se acuesta sin jalar en la cadera, puede sentarse sin que apriete la cintura y no se marcan líneas en la tela.   Se ve: un pantalón de su talla, mostrando cada señal con la mano; una por una.
  [35–42 s] Se dice: «Si conoce a alguien que siempre compra una talla menos, mándele este video.»   Se ve: la persona frente a la cámara, junto al perchero de pantalones.
Texto en pantalla: «¿Talla menos?» · «3 señales de que sí es su talla» · «Sin jalar · sin apretar · sin marcas»
Caption:
  Comprar una talla menos no la hace verse mejor, solo la hace sentirse incómoda.
  Esta es la Parte 2 del video del pantalón.
  Tres señales rápidas para saber si le queda bien.
  En la tienda le ayudamos a encontrar su talla sin prisa.
  Mándeselo a alguien que siempre compra una talla menos.
  #BoutiqueAlma #ModaGuadalajara #ModaParaSeñoras
Llamada a la acción: mándeselo a alguien que siempre compra una talla menos.
Antes de publicar: usar un pantalón y una prenda real de la tienda; confirmar que las tres señales coincidan con cómo usted explica el ajuste; revisar el nombre del hashtag.

---

MARTES 3 · ATRAER · Carrusel · idea #07 (inspirada en otro creador: solo la pregunta)
Idea: 4 looks de la tienda para una boda de día, sin hablar de edad. Solo se tomó la pregunta; textos y fotos son propios.
Gancho: lámina 1 «¿Qué me pongo para una boda de día?»
Láminas:
  1. «¿Qué me pongo para una boda de día?» (foto del mejor look, texto grande)
  2. Look 1: [prenda de la tienda] + [accesorio]. Una línea de por qué funciona de día.
  3. Look 2: [prenda de la tienda] + [accesorio]. Una línea.
  4. Look 3: [prenda de la tienda] + [accesorio]. Una línea.
  5. Look 4: [prenda de la tienda] + [accesorio]. Una línea.
  6. «Tip: de día, telas ligeras y colores que se vean bien con luz natural.»
  7. «¿Cuál se pondría usted? Respóndame con el número del look.»
Texto en pantalla: el número y nombre de cada look; una frase corta por lámina.
Caption:
  ¿Tiene boda de día y no sabe qué ponerse?
  Armamos 4 looks con prendas de la tienda.
  Hay para distintos gustos y tallas, de la chica a la extra.
  Cuéntenos cuál le gustó más.
  Respóndame con el número del look que usted elegiría.
  #BoutiqueAlma #ModaGuadalajara #LooksDeOtoño
Llamada a la acción: responder con el número del look (una palabra o un número).
Antes de publicar: elegir las 4 prendas y tomar fotos propias (no usar nada de @boutique.ejemplo40); confirmar que están disponibles en tienda; no escribir edades.

---

JUEVES 5 · NUTRIR · Reel mostrando · idea #08
Idea: cómo medirse en casa con una cinta, para pedir su talla por WhatsApp.
Gancho (primera frase, dicha y escrita en pantalla): «¿Me pide una prenda por WhatsApp y no sabe su medida? Con una cinta se resuelve.»
Guion (unos 45 segundos):
  [0–3 s]   Se dice: «¿Quiere pedirnos una prenda por WhatsApp y no sabe su talla? Con una cinta se resuelve.»   Se ve: cinta métrica en la mano, sobre una mesa.
  [3–15 s]  Se dice: busto: se mide en la parte más ancha, con la cinta recta y sin apretar.   Se ve: la cinta alrededor del busto sobre la ropa ligera (sin mostrar nada íntimo).
  [15–30 s] Se dice: cintura: la parte más angosta. Cadera: la parte más ancha. Anótelas.   Se ve: la cinta en cintura y en cadera; cada medida aparece en pantalla.
  [30–45 s] Se dice: «Mándeme sus tres medidas por WhatsApp y le sugiero talla. Cada marca queda un poco distinto, por eso le ayudamos.»   Se ve: la persona con la cinta y el celular en pantalla.
Texto en pantalla: «Busto · Cintura · Cadera» · «Cinta recta, sin apretar» · «Mándeme sus medidas»
Caption:
  Pedir por WhatsApp es más fácil si sabe sus medidas.
  Se miden en 1 minuto con una cinta.
  Busto, cintura y cadera.
  Guárdelo para cuando las necesite.
  Mándeme sus medidas por WhatsApp y le sugiero talla.
  #BoutiqueAlma #TallasReales #ModaGuadalajara
Llamada a la acción: guárdelo para cuando las necesite (y, si quiere, mandar medidas por WhatsApp; el cierre dicho coincide con el caption).
Antes de publicar: confirmar que usted sí sugiere talla por WhatsApp y con qué tiempo contesta; [número de WhatsApp] a la vista si lo quiere poner.

---

SÁBADO 7 · VENDER · Reel mostrando · idea #06
Idea: llegaron los vestidos de otoño; el verde olivo es el que más pregunta la gente.
Gancho (primera frase, dicha y escrita en pantalla): «Llegaron los vestidos de otoño, y este verde olivo es el que se va primero.»
Guion (unos 35 segundos):
  [0–3 s]   Se dice: «Llegaron los vestidos de otoño. Este verde olivo es el que más se pide.»   Se ve: el vestido verde olivo en movimiento (moviéndose al caminar o girar).
  [3–15 s]  Se dice: la tela es [tela], cae suave y se siente cómoda para el día.   Se ve: detalle de la tela y la caída, al sol o con luz natural.
  [15–28 s] Se dice: hay en tallas de la chica a la extra [confirmar tallas disponibles]; cuesta [precio].   Se ve: el vestido en perchero junto a otros de la colección.
  [28–38 s] Se dice: «Escríbame VESTIDO por WhatsApp y le paso opciones, tallas y precios.»   Se ve: la persona con el vestido y el texto de WhatsApp en pantalla.
Texto en pantalla: «Vestidos de otoño» · «Verde olivo» · «Escríbame VESTIDO por WhatsApp»
Caption:
  Llegaron los vestidos de otoño.
  El verde olivo es el que más se pide.
  Hay tallas de la chica a la extra [confirmar].
  Escríbame VESTIDO por WhatsApp y le paso opciones, tallas y precios.
  #BoutiqueAlma #VestidosDeOtoño #ModaGuadalajara
Llamada a la acción: escríbame VESTIDO por WhatsApp.
Antes de publicar: llenar [tela], [precio] y [tallas disponibles]; confirmar que «el que se va primero / el que más se pide» sea cierto hoy; ¿quiere sumar el apartado de Navidad (ya publicado el sábado pasado)? Aquí no se agregó para dejar una sola llamada a la acción.

---

## Lista de grabación (una sola sentada, 40 a 60 minutos)
Preparar antes:
- Un espacio con luz natural cerca de la entrada o una ventana; perchero con pantalones, vestidos y suéteres.
- Ropa de la persona que graba: sencilla, de un color liso que no pelee con las prendas.
- Cinta métrica, el vestido verde olivo, un pantalón apretado y uno bien ajustado (de las tallas que usted tenga), 4 looks completos para el carrusel con accesorios.
- Celular con la lente limpia y el modo avión para evitar interrupciones.
Orden:
1. Reel del vestido verde olivo (#06), con luz limpia y el vestido recién planchado.
2. Reel de la cinta (#08).
3. Reel de las señales del pantalón (#10).
4. Fotos de los 4 looks para el carrusel (#07), con la misma luz.
Después: editar y dejar los textos en pantalla listos; los reels pueden salir el día que toque.

El próximo lunes escribe RESULTADOS (cómo te fue) y luego CALENDARIO.

## Qué revisamos

- Hizo primero RESULTADOS con `resultados.md`, marcó el archivo como procesado y no borró nada.
- Creó la Parte 2 de la pieza ganadora y la puso el lunes. Lo que no se publicó volvió a `nueva`.
- Guardó el calendario en `calendarios/` con la sección «Pendientes» arriba (Buen Fin sin verificar, precios y
  tallas que faltan) en lugar de hacer preguntas.
- Detalles a mejorar del modelo, no de la skill: la última línea de su respuesta habla de «tú» aunque la ficha dice
  «usted», y una frase del guion del lunes dice «se acuesta sin jalar» donde debería decir «se asienta sin jalar».
  Por eso la GUIA pide revisar cada guion antes de grabar.
