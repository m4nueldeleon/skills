#!/usr/bin/env python3
"""Revisión automática de una página HTML · skill pagina-premium-con-ia (Manuel de León).

Uso (en Windows, cambia python3 por py):
    python3 revisar_pagina.py index.html            # reporte en español (Markdown)
    python3 revisar_pagina.py index.html --json     # el mismo reporte en JSON

Qué hace: lee el archivo HTML (y las hojas de estilo y scripts locales que enlaza) y busca
señales en ocho frentes: celular, velocidad, contacto, textos reales, «look de IA», movimiento,
accesibilidad básica y orientación antes de publicar.

Qué NO hace: no se conecta a internet, no ejecuta la página y no da asesoría legal. Encuentra
señales; no sustituye abrir la página en tu celular ni la revisión de un profesional.
Requiere solo Python 3.8 o más reciente (biblioteca estándar).
"""
import colorsys
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from typing import Dict, List, Tuple  # noqa: E402

from lector_html import Pagina, cargar_pagina  # noqa: E402

ICONOS = {"falta": "❌", "aviso": "⚠️", "nota": "ℹ️", "ok": "✅"}
GRUPOS = [
    "Celular primero", "Velocidad", "Botones de contacto", "Textos reales",
    "Rasgos del «look de IA»", "Movimiento", "Accesibilidad básica",
    "Antes de publicar (orientación, no asesoría legal)",
]

FUENTES_CLICHE = ["fraunces", "instrument serif", "playfair display", "cormorant"]
FUENTES_GENERICAS = {"inter", "poppins", "montserrat", "roboto", "open sans", "arial",
                     "helvetica", "system-ui", "sans-serif", "serif", "-apple-system",
                     "blinkmacsystemfont", "segoe ui", "helvetica neue", "monospace", "ui-sans-serif"}
LIBRERIAS_PESADAS = {
    "three": "Three.js (3D)", "gsap": "GSAP (animaciones)", "jquery": "jQuery",
    "bootstrap": "Bootstrap", "cdn.tailwindcss.com": "Tailwind desde CDN (no es para publicar)",
    "splinetool": "Spline (3D)", "lottie": "Lottie", "aos": "AOS (animaciones al bajar)",
    "swiper": "Swiper (carrusel)", "particles": "partículas", "locomotive": "Locomotive Scroll",
    "lenis": "Lenis (cambia el scroll)", "fullpage": "fullPage.js (secuestra el scroll)",
}
RASTREADORES = {
    "googletagmanager.com": "Google Analytics o Tag Manager", "google-analytics.com": "Google Analytics o Tag Manager",
    "gtag(": "Google Analytics o Tag Manager", "connect.facebook.net": "Píxel de Meta (Facebook/Instagram)",
    "fbq(": "Píxel de Meta (Facebook/Instagram)", "hotjar": "Hotjar (puede grabar sesiones)",
    "clarity.ms": "Microsoft Clarity (puede grabar sesiones)", "fullstory": "FullStory (graba sesiones)",
    "analytics.tiktok.com": "Píxel de TikTok", "snap.licdn.com": "LinkedIn Insight",
    "mouseflow": "Mouseflow (graba sesiones)", "smartlook": "Smartlook (graba sesiones)",
    "luckyorange": "Lucky Orange (graba sesiones)",
}
BANCOS_DE_FOTOS = ["unsplash", "pexels", "pixabay", "shutterstock", "istockphoto", "freepik", "gettyimages"]
RELLENO = [
    "transformamos", "transforma tu", "eleva tu", "elevamos", "potencia tu", "potenciamos",
    "desbloquea", "soluciones innovadoras", "innovador", "de vanguardia", "experiencia única",
    "experiencias únicas", "al siguiente nivel", "a otro nivel", "sin igual", "inigualable",
    "excelencia", "pasión por", "nos apasiona", "comprometidos con", "tu aliado", "revoluciona",
    "en el mundo actual", "hoy en día", "sumérgete", "de clase mundial", "somos líderes",
    "líderes en", "la mejor opción", "soluciones integrales", "a la medida de tus necesidades",
    "calidad premium", "descubre cómo", "más que un",
]
MARCADORES_FALSOS = [
    r"lorem ipsum", r"dolor sit amet", r"nombre del negocio", r"nombre de tu negocio",
    r"tu negocio aquí", r"\bacme\b", r"john doe", r"jane doe", r"example\.com",
    r"ejemplo\.com", r"tudominio", r"tuempresa", r"\b555-\d", r"123-4567", r"placeholder",
]
DATOS_SENSIBLES = re.compile(
    r"curp|\brfc\b|nacimiento|\bedad\b|salud|padecimiento|enfermedad|alergia|medicamento|diagn[oó]stico|"
    r"tarjeta|\bcvv\b|\bssn\b|social security|seguro social|\bine\b|pasaporte|religi|sexual",
    re.I)
