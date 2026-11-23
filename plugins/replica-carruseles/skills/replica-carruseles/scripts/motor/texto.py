"""Texto de las láminas: marcar acentos, limpiar emojis y partir en renglones.

No depende de Pillow: recibe una función `medir(texto) -> ancho en px`, así se puede probar
sin fuentes y la usa igual el dibujo con Pillow.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Callable

Medir = Callable[[str], float]

_EMOJI = re.compile(
    "[\U0001F000-\U0001FAFF\U00002600-\U000027BF\U00002B00-\U00002BFF"
    "\U0001F1E6-\U0001F1FF\U0000FE0F\U0000200D\U000020E3]"
)
# Si a una fuente le falta un signo, se cambia por uno que sí tiene.
SUSTITUTOS = {"“": '"', "”": '"', "‘": "'", "’": "'", "—": "-", "–": "-", "…": "...",
              "→": "›", "✓": "", "•": "·"}


@dataclass(frozen=True)
class Palabra:
    texto: str
    acento: bool
    pegada: bool = False  # va pegada a la anterior, sin espacio («*alguna*?» -> «alguna» + «?»)


def unir(renglon: list | tuple) -> str:
    """El texto de un renglón, con espacios solo donde los hay de verdad."""
    salida = ""
    for i, palabra in enumerate(renglon):
        salida += ("" if i == 0 or palabra.pegada else " ") + palabra.texto
    return salida


def quitar_emojis(texto: str) -> tuple[str, bool]:
    """Devuelve (texto sin emojis, ¿había emojis?)."""
    limpio = _EMOJI.sub("", texto)
    if limpio == texto:
        return texto, False
    return re.sub(r"[ \t]{2,}", " ", limpio).strip(), True


def palabras(texto: str) -> list[list[Palabra]]:
    """'Sin *dolor* no\\nhay' -> párrafos de palabras; lo que va entre *asteriscos* es acento."""
    parrafos = []
    for renglon in str(texto).split("\n"):
        actual: list[Palabra] = []
        acento = False
        hubo_espacio = True
        for trozo in re.split(r"(\*)", renglon):
            if trozo == "*":
                acento = not acento
                continue
            for i, p in enumerate(trozo.split()):
                pegada = i == 0 and bool(actual) and not hubo_espacio and not trozo[:1].isspace()
                actual.append(Palabra(p, acento, pegada))
            hubo_espacio = trozo[-1:].isspace() if trozo else hubo_espacio
        parrafos.append(actual)
    return parrafos


def _grupos(parrafo: list[Palabra]) -> list[list[Palabra]]:
    """Junta cada palabra con las que van pegadas a ella: no se separan al cambiar de renglón."""
    grupos: list[list[Palabra]] = []
    for palabra in parrafo:
        if palabra.pegada and grupos:
            grupos[-1] = grupos[-1] + [palabra]
        else:
            grupos.append([palabra])
    return grupos


def _partir_palabra(palabra: Palabra, medir: Medir, ancho: float) -> list[Palabra]:
    """Una palabra más ancha que el renglón se parte en trozos con guion."""
    trozos, actual = [], ""
    for letra in palabra.texto:
        if actual and medir(actual + letra + "-") > ancho:
            trozos.append(Palabra(actual + "-", palabra.acento))
            actual = letra
        else:
            actual += letra
    trozos.append(Palabra(actual, palabra.acento))
    return trozos


def _ancho_renglon(renglon: list[Palabra], medir: Medir) -> float:
    return medir(unir(renglon))


def _envolver_parrafo(parrafo: list[Palabra], medir: Medir, ancho: float) -> tuple[list, bool]:
    renglones: list[list[Palabra]] = []
    actual: list[Palabra] = []
    partida = False
    for grupo in _grupos(parrafo):
        piezas = [grupo]
        if len(grupo) == 1 and medir(grupo[0].texto) > ancho:
            piezas, partida = [[p] for p in _partir_palabra(grupo[0], medir, ancho)], True
        for pieza in piezas:
            if actual and _ancho_renglon(actual + pieza, medir) > ancho:
                renglones.append(actual)
                actual = [Palabra(pieza[0].texto, pieza[0].acento)] + pieza[1:]
            else:
                actual = actual + pieza
    renglones.append(actual)
    return renglones, partida


def _sin_viuda(renglones: list, medir: Medir, ancho: float) -> list:
    """Evita que el último renglón quede con una sola palabra (se ve descuidado)."""
    def cuenta(renglon: list) -> int:
        return sum(1 for p in renglon if not p.pegada)
    if len(renglones) < 2 or cuenta(renglones[-1]) != 1 or cuenta(renglones[-2]) < 3:
        return renglones
    previo, ultimo = renglones[-2], renglones[-1]
    if previo[-1].pegada or ultimo[0].pegada:
        return renglones
    nuevo_ultimo = [previo[-1]] + [Palabra(ultimo[0].texto, ultimo[0].acento)] + ultimo[1:]
    if _ancho_renglon(nuevo_ultimo, medir) > ancho:
        return renglones
    return renglones[:-2] + [previo[:-1], nuevo_ultimo]


def envolver(texto: str, medir: Medir, ancho: float, evitar_viudas: bool = True) -> tuple[list, bool]:
    """Parte el texto en renglones que caben en `ancho`.

    Devuelve (renglones, ¿hubo que partir una palabra?). Cada renglón es una lista de Palabra.
    """
    renglones: list[list[Palabra]] = []
    partida = False
    for parrafo in palabras(texto):
        if not parrafo:
            renglones.append([])
            continue
        nuevos, rota = _envolver_parrafo(parrafo, medir, ancho)
        if evitar_viudas:
            nuevos = _sin_viuda(nuevos, medir, ancho)
        renglones.extend(nuevos)
        partida = partida or rota
    return renglones, partida
