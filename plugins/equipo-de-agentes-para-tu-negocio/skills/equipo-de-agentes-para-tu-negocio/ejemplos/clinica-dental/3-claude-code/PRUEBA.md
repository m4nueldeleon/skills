# Prueba real · Claude Code · Clínica Dental Arcos (negocio de ejemplo)

Prueba hecha el 20 de octubre de 2026 siguiendo el paso 5B de la skill, con Claude Code 2.1.296 y los archivos de
`mi-equipo/` tal como están en esta carpeta.

> En tu computadora, la carpeta `claude/agents/` de este ejemplo se llama `.claude/agents/` (con punto al inicio).
> Aquí va sin punto para que se vea y se descargue con el resto.

## 1. Revisión de archivos

```text
$ python3 scripts/revisar_equipo.py mi-equipo
Agentes encontrados: administracion, atencion-a-clientes, coordinador, marketing, operaciones, ventas
✔ Equipo listo (6 agentes).
```

## 2. La tarea real

Desde `mi-equipo/`:

```text
claude --agent coordinador -p "<tarea>" --permission-mode acceptEdits
```

La tarea, escrita como la escribiría la dueña:

```text
Hola. Hoy es martes 20 de octubre de 2026. Necesito tres cosas para mandarlas hoy en la tarde:

1) Las confirmaciones de las citas de mañana miércoles 21:
- 9:00 Sra. Teresa – limpieza
- 10:30 Jorge – resina
- 12:00 Ana – valoración general
- 16:00 Luis – ajuste de brackets con el Dr. Iván
- 17:30 Sra. Carmen – extracción
- 19:00 Paola – blanqueamiento

2) Contestar este WhatsApp que llegó hace rato: «Hola buenas tardes, ¿cuánto cuesta el blanqueamiento? ¿duele?
¿me lo pueden hacer este sábado?»

3) Recordatorios de pago para 3 pacientes de ortodoncia (mensualidad de $1,200 cada uno):
- J. M.: 2 mensualidades atrasadas, siempre paga en su ajuste
- Sra. R.: 1 mensualidad, venció el 15 de octubre
- Paciente C. (adolescente, paga su mamá): 3 mensualidades atrasadas y no ha venido a su ajuste desde agosto
```

## 3. Qué pasó

- El coordinador leyó la ficha y los datos, y **repartió a 2 subagentes nativos al mismo tiempo**:
  `atencion-a-clientes` (confirmaciones + WhatsApp) y `administracion` (recordatorios). No llamó a ventas, marketing ni
  operaciones porque el encargo no era de ellos. Lo verificamos en el registro de la sesión: dos llamadas a la
  herramienta `Agent`, una por departamento.
- Cada subagente dejó su borrador en `entregables/` (están en esta carpeta, sin cambios).
- El coordinador revisó los dos borradores y entregó un solo resumen. Tardó unos 4 minutos.

## 4. Lo que detectó el equipo

- **Luis, ajuste de brackets el miércoles:** el Dr. Iván solo viene martes y jueves. Este choque lo pusimos a propósito
  para probar. El agente dejó dos mensajes, uno para confirmar si el doctor viene como excepción y otro para pasarlo
  al jueves, y le dejó la decisión a la dueña.
- **Sra. Teresa a las 9:00 un miércoles:** la clínica abre a las 10:00. Este choque **no** lo pusimos a propósito: fue
  un error real al escribir la agenda de prueba, y el equipo lo encontró.
- **Blanqueamiento:** dio el precio de la lista ($3,500), no prometió que «no duele» y no afirmó lo que la ficha tiene
  marcado [CONFIRMAR] (si hace falta valoración antes). Además avisó que eso también afecta a Paola, que tiene
  blanqueamiento mañana.
- **Pagos:** las cuentas cuadran (2 400 + 1 200 + 3 600 = 7 200). No inventó recargos ni ofreció descuentos. En el caso
  del adolescente primero invita a retomar los ajustes y luego menciona el pago.

## 5. Resumen que entregó el coordinador (copia textual)

> Ya están listos los tres encargos en borrador, y los revisé. No se envió nada. Antes de mandarlos hoy en la tarde
> tiene que decidir dos cosas sobre la agenda de mañana: dos citas caen en horarios que no corresponden con los de la
> clínica.
>
> **Las dos citas que hay que decidir primero**
> - Sra. Teresa, 9:00 (limpieza): los miércoles abrimos a las 10:00. ¿Abre antes para ella o se le cambia la hora?
> - Luis, 16:00 (ajuste de brackets): el Dr. Iván solo viene martes y jueves en la tarde. ¿Viene este miércoles como
>   excepción o se pasa al jueves 22?
>
> Para cada uno dejé dos mensajes: uno que confirma la cita como está y otro que la reacomoda. Mónica manda el que
> usted elija.
>
> *(Sigue: lo que quedó listo por departamento con la ruta de cada borrador, 4 decisiones [CONFIRMAR], 5 datos
> [PENDIENTE] y el siguiente paso.)*

## 6. Revisión de calidad (paso 6 de la skill)

| Pregunta | Resultado |
|---|---|
| ¿Usa datos reales de la ficha (giro, ciudad, servicios, tono)? | ✅ De usted, un emoji, firma de Mónica, precios y horarios de la lista |
| ¿Inventó algún precio, fecha, promoción o nombre? | ✅ No. Lo que faltaba quedó como [PENDIENTE] |
| ¿Respeta los límites de la dueña? | ✅ Sin diagnósticos, sin «no duele», sin descuentos, sin precio cerrado de ortodoncia |
| ¿Los departamentos se pisan? | ✅ No. Administración aclaró que agendar a C. le toca a atención |
| ¿Hace falta corregir algún agente? | No en esta prueba |