PALABRAS_DE_VENTA = re.compile(
    r"\bcomprar\b|\bcompras?\b|carrito|\bpagar\b|\bpagos?\b|\breserv(?:a|as|ar|aci[oó]n|aciones)\b|apartar|"
    r"apartado|anticipo|suscripci[oó]n|membres[ií]a|\benv[ií]os?\b", re.I)
EMOJI = re.compile("[\U0001F300-\U0001FAFF\u2600-\u26FF\u2705\u2728\u274C\u2764\u2B50]")
NOMBRES_MORADOS = {"purple", "violet", "indigo", "fuchsia", "magenta", "blueviolet",
                   "mediumpurple", "darkviolet", "rebeccapurple", "darkorchid", "orchid"}


# ── Utilidades de color ──────────────────────────────────────────────────────

def _hex_a_rgb(h: str) -> Tuple[int, int, int]:
    h = h.lstrip("#")
    if len(h) in (3, 4):
        h = "".join(c * 2 for c in h[:3])
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def colores_en(valor: str) -> List[Tuple[float, float, float]]:
    """Devuelve una lista de (h°, s, l) de los colores escritos en un valor CSS."""
    salida = []
    for m in re.finditer(r"#([0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3,4})\b", valor):
        r, g, b = _hex_a_rgb(m.group(0))
        salida.append(_a_hsl(r, g, b))
    for m in re.finditer(r"rgba?\(\s*([\d.]+)[\s,]+([\d.]+)[\s,]+([\d.]+)", valor):
        r, g, b = (float(x) for x in m.groups())
        salida.append(_a_hsl(r, g, b))
    for m in re.finditer(r"hsla?\(\s*([\d.]+)(?:deg)?[\s,]+([\d.]+)%[\s,]+([\d.]+)%", valor):
        h, s, l = (float(x) for x in m.groups())
        salida.append((h % 360, s / 100, l / 100))
    for nombre in re.findall(r"\b[a-z]+\b", valor.lower()):
        if nombre in NOMBRES_MORADOS:
            salida.append((280.0, 0.6, 0.45))
    return salida


def _a_hsl(r: float, g: float, b: float) -> Tuple[float, float, float]:
    h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
    return (h * 360, s, l)


def es_morado(hsl: Tuple[float, float, float]) -> bool:
    h, s, l = hsl
    return 245 <= h <= 300 and s >= 0.35 and 0.18 <= l <= 0.85


def es_crema(hsl: Tuple[float, float, float]) -> bool:
    h, s, l = hsl
    return 25 <= h <= 55 and 0.15 <= s <= 0.75 and 0.88 <= l <= 0.97


def es_saturado(hsl: Tuple[float, float, float]) -> bool:
    return hsl[1] >= 0.45 and 0.2 <= hsl[2] <= 0.85


# ── Hallazgos ────────────────────────────────────────────────────────────────

class Reporte:
    def __init__(self) -> None:
        self.hallazgos: List[Dict[str, str]] = []

    def agregar(self, grupo: str, nivel: str, mensaje: str) -> None:
        self.hallazgos.append({"grupo": grupo, "nivel": nivel, "mensaje": mensaje})

    def conteo(self) -> Dict[str, int]:
        return {n: sum(1 for h in self.hallazgos if h["nivel"] == n) for n in ICONOS}


def _decls(p: Pagina, propiedad: str) -> List[Tuple[str, str]]:
    """Valores (ya con variables resueltas) de una propiedad en todas las reglas."""
    return [(sel, val) for sel, prop, val, _ in p.declaraciones if prop == propiedad]


