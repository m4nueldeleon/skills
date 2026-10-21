"""Lector de páginas HTML para revisar_pagina.py (solo biblioteca estándar).

Convierte un archivo HTML, más las hojas de estilo y scripts LOCALES que enlaza, en datos
simples: textos visibles, enlaces, imágenes, campos de formulario y declaraciones CSS.
No descarga nada de internet.
"""
import re
from html.parser import HTMLParser
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import parse_qs, unquote, urlparse

IGNORAR_TEXTO = {"script", "style", "noscript", "template", "svg", "head", "title"}
CAMPOS = {"input", "textarea", "select"}
TIPOS_SIN_DATO = {"hidden", "submit", "button", "reset", "image"}


def es_local(ruta: str) -> bool:
    return bool(ruta) and not re.match(r"^(?:[a-z][a-z0-9+.-]*:|//|#)", ruta, re.I)


def reglas_css(css: str) -> List[Tuple[str, str, Tuple[str, ...]]]:
    """Separa el CSS en (selector, bloque de declaraciones, reglas @ que lo contienen)."""
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    reglas, pila, buf = [], [], []
    for ch in css:
        if ch == "{":
            pila.append("".join(buf).strip())
            buf = []
        elif ch == "}":
            if pila:
                prelude = pila.pop()
                if not prelude.startswith("@"):
                    reglas.append((prelude, "".join(buf).strip(), tuple(x for x in pila if x.startswith("@"))))
            buf = []
        else:
            buf.append(ch)
    return reglas


def declaraciones_de(bloque: str) -> List[Tuple[str, str]]:
    salida = []
    for parte in re.split(r";(?![^(]*\))", bloque):
        if ":" in parte:
            prop, valor = parte.split(":", 1)
            salida.append((prop.strip().lower(), valor.strip()))
    return salida


class _Parser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.pila: List[str] = []
        self.meta: Dict[str, str] = {}
        self.lang = ""
        self.estilos: List[str] = []
        self.estilos_inline: List[str] = []
        self.js_inline: List[str] = []
        self.scripts_src: List[str] = []
        self.hojas: List[str] = []
        self.imagenes: List[Dict[str, Optional[str]]] = []
        self.enlaces: List[Dict[str, str]] = []
        self.botones: List[Dict[str, str]] = []
        self.abiertos: List[Dict[str, str]] = []
        self.textos: List[str] = []
        self.clases: List[List[str]] = []
        self.campos: List[Dict[str, str]] = []
        self.labels_for: set = set()
        self.label_abierto = 0
        self.textos_label: List[str] = []
        self.h1 = 0
        self.secciones = 0
        self.h2 = 0
        self.videos_autoplay = 0
        self._en_style = False
        self._en_script = False

    def handle_starttag(self, tag: str, attrs: list) -> None:
        a = {k.lower(): (v if v is not None else "") for k, v in attrs}
        if tag not in ("meta", "link", "img", "input", "br", "hr", "source", "area", "base", "col", "embed", "wbr"):
            self.pila.append(tag)
        if a.get("class"):
            self.clases.append(a["class"].split())
        if a.get("style"):
            self.estilos_inline.append(a["style"])
        self._registrar(tag, a)

    def handle_startendtag(self, tag: str, attrs: list) -> None:
        a = {k.lower(): (v if v is not None else "") for k, v in attrs}
        if a.get("class"):
            self.clases.append(a["class"].split())
        if a.get("style"):
            self.estilos_inline.append(a["style"])
        self._registrar(tag, a)
        self._en_script = self._en_style = False

    def _registrar(self, tag: str, a: Dict[str, str]) -> None:
        if tag == "html":
            self.lang = a.get("lang", "")
        elif tag == "meta" and a.get("name"):
            self.meta[a["name"].lower()] = a.get("content", "")
        elif tag == "link" and "stylesheet" in a.get("rel", "").lower():
            self.hojas.append(a.get("href", ""))
        elif tag == "script":
            self._en_script = True
            if a.get("src"):
                self.scripts_src.append(a["src"])
        elif tag == "style":
            self._en_style = True
        elif tag == "img":
            self.imagenes.append({"src": a.get("src", ""), "alt": a.get("alt") if "alt" in a else None,
                                  "width": a.get("width"), "height": a.get("height"), "loading": a.get("loading")})
        elif tag == "video" and "autoplay" in a:
            self.videos_autoplay += 1
        elif tag in ("a", "button"):
            item = {"href": a.get("href", ""), "texto": "", "aria-label": a.get("aria-label", ""),
                    "title": a.get("title", ""), "_tag": tag}
            self.abiertos.append(item)
            (self.enlaces if tag == "a" else self.botones).append(item)
        elif tag == "label":
            self.label_abierto += 1
            if a.get("for"):
                self.labels_for.add(a["for"])
        elif tag in CAMPOS and a.get("type", "text").lower() not in TIPOS_SIN_DATO:
            self.campos.append({"tipo": a.get("type", tag), "name": a.get("name", ""), "id": a.get("id", ""),
                                "placeholder": a.get("placeholder", ""), "aria-label": a.get("aria-label", ""),
                                "envuelto": "1" if self.label_abierto else ""})
        elif tag == "h1":
            self.h1 += 1
        elif tag == "h2":
            self.h2 += 1
        elif tag == "section":
            self.secciones += 1

    def handle_endtag(self, tag: str) -> None:
        if tag == "style":
            self._en_style = False
        elif tag == "script":
            self._en_script = False
        elif tag == "label":
            self.label_abierto = max(0, self.label_abierto - 1)
        if tag in ("a", "button"):
            for i in range(len(self.abiertos) - 1, -1, -1):
                if self.abiertos[i]["_tag"] == tag:
                    self.abiertos.pop(i)
                    break
        if tag in self.pila:
            while self.pila and self.pila.pop() != tag:
                pass

    def handle_data(self, data: str) -> None:
        if self._en_style:
            self.estilos.append(data)
            return
        if self._en_script:
            self.js_inline.append(data)
            return
        if any(t in IGNORAR_TEXTO for t in self.pila):
            return
        limpio = data.strip()
        if limpio:
            self.textos.append(limpio)
            if self.label_abierto:
                self.textos_label.append(limpio)
        for item in self.abiertos:
            item["texto"] += data


