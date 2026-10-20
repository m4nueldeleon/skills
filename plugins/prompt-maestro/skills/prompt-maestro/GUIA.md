# El prompt maestro: tú dices lo que quieres, la IA arma las instrucciones

Manuel de León · Recursos de IA para negocios · 20 de octubre de 2026

Una skill para que la IA te escriba el prompt que tú no sabrías escribir, y te explique por qué funciona.

## Qué hace

Un *prompt* son las instrucciones que le das a la IA. Casi todos le escribimos una línea («hazme un mensaje para cobrar») y nos llega algo genérico. No es culpa de la IA: no conoce tu negocio, ni a tu cliente, ni cómo hablas tú.

Con esta skill le dices lo que quieres con tus palabras. Ella:

1. Te hace de 2 a 4 preguntas cortas, una a la vez. Muchas se contestan con una letra.
2. Arma el prompt completo: tu negocio, a quién va dirigido, la tarea, el tono, el formato, un ejemplo y qué evitar.
3. Te explica cada parte en lenguaje simple.
4. Lo usa ahí mismo si escribes **úsalo**, o te lo da listo para pegarlo en ChatGPT, Gemini o Claude.
5. Termina con una línea: por qué ese prompt funciona. Así, cada vez que la usas, aprendes un poco.

La idea detrás: la IA es como un empleado muy capaz en su primer día. Sabe mucho, pero no conoce tu negocio. Un buen prompt le contesta lo que ese empleado preguntaría antes de empezar: ¿para quién trabajo?, ¿a quién le hablo?, ¿qué hago y para qué?, ¿cómo hablo?, ¿cómo lo entrego?, ¿me enseñas uno?, ¿qué no debo hacer?

## Instálala en Claude (claude.ai o la app de escritorio)

Hazlo desde la computadora; toma unos 3 minutos.

1. Descarga el archivo: https://github.com/m4nueldeleon/skills/releases/download/descargas/prompt-maestro.zip. No lo descomprimas.
2. En Claude, haz clic en tu nombre (abajo a la izquierda) → **Configuración → Capacidades** y activa **Ejecución de código y creación de archivos**.
3. Abre **Personalizar → Habilidades** (si tu Claude está en inglés: **Customize → Skills**), pulsa **+**, elige **Crear habilidad → Cargar una habilidad** y selecciona el ZIP.
4. Revisa que el interruptor de **prompt-maestro** quede encendido.

Funciona en todos los planes de Claude, también en el gratuito. Para usarla, abre un chat nuevo y empieza tu mensaje con **«Prompt maestro:»**. Así Claude sabe que quieres usar esta skill.

Si tu cuenta es de empresa y no ves la opción, pídele al administrador que active las habilidades, o usa el camino sin instalar (abajo): funciona igual.

## Instálala en Claude Code

Escribe estos dos comandos dentro de Claude Code:

```text
/plugin marketplace add m4nueldeleon/skills
/plugin install prompt-maestro@manuel-de-leon
```

Confirma en el panel que se abre y escribe `/reload-plugins` (o reinicia Claude Code).

## Sin instalar nada: en un Proyecto de Claude, de ChatGPT o en un Gem de Gemini

1. Abre el archivo `SKILL.md` de esta skill: https://github.com/m4nueldeleon/skills/tree/main/plugins/prompt-maestro/skills/prompt-maestro
2. Copia todo el texto desde «# Prompt maestro» hasta el final.
3. Pégalo como instrucciones fijas:
   - **Claude:** Proyectos → Crear proyecto → Instrucciones del proyecto.
   - **ChatGPT:** Proyectos → Nuevo proyecto → Instrucciones.
   - **Gemini:** Gems → Nuevo Gem → Instrucciones.
4. Cada vez que necesites algo, entra a ese proyecto o Gem y escribe lo que quieres.

## Pruébala con estos mensajes

Copia uno, cambia lo que está entre [corchetes] y envíalo.

**1. Cobrarle a un cliente sin perderlo**

```text
Prompt maestro: quiero un mensaje para cobrarle a un cliente que no ha pagado. Tengo [tu negocio, por ejemplo: un taller mecánico].
```

**2. Contestar una reseña mala**

```text
Prompt maestro: me dejaron una reseña de una estrella en Google y quiero contestarla bien. Tengo [tu negocio, por ejemplo: un restaurante de mariscos]. Esta es la reseña: [pega aquí la reseña].
```

**3. Una imagen para tus redes**

```text
Prompt maestro: necesito una imagen para anunciar [tu producto o promoción, por ejemplo: el pan de muerto] en Instagram.
```

También sirve para mejorar un prompt que ya tienes: «Prompt maestro: mejora este prompt: [pégalo aquí]».

En la carpeta `ejemplos/` hay dos conversaciones completas, de principio a fin, con negocios de ejemplo.

## Qué esperar

- **Preguntas cortas, una a la vez.** Contesta como si fuera WhatsApp. Si no sabes algo, escribe «tú decide» y la skill elige lo más razonable y te dice qué supuso.
- **Un prompt que puedes reusar.** Guárdalo en tus notas. La próxima vez cambias dos datos y listo.
- **Imágenes:** la skill te arma el prompt y tú lo pegas en una IA que crea imágenes, como ChatGPT o Gemini. Revisa que el texto de la imagen salga bien escrito; las IA de imagen se equivocan seguido con las letras.
- **Temas delicados** (contratos, salud, impuestos): te da un borrador para revisar con tu abogado, médico o contador. No es asesoría profesional.

## Antes de usar lo que te dé la IA

Léelo completo. Revisa montos, fechas, nombres y precios; cambia lo que está entre [corchetes]. Un buen prompt mejora el primer borrador, pero la última palabra es tuya.

No pegues en ninguna IA contraseñas, datos de tarjetas ni expedientes de tus clientes o pacientes. Usa [corchetes] y llénalos tú al final.

## Enlaces oficiales

- [Usar habilidades (skills) en Claude](https://support.claude.com/es/articles/12512180-uso-de-skills-en-claude)
- [Instalar skills en Claude Code](https://code.claude.com/docs/en/skills)
