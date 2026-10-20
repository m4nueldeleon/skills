# Ejemplo · Paso 4 · Revisión final

> Negocio de ejemplo (ficticio). Revisión de `despues/index.html` siguiendo el Paso 4 de la skill.

## 1. Revisión automática

Comando: `python3 scripts/revisar_pagina.py ejemplos/panaderia/despues/index.html`

```
❌ 3 por arreglar · ⚠️ 1 por revisar · ℹ️ 3 notas · ✅ 9 bien

Textos reales
- ❌ 4 marca(s) [PENDIENTE] por llenar antes de publicar (las da el dueño; no se inventan), p. ej. «[PENDIENTE: …]».
- ⚠️ Hay reseñas o testimonios: cada uno debe ser real, de un cliente que dio permiso. Nunca inventados.
Rasgos del «look de IA»
- ✅ No se encontraron los rasgos típicos del «look de IA» que esta revisión sabe medir.
Botones de contacto
- ✅ WhatsApp bien escrito (5233…), con mensaje prellenado.  ✅ Tiene enlace de «Cómo llegar».
Velocidad
- ✅ Peso del código: 22 KB.
Antes de publicar
- ❌ El enlace «Aviso de privacidad» lleva a aviso-de-privacidad.html, que todavía no existe: créalo con el texto
  que te dé tu abogado antes de publicar.
- ❌ El enlace «Términos de pedidos y anticipos» lleva a terminos-de-pedidos.html, que todavía no existe: (…)
```

Los ❌ se quedan a propósito y no se «arreglan» inventando: son los cuatro datos que solo la dueña puede dar (tres
fotos y cómo se paga el anticipo) y los dos documentos que prepara su abogado. Van a «Lo que tienes que hacer tú».
Las reseñas son las que la dueña pegó de Google.

## 2. Revisión con los ojos (capturas a 390 px y a 1280 px)

Capturas en `capturas/` (en la captura de página completa, la barra fija de WhatsApp sale a media página por
cómo se toma la captura; en el celular va siempre abajo). Lo que se vio y se corrigió en la primera vuelta:
- La letra del texto dibujaba el cero con raya («6:3Ø», «$48Ø»): se cambió Atkinson Hyperlegible por Source Sans 3.
- El encabezado se partía en cuatro renglones en el celular: el nombre ya no se corta y el horario baja si no cabe.
- En computadora, los botones de la portada se partían en dos renglones: ya no.

## 3. Tabla para la persona

| Qué revisé | Cómo está | Qué falta |
|---|---|---|
| Velocidad: peso, fotos reducidas, sin librerías de más, letras ≤ 2 familias | ✅ 22 KB de código, sin librerías, 2 familias de letra | Cuando pongas las fotos, que pesen menos de 400 KB cada una |
| Celular primero: se lee sin hacer zoom, nada se sale de lado, botones grandes | ✅ Diseñada a 390 px; botones de 48 a 52 px de alto | — |
| Textos reales: sin relleno, sin datos inventados, sin `[PENDIENTE]` olvidados | ❌ 4 pendientes | 3 fotos y cómo se paga el anticipo |
| Pie de página: quién vende y enlaces legales | ❌ Los enlaces están, los documentos no | Aviso de privacidad y términos de pedidos, de tu abogado |
| Botones de contacto: WhatsApp y teléfono funcionan, «Cómo llegar», visibles sin buscar | ✅ WhatsApp con mensaje listo, Llamar, Cómo llegar y barra fija abajo | Probarlos en tu celular (5 pruebas abajo) |
| Sin «look de IA»: se contaron los rasgos de la lista | ✅ Cero degradados, cero tarjetas, cero emojis, una sola escala de esquinas, sin etiquetitas en mayúsculas | — |
| Movimiento: con propósito, respeta «reducir movimiento», se ve sin JavaScript | ✅ Tres movimientos: entradas al bajar, trazo bajo la siguiente horneada y barra de contacto. Sin JavaScript todo se ve | — |
| Accesibilidad básica: textos alternativos, un solo título principal, contraste | ✅ Un título principal; contraste de 5.5:1 a 14.5:1 | Revisarla a pleno sol |

**Lo que tienes que hacer tú:**
1. Tomar 3 fotos con tu celular, horizontales y con luz de día: la charola de conchas recién salida, el mostrador
   con el pan dulce y un tres leches que hayan hecho. Mándamelas y las pongo.
2. Decirme cómo se paga el anticipo (efectivo en la panadería, transferencia…).
3. Confirmar que Laura M. y Ricardo T. están de acuerdo en que su reseña aparezca en tu página.
4. Pedirle a tu abogado el aviso de privacidad y los términos de pedidos y anticipos (la revisión para publicar
   te deja la lista de lo que necesita).
5. Subir la página a una dirección de prueba y hacer las 5 pruebas en tu celular:
   1) ¿se entiende qué vendes en 5 segundos? 2) toca el botón de WhatsApp: ¿abre con tu número y el mensaje?
   3) toca «Llamar»: ¿marca? 4) «Cómo llegar»: ¿abre el mapa en tu local? 5) en datos móviles, ¿carga en menos
   de 3 segundos?

**Siguiente paso:** ¿hacemos la revisión básica para publicar? Sales con la lista de pendientes para tu abogado o
contador.
