# Ejemplo · Modo «Revisar» sobre una página con cara de IA

> Negocio de ejemplo (ficticio). `antes-cara-de-ia.html` es la página que sale cuando se le pide a una IA «hazme
> una página premium para mi panadería» sin dirección de arte. Captura: `capturas/antes-celular.jpg`.

**Persona:** Revisa mi página, siento que se ve como de plantilla. (adjunta el archivo)

**Claude:** Corrí la revisión y la miré en tamaño de celular. Estos son los 5 problemas que más te cuestan, en el
orden en que los ve un cliente:

1. **No dice nada útil en la primera pantalla.** «Donde cada pan es una obra maestra» y «Transformamos cada mañana
   en una experiencia única» le sirven a cualquier panadería. Tu cliente quiere saber a qué hora sale el pan, cuánto
   cuesta y cómo encargar. Qué hacer: un título con tu dato fuerte («Pan caliente dos veces al día») y la hora de
   la siguiente horneada.
2. **Los botones no llevan a ningún lado.** «Comenzar» y «Saber más» apuntan a `#`, y el WhatsApp está mal escrito
   (`wa.me/+52 33 0000 0000` no abre: van solo dígitos, `wa.me/523300000000`). Qué hacer: un botón que diga
   «Encargar un pastel por WhatsApp» con el número bien escrito, más «Llamar» y «Cómo llegar».
3. **Se ve hecha por IA:** degradado morado con rosa, letras con resplandor, título en Playfair itálica con una
   palabra en degradado, seis tarjetas con emojis, etiquetitas en mayúsculas en cada sección y orbes que flotan sin
   parar. Nada de eso sale de tu panadería. Qué hacer: colores de tu fachada y de tu bolsa de pan, una sola letra
   para títulos con carácter y nada que se mueva sin razón.
4. **Datos que nadie puede comprobar:** «+10,000 clientes felices», «99 % de satisfacción» y dos reseñas con cinco
   estrellas que no vienen de ningún lado. Qué hacer: borrarlos y poner reseñas reales de Google, con permiso.
5. **Pide datos que no necesitas y no dice para qué:** el formulario pide fecha de nacimiento y correo para
   promociones, sin aviso de privacidad, y la página carga Google Analytics y el píxel de Meta. Qué hacer: quitar el
   formulario (el WhatsApp basta), enlazar tu aviso de privacidad y quitar los rastreadores que no estés usando.
   Esto es orientación, no asesoría legal.

¿La rehago? Me quedo con lo tuyo (nombre, productos, horario) y cambio el look. → Resultado: `despues/index.html`.

---

## Salida completa de la revisión automática

### Revisión automática · antes-cara-de-ia.html

❌ 3 por arreglar · ⚠️ 32 por revisar · ℹ️ 4 notas · ✅ 2 bien

_Encuentra señales en el código; no sustituye abrir la página en tu celular ni la revisión de un profesional._

#### Celular primero
- ⚠️ La página impide hacer zoom con los dedos; quítalo (a mucha gente le cuesta leer letra chica).
- ⚠️ Falta el idioma en `<html lang="es-MX">` (ayuda a lectores de pantalla y a Google).
- ✅ Tiene la etiqueta que adapta la página al ancho del celular (viewport).

#### Velocidad
- ⚠️ Cargas 3 familias de letra (Playfair Display, Inter, Poppins): con 2 basta.
- ⚠️ Cargas 11 grosores de letra: usa solo los que de verdad aparecen.
- ⚠️ Agrega `&display=swap` al enlace de Google Fonts para que el texto se vea mientras carga la letra.
- ✅ Peso del código: 6 KB.

#### Botones de contacto
- ❌ El enlace de WhatsApp «+52 33 0000 0000» no funciona así: van solo dígitos, sin +, espacios ni guiones (ej. wa.me/523300000000).
- ⚠️ No hay enlace a mapa («Cómo llegar»); si tienes local, agrégalo.
- ⚠️ 5 enlace(s) que no llevan a ningún lado (href="#"). Conéctalos o quítalos.

