#!/usr/bin/env python3
"""Arma la presentación final: toma el motor de plantilla/presentacion.html y le pone tus láminas.

Uso:
    python3 armar.py laminas.html --titulo "Plan dental para empresas" --look cine --salida presentacion.html
    python3 armar.py laminas.html --titulo "…" --look marca --colores "#0e1f3a,#ffffff,#ffb000" --salida …

laminas.html lleva solo las <section class="lamina" …> (como las de la plantilla). Si una lámina usa una foto
guardada en tu computadora (<img src="fotos/fachada.jpg">), la foto se mete dentro del HTML para que el
archivo funcione solo, sin carpetas aparte.

--colores (solo con --look marca): fondo, texto y acento, separados por comas. El texto suave y el color del
texto sobre el acento se calculan solos.

Solo usa Python 3 (sin instalar nada).
"""
from __future__ import annotations

import argparse
import base64
import html
import mimetypes
import re
import sys
from pathlib import Path

PLANTILLA = Path(__file__).resolve().parent.parent / "plantilla" / "presentacion.html"
LOOKS = ("cine", "estudio", "bosque", "marca")
MAX_FOTO = 8_000_000


def hex_a_rgb(color: str) -> tuple[int, int, int]:
    limpio = color.strip().lstrip("#")
    if len(limpio) == 3:
        limpio = "".join(c * 2 for c in limpio)
    if not re.fullmatch(r"[0-9a-fA-F]{6}", limpio):
        raise ValueError(f"«{color}» no es un color como #1a2b3c")
    return int(limpio[0:2], 16), int(limpio[2:4], 16), int(limpio[4:6], 16)


def mezclar(a: str, b: str, peso_a: float) -> str:
    ra, rb = hex_a_rgb(a), hex_a_rgb(b)
    return "#" + "".join(f"{round(x * peso_a + y * (1 - peso_a)):02x}" for x, y in zip(ra, rb))


def luminancia(color: str) -> float:
    canales = []
    for c in hex_a_rgb(color):
        v = c / 255
        canales.append(v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4)
    return 0.2126 * canales[0] + 0.7152 * canales[1] + 0.0722 * canales[2]


def estilo_marca(colores: str) -> str:
    partes = [c.strip() for c in colores.split(",") if c.strip()]
    if len(partes) != 3:
        raise ValueError("--colores lleva tres colores: fondo, texto y acento (ej. \"#0e1f3a,#ffffff,#ffb000\")")
    fondo, texto, acento = (f"#{c.lstrip('#')}" for c in partes)
    for c in (fondo, texto, acento):
        hex_a_rgb(c)
    suave = mezclar(texto, fondo, 0.62)
    sobre = "#111216" if luminancia(acento) > 0.35 else "#ffffff"
    return f"--fondo:{fondo};--texto:{texto};--suave:{suave};--acento:{acento};--sobre-acento:{sobre}"


def incrustar_fotos(laminas: str, carpeta: Path) -> tuple[str, list[str]]:
    avisos: list[str] = []

    def cambiar(m: re.Match[str]) -> str:
        src = m.group(2)
        if src.startswith(("data:", "http://", "https://")) or not src.strip():
            return m.group(0)
        ruta = (carpeta / html.unescape(src)).resolve()
        if not ruta.is_file():
            avisos.append(f"No encontré la foto «{src}»; esa lámina se verá sin foto.")
            return m.group(0)
        if ruta.stat().st_size > MAX_FOTO:
            avisos.append(f"La foto «{src}» pesa más de 8 MB; redúcela para que el archivo no quede enorme.")
        tipo = mimetypes.guess_type(ruta.name)[0] or "image/jpeg"
        datos = base64.b64encode(ruta.read_bytes()).decode("ascii")
        return f"{m.group(1)}data:{tipo};base64,{datos}{m.group(3)}"

    nuevo = re.sub(r'(<img\b[^>]*?\bsrc=")([^"]*)(")', cambiar, laminas)
    return nuevo, avisos


def armar(laminas: str, titulo: str, look: str, colores: str | None, carpeta: Path) -> tuple[str, list[str]]:
    plantilla = PLANTILLA.read_text(encoding="utf-8")
    inicio = re.search(r'<main id="escenario"[^>]*>', plantilla)
    fin = plantilla.find("</main>")
    if not inicio or fin < 0:
        raise ValueError("La plantilla no tiene <main id=\"escenario\">: vuelve a descargar la skill.")
    if "<section" not in laminas or 'class="lamina' not in laminas:
        raise ValueError("El archivo de láminas no trae ninguna <section class=\"lamina\">.")
    if "data-ejemplo" in laminas:
        raise ValueError("Tus láminas todavía traen data-ejemplo: son las de la plantilla. Escríbelas de nuevo.")
    laminas, avisos = incrustar_fotos(laminas, carpeta)
    salida = plantilla[: inicio.end()] + "\n" + laminas.strip() + "\n" + plantilla[fin:]
    salida = re.sub(r"<title>[^<]*</title>", lambda _: f"<title>{html.escape(titulo)}</title>", salida, count=1)
    cuerpo = f'<body data-look="{look}"'
    if look == "marca":
        if not colores:
            raise ValueError("Con --look marca pon también --colores \"#fondo,#texto,#acento\".")
        cuerpo += f' style="{estilo_marca(colores)}"'
    salida = salida.replace('<body data-look="cine"', cuerpo, 1)
    return salida, avisos


def main() -> None:
    p = argparse.ArgumentParser(description="Arma la presentación con el motor de la plantilla y tus láminas.")
    p.add_argument("laminas", help="archivo con las <section class=\"lamina\">")
    p.add_argument("--titulo", required=True, help="nombre de la presentación (se ve en la pestaña del navegador)")
    p.add_argument("--look", choices=LOOKS, default="cine", help="estilo: cine, estudio, bosque o marca")
    p.add_argument("--colores", help="solo con --look marca: \"#fondo,#texto,#acento\"")
    p.add_argument("--salida", required=True, help="archivo .html que se va a crear")
    a = p.parse_args()
    origen = Path(a.laminas)
    try:
        texto, avisos = armar(origen.read_text(encoding="utf-8"), a.titulo, a.look, a.colores, origen.resolve().parent)
    except (OSError, ValueError) as e:
        print(f"No se pudo armar: {e}")
        sys.exit(1)
    destino = Path(a.salida)
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(texto, encoding="utf-8")
    for aviso in avisos:
        print("⚠ " + aviso)
    print(f"Listo: {destino} ({len(texto.encode('utf-8')) / 1000:.0f} KB). Revísala con: python3 revisar.py {destino}")


if __name__ == "__main__":
    main()