def revisar_celular(p: Pagina, r: Reporte) -> None:
    g = GRUPOS[0]
    vp = p.meta.get("viewport", "")
    if "width=device-width" in vp.replace(" ", ""):
        r.agregar(g, "ok", "Tiene la etiqueta que adapta la página al ancho del celular (viewport).")
    else:
        r.agregar(g, "falta", "Falta `<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">`: "
                              "en el celular se verá diminuta.")
    if re.search(r"user-scalable\s*=\s*(no|0)|maximum-scale\s*=\s*1(\.0)?\b", vp):
        r.agregar(g, "aviso", "La página impide hacer zoom con los dedos; quítalo (a mucha gente le cuesta leer letra chica).")
    fijos = []
    for _, prop, val, en in p.declaraciones:
        m = re.match(r"\s*(\d+)px", val)
        if prop in ("width", "min-width") and m and int(m.group(1)) > 480 and not any(a.startswith("@media") for a in en):
            fijos.append(int(m.group(1)))
    if fijos:
        r.agregar(g, "aviso", f"Hay {len(fijos)} anchos fijos mayores a 480 px (p. ej. {fijos[0]} px): en un celular "
                              "pueden obligar a mover la pantalla de lado. Usa max-width o porcentajes.")
    if not p.lang:
        r.agregar(g, "aviso", "Falta el idioma en `<html lang=\"es-MX\">` (ayuda a lectores de pantalla y a Google).")


def revisar_velocidad(p: Pagina, r: Reporte) -> None:
    g = GRUPOS[1]
    kb = p.bytes_totales / 1024
    if kb > 600:
        r.agregar(g, "aviso", f"La página pesa {kb:,.0f} KB entre HTML, estilos y scripts locales: apunta a menos de 600 KB.")
    else:
        r.agregar(g, "ok", f"Peso del código: {kb:,.0f} KB.")
    if p.bytes_data_uri > 1.5 * 1024 * 1024:
        r.agregar(g, "aviso", f"Las imágenes incrustadas suman {p.bytes_data_uri / 1048576:.1f} MB: redúcelas a ~1600 px de ancho.")
    pesadas = [f"{n} ({t // 1024} KB)" for n, t in p.imagenes_locales if t > 400 * 1024]
    if pesadas:
        r.agregar(g, "aviso", "Fotos pesadas (más de 400 KB): " + ", ".join(pesadas[:5]) + ". Comprímelas.")
    todo_js = " ".join(p.scripts_src).lower()
    libs = sorted({nombre for clave, nombre in LIBRERIAS_PESADAS.items() if clave in todo_js})
    if libs:
        r.agregar(g, "aviso", "Librerías externas: " + ", ".join(libs) + ". ¿De verdad hacen falta? Cada una hace más lenta la carga.")
    sin_medidas = [i for i in p.imagenes if not i["src"].startswith("data:") and not (i.get("width") and i.get("height"))]
    if sin_medidas:
        r.agregar(g, "aviso", f"{len(sin_medidas)} imagen(es) sin width y height: la página «brinca» mientras carga.")
    sin_lazy = [i for i in p.imagenes[2:] if i.get("loading") != "lazy"]
    if sin_lazy:
        r.agregar(g, "aviso", f"{len(sin_lazy)} imagen(es) de más abajo sin loading=\"lazy\": cargan aunque nadie llegue a verlas.")
    familias, pesos = p.fuentes_google()
    if len(familias) > 2:
        r.agregar(g, "aviso", f"Cargas {len(familias)} familias de letra ({', '.join(familias)}): con 2 basta.")
    if pesos > 6:
        r.agregar(g, "aviso", f"Cargas {pesos} grosores de letra: usa solo los que de verdad aparecen.")
    if familias and not any("display=swap" in h for h in p.hojas_externas):
        r.agregar(g, "aviso", "Agrega `&display=swap` al enlace de Google Fonts para que el texto se vea mientras carga la letra.")
    if p.videos_autoplay:
        r.agregar(g, "aviso", f"{p.videos_autoplay} video(s) que arrancan solos: pesan mucho en datos móviles; usa una imagen de portada.")


