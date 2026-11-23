"""Tipografías que viajan con la skill (todas con licencia SIL OFL 1.1, ver fuentes/*/OFL.txt).

Cada familia tiene tres papeles: `titulo` (el gancho), `texto` (el cuerpo) y `fuerte`
(listas, @usuario, botón). Oswald solo trae titular: su texto sale de Inter.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

CARPETA = Path(__file__).resolve().parents[2] / "fuentes"

FAMILIAS: dict[str, dict[str, str]] = {
    "archivo": {
        "titulo": "Archivo/Archivo-ExtraBold.ttf",
        "texto": "Archivo/Archivo-Medium.ttf",
        "fuerte": "Archivo/Archivo-ExtraBold.ttf",
    },
    "inter": {
        "titulo": "Inter/Inter-ExtraBold.ttf",
        "texto": "Inter/Inter-Regular.ttf",
        "fuerte": "Inter/Inter-SemiBold.ttf",
    },
    "montserrat": {
        "titulo": "Montserrat/Montserrat-ExtraBold.ttf",
        "texto": "Montserrat/Montserrat-Medium.ttf",
        "fuerte": "Montserrat/Montserrat-ExtraBold.ttf",
    },
    "oswald": {
        "titulo": "Oswald/Oswald-SemiBold.ttf",
        "texto": "Inter/Inter-Regular.ttf",
        "fuerte": "Inter/Inter-SemiBold.ttf",
    },
}

POR_ESTILO: dict[str, tuple[str, str]] = {
    "claro": ("archivo", "inter"),
    "oscuro": ("inter", "inter"),
    "foto": ("oswald", "inter"),
}


@dataclass(frozen=True)
class Fuentes:
    titulo: Path
    texto: Path
    fuerte: Path


def _ruta(valor: str, papel: str, base: Path) -> Path:
    """Una familia de la lista o la ruta a un .ttf/.otf propio de la marca."""
    nombre = valor.strip().lower()
    if nombre in FAMILIAS:
        return CARPETA / FAMILIAS[nombre][papel]
    propia = (base / valor).expanduser()
    if propia.suffix.lower() in (".ttf", ".otf") and propia.is_file():
        return propia
    opciones = ", ".join(FAMILIAS)
    raise ValueError(f"No conozco la fuente «{valor}». Usa una de estas: {opciones}, o la ruta a un .ttf")


def elegir(pedido: dict | None, estilo: str, base: Path) -> Fuentes:
    """Resuelve las rutas de las tres fuentes desde el campo `fuentes` del carrusel.json."""
    pedido = pedido or {}
    titulo_def, texto_def = POR_ESTILO[estilo]
    titulo = str(pedido.get("titulo") or titulo_def)
    texto = str(pedido.get("texto") or texto_def)
    return Fuentes(
        titulo=_ruta(titulo, "titulo", base),
        texto=_ruta(texto, "texto", base),
        fuerte=_ruta(texto, "fuerte", base),
    )
