# Arma tu equipo de agentes de IA para tu negocio

Manuel de León · Recursos de IA para negocios · 20 de octubre de 2026

Una skill que te entrevista y te deja listos 5 agentes de IA, uno por departamento: ventas, marketing, atención a
clientes, operaciones y administración. Cada uno conoce tu negocio y trabaja en borrador: nada sale sin que tú lo
apruebes.

## Qué es un «agente» aquí

Es Claude con un trabajo fijo, instrucciones escritas para tu negocio y los datos que necesita (tu lista de precios,
tus horarios, tus políticas). No es un empleado que trabaja solo mientras duermes. Es más parecido a tener a alguien
que ya sabe cómo hablas y qué vendes, al que le pides un borrador y te lo entrega en segundos. Tú revisas y tú mandas.

## Empieza por aquí

Antes de usar la skill, ten a la mano:

- Tu lista de precios (aunque sea una foto o un Excel).
- Tus horarios y tu ubicación.
- Uno o dos mensajes reales que les hayas mandado a tus clientes. Quítales nombres y teléfonos.
- Las 3 tareas que más tiempo te quitan a la semana. Es lo más importante: de ahí sale con qué agentes empiezas.

No necesitas preguntas frecuentes ni políticas escritas: si no las tienes, la skill te deja un borrador para que lo
corrijas.

## Qué vas a recibir

- Una **ficha de tu negocio** que leen todos los agentes.
- **5 agentes**, cada uno con su misión, sus instrucciones, los datos que necesita, sus límites y 3 mensajes listos
  para copiar.
- La recomendación de **con cuáles 2 empezar** esta semana.
- **En la app de Claude:** el texto listo para pegar en un Proyecto por agente, con el paso a paso para crearlo.
- **En Claude Code:** los agentes creados en tu computadora, un coordinador que reparte el trabajo entre ellos y una
  prueba con una tarea real de tu negocio.

## Instálala

Sigue el asistente de instalación: https://manueldeleonm.com/recursos/equipo-de-agentes-para-tu-negocio/

O hazlo a mano:

**En la app de Claude (web, escritorio o celular)**

1. Descarga el ZIP: https://github.com/m4nueldeleon/skills/releases/download/descargas/equipo-de-agentes-para-tu-negocio.zip
2. En Claude, entra a **Configuración → Capacidades** (en inglés: Settings → Capabilities) y prende la ejecución de
   código y creación de archivos («Code execution and file creation»). Las skills lo necesitan.
3. Entra a **Personalizar → Skills** (Customize → Skills), toca **+**, luego crear skill («Create skill») y subir una
   skill («Upload a skill»), y elige el ZIP.
4. Prende la skill en la lista.

Los nombres de los menús pueden cambiar con las actualizaciones de Claude. Las skills funcionan también en el plan
gratis.

**En Claude Code**

```text
/plugin marketplace add m4nueldeleon/skills
/plugin install equipo-de-agentes-para-tu-negocio@manuel-de-leon
```

## Cómo usarla sin instalar nada

Abre las instrucciones en GitHub:
https://github.com/m4nueldeleon/skills/blob/main/plugins/equipo-de-agentes-para-tu-negocio/skills/equipo-de-agentes-para-tu-negocio/SKILL.md

Copia todo el texto, pégalo en un chat nuevo de Claude y agrega: «Sigue estas instrucciones conmigo. Mi negocio es
[qué vendes y dónde]». Funciona, solo que sin las plantillas ni el ejemplo que trae la versión instalada.

## 3 formas de usarla (mensajes listos para copiar)

**1. Armar todo el equipo desde cero**

```text
Usa la skill equipo-de-agentes-para-tu-negocio. Mi negocio es [qué vendes, a quién y en qué ciudad]
y lo que más tiempo me quita es [tarea 1], [tarea 2] y [tarea 3].
```

**2. Empezar solo con dos agentes**

```text
Usa la skill equipo-de-agentes-para-tu-negocio, pero por ahora solo quiero los agentes de
[atención a clientes] y [ventas]. Tengo un/una [giro] en [ciudad]. Aquí está mi lista de precios: [pégala].
```

**3. En Claude Code, crear los agentes y probarlos**

```text
Usa la skill equipo-de-agentes-para-tu-negocio. Estoy en Claude Code: crea mi equipo en la carpeta mi-equipo
y pruébalo con esta tarea real: [por ejemplo, contestar estos 3 WhatsApp que me llegaron hoy: ...].
```

## Qué esperar

- **La entrevista son hasta 7 preguntas, una a la vez** (se salta lo que ya le dijiste). Puedes contestar corto o
  dictar por voz. Si no sabes algo, escribe «no sé» y sigue.
- **Calcula entre 20 y 40 minutos** para armar el equipo la primera vez, contando la creación de los proyectos.
- **En Claude Code, la prueba con una tarea real tarda unos minutos** y usa tu plan de Claude como cualquier
  conversación.
- **Los agentes entregan borradores.** Tú los lees, cambias lo que no dirías y los mandas. Nada se envía, se publica ni
  se cobra solo.
- **La primera semana vas a corregir.** Cuando un agente se equivoque, dile a Claude qué hizo y qué esperabas, y él
  ajusta sus instrucciones. Con unos días de uso, suenan más a ti.
- **Si tu plan es gratis**, Claude te deja tener hasta 5 proyectos. Si ya tienes otros, la skill te ofrece un solo
  proyecto «Mi equipo» que reparte el trabajo entre los 5 departamentos.

## Antes de usarlo con clientes

- Revisa los precios y horarios que quedaron en la ficha. Si algo está mal ahí, todos los agentes lo repiten.
- No subas contraseñas, números de tarjeta, identificaciones ni expedientes de tus clientes.
- En temas de impuestos, contratos o salud, los agentes te orientan, pero no sustituyen a tu contador, a tu abogado
  ni a un profesional de salud.
- Esta skill no promete más ventas ni horas ahorradas. Te ahorra el arranque en blanco; el resultado depende de qué
  tan bien la alimentes y la uses.

## Enlaces oficiales

- [Proyectos en Claude](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)
- [Skills en Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [Subagentes en Claude Code](https://code.claude.com/docs/en/sub-agents)