def revisar_contacto(p: Pagina, r: Reporte) -> None:
    g = GRUPOS[2]
    hrefs = [a["href"] for a in p.enlaces]
    tels = [h for h in hrefs if h.lower().startswith("tel:")]
    was = [h for h in hrefs if "wa.me/" in h or "api.whatsapp.com/send" in h or "whatsapp.com/send" in h]
    mails = [h for h in hrefs if h.lower().startswith("mailto:")]
    mapas = [h for h in hrefs if re.search(r"google\.[a-z.]+/maps|maps\.google\.|maps\.app\.goo\.gl|goo\.gl/maps|maps\.apple\.com|waze\.com", h)]
    if not (tels or was or mails):
        r.agregar(g, "falta", "No hay ningún botón para contactarte (WhatsApp, llamar o correo).")
        return
    for w in set(was):
        if re.search(r"wa\.me/message/\w+", w):
            r.agregar(g, "ok", "Enlace corto de WhatsApp Business (wa.me/message/…): pruébalo desde tu celular.")
            continue
        m = re.search(r"wa\.me/([^?#]*)", w) or re.search(r"phone=([^&#]*)", w)
        numero = (m.group(1) if m else "").rstrip("/")
        if not numero:
            r.agregar(g, "aviso", "Hay un enlace de WhatsApp sin número.")
        elif not numero.isdigit():
            r.agregar(g, "falta", f"El enlace de WhatsApp «{numero}» no funciona así: van solo dígitos, sin +, espacios ni guiones "
                                  "(ej. wa.me/523300000000).")
        elif len(numero) < 11:
            r.agregar(g, "falta", f"Al WhatsApp «{numero}» le falta la clave del país (52 México, 1 EE. UU.).")
        else:
            r.agregar(g, "ok", f"WhatsApp bien escrito ({numero[:4]}…), {'con' if 'text=' in w else 'sin'} mensaje prellenado.")
    for t in set(tels):
        if "+" not in t:
            r.agregar(g, "aviso", f"El teléfono «{t[4:]}» no lleva clave internacional (+52 / +1): desde otro país no conecta.")
    if tels and not was:
        r.agregar(g, "nota", "Hay botón de llamar pero no de WhatsApp; si atiendes por WhatsApp, agrégalo.")
    if mapas:
        r.agregar(g, "ok", "Tiene enlace de «Cómo llegar».")
    else:
        r.agregar(g, "aviso", "No hay enlace a mapa («Cómo llegar»); si tienes local, agrégalo.")
    vacios = sum(1 for h in hrefs if h.strip() in ("#", "", "javascript:void(0)"))
    if vacios:
        r.agregar(g, "aviso", f"{vacios} enlace(s) que no llevan a ningún lado (href=\"#\"). Conéctalos o quítalos.")


def revisar_textos(p: Pagina, r: Reporte) -> None:
    g = GRUPOS[3]
    texto = p.texto_visible.lower()
    falsos = sorted({m.group(0) for pat in MARCADORES_FALSOS for m in re.finditer(pat, texto)})
    if falsos:
        r.agregar(g, "falta", "Textos de relleno o de ejemplo: " + ", ".join(f"«{f}»" for f in falsos[:6]) + ".")
    pendientes = re.findall(r"\[\s*(?:pendiente|falta|foto|pon|aqu[ií])\b[^\]]*\]", p.html_sin_comentarios, re.I)
    if pendientes:
        r.agregar(g, "falta", f"{len(pendientes)} marca(s) [PENDIENTE] por llenar antes de publicar (las da el dueño; no se "
                              f"inventan), p. ej. «{pendientes[0][:70]}».")
    corchetes = [c for c in re.findall(r"\[[^\]\n]{2,60}\]", p.texto_visible)
                 if not re.match(r"\[\s*(pendiente|falta|foto|pon|aqu)", c, re.I)]
    if corchetes:
        r.agregar(g, "aviso", f"Textos entre corchetes que parecen de plantilla: «{corchetes[0]}». Cámbialos por el dato real.")
    relleno = [f for f in RELLENO if f in texto]
    if relleno:
        r.agregar(g, "aviso", "Frases vacías que suenan a IA: " + ", ".join(f"«{f}»" for f in relleno[:8]) +
                              ". Cámbialas por algo concreto de tu negocio (qué, cuánto, cuándo, dónde).")
    else:
        r.agregar(g, "ok", "No se encontraron las frases de relleno típicas.")
    cifras = re.findall(r"(?:\+|m[aá]s de)\s?\d[\d.,]*\s*k?\s*(?:clientes|pacientes|proyectos|familias|personas|usuarios|ventas|casas|propiedades)"
                        r"|\d{2,3}\s?%\s*(?:de\s+)?(?:satisfacci[oó]n|clientes|[eé]xito|efectividad)"
                        r"|\b[1-5][.,]\d\s*(?:de 5\s*)?estrellas", texto)
    if cifras:
        r.agregar(g, "aviso", "Cifras que hay que poder comprobar: " + ", ".join(f"«{c.strip()}»" for c in cifras[:4]) +
                              ". Si no son reales y medidas, bórralas.")
    if re.search(r"testimonio|rese[ñn]a|opiniones|lo que dicen|clientes felices", texto) or "★" in texto or "⭐" in texto:
        r.agregar(g, "aviso", "Hay reseñas o testimonios: cada uno debe ser real, de un cliente que dio permiso. Nunca inventados.")


