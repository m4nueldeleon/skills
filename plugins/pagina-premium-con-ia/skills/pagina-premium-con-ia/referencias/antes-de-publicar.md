# Revisión básica para publicar · México y EE. UU.

> **Esto es una lista de orientación, no asesoría legal.** Sirve para llegar preparado con tu abogado (y con tu
> contador para precios, IVA y facturación).
> No sustituye a un profesional: las leyes cambian y lo que te aplica depende de tu giro, de tu tamaño y de dónde
> están tus clientes. Lista preparada en octubre de 2026.

## Cómo la usa Claude

1. Si no lo sabe, pregunta, una a la vez: dónde están los clientes (México, EE. UU. o los dos) y si la página pide
   datos, cobra, hace reservas o usa analítica o píxeles de anuncios.
2. Revisa cada tema y marca ✅ listo · ⚠️ revisar · ❌ falta.
3. Entrega el semáforo, el inventario de datos, las preguntas para el profesional y los arreglos técnicos que ya
   hizo en la página.
4. Nunca redacta el aviso de privacidad, los términos ni la política de cookies definitivos, nunca dice que la
   página «cumple con la ley», no concluye por la persona que algo «no le aplica» y no usa montos de multas para
   asustar.

## 1. Quién vende

- **México:** la Ley Federal de Protección al Consumidor pide que, cuando vendes por internet, el cliente sepa
  quién le vende: nombre o razón social, domicilio físico y cómo contactarte, antes de comprar.
- **EE. UU.:** las reglas varían por estado y por giro; mostrar quién eres y cómo contactarte es lo mínimo
  para generar confianza.
- **Claude hace:** pone en el pie el nombre comercial, la razón social si la hay (`[PENDIENTE]` si no la sabe),
  dirección, teléfono, correo y horario.

## 2. Aviso de privacidad (México) / política de privacidad (EE. UU.)

- **México:** si tu negocio recaba datos personales, aunque sea nombre y teléfono para un pedido por WhatsApp, la
  Ley Federal de Protección de Datos Personales en Posesión de los Particulares (la nueva, publicada en marzo de
  2025) te pide un aviso de privacidad disponible antes de recabarlos. En general debe decir: quién eres y tu
  domicilio; qué datos pides; para qué los usas (lo necesario para atenderte y lo que no, como promociones); cómo
  negarse a lo que no es necesario; cómo pedir acceso, corrección, cancelación u oposición (derechos ARCO); si
  compartes datos con otros, y cómo avisarás de cambios. Existe una versión corta (aviso simplificado) para poner
  junto a un formulario, con enlace al completo. Los datos sensibles (salud, religión, vida sexual, origen étnico,
  entre otros) piden consentimiento expreso y por escrito. Con la ley de 2025, las funciones del antiguo INAI
  pasaron a la Secretaría Anticorrupción y Buen Gobierno; tu abogado te dice cuál es la guía vigente.
- **EE. UU.:** no hay una ley federal general. California (ley CalOPPA) pide que todo sitio comercial que reciba
  datos personales de residentes de California publique una política de privacidad visible, sin importar el
  tamaño del negocio. Otros estados tienen leyes más amplias que suelen aplicar a empresas que pasan ciertos
  tamaños o volúmenes de datos; tu abogado te dice si te tocan.
- **Claude hace:** el inventario de datos (abajo), la lista de lo que el aviso debe cubrir, el enlace en el pie y
  el espacio para la línea corta junto a cada formulario. **No hace** el texto final.

**Inventario de datos** (se llena con el dueño y se le entrega al profesional):

| Dato | Dónde se pide | Para qué | Quién más lo recibe | Cuánto tiempo se guarda |
|---|---|---|---|---|
| Nombre y teléfono | Botón de WhatsApp | Tomar el pedido | WhatsApp (Meta) | [PENDIENTE] |
| Visitas a la página | Analítica (si hay) | Saber cuánta gente entra | [Herramienta] | [PENDIENTE] |
| … | … | … | … | … |

## 3. Formularios: pide lo menos posible

- La forma más sencilla de cumplir es pedir menos. Para un negocio local, un botón de WhatsApp o de llamada suele
  bastar.
- Si hay formulario: nombre, una forma de contacto y el mensaje. Nada de fecha de nacimiento, CURP, RFC, INE,
  número de seguro social, tarjetas ni datos de salud en un formulario común.
- **Consultorios:** en EE. UU., los datos de salud que maneja un consultorio pueden estar protegidos por HIPAA, y
  algunos estados (como Washington) protegen los datos de salud aunque el negocio sea pequeño; no pidas síntomas en
  un formulario común ni pongas píxeles de anuncios en las páginas de citas sin asesoría. En México, los datos de
  salud son sensibles.
- **Menores:** si la página está dirigida a menores de 13 años, en EE. UU. aplica COPPA (permiso de los padres).
- **Productos con edad mínima** (alcohol, tabaco y otros para adultos): en México suele ser 18 años y en EE. UU. 21;
  tu asesor te dice qué avisos y controles necesitas.
