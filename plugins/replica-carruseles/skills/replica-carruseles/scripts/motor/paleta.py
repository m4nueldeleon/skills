"""Los colores de cada estilo, sacados de los colores de la marca y siempre legibles.

- claro: fondo blanco, texto casi negro, el color de la marca en la palabra clave y los números.
- oscuro: fondo casi negro con un toque del color de la marca, texto blanco, acento aclarado.
- foto: el color de la marca como franja o fondo sólido, palabra clave resaltada en una caja.
El cierre cambia de paleta a propósito: avisa que ahí está la acción.
"""
from __future__ import annotations

from dataclasses import dataclass, replace

from .colores import BLANCO, asegurar_contraste, distintos, mezclar, texto_sobre

TINTA_CLARA = "#15171C"
TINTA_OSCURA = "#F5F5F3"
FONDO_OSCURO = "#0E1013"


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


def _armar(fondo: str, texto: str, acento_base: str, suave_mezcla: float) -> Paleta:
    suave = asegurar_contraste(mezclar(texto, fondo, suave_mezcla), fondo, 4.5)
    acento = asegurar_contraste(acento_base, fondo, 4.0)
    caja = acento_base if distintos(acento_base, fondo) else texto
    sobre_caja = fondo if distintos(fondo, caja, 3.0) else texto_sobre(caja)
    boton = asegurar_contraste(acento_base, fondo, 3.0)
    return Paleta(fondo=fondo, texto=texto, suave=suave, acento=acento,
                  acento_chico=asegurar_contraste(acento_base, fondo, 4.5),
                  linea=mezclar(texto, fondo, 0.84), resaltado=caja, sobre_resaltado=sobre_caja,
                  boton=boton, sobre_boton=texto_sobre(boton))


def para(estilo: str, principal: str, acento: str | None, fondo: str | None = None) -> Paleta:
    """Paleta de las láminas normales."""
    marca = acento or principal
    if estilo == "oscuro":
        base = fondo or mezclar(FONDO_OSCURO, principal, 0.08)
        return _armar(base, TINTA_OSCURA, marca, 0.3)
    if estilo == "foto":
        base = fondo or principal
        texto = texto_sobre(base)
        destacado = acento if acento and distintos(acento, base) else texto
        return _armar(base, texto, destacado, 0.22)
    base = fondo or BLANCO
    return _armar(base, asegurar_contraste(TINTA_CLARA, base, 7.0), marca, 0.3)


def para_cierre(estilo: str, principal: str, acento: str | None) -> Paleta:
    """Paleta del cierre: invierte la del carrusel para que la acción se note."""
    if estilo == "foto":
        return _armar(BLANCO, TINTA_CLARA, principal, 0.38)
    texto = texto_sobre(principal)
    destacado = acento if acento and distintos(acento, principal, 2.0) else texto
    paleta = _armar(principal, texto, destacado, 0.2)
    sobre_boton = principal if distintos(principal, texto, 4.5) else texto_sobre(texto)
    return replace(paleta, boton=texto, sobre_boton=sobre_boton)