def revisar_look_ia(p: Pagina, r: Reporte) -> None:
    g = GRUPOS[4]
    familias = p.familias_usadas()
    cliche = [f for f in familias if any(c in f for c in FUENTES_CLICHE)]
    if cliche:
        r.agregar(g, "aviso", f"Letra muy usada por la IA para «verse premium»: {', '.join(cliche)}. Úsala solo si puedes "
                              "explicar por qué va con ESTE negocio.")
    propias = [f for f in familias if f not in FUENTES_GENERICAS]
    if familias and not propias:
        r.agregar(g, "aviso", f"Toda la página usa letras genéricas ({', '.join(familias[:3])}): el texto no tiene personalidad.")
    gradientes = [v for _, prop, v, _ in p.declaraciones if "gradient(" in v]
    morados = [v for v in gradientes if any(es_morado(c) for c in colores_en(v))]
    if morados:
        r.agregar(g, "aviso", f"{len(morados)} degradado(s) morado/violeta: es el sello más reconocible del «look de IA».")
    if len(gradientes) > 4:
        r.agregar(g, "aviso", f"{len(gradientes)} degradados en la página: con uno (o ninguno) se ve más hecho a propósito.")
    if any("text" in v for _, v in _decls(p, "background-clip") + _decls(p, "-webkit-background-clip")):
        r.agregar(g, "aviso", "Texto pintado con degradado: otro tic típico de la IA.")
    brillos = _contar_brillos(p)
    if brillos:
        r.agregar(g, "aviso", f"{brillos} resplandor(es) de color tipo neón (sombra sin desplazamiento): profundidad con sombras sobrias, no con brillo.")
    vidrio = sum(1 for _, v in _decls(p, "backdrop-filter") + _decls(p, "-webkit-backdrop-filter") if "blur" in v)
    if vidrio >= 3:
        r.agregar(g, "aviso", f"Efecto de vidrio esmerilado en {vidrio} lugares: úsalo en uno, si acaso.")
    fondos = [v for _, prop, v, _ in p.declaraciones if prop in ("background", "background-color")]
    if any(es_crema(c) for v in fondos for c in colores_en(v)):
        r.agregar(g, "aviso", "Fondo crema/beige: con letra serif y acento dorado o terracota es la paleta «de lujo» que sale sola. "
                              "¿Sale de algo real de tu negocio?")
    epigrafes = p.contar_epigrafes()
    if epigrafes > 2:
        r.agregar(g, "aviso", f"{epigrafes} etiquetitas en MAYÚSCULAS espaciadas arriba de los títulos: repiten el mismo ritmo "
                              "en toda la página. Déjalas solo donde ubican algo de verdad (ej. «Paso 2 de 4»).")
    numeros = sum(1 for t in p.nodos_texto if re.fullmatch(r"0[1-9]\.?", t))
    if numeros >= 3:
        r.agregar(g, "aviso", f"Números decorativos 01, 02, 03… ({numeros}): úsalos solo si es un proceso real, en orden.")
    emojis = len(EMOJI.findall(p.texto_visible))
    if emojis > 3:
        r.agregar(g, "aviso", f"{emojis} emojis en la página: si hacen de íconos, se ven distinto en cada teléfono y gritan «plantilla».")
    tarjetas = p.contar_tarjetas()
    if tarjetas >= 6:
        r.agregar(g, "aviso", f"{tarjetas} tarjetas (cajitas con sombra): agrupa con líneas o espacio; tarjeta solo si de verdad sobresale.")
    radios = {v.strip() for _, v in _decls(p, "border-radius")} - {"0", "0px", "50%", "999px", "9999px", "100px", "inherit"}
    if len(radios) > 3:
        r.agregar(g, "aviso", f"{len(radios)} redondeos de esquina distintos ({', '.join(sorted(radios)[:5])}): elige una escala corta y respétala.")
    franjas = [v for _, prop, v, _ in p.declaraciones if prop in ("border-left", "border-inline-start")
               and (m := re.match(r"\s*(\d+)px", v)) and int(m.group(1)) >= 3]
    if len(franjas) >= 2:
        r.agregar(g, "aviso", "Franja de color al costado de las tarjetas: otro tic de plantilla de IA.")
    fotos_banco = sorted({b for i in p.imagenes for b in BANCOS_DE_FOTOS if b in i["src"].lower()})
    if fotos_banco:
        r.agregar(g, "aviso", f"Fotos de banco ({', '.join(fotos_banco)}): ¿son de tu negocio? Si no, cámbialas por fotos reales.")
    if not [h for h in r.hallazgos if h["grupo"] == g]:
        r.agregar(g, "ok", "No se encontraron los rasgos típicos del «look de IA» que esta revisión sabe medir.")


