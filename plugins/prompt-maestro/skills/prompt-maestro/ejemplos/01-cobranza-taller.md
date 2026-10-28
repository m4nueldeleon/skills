# Ejemplo 1 · Mensaje para cobrarle a un cliente

**Negocio de ejemplo** (inventado, para mostrar cómo trabaja la skill): un taller mecánico en Zapopan, Jalisco. Ni el taller ni el cliente existen.

Esta es la conversación completa, tal como la conduce la skill, con el resultado al final.

---

**Persona:** Prompt maestro: quiero un mensaje para cobrarle a un cliente que no ha pagado

**Claude:** Va. Te hago 3 preguntas rápidas y te armo el prompt (las instrucciones que le das a la IA). **1 de 3:** ¿Qué negocio tienes, cuánto te debe y desde cuándo? Por ejemplo: «estética, 1,200 pesos, desde hace un mes».

**Persona:** tengo un taller mecanico en zapopan. le cambie los frenos a su camioneta, son 4,800 y ya van 3 semanas. quedamos que me pagaba en una semana

**Claude:** **2 de 3:** ¿Qué tipo de cliente es?
a) Cliente de años, lo quiero conservar
b) Cliente nuevo o de una sola vez
c) Ya le cobré antes y no contesta
Si son dos, dime las dos. O dime «tú decide».

**Persona:** la a y la c. es don Beto, tiene como 4 años viniendo, siempre habia pagado. la semana pasada le mande un whats y me dejo en visto

**Claude:** **3 de 3:** ¿Cómo te puede pagar?
a) Por transferencia
b) Pasando al taller
c) Cualquiera de las dos
O dime «tú decide».

**Persona:** cualquiera de las dos. y si no puede todo junto, en partes si se puede

**Claude:**

**Tu prompt, listo para copiar**

```text
Actúa como la persona que lleva la cobranza de un taller mecánico y quiere cobrar sin perder al cliente.

MI NEGOCIO:
Taller mecánico en Zapopan, Jalisco. Hace 3 semanas le cambié los frenos a la camioneta de un cliente. El servicio fue de 4,800 pesos y quedamos en que pagaría en una semana. La semana pasada le mandé un recordatorio por WhatsApp; lo leyó y no contestó.

PARA QUIÉN ES:
Don Beto, cliente del taller desde hace unos 4 años. Siempre había pagado a tiempo; es la primera vez que se atrasa. Lo quiero conservar. Puede que se le haya pasado o que ahorita no tenga el dinero completo.

LA TAREA:
Escribe un mensaje de WhatsApp para recordarle el pago. La meta es que conteste hoy y me diga qué día va a pagar. Dile que puede transferir a [Número de cuenta o CLABE] o pasar a pagar al taller, y que, si le acomoda mejor, lo podemos dividir en partes.

EL TONO:
De usted y con confianza, como a un cliente de años. Amable y firme, sin ser grosero. No debe sonar a despacho de cobranza ni a regaño.

EL FORMATO:
Dos versiones para que yo elija: una más cálida y otra más directa. Cada una de 3 a 5 líneas, que se lea en menos de 20 segundos. Sin emojis. Que termine con una pregunta fácil de contestar.

EL EJEMPLO:
Solo para que veas el tono; no la copies: "Don Beto, buenas tardes, ¿cómo le ha ido con la camioneta?"

QUÉ EVITAR:
No inventes datos, cifras, testimonios ni promesas que no estén aquí: nada de recargos ni fechas límite que yo no puse. Nada de amenazas, groserías ni menciones de abogados. No lo hagas sentir exhibido ni culpable, y no le reclames que dejó el mensaje en visto.

ANTES DE RESPONDER:
Si te falta un dato indispensable, pregúntamelo antes de escribir. Si falta un dato menor, deja [CORCHETES] en vez de inventarlo.
```

**Qué hace cada parte**
- **Mi negocio:** le cuenta a la IA qué pasó, cuánto es y que ya le escribiste una vez; así no inventa nada.
- **Para quién es:** le dice que don Beto es buen cliente de años, y por eso el mensaje cuida la relación.
- **La tarea:** no pide «un mensaje de cobranza»; pide que te conteste hoy con una fecha, y le da las dos formas de pagar.
- **El tono:** de usted y con confianza; firme, pero sin regaño.
- **El formato:** dos versiones cortas para WhatsApp, para que tú elijas.
- **El ejemplo:** una frase que le enseña a la IA cómo suena tu trato con él.
- **Qué evitar:** cierra la puerta a amenazas, recargos inventados y al reclamo por el «visto».

**Lo que supuse:** que le hablas de usted y que no cobras recargos por atraso. Cámbialo si no es así.

**¿Y ahora?**
- Si quieres el resultado aquí mismo, escribe **úsalo**.
- Para otra IA: cópialo completo y pégalo en un chat nuevo de ChatGPT, Gemini o Claude. Antes de enviarlo, cambia lo que está entre [corchetes].

**Por qué este prompt funciona:** porque le dice a la IA que don Beto es un cliente de cuatro años que siempre ha pagado y que la meta es una fecha de pago, no un regaño; sin eso te habría dado un aviso de cobranza genérico que puede costarte al cliente.

---

**Persona:** úsalo

**Claude:**

**Versión cálida**

> Don Beto, buenas tardes, espero que ande muy bien. Le escribo por lo del cambio de frenos: quedaron pendientes los 4,800 pesos. Me puede transferir a [Número de cuenta o CLABE] o pasar al taller, como le quede mejor. Y si le acomoda en partes, lo platicamos sin problema. ¿Qué día lo vemos?

**Versión directa**

> Don Beto, buenas tardes. Le recuerdo el pago pendiente del cambio de frenos de su camioneta: 4,800 pesos. Puede ser por transferencia a [Número de cuenta o CLABE] o aquí en el taller; si necesita dividirlo en partes, dígame y lo acomodamos. ¿Qué día me lo puede cubrir?

¿Lo quieres más corto, más firme o más cálido?

---

## Prueba: el mismo prompt pegado en otras IA

Para comprobar que el prompt funciona fuera de esta conversación, se pegó tal cual en un chat nuevo de Gemini y en uno de Claude, sin ninguna otra instrucción (20 de octubre de 2026). Las dos IA entregaron dos versiones de usted, con las dos formas de pago, la opción de pagar en partes y una pregunta al final; ninguna inventó recargos ni mencionó el «visto». Lo que respondió Gemini, sin editar:

> **Opción 1: Más cálida**
> Don Beto, buenas tardes, espero que todo ande bien. Le escribo para saber cómo sintió la camioneta con el cambio de frenos y revisar lo de la cuenta pendiente de los 4,800 pesos. Sabe que con toda confianza puede pasar al taller, transferir a [Número de cuenta o CLABE] o, si lo prefiere, lo podemos dividir en partes para que le sea más cómodo. ¿Qué día le acomoda mejor para programar su pago?
>
> **Opción 2: Más directa**
> Don Beto, buenas tardes, gusto en saludarlo. Me comunico con usted para ponernos de acuerdo con el pago pendiente de los 4,800 pesos del servicio de su camioneta. Puede liquidarlo aquí en el taller, por transferencia a [Número de cuenta o CLABE], o si ahorita se le complica, con gusto lo dividimos en partes. ¿Cree que me pueda confirmar hoy qué día le queda bien realizar el pago?

Cada IA lo redacta a su manera; lo que se mantiene es lo que pide el prompt. Antes de mandarlo, revisa el monto y cambia los [corchetes].
