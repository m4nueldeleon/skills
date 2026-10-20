# Ejemplo real · Clínica Dental Ladera (negocio de ejemplo)

**Negocio de ejemplo.** Clínica Dental Ladera no existe: la clínica, sus datos y la «usuaria» son ficticios.
Todo lo demás es la salida real de la skill, hecha siguiendo `SKILL.md` paso por paso. Como el repositorio es
público, la portada dice «Negocio de ejemplo · datos ficticios»; en una presentación de verdad ahí va quién
presenta.

Archivos de este ejemplo:

| Archivo | Qué es |
|---|---|
| `muestrario.html` | Las tres portadas para elegir estilo (paso 2) |
| `laminas.html` | Las láminas que escribió Claude (paso 3) |
| `presentacion.html` | La presentación final: ábrela en el navegador y presiona F |
| `prueba/hoja.jpg` | Las 10 láminas en una sola imagen |
| `prueba/presentacion.pdf` | El PDF que sale con Ctrl/Cmd + P (una lámina por página) |
| `prueba/verificacion.json` | El reporte de la prueba en navegador |

---

## 1 · Lo que escribió la usuaria

> Usa la skill presentacion-cinematografica. Tengo una clínica dental. El jueves le presento a la gerente de
> Recursos Humanos de una empresa de 60 personas nuestro plan dental para empresas. Hablo unos 8 minutos. El plan
> incluye dos limpiezas al año con revisión, citas desde las 7 de la mañana y los sábados, y 20% de descuento en
> tratamientos para el empleado y su familia. Al final quiero que acepte una revisión gratis para sus directivos.

El mensaje ya trae de qué trata, quién la ve y qué quiere que hagan al final (A y B del paso 1). Por eso Claude
no pregunta nada y pasa directo al guion.

## 2 · El guion que propuso Claude (una sola vuelta)

> **Tu equipo sano, sin perder mañanas**
> Para: la gerente de Recursos Humanos de una empresa de 60 personas · Duración: ~8 min · 10 láminas · Al final:
> que acepte una revisión gratis para sus directivos
>
> 1. Gancho · portada: «Tu equipo sano, sin perder mañanas»
> 2. Gancho · frase: «¿Cuántas mañanas se fueron este año en ir al dentista?»
> 3. Problema · lista: «Hoy, una cita dental es:» Pedir permiso / Cruzar la ciudad / Esperar turno / Regresar a
>    media tarde
> 4. Problema · contraste: «Lo que se pospone, crece» Dolor, urgencias y varias citas / Una limpieza y una
>    revisión
> 5. Solución · pausa: «¿Y si la revisión se acomodara al horario de tu equipo?»
> 6. Solución · palabra: «Plan Empresa». Le puse ese nombre; cámbialo si ya tiene uno.
> 7. Solución · pasos: «Qué incluye» Dos limpiezas al año / Citas desde las 7 am y sábados / 20% menos en
>    tratamientos
> 8. Prueba · frase: «Ya lo tienen [N] empresas» + desde qué año atienden
> 9. Llamado · cifra: [precio] por empleado al año
> 10. Llamado · llamado: «Empieza sin costo: una revisión gratis para tus directivos» + elegimos la fecha hoy +
>     esta semana, desde las 7 am o el sábado
>
> **Estilo** (te dejo las tres portadas para que las veas):
> 1 · Cine: oscuro y dramático; luce en pantalla grande y proyector
> 2 · Estudio: claro y limpio; cómodo para juntas y videollamadas
> 3 · Bosque: cálido y cercano; para salud, comida y servicios personales
> Te recomiendo el 3 porque es un servicio de salud y se siente cercano; si vas a proyectar en una sala con poca
> luz, el 1 luce más. Si tienes colores de marca, pásamelos y uso los tuyos.
>
> **Me faltan estos datos** (si no los tienes, armo esas láminas sin números):
> - El precio por empleado al año (lámina 9).
> - Una prueba real: cuántas empresas ya tienen el plan o desde qué año atienden (lámina 8).
>
> ¿La armo así? Responde «sí» o dime qué cambio (por ejemplo: «quita la 4» o «estilo 2»).

Junto con ese mensaje, Claude creó el artifact `muestrario.html` con las tres portadas.

## 3 · La respuesta de la usuaria

> Sí. Estilo 1, porque lo voy a proyectar en su sala de juntas. Sí se llama Plan Empresa. Cobramos 1,450 pesos
> por empleado al año. Ya lo tienen 8 empresas de la zona y atendemos desde 2014. Mi logo te lo paso después.

## 4 · Construcción y revisión

Claude escribió las láminas (`laminas.html`) y armó la presentación con el motor sin cambios:

```bash
python3 scripts/armar.py ejemplos/clinica-dental/laminas.html --titulo "Plan Empresa · Clínica Dental Ladera" \
  --look cine --salida ejemplos/clinica-dental/presentacion.html
```

`revisar.py`, en la primera pasada, marcó dos avisos: 37 palabras en la lámina de pasos y 27 en el llamado.
Claude recortó las dos (31 y 23 palabras) y la segunda pasada salió así:

```text
Revisión · presentacion.html · 10 láminas · look cine

Historia: gancho (1-2) → problema (3-4) → solución (5-7) → prueba (8) → llamado (9-10)
Palabras por lámina: 1:23, 2:21, 3:16, 4:25, 5:11, 6:10, 7:31, 8:12, 9:13, 10:23
Revelados (clics extra): 15

Cifras en pantalla. Confirma que cada una salió del usuario o de una fuente real:
  7 (lámina 7) · 20% (lámina 7) · 8 (lámina 8) · 2014 (lámina 8) · 1,450 (lámina 9) · 121 (lámina 9) · 7 (lámina 10)

Lista para entregar.
```

Todas las cifras salieron de la usuaria. La única cuenta es 1,450 ÷ 12 = 120.83, que se redondea a «unos 121
pesos al mes».

La prueba en navegador (`probar-en-navegador.mjs --capturas --pdf --webkit`):

```text
  ✔ Medición: 10 láminas; letra mínima 32 px en lienzo de 1920.
  ✔ Navegación: 24 clics recorren las 10 láminas y sus 15 revelados, en orden.
  ✔ Vista general (G): muestra todas las láminas.
  ✔ Edición (E): 37 textos editables; «Guardar copia» genera un archivo que abre bien.
  ✔ Teléfono (390×844): la lámina cabe completa (390×219 px; se ve mejor con el teléfono acostado).
  ✔ Capturas: 10 imágenes en prueba/capturas y la hoja de contacto prueba/hoja.jpg.
  ✔ PDF: 10 páginas, una por lámina (0.3 MB).
  ✔ WebKit (Safari): abre y navega (quedó en la lámina 3).

Sin errores.
```

## 5 · Lo que Claude entregó

> Aquí está tu presentación: 10 láminas, unos 8 minutos, estilo Cine.
>
> **Cómo presentarla:** descárgala con el botón de descarga, ábrela con Chrome, Edge o Safari, presiona **F**
> para pantalla completa y avanza con la flecha → o con un clic. **P** abre tus notas y un reloj en otra ventana.
>
> **Para el PDF:** en Chrome o Edge, Cmd + P (Ctrl + P en Windows) → «Guardar como PDF» → márgenes «Ninguno».
>
> **Falta tu logo:** abre el archivo, presiona **E**, arrastra el logo al recuadro amarillo de la portada y al del
> cierre, y elige «Guardar copia». Mientras no lo pongas, esas láminas se ven completas, sin hueco.
>
> Supuse que la revisión gratis es para todos sus directivos, sin número fijo. Si quieres poner cuántos, dime.
