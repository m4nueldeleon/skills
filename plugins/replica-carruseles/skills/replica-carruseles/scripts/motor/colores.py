"""Colores: leer hex, mezclar y asegurar contraste legible (WCAG).

Todo es puro (sin Pillow) para que también lo use el respaldo en HTML.
"""
from __future__ import annotations

import re

_HEX = re.compile(r"^#?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$")
BLANCO = "#FFFFFF"
NEGRO = "#111214"


def es_hex(valor: object) -> bool:
    return isinstance(valor, str) and bool(_HEX.match(valor.strip()))


def normalizar(valor: str) -> str:
    """'#0e7' o '0E7C7B' -> '#0E7C7B'. Lanza ValueError si no es un color."""
    if not es_hex(valor):
        raise ValueError(f"«{valor}» no es un color en hexadecimal (ejemplo: #0E7C7B)")
    limpio = valor.strip().lstrip("#")
    if len(limpio) == 3:
        limpio = "".join(c * 2 for c in limpio)
    return "#" + limpio.upper()


def a_rgb(color: str) -> tuple[int, int, int]:
    c = normalizar(color).lstrip("#")
    return (int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16))


def a_hex(rgb: tuple[float, float, float]) -> str:
    return "#" + "".join(f"{max(0, min(255, round(v))):02X}" for v in rgb)


def mezclar(color: str, otro: str, cantidad: float) -> str:
    """Mezcla `cantidad` (0 a 1) de `otro` dentro de `color`."""
    a, b = a_rgb(color), a_rgb(otro)
    return a_hex((a[0] + (b[0] - a[0]) * cantidad, a[1] + (b[1] - a[1]) * cantidad,
                  a[2] + (b[2] - a[2]) * cantidad))


def luminancia(color: str) -> float:
    def canal(v: int) -> float:
        x = v / 255
        return x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4
    r, g, b = (canal(v) for v in a_rgb(color))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contraste(color: str, fondo: str) -> float:
    l1, l2 = sorted((luminancia(color), luminancia(fondo)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


def texto_sobre(fondo: str) -> str:
    """Blanco o casi negro: el que se lea mejor sobre `fondo`."""
    return BLANCO if contraste(BLANCO, fondo) >= contraste(NEGRO, fondo) else NEGRO


def asegurar_contraste(color: str, fondo: str, minimo: float = 4.5) -> str:
    """Devuelve `color` o la versión más cercana que cumpla el contraste mínimo.

    Lo lleva, en pasos pequeños, hacia el blanco o el casi negro (el que más contraste con `fondo`),
    para que el color siga pareciéndose al de la marca. Sobre un color medio, como un rosa, eso es
    hacia el casi negro: aclarar ahí nunca llega a 4.5:1.
    """
    color = normalizar(color)
    if contraste(color, fondo) >= minimo:
        return color
    destino = texto_sobre(fondo)
    for paso in range(1, 21):
        candidato = mezclar(color, destino, paso / 20)
        if contraste(candidato, fondo) >= minimo:
            return candidato
    return destino


def par_legible(fondo: str, minimo: float = 4.5) -> tuple[str, str]:
    """(fondo, letra) que se leen con al menos `minimo` de contraste.

    Primero prueba letra blanca o casi negra sobre el color tal cual. Los colores de marca medios
    (un rosa, un naranja, un turquesa) a veces no llegan a 4.5:1 con ninguna de las dos: entonces
    oscurece el fondo en pasos pequeños, para que siga pareciéndose al de la marca, y usa letra blanca.
    """
    fondo = normalizar(fondo)
    letra = texto_sobre(fondo)
    if contraste(letra, fondo) >= minimo:
        return fondo, letra
    for paso in range(1, 41):
        candidato = mezclar(fondo, NEGRO, paso / 40)
        if contraste(BLANCO, candidato) >= minimo:
            return candidato, BLANCO
    return NEGRO, BLANCO


def distintos(a: str, b: str, minimo: float = 1.6) -> bool:
    """¿Se distinguen a simple vista dos colores? (para no pintar acento igual al fondo)."""
    return contraste(a, b) >= minimo