- **Claude hace:** reduce los campos, separa la casilla de promociones (sin marcar) y deja junto al botón un
  espacio `[PENDIENTE: aviso simplificado que te dé tu abogado]` con enlace al aviso completo.

## 4. Cookies y herramientas que rastrean

- Haz la lista: Google Analytics o Tag Manager, píxel de Meta (Facebook/Instagram), de TikTok, herramientas que
  graban sesiones (Hotjar, Microsoft Clarity y similares), chats, mapas o videos incrustados, letras cargadas
  desde Google.
- **México:** el aviso de privacidad debe mencionar si usas cookies u otras tecnologías que obtienen datos, cuáles
  y cómo desactivarlas.
- **EE. UU.:** en California ha habido demandas contra sitios por grabar sesiones o compartir datos con píxeles y
  chats sin avisar. Si no usas la grabación de sesiones, apágala; si la usas, oculta lo que la gente escribe.
- **Visitantes de Europa:** ahí el permiso previo para cookies es obligatorio y cargar letras desde los servidores
  de Google ha generado reclamaciones; conviene alojar las letras en tu propio servidor.
- **Claude hace:** quita lo que no se usa, dice qué herramientas encontró y, si el profesional lo recomienda, deja
  los rastreadores para que carguen solo después de que el visitante acepte. Si hay aviso de cookies, «Aceptar» y
  «Rechazar» igual de visibles.

## 5. Promociones por correo, WhatsApp o SMS

- **México:** la ley de protección al consumidor obliga a respetar a quien no quiere recibir publicidad; PROFECO
  tiene el Registro Público para Evitar Publicidad (REPEP). Cada mensaje dice quién lo manda y cómo dejar de
  recibirlos.
- **EE. UU.:** para correos, la ley CAN-SPAM pide decir quién manda, una dirección postal física, un asunto que no
  engañe y una forma clara de darse de baja que se respete en máximo 10 días hábiles (no exige permiso previo, pero
  pedirlo evita problemas). Para mensajes de texto o llamadas automatizadas de promoción, la ley TCPA pide permiso
  previo por escrito, y para llamar a vender hay que respetar el registro nacional «Do Not Call».
- **WhatsApp:** sus reglas para empresas piden que la persona haya aceptado recibir tus mensajes.
- **Claude hace:** casilla aparte y sin marcar para promociones; recordatorio de incluir la forma de darse de baja
  en cada envío.

## 6. Términos y condiciones (si vendes, cobras anticipos o reservas)

- Lo que suelen cubrir: qué incluye; precio total y forma de pago; anticipos; cancelaciones y reembolsos;
  entregas; garantías; quién vende; ley y autoridad aplicable (en México, PROFECO para el consumidor).
- **Suscripciones con renovación automática:** en EE. UU., una ley federal para ventas en línea (ROSCA) y varias
  estatales (como la de California) piden mostrar las condiciones de renovación antes de cobrar, pedir aceptación
  expresa y permitir cancelar fácil.
- **Ventas a distancia en México:** pregunta a tu abogado si te aplica el plazo para que el cliente cancele una
  compra hecha por teléfono o internet, y cómo avisarlo.
- **Claude hace:** la lista de puntos que el dueño debe decidir (por ejemplo, «¿devuelves el anticipo si cancelan
  con 24 horas?») y el enlace en el pie. **No hace** el texto final.

## 7. Precios y promociones

- **México:** al consumidor se le muestra el precio total, el que va a pagar, con impuestos incluidos; si tu precio
  no incluye IVA, se cambia el precio, no la etiqueta. Las promociones dicen sus condiciones y su vigencia; la
  publicidad debe ser veraz y no inducir a error.
- **EE. UU.:** precio completo, sin cargos que aparecen al final; promociones con condiciones claras.
- **Sorteos, rifas y concursos:** en México suelen necesitar permiso de la Secretaría de Gobernación; en EE. UU.,
  por lo general no se puede exigir una compra para participar y algunos estados piden registro cuando el premio es
  grande. Pregúntale a tu abogado antes de anunciarlos.
- **Claude hace:** aclara la moneda (MXN / USD) y le recuerda al dueño confirmar con su contador que el precio
  publicado es el total.

## 8. Reseñas, testimonios y cifras

- **EE. UU.:** desde octubre de 2024 la FTC (la autoridad federal de comercio) prohíbe reseñas y testimonios falsos,
  incluidos los generados con IA, y presentar como independientes reseñas que no lo son.
- **México:** la publicidad engañosa está prohibida por la ley de protección al consumidor.
- Reseñas reales, con permiso de quien las escribió y sin cambiar su sentido; si alguien recibió algo a cambio,
  se dice. Cifras solo si se pueden comprobar.

## 9. Imágenes, videos y música

- **Propias:** si las tomó un fotógrafo contratado, que el acuerdo diga que puedes usarlas.
- **Bancos de fotos:** guarda la licencia y respeta sus límites. Google Imágenes no es un banco gratis: casi todo
  tiene dueño.
