# Roba como un artista: de una referencia a un carrusel propio

Lo lee Claude antes de escribir cuando la persona trae un carrusel de referencia. La idea de toda la skill cabe en una
frase: **roba la receta, ponle tu sazón**.

## De dónde sale la idea

Austin Kleon, *Steal Like an Artist* (Workman, 2012). En español: *Roba como un artista* (Aguilar). Kleon publicó en
su blog una tabla de «buen robo contra mal robo» (https://austinkleon.com/2018/01/11/good-theft-vs-bad-theft/). Son
seis pares, en este orden (la traducción es nuestra, no la de la edición en español):

| Buen robo | Mal robo |
|---|---|
| Honrar | Degradar |
| Estudiar | Hojear |
| Robar de muchos | Robar de uno |
| Dar crédito | Plagiar |
| Transformar | Imitar |
| Remezclar | Fusilar |

Dos ideas suyas que sirven como prueba (traducción libre):

- «Imitar no es halagar; transformar sí.»
- «Si se siente barato o chueco, probablemente lo es.» Kleon propone imaginar que te quedas atorado en un elevador con
  la persona a la que le tomaste la idea: ¿te daría la mano o te reclamaría?

No cites páginas ni frases «del libro en español»: solo lo de arriba, con su fuente.

## Lo que dice Instagram

Desde abril de 2026, Instagram dejó de recomendar las cuentas que principalmente vuelven a subir trabajo ajeno en
fotos y carruseles. Volver a subir algo con un borde, una marca de agua o el crédito **no cuenta como original**. Lo que
sí cuenta es agregar texto, contexto o información nueva que no estaba en lo original
(https://creators.instagram.com/blog/rewarding-original-creators-on-instagram?locale=es_LA).

Por eso esta skill nunca copia: se queda con la receta y escribe todo lo demás con la voz, el cliente y las fotos de la
persona.

## La ficha de la referencia

Llénala con lo que se ve en las capturas. Lo que no se ve, se deja en blanco: no se estima.

```markdown
## Referencia
- Cuenta: @___ · fecha si se ve: ___
- Números visibles: Me gusta ___ · comentarios ___ · veces compartido ___ (si aparece)
- Lo normal de esa cuenta (Me gusta de la publicación de en medio de las últimas 9 a 12): ___ → múltiplo: ___×
- Gancho: fórmula ___ (número, error, pregunta, contraste, mito, advertencia…). No se copia la frase.
- Promesa: al terminar, sabes o tienes ___
- Estructura: portada → ___ → ___ → resumen → cierre (N láminas = __)
- Por qué se guarda o se comparte: ___
- Llamado a la acción: qué pide ___
- Estilo visual: fondo ___ · letra ___ (gruesa / condensada / mayúsculas) · alineación ___ · acento ___
  · fotos ___ (a sangre, arriba, en círculo, sin fotos) · texto por lámina ___ (poco / medio / mucho)

## Mi versión
- Tema para mi cliente: ___
- Lo mío que la referencia no tiene: ___ (mi foto real, mi caso con permiso, mi zona, mi cliente, mi precio)
- Gancho propio (misma fórmula, otras palabras): ___
- Lo que NO tomo: ___
```

## Qué se toma y qué no

| Se toma | No se toma nunca |
|---|---|
| Estructura y orden de las láminas | El texto, ni traducido ni parafraseado línea por línea |
| Ritmo: número de láminas y cantidad de texto | Fotos, ilustraciones, capturas y logo |
| Fórmula del gancho | La frase del gancho |
| Estilo visual (retícula, tipo de letra, tratamiento de foto) | Personas, clientes, casos y testimonios |
| Tipo de llamado a la acción | Cifras y datos sin su fuente original |
| La forma de explicar (comparación, lista, antes y después) | Su nombre o su @ dentro de las láminas |

**Prueba lado a lado:** las dos versiones comparten estructura y estilo, y no comparten ninguna frase de más de tres
palabras ni ninguna imagen. Si al escribir una lámina tienes que volver a mirar el original, estás copiando texto:
cierra la referencia y escribe desde la ficha.

**Robar de muchos:** cuando haya dos o tres referencias, toma la estructura de una, el gancho de otra y el estilo de
una tercera. Así el resultado ya no se parece a ninguna.

**Crédito:** opcional y a decisión de la persona. Va en el texto de la publicación como «Inspirado en @cuenta»
(campo `credito` del `carrusel.json`). Nunca dentro de las láminas.

## Del estilo de la referencia al `carrusel.json`

Los colores siempre son los de la marca. Del estilo de la referencia se toma lo demás:

| Si la referencia tiene… | En `carrusel.json` |
|---|---|
| Fondo blanco o claro, mucho aire | `"estilo": "claro"` |
| Fondo negro o muy oscuro | `"estilo": "oscuro"` |
| Foto grande con el texto en una banda de color | `"estilo": "foto"` y `"foto"` en las láminas |
| Titulares en mayúsculas | `"diseno": {"mayusculas": true}` |
| Letra condensada, alta y angosta | `"fuentes": {"titulo": "oswald"}` |
| Letra redonda y amigable | `"fuentes": {"titulo": "montserrat", "texto": "montserrat"}` |
| Letra gruesa y seria | `"fuentes": {"titulo": "archivo"}` o `"inter"` |
| Texto centrado | `"diseno": {"alineacion": "centro"}` |
| Palabra clave con una caja de color detrás | `"diseno": {"acento_modo": "resaltado"}` |
| Palabra clave en otro color | `"diseno": {"acento_modo": "color"}` |
| Titulares enormes | `"diseno": {"tamano_titulo": "grande"}` |
| Puntos numerados grandes («01», «02») | `"numero": "01"` en cada lámina de la serie |
| Fondo de un color especial | `"diseno": {"fondo": "#F4EFE6"}` (que contraste con la letra) |
| La marca tiene su propia tipografía | `"fuentes": {"titulo": "fuentes/MiLetra.ttf"}` (archivo en su carpeta) |

Lo que el script no hace (ilustraciones, collages, letra a mano, capturas de pantalla con flechas): dilo con
honestidad y propón la versión más cercana que sí puede hacer.