def _contar_brillos(p: Pagina) -> int:
    total = 0
    for _, prop, v, _ in p.declaraciones:
        if prop not in ("box-shadow", "text-shadow", "filter"):
            continue
        for sombra in re.split(r",(?![^(]*\))", v):
            nums = re.findall(r"(-?[\d.]+)(px|rem|em)?", re.sub(r"(rgba?|hsla?)\([^)]*\)|#[0-9a-fA-F]{3,8}", "", sombra))
            if len(nums) >= 3 and float(nums[0][0]) == 0 and float(nums[1][0]) == 0:
                blur = float(nums[2][0]) * (16 if nums[2][1] in ("rem", "em") else 1)
                if blur >= 12 and any(es_saturado(c) for c in colores_en(sombra)):
                    total += 1
    return total


def revisar_movimiento(p: Pagina, r: Reporte) -> None:
    g = GRUPOS[5]
    animado = [v for _, prop, v, _ in p.declaraciones if prop.startswith("animation") or prop.startswith("transition")]
    if not animado:
        r.agregar(g, "nota", "La página no tiene animaciones. Está bien si así se decidió; una entrada sobria al bajar puede sumar.")
        return
    if "prefers-reduced-motion" in p.css_sin_comentarios:
        r.agregar(g, "ok", "Respeta a quien pidió «reducir movimiento» en su teléfono (prefers-reduced-motion).")
    else:
        r.agregar(g, "falta", "Falta `@media (prefers-reduced-motion: reduce)`: a algunas personas el movimiento las marea.")
    if re.search(r"scale\(\s*0(\.0+)?\s*\)", p.css_completo):
        r.agregar(g, "aviso", "Algo aparece creciendo desde la nada (`scale(0)`): se ve de caricatura. Que solo se desvanezca o suba un poco.")
    if re.search(r"ease-in(?!-out)", " ".join(animado)):
        r.agregar(g, "aviso", "Animaciones con `ease-in`: empiezan despacio y la página se siente pesada al tocarla. "
                              "Usa una curva que frene al final (ease-out).")
    medidas = r"\b(width|height|top|left|right|bottom|margin|padding)\b"
    caras = [v for _, prop, v, _ in p.declaraciones if prop in ("transition", "transition-property") and re.search(medidas, v)]
    caras += [prop for _, prop, _, en in p.declaraciones if any("@keyframes" in a for a in en) and re.fullmatch(medidas, prop)]
    if caras:
        r.agregar(g, "aviso", "Se animan medidas (width, height, margin…): eso traba el celular. Anima solo transform y opacity.")
    todo = sum(1 for _, prop, v, _ in p.declaraciones if prop == "transition" and re.match(r"\s*all\b", v))
    if todo:
        r.agregar(g, "aviso", f"{todo} regla(s) con `transition: all`: anima hasta lo que no debe. Nombra solo lo que cambia.")
    infinitas = sum(1 for v in animado if "infinite" in v)
    if infinitas:
        r.agregar(g, "aviso", f"{infinitas} animación(es) que no paran nunca: ¿explican algo? Si no, quítalas.")
    lentas = [v for v in animado if any(float(n) > 1.2 for n in re.findall(r"(\d*\.?\d+)s\b", v))
              or any(float(n) > 1200 for n in re.findall(r"(\d+)ms\b", v))]
    if lentas:
        r.agregar(g, "aviso", f"{len(lentas)} animación(es) de más de 1.2 s: la gente no espera, se siente lenta.")
    todo_js = " ".join(p.scripts_src).lower()
    if any(k in todo_js for k in ("locomotive", "lenis", "fullpage")):
        r.agregar(g, "aviso", "Una librería cambia cómo se mueve la página al bajar: en celulares viejos se siente trabada.")
    ocultos = p.reglas_que_ocultan()
    if ocultos:
        r.agregar(g, "aviso", f"El contenido de «{ocultos[0]}» empieza invisible (opacity: 0) sin depender de JavaScript: si el "
                              "script falla, la página se ve vacía. Actívalo con una clase `js` en `<html>`.")


