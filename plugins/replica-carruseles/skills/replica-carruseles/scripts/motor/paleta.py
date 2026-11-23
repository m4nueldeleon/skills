"""Los colores de cada estilo, sacados de los colores de la marca y siempre legibles.

- claro: fondo blanco, texto casi negro, el color de la marca en la palabra clave y los números.
- oscuro: fondo casi negro con un toque del color de la marca, texto blanco, acento aclarado.
- foto: el color de la marca como franja o fondo sólido, palabra clave resaltada en una caja.
El cierre cambia de paleta a propósito: avisa que ahí está la acción.

Toda letra sobre un color sólido (fondo, franja, caja de la palabra clave, botón) queda en 4.5:1 o más.
"""
from __future__ import annotations

from dataclasses import dataclass, replace

from .colores import (BLANCO, asegurar_contraste, contraste, distintos, luminancia, mezclar, par_legible,
                      texto_sobre)

TINTA_CLARA = "#15171C"
TINTA_OSCURA = "#F5F5F3"
FONDO_OSCURO = "#0E1013"
MINIMO_LETRA = 4.5        # contraste mínimo de cualquier letra sobre su fondo
LUMINANCIA_MUY_BAJA = 0.03  # por debajo, el color se ve casi negro y no resalta en ningún estilo
PARECIDO_AL_TEXTO = 0.75    # acento con 75 % o más del contraste de la letra = casi tan oscuro como ella


@dataclass(frozen=True)
class Paleta:
    fondo: str
    texto: str
    suave: str
    acento: str          # palabra clave en titulares (letra grande)
    acento_chico: str    # números de lista, «Desliza» (letra chica: pide más contraste)
    linea: str
    resaltado: str       # caja detrás de la palabra clave (modo «resaltado»)
    sobre_resaltado: str
    boton: str
    sobre_boton: str


def _caja(color: str, fondo: str) -> tuple[str, str]:
    """Caja de la palabra resaltada y su letra: el fondo de la lámina si se lee, si no blanco o casi negro."""
    if contraste(fondo, color) >= MINIMO_LETRA:
        return color, fondo
    return par_legible(color, MINIMO_LETRA)


def _armar(fondo: str, texto: str, acento_base: str, suave_mezcla: float) -> Paleta:
    suave = asegurar_contraste(mezclar(texto, fondo, suave_mezcla), fondo, MINIMO_LETRA)
    acento = asegurar_contraste(acento_base, fondo, 4.0)
    caja, sobre_caja = _caja(acento_base if distintos(acento_base, fondo) else texto, fondo)
    boton, sobre_boton = par_legible(asegurar_contraste(acento_base, fondo, 3.0), MINIMO_LETRA)
    return Paleta(fondo=fondo, texto=texto, suave=suave, acento=acento,
                  acento_chico=asegurar_contraste(acento_base, fondo, MINIMO_LETRA),
                  linea=mezclar(texto, fondo, 0.84), resaltado=caja, sobre_resaltado=sobre_caja,
                  boton=boton, sobre_boton=sobre_boton)


def se_pierde(color: str, fondo: str, texto: str) -> bool:
    """¿La palabra clave en este color se confunde con la letra normal?

    Pasa cuando el color es casi negro, o cuando la letra es oscura y el color tiene casi el mismo
    contraste que ella contra el fondo (por ejemplo, un acento gris carbón en el estilo claro).
    """
    if luminancia(color) < LUMINANCIA_MUY_BAJA:
        return True
    letra_oscura = luminancia(texto) < luminancia(fondo)
    return letra_oscura and contraste(color, fondo) >= PARECIDO_AL_TEXTO * contraste(texto, fondo)


def acento_vivo(principal: str, acento: str | None, fondo: str, texto: str) -> str:
    """El color de la palabra clave: el acento si resalta; si se pierde junto a la letra, el principal."""
    if not acento or not se_pierde(acento, fondo, texto):
        return acento or principal
    if distintos(principal, fondo, 1.2) and not se_pierde(principal, fondo, texto):
        return principal
    return acento


def _base(estilo: str, principal: str, fondo: str | None) -> tuple[str, str]:
    """Fondo y letra de las láminas normales de cada estilo."""
    if estilo == "oscuro":
        return fondo or mezclar(FONDO_OSCURO, principal, 0.08), TINTA_OSCURA
    if estilo == "foto":
        return par_legible(fondo or principal, MINIMO_LETRA)
    base = fondo or BLANCO
    return base, asegurar_contraste(TINTA_CLARA, base, 7.0)


def acento_cambiado(estilo: str, principal: str, acento: str | None, fondo: str | None = None) -> bool:
    """¿El acento de la marca se perdía junto a la letra y se usó el principal en su lugar?"""
    base, texto = _base(estilo, principal, fondo)
    return bool(acento) and acento_vivo(principal, acento, base, texto) != acento


def para(estilo: str, principal: str, acento: str | None, fondo: str | None = None) -> Paleta:
    """Paleta de las láminas normales."""
    base, texto = _base(estilo, principal, fondo)
    vivo = acento_vivo(principal, acento, base, texto)
    if estilo == "foto":
        destacado = vivo if acento and distintos(vivo, base) else texto
        return _armar(base, texto, destacado, 0.22)
    return _armar(base, texto, vivo, 0.3)


def para_cierre(estilo: str, principal: str, acento: str | None) -> Paleta:
    """Paleta del cierre: invierte la del carrusel para que la acción se note."""
    if estilo == "foto":
        return _armar(BLANCO, TINTA_CLARA, principal, 0.38)
    fondo, texto = par_legible(principal, MINIMO_LETRA)
    destacado = acento if acento and distintos(acento, fondo, 2.0) else texto
    paleta = _armar(fondo, texto, destacado, 0.2)
    sobre_boton = fondo if distintos(fondo, texto, MINIMO_LETRA) else texto_sobre(texto)
    return replace(paleta, boton=texto, sobre_boton=sobre_boton)