#### Textos reales
- ⚠️ Frases vacías que suenan a IA: «transformamos», «soluciones innovadoras», «innovador», «de vanguardia», «experiencia única», «al siguiente nivel», «sin igual», «inigualable». Cámbialas por algo concreto de tu negocio (qué, cuánto, cuándo, dónde).
- ⚠️ Cifras que hay que poder comprobar: «+10,000 clientes», «99% de satisfacción». Si no son reales y medidas, bórralas.
- ⚠️ Hay reseñas o testimonios: cada uno debe ser real, de un cliente que dio permiso. Nunca inventados.

#### Rasgos del «look de IA»
- ⚠️ Letra muy usada por la IA para «verse premium»: playfair display. Úsala solo si puedes explicar por qué va con ESTE negocio.
- ⚠️ 5 degradado(s) morado/violeta: es el sello más reconocible del «look de IA».
- ⚠️ 6 degradados en la página: con uno (o ninguno) se ve más hecho a propósito.
- ⚠️ Texto pintado con degradado: otro tic típico de la IA.
- ⚠️ 3 resplandor(es) de color tipo neón (sombra sin desplazamiento): profundidad con sombras sobrias, no con brillo.
- ⚠️ Efecto de vidrio esmerilado en 3 lugares: úsalo en uno, si acaso.
- ⚠️ 6 etiquetitas en MAYÚSCULAS espaciadas arriba de los títulos: repiten el mismo ritmo en toda la página. Déjalas solo donde ubican algo de verdad (ej. «Paso 2 de 4»).
- ⚠️ Números decorativos 01, 02, 03… (3): úsalos solo si es un proceso real, en orden.
- ⚠️ 18 emojis en la página: si hacen de íconos, se ven distinto en cada teléfono y gritan «plantilla».
- ⚠️ 9 tarjetas (cajitas con sombra): agrupa con líneas o espacio; tarjeta solo si de verdad sobresale.
- ⚠️ 4 redondeos de esquina distintos (12px, 16px, 20px, 24px): elige una escala corta y respétala.
- ⚠️ Franja de color al costado de las tarjetas: otro tic de plantilla de IA.

#### Movimiento
- ❌ Falta `@media (prefers-reduced-motion: reduce)`: a algunas personas el movimiento las marea.
- ⚠️ Algo aparece creciendo desde la nada (`scale(0)`): se ve de caricatura. Que solo se desvanezca o suba un poco.
- ⚠️ Animaciones con `ease-in`: empiezan despacio y la página se siente pesada al tocarla. Usa una curva que frene al final (ease-out).
- ⚠️ 1 regla(s) con `transition: all`: anima hasta lo que no debe. Nombra solo lo que cambia.
- ⚠️ 2 animación(es) que no paran nunca: ¿explican algo? Si no, quítalas.
- ⚠️ 2 animación(es) de más de 1.2 s: la gente no espera, se siente lenta.

#### Accesibilidad básica
- ⚠️ Se quitó el contorno de foco y no hay `:focus-visible`: quien navega con teclado se pierde.
- ⚠️ 3 campo(s) de formulario sin etiqueta (label): el texto de ejemplo desaparece al escribir.
- ℹ️ El contraste de colores no se mide aquí: revisa a pleno sol en tu celular que todo se lea.

#### Antes de publicar (orientación, no asesoría legal)
- ❌ Pides datos y no hay enlace a un aviso de privacidad. Ponlo junto al botón de enviar.
- ⚠️ Pides datos delicados o de identificación (nacimiento): casi nunca hacen falta en una página; si los necesitas, pregúntale a un profesional cómo pedirlos.
- ⚠️ Juntas correos o teléfonos para promociones: cada envío debe traer cómo darse de baja y quién lo manda.
- ⚠️ Herramientas que registran a tus visitantes: Google Analytics o Tag Manager; Píxel de Meta (Facebook/Instagram). Menciónalas en tu aviso de privacidad, evalúa un aviso de cookies y apaga la grabación de sesiones si no la usas.
- ℹ️ Tu página pide estos datos: Nombre completo, Correo electrónico, Fecha de nacimiento. Pide solo lo indispensable.
- ℹ️ Las letras vienen de Google Fonts: su licencia permite uso comercial. Si tienes visitas de Europa, conviene alojarlas en tu propio servidor.
- ℹ️ Esto es orientación, no asesoría legal. Lo que dice la ley en tu caso lo confirma un abogado.