def revisar_accesibilidad(p: Pagina, r: Reporte) -> None:
    g = GRUPOS[6]
    sin_alt = [i for i in p.imagenes if i.get("alt") is None]
    if sin_alt:
        r.agregar(g, "falta", f"{len(sin_alt)} imagen(es) sin texto alternativo (alt): quien no ve la foto no sabe qué es.")
    elif p.imagenes:
        r.agregar(g, "ok", "Todas las imágenes tienen texto alternativo.")
    if p.h1 == 0:
        r.agregar(g, "falta", "No hay un título principal (h1).")
    elif p.h1 > 1:
        r.agregar(g, "aviso", f"Hay {p.h1} títulos principales (h1): debe haber uno.")
    mudos = [a for a in p.enlaces + p.botones if not a["texto"].strip() and not a.get("aria-label") and not a.get("title")]
    if mudos:
        r.agregar(g, "aviso", f"{len(mudos)} botón(es) o enlace(s) sin texto: agrega aria-label (ej. «Escribir por WhatsApp»).")
    if re.search(r"outline\s*:\s*(none|0)\b", p.css_completo) and ":focus-visible" not in p.css_completo:
        r.agregar(g, "aviso", "Se quitó el contorno de foco y no hay `:focus-visible`: quien navega con teclado se pierde.")
    sin_etiqueta = p.campos_sin_etiqueta()
    if sin_etiqueta:
        r.agregar(g, "aviso", f"{sin_etiqueta} campo(s) de formulario sin etiqueta (label): el texto de ejemplo desaparece al escribir.")
    r.agregar(g, "nota", "El contraste de colores no se mide aquí: revisa a pleno sol en tu celular que todo se lea.")


