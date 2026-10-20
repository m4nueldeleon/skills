# Prueba · camino app · Clínica Dental Arcos (negocio de ejemplo)

Prueba hecha el 20 de octubre de 2026 con el proyecto 1 de `EQUIPO-EN-LA-APP.md` (Atención a pacientes).

**Cómo se probó:** imitamos un Proyecto de Claude. Las «Instrucciones del proyecto» fueron las instrucciones del
sistema, y la ficha y los 5 archivos de datos se dieron como conocimiento del proyecto. Claude no tuvo herramientas:
solo esas instrucciones y esos archivos, igual que un chat dentro del proyecto. No es la pantalla de la app, pero el
modelo recibe lo mismo.

**Mensaje de prueba:**

```text
Contesta este WhatsApp: «Hola buenas tardes, ¿cuánto cuesta el blanqueamiento? ¿duele? ¿me lo pueden hacer este sábado?»
```

**Respuesta (copia textual de la parte para mandar):**

> **Versión A: si NO se necesita revisión previa**
>
> Buenas tardes, le escribe Mónica de Clínica Dental Arcos. Con gusto le comparto la información.
>
> El blanqueamiento en consultorio tiene un costo de $3,500 y es una sesión de aproximadamente 1 hora.
>
> La doctora le explica todo antes de empezar. Si tiene sensibilidad o algún temor, coméntelo en su cita y lo
> valoramos juntos.
>
> Sí atendemos este sábado 24, de 9:00 a 14:00, con la Dra. Laura. ¿Le aparto un espacio a las [PENDIENTE: hora
> libre el sábado 24]? 😊
>
> **Versión B: si SÍ se necesita valoración antes**
> *(Igual, más la valoración de $300 de la lista y la invitación a apartarla el sábado.)*

Después agregó qué datos usó (precios, horarios, preguntas frecuentes) y dos pendientes para la dueña:
confirmar si hace falta valoración antes del blanqueamiento y la hora libre del sábado. También avisó que el
blanqueamiento debe empezar a más tardar a las 13:00, porque dura 1 hora y el sábado se cierra a las 14:00.

**Revisión de calidad:** precio de la lista ✅ · sin prometer «sin dolor» ✅ · respetó el [CONFIRMAR] ✅ · tono de
usted con un emoji ✅ · siguiente paso concreto ✅.
