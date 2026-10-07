# Skills de Manuel de León

Skills gratuitas para que tu IA trabaje mejor en tu negocio: escribir con tu voz, responder sin relleno, analizar anuncios o editar tus videos.

Una *skill* es un paquete de instrucciones (y a veces herramientas) que Claude aprende una vez y usa cada vez que la necesitas. Todas las de este repositorio son públicas y puedes revisarlas antes de instalarlas.

**¿Primera vez?** Cada skill tiene una guía paso a paso, con botones para copiar, en [manueldeleonm.com/recursos](https://manueldeleonm.com/recursos/).

## Catálogo

<!-- catalogo:inicio -->
| Skill | Qué hace | Descarga |
|---|---|---|
| **analizar-anuncios** | Analiza anuncios públicos proporcionados por el usuario y desarrolla conceptos propios distinguiendo evidencia, hipótesis y resultados desconocidos. | [ZIP](https://github.com/m4nueldeleon/skills/releases/download/descargas/analizar-anuncios.zip) · [archivos](plugins/analizar-anuncios/skills/analizar-anuncios) |
| **editor-de-reels-con-ia** | Edita grabaciones propias para Reels con FFmpeg, elige un inicio con evidencia de la transcripción y exporta subtítulos sincronizados, audio normalizado y formato vertical u horizontal. | [ZIP](https://github.com/m4nueldeleon/skills/releases/download/descargas/editor-de-reels-con-ia.zip) · [archivos](plugins/editor-de-reels-con-ia/skills/editor-de-reels-con-ia) |
| **humaniza-tu-ia** | Edita textos de negocio usando ejemplos reales de la voz del autor, quitando relleno y preservando hechos y condiciones. | [ZIP](https://github.com/m4nueldeleon/skills/releases/download/descargas/humaniza-tu-ia.zip) · [archivos](plugins/humaniza-tu-ia/skills/humaniza-tu-ia) |
| **lbo-respuestas-precisas** | Produce respuestas de negocio proporcionadas al encargo, definiendo resultado, evidencia, límites y formato antes de ampliar explicaciones. | [ZIP](https://github.com/m4nueldeleon/skills/releases/download/descargas/lbo-respuestas-precisas.zip) · [archivos](plugins/lbo-respuestas-precisas/skills/lbo-respuestas-precisas) |
<!-- catalogo:fin -->

## Cómo instalar una skill

### En Claude (app de escritorio o claude.ai)

1. Descarga el ZIP de la skill (columna «Descarga»). No lo descomprimas.
2. En Claude, activa **Configuración → Capacidades → Ejecución de código y creación de archivos**.
3. Abre **Personalizar → Skills**, pulsa **+**, elige **Crear skill → Subir una skill** y selecciona el ZIP.
4. Revisa que el interruptor de la skill quede encendido.

### En Claude Code

Dentro de Claude Code, escribe estos dos comandos (cambia `humaniza-tu-ia` por la skill que quieras):

```text
/plugin marketplace add m4nueldeleon/skills
/plugin install humaniza-tu-ia@manuel-de-leon
```

Confirma la instalación en el panel que se abre y escribe `/reload-plugins` (o reinicia Claude Code). Cuando publiquemos mejoras, `/plugin marketplace update manuel-de-leon` te las trae.

### En ChatGPT, Gemini u otra IA

Abre el `SKILL.md` de la skill, copia su texto y pégalo en las instrucciones de un Proyecto de ChatGPT o de un Gem de Gemini. Funciona como instrucciones fijas; las skills con scripts (como el editor de Reels) necesitan Claude Code.

## Más skills de Manuel en su propio repositorio

- [carruseles-virales-ia](https://github.com/m4nueldeleon/carruseles-virales-ia): carruseles de Instagram listos para subir.
- [shorts-virales-ia](https://github.com/m4nueldeleon/shorts-virales-ia): de tu video en crudo a un short con subtítulos.
- [sin-huella-ia](https://github.com/m4nueldeleon/sin-huella-ia): quita lo que delata que un texto lo escribió una IA.
- [experto-ads-ia](https://github.com/m4nueldeleon/experto-ads-ia): de tu oferta a guiones de anuncios de Meta.
- [estrategia-contenido-viral](https://github.com/m4nueldeleon/estrategia-contenido-viral): tus métricas reales convertidas en guiones.
- [diapositivas-pizarron-ia](https://github.com/m4nueldeleon/diapositivas-pizarron-ia): diapositivas estilo pizarrón reveladas frase por frase.
- [cotizador-profesional-ia](https://github.com/m4nueldeleon/cotizador-profesional-ia): cotizaciones profesionales en PDF.
- [catalogo-vivo](https://github.com/m4nueldeleon/catalogo-vivo): tu catálogo de productos con IA, disponible 24/7.

## ¿Ya la tienes funcionando?

Si quieres llevar la IA a más áreas de tu negocio, [agenda tu diagnóstico](https://vsl.certificacionlegendaria.com/legendaria-us/aplicar?utm_source=github&utm_medium=referral&utm_campaign=leadmagnet_organico_mdl&utm_content=skills-readme): 15 minutos con el equipo de la certificación LEGENDAR·IA para revisar tu caso, conocer el programa y la inversión, y ver si encaja contigo.

## Para el equipo

Cómo crear, probar y publicar una skill: [CLAUDE.md](CLAUDE.md). Cada cambio en `main` publica los ZIP solo (GitHub Actions → «Validar y publicar skills»).

Licencia [MIT](LICENSE) · © 2026 Manuel de León