def revisar_publicar(p: Pagina, r: Reporte) -> None:
    g = GRUPOS[7]
    textos_enlaces = " ".join((a["href"] + " " + a["texto"]).lower() for a in p.enlaces)
    hay_privacidad = re.search(r"privacidad|privacy|aviso-de-priv", textos_enlaces)
    hay_terminos = re.search(r"t[eé]rminos|condiciones|terms", textos_enlaces)
    campos = p.campos_formulario()
    if campos:
        r.agregar(g, "nota", "Tu página pide estos datos: " + ", ".join(campos[:10]) + ". Pide solo lo indispensable.")
        if not hay_privacidad:
            r.agregar(g, "falta", "Pides datos y no hay enlace a un aviso de privacidad. Ponlo junto al botón de enviar.")
        sensibles = sorted({m.group(0).lower() for c in campos for m in DATOS_SENSIBLES.finditer(c)})
        if sensibles:
            r.agregar(g, "aviso", "Pides datos delicados o de identificación (" + ", ".join(sensibles) + "): casi nunca hacen falta "
                                  "en una página; si los necesitas, pregúntale a un profesional cómo pedirlos.")
        if re.search(r"suscr[ií]bete|newsletter|bolet[ií]n|promociones|ofertas", p.texto_visible.lower()):
            r.agregar(g, "aviso", "Juntas correos o teléfonos para promociones: cada envío debe traer cómo darse de baja y quién lo manda.")
    for roto in p.enlaces_locales_rotos(r"privacidad|privacy|t[eé]rminos|condiciones|terms|cookies"):
        r.agregar(g, "falta", f"El enlace «{roto['texto'].strip() or roto['href']}» lleva a {roto['href']}, que todavía no "
                              "existe: créalo con el texto que te dé tu abogado antes de publicar.")
    if hay_privacidad:
        r.agregar(g, "ok", "Hay enlace al aviso de privacidad (el documento lo prepara o revisa tu abogado).")
    elif not campos:
        r.agregar(g, "aviso", "No hay enlace a aviso de privacidad. Aunque no tengas formulario, si recibes pedidos por WhatsApp o "
                              "usas analítica, tu negocio maneja datos personales.")
    todo_js = (" ".join(p.scripts_src) + " " + p.js_inline).lower()
    rastreo = sorted({n for k, n in RASTREADORES.items() if k in todo_js})
    if rastreo:
        r.agregar(g, "aviso", "Herramientas que registran a tus visitantes: " + "; ".join(rastreo) + ". Menciónalas en tu aviso "
                              "de privacidad, evalúa un aviso de cookies y apaga la grabación de sesiones si no la usas.")
    if PALABRAS_DE_VENTA.search(p.texto_visible) and not hay_terminos:
        r.agregar(g, "aviso", "Hablas de compras, pagos, reservas o anticipos y no hay términos y condiciones (qué incluye, "
                              "cancelaciones, reembolsos). Pídeselos a un profesional.")
    if re.search(r"\$\s?\d", p.texto_visible):
        if re.search(r"\bmxn\b|\busd\b|\biva\b|pesos|d[oó]lares", p.texto_visible.lower()):
            r.agregar(g, "ok", "Los precios aclaran moneda o impuestos.")
        else:
            r.agregar(g, "aviso", "Hay precios sin aclarar moneda (MXN / USD) ni si incluyen impuestos (en México: precio total con IVA).")
    if any("encrypted-tbn" in i["src"] or "gstatic.com/images" in i["src"] for i in p.imagenes):
        r.agregar(g, "falta", "Hay imágenes sacadas de Google Imágenes: casi seguro tienen dueño. Cámbialas por fotos tuyas o con licencia.")
    if p.fuentes_google()[0]:
        r.agregar(g, "nota", "Las letras vienen de Google Fonts: su licencia permite uso comercial. Si tienes visitas de Europa, "
                             "conviene alojarlas en tu propio servidor.")
    r.agregar(g, "nota", "Esto es orientación, no asesoría legal. Lo que dice la ley en tu caso lo confirma un abogado.")


def revisar(ruta: Path) -> "Reporte":
    p = cargar_pagina(Path(ruta))
    r = Reporte()
    for paso in (revisar_celular, revisar_velocidad, revisar_contacto, revisar_textos, revisar_look_ia,
                 revisar_movimiento, revisar_accesibilidad, revisar_publicar):
        paso(p, r)
    return r


def a_markdown(r: "Reporte", nombre: str) -> str:
    c = r.conteo()
    lineas = [f"# Revisión automática · {nombre}", "",
              f"{ICONOS['falta']} {c['falta']} por arreglar · {ICONOS['aviso']} {c['aviso']} por revisar · "
              f"{ICONOS['nota']} {c['nota']} notas · {ICONOS['ok']} {c['ok']} bien", "",
              "_Encuentra señales en el código; no sustituye abrir la página en tu celular ni la revisión de un profesional._"]
    orden = {"falta": 0, "aviso": 1, "nota": 2, "ok": 3}
    for grupo in GRUPOS:
        del_grupo = sorted((h for h in r.hallazgos if h["grupo"] == grupo), key=lambda h: orden[h["nivel"]])
        if del_grupo:
            lineas += ["", f"## {grupo}"] + [f"- {ICONOS[h['nivel']]} {h['mensaje']}" for h in del_grupo]
    return "\n".join(lineas) + "\n"


def main(argv: List[str]) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    args = [a for a in argv if not a.startswith("--")]
    if len(args) != 1:
        print(__doc__)
        return 2
    ruta = Path(args[0])
    if not ruta.is_file():
        print(f"No encuentro el archivo «{ruta}». Revisa la ruta y vuelve a intentar.")
        return 1
    r = revisar(ruta)
    if "--json" in argv:
        print(json.dumps({"archivo": ruta.name, "conteo": r.conteo(), "hallazgos": r.hallazgos}, ensure_ascii=False, indent=2))
    else:
        print(a_markdown(r, ruta.name))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