class Pagina:
    """Datos de una página listos para revisar."""

    def __init__(self, ruta: Path) -> None:
        html = ruta.read_text(encoding="utf-8", errors="replace")
        self.parser = _Parser()
        self.parser.feed(html)
        q = self.parser
        base = ruta.parent
        css_local, js_local, self.imagenes_locales = [], [], []
        self.bytes_totales = len(html.encode("utf-8"))
        for href in q.hojas:
            f = base / unquote(href.split("?")[0]) if es_local(href) else None
            if f and f.is_file():
                texto = f.read_text(encoding="utf-8", errors="replace")
                css_local.append(texto)
                self.bytes_totales += f.stat().st_size
        for src in q.scripts_src:
            f = base / unquote(src.split("?")[0]) if es_local(src) else None
            if f and f.is_file():
                js_local.append(f.read_text(encoding="utf-8", errors="replace"))
                self.bytes_totales += f.stat().st_size
        for img in q.imagenes:
            src = img["src"] or ""
            f = base / unquote(src.split("?")[0]) if es_local(src) else None
            if f and f.is_file():
                self.imagenes_locales.append((f.name, f.stat().st_size))
        self.bytes_data_uri = sum(len(m) for m in re.findall(r"data:image/[^\"')\s]+", html))
        self.bytes_totales -= self.bytes_data_uri
        self.base = base
        self.html_sin_comentarios = re.sub(r"<!--.*?-->", "", html, flags=re.S)
        self.css_completo = "\n".join(q.estilos + css_local)
        self.css_sin_comentarios = re.sub(r"/\*.*?\*/", "", self.css_completo, flags=re.S)
        self.js_inline = "\n".join(q.js_inline + js_local)
        self.meta, self.lang = q.meta, q.lang
        self.scripts_src, self.hojas_externas = q.scripts_src, [h for h in q.hojas if not es_local(h)]
        self.imagenes, self.enlaces, self.botones = q.imagenes, q.enlaces, q.botones
        self.texto_visible = "\n".join(q.textos)
        self.nodos_texto = q.textos
        self.h1, self.videos_autoplay = q.h1, q.videos_autoplay
        self.secciones = q.secciones or q.h2
        self.reglas = reglas_css(self.css_completo) + [("[style]", s, ()) for s in q.estilos_inline]
        self.variables = self._variables()
        self.declaraciones = [(sel, prop, self._resolver(val), en)
                              for sel, bloque, en in self.reglas for prop, val in declaraciones_de(bloque)]

    def _variables(self) -> Dict[str, str]:
        variables = {}
        for _, bloque, _ in self.reglas:
            for prop, val in declaraciones_de(bloque):
                if prop.startswith("--"):
                    variables[prop] = val
        return variables

    def _resolver(self, valor: str, profundidad: int = 0) -> str:
        if "var(" not in valor or profundidad > 5:
            return valor
        nuevo = re.sub(r"var\(\s*(--[\w-]+)\s*(?:,\s*([^)]*))?\)",
                       lambda m: self.variables.get(m.group(1), m.group(2) or ""), valor)
        return self._resolver(nuevo, profundidad + 1)

    def fuentes_google(self) -> Tuple[List[str], int]:
        familias, pesos = [], 0
        urls = self.hojas_externas + re.findall(r"@import\s+url\(['\"]?([^'\")]+)", self.css_completo)
        for url in urls:
            if "fonts.googleapis.com" not in url:
                continue
            for fam in parse_qs(urlparse(url).query).get("family", []):
                nombre, _, ejes = fam.partition(":")
                familias.append(nombre.replace("+", " "))
                valores = ejes.split("@", 1)[1] if "@" in ejes else ""
                pesos += max(1, len([v for v in valores.split(";") if v]))
        return familias, pesos

    def familias_usadas(self) -> List[str]:
        vistas = []
        for _, prop, val, _ in self.declaraciones:
            if prop in ("font-family", "font"):
                primera = val.split(",")[0].strip().strip("'\"").lower()
                if prop == "font":
                    m = re.search(r"['\"]([^'\"]+)['\"]", val)
                    primera = m.group(1).lower() if m else ""
                if primera and primera not in vistas and not primera.startswith("var("):
                    vistas.append(primera)
        for fam in self.fuentes_google()[0]:
            if fam.lower() not in vistas:
                vistas.append(fam.lower())
        return vistas

    def contar_tarjetas(self) -> int:
        """Elementos cuya clase ES una tarjeta («card», «product-card», «tarjeta»), no sus partes («card-title»)."""
        patron = re.compile(r"(?:[\w-]*[-_])?(?:card|tarjeta)s?", re.I)
        return sum(1 for clases in self.parser.clases if any(patron.fullmatch(c) for c in clases))

    def enlaces_locales_rotos(self, patron: str) -> List[Dict[str, str]]:
        """Enlaces cuyo texto o destino coincide con el patrón y apuntan a un archivo local que no existe."""
        rotos = []
        for a in self.enlaces:
            href = a["href"].split("#")[0].split("?")[0]
            if href and es_local(href) and re.search(patron, (href + " " + a["texto"]).lower()):
                if not (self.base / unquote(href)).exists():
                    rotos.append(a)
        return rotos

    def contar_epigrafes(self) -> int:
        clases = set()
        for sel, bloque, en in self.reglas:
            decl = dict(declaraciones_de(bloque))
            if decl.get("text-transform") == "uppercase" and "letter-spacing" in decl:
                tamano = decl.get("font-size", "")
                if re.search(r"(\d+(\.\d+)?)(px|rem|em)", tamano) and _tamano_px(tamano) > 20:
                    continue
                clases.update(re.findall(r"\.([\w-]+)", sel))
        return sum(1 for c in self.parser.clases if clases.intersection(c))

    def reglas_que_ocultan(self) -> List[str]:
        exentos = (".js", "html.", "[data-", ":not(", ".is-", ":hover", "::", "hidden", "menu", "modal",
                   "dialog", "tooltip", ".visible", ".activo", ".active", ".open")
        salida = []
        for sel, bloque, en in self.reglas:
            if any("@keyframes" in a for a in en) or "prefers-reduced-motion" in " ".join(en):
                continue
            decl = dict(declaraciones_de(bloque))
            if re.fullmatch(r"0(\.0+)?", decl.get("opacity", "").strip()) and not any(x in sel for x in exentos):
                clases = re.findall(r"\.([\w-]+)", sel)
                if clases and sum(1 for c in self.parser.clases if clases[-1] in c) >= 3:
                    salida.append(sel)
        return salida

    def campos_formulario(self) -> List[str]:
        """Campos que piden un dato escrito; las casillas y opciones (checkbox, radio) no piden datos por sí solas."""
        return [c["aria-label"] or c["placeholder"] or c["name"] or c["id"] or c["tipo"] for c in self.parser.campos
                if c["tipo"].lower() not in ("checkbox", "radio")]

    def campos_sin_etiqueta(self) -> int:
        return sum(1 for c in self.parser.campos
                   if not c["envuelto"] and not c["aria-label"] and c["id"] not in self.parser.labels_for)


def _tamano_px(valor: str) -> float:
    m = re.search(r"(\d+(?:\.\d+)?)(px|rem|em)", valor)
    if not m:
        return 0.0
    return float(m.group(1)) * (16 if m.group(2) in ("rem", "em") else 1)


def cargar_pagina(ruta: Path) -> Pagina:
    return Pagina(ruta)