- **Personas que salen:** permiso por escrito (en México, la Ley Federal del Derecho de Autor pide consentimiento
  expreso para usar el retrato de una persona); con menores, de sus padres. Fotos de antes y después de pacientes,
  solo con consentimiento escrito.
- **Generadas con IA:** revisa que la herramienta permita uso comercial y no las presentes como fotos reales de tu
  producto, local, equipo o resultados.
- **Logotipos ajenos:** solo con permiso (los métodos de pago suelen dar logos oficiales para mostrar que los
  aceptas).
- **Música o videos incrustados:** con licencia.
- **EE. UU.:** si tus clientes pueden subir fotos o comentarios a tu página, registrar un agente de derechos de
  autor (agente DMCA) en la Oficina de Derechos de Autor es uno de los requisitos para protegerte si alguien sube
  algo ajeno; también hay que publicar sus datos y retirar rápido lo que te reporten. Tu abogado te dice el resto.

## 10. Tipografías

- Las de Google Fonts tienen licencias abiertas (la mayoría SIL Open Font License) que permiten uso comercial y en
  páginas web.
- Letras compradas o descargadas de otros sitios: revisa que la licencia incluya uso web; la de escritorio no
  siempre alcanza. Las de Adobe Fonts dependen de tener la suscripción activa.

## 11. Nombre, dominio y marca

- Antes de invertir en un nombre o dominio, busca que no sea marca registrada de otro en tu giro: IMPI (México) y
  USPTO (EE. UU.). Registrar tu marca es otro trámite; pregúntale a un especialista.

## 12. Giros con reglas propias de publicidad

- **Salud:** en México, la Ley General de Salud pide que la publicidad de profesionales de la salud diga qué
  institución dio el título y el número de cédula profesional, y COFEPRIS tiene reglas sobre promesas de resultados
  y fotos de antes y después. En EE. UU., los consejos estatales (dental, médico) regulan la publicidad.
- **Inmobiliario:** varios estados de México y de EE. UU. piden registro o licencia del agente y mostrarla; en EE.
  UU., además, los anuncios de vivienda siguen reglas de vivienda justa (Fair Housing).
- **Alimentos, bebidas alcohólicas, suplementos, finanzas y seguros:** tienen reglas propias.
- **Claude hace:** lo menciona y pregunta; no afirma requisitos específicos sin que el profesional los confirme.

## 13. Accesibilidad (sobre todo en EE. UU.)

- En EE. UU. hay demandas frecuentes, bajo la ley ADA, contra negocios cuyas páginas no pueden usar personas con
  discapacidad. La referencia técnica más usada es WCAG nivel AA.
- Básicos: texto alternativo en imágenes, buen contraste, que se pueda usar con teclado, letra legible, formularios
  con etiquetas y videos con subtítulos.
- Ojo con los complementos o «widgets» de accesibilidad que prometen que con instalarlos ya cumples: ninguno lo
  logra solo, y en EE. UU. la autoridad de comercio ya sancionó a una empresa de estos por prometerlo.

## Lo que se entrega

1. **Semáforo:**

   | Tema | Cómo está | Qué hacer | ¿Lo ve un profesional? |
   |---|---|---|---|

2. **Inventario de datos** (tabla de la sección 2).
3. **Preguntas para tu abogado (y para tu contador, las de precios):**
   - Según dónde están mis clientes, ¿qué leyes de privacidad me aplican?
   - Con este inventario, ¿me preparas el aviso de privacidad completo y el simplificado?
   - ¿Necesito términos y condiciones? ¿Qué política de cancelación y reembolso me conviene?
   - ¿Puedo usar estas herramientas de analítica y anuncios? ¿Necesito aviso de cookies?
   - ¿Mi giro tiene reglas de publicidad (permisos, cédula, leyendas obligatorias)?
   - ¿Cómo pido permiso para mandar promociones por WhatsApp o correo?
   - ¿Mi nombre comercial choca con una marca registrada?
   - ¿Cómo debo mostrar precios e impuestos? (con tu contador)
   - ¿Puedo hacer sorteos o rifas en mi página o redes, y qué permiso necesito?
   - Si vendo por teléfono o internet, ¿qué plazo tiene el cliente para cancelar y cómo lo aviso?
4. **Arreglos técnicos hechos** en la página (lista).

## Sitios oficiales para leer más

- México: gob.mx/profeco (consumidor y REPEP) · diputados.gob.mx/LeyesBiblio (texto vigente de las leyes) ·
  gob.mx/impi (marcas) · gob.mx/cofepris (publicidad en salud).
- EE. UU.: ftc.gov/business-guidance (privacidad, reseñas, CAN-SPAM, COPPA) · ada.gov (accesibilidad web) ·
  copyright.gov (derechos de autor y agente DMCA) · uspto.gov (marcas) · oag.ca.gov/privacy (California).

> Repite al final: **orientación, no asesoría legal.** Con esta lista llegas preparado a tu cita con el abogado.
