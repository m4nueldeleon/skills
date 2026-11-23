"""Herramientas para componer una lámina: registro de avisos, piezas apiladas y el pie."""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

from PIL import Image, ImageDraw

from . import paleta as paletas
from .datos import Carrusel
from .dibujo import ALTO, ANCHO, Maqueta, Tinta, flecha, fuente, limpiar, maquetar, pintar

M = 96                     # margen de los lados
ARRIBA, ABAJO = 150, ALTO - 170
PIE_Y = ALTO - 92          # renglón del @usuario y el número de lámina
ANCHO_UTIL = ANCHO - 2 * M
ESCALAS = (1.0, 0.93, 0.86, 0.8, 0.74, 0.68)
Pieza = tuple  # (alto, espacio_despues, dibujar(y))


@dataclass
class Registro:
    """Lo que pasó al dibujar una lámina: avisos, tamaños de letra y si algún texto no cupo."""
    n: int
    avisos: list = field(default_factory=list)
    no_cupo: list = field(default_factory=list)
    tamanos: dict = field(default_factory=dict)

    def sumar(self, otro: "Registro") -> None:
        self.avisos.extend(otro.avisos)
        self.no_cupo.extend(otro.no_cupo)
        self.tamanos.update(otro.tamanos)


@dataclass(frozen=True)
class Contexto:
    carrusel: Carrusel
    paleta: paletas.Paleta
    cierre: paletas.Paleta
    total: int


def maq(reg: Registro, campo: str, texto: str, ruta: Path, tmax: float, tmin: float, ancho: float,
        alto: float, inter: float = 1.1, mayus: bool = False, maxr: int = 99) -> Maqueta:
    """Limpia el texto, lo acomoda en la caja y anota lo que haya pasado."""
    limpio, avisos = limpiar(texto, ruta)
    reg.avisos.extend(f"{campo}: {a}" for a in avisos)
    tmax = max(tmax, tmin)
    m = maquetar(limpio, ruta, int(tmax), int(tmin), ancho, alto, inter, mayus, maxr, campo == "titulo")
    reg.tamanos[campo] = m.tam
    if not m.cupo:
        reg.no_cupo.append(campo)
    return m


def alto_total(piezas: list) -> float:
    piezas = [p for p in piezas if p]
    return sum(a + e for a, e, _ in piezas) - (piezas[-1][1] if piezas else 0)


def encajar(reg: Registro, construir: Callable[[Registro, float], list], alto: float) -> list:
    """Arma las piezas con letra cada vez más chica hasta que todas juntas caben en `alto`."""
    for escala in ESCALAS:
        prueba = Registro(reg.n)
        piezas = [p for p in construir(prueba, escala) if p]
        if alto_total(piezas) <= alto or escala == ESCALAS[-1]:
            reg.sumar(prueba)
            if alto_total(piezas) > alto:
                reg.no_cupo.append("la lámina completa")
            return piezas
    return []


def apilar(piezas: list, y0: float, y1: float, sesgo: float = 0.5) -> float:
    """Dibuja las piezas una debajo de otra; `sesgo` 0 = arriba, 0.5 = centradas. Devuelve la y final."""
    piezas = [p for p in piezas if p]
    y = y0 + max(0.0, (y1 - y0 - alto_total(piezas)) * sesgo)
    for alto, espacio, dibujar in piezas:
        dibujar(y)
        y += alto + espacio
    return y


def tinta(ctx: Contexto, pal: paletas.Paleta, color: str | None = None) -> Tinta:
    d = ctx.carrusel.diseno
    acento = pal.resaltado if d.acento_modo == "resaltado" else pal.acento
    return Tinta(color or pal.texto, acento, d.acento_modo, pal.sobre_resaltado)


def pieza_texto(draw: ImageDraw.ImageDraw, m: Maqueta, tinta_: Tinta, alineacion: str,
                espacio: float, x: float = M, ancho: float = ANCHO_UTIL) -> Pieza:
    return (m.alto, espacio, lambda y: pintar(draw, m, x, y, ancho, tinta_, alineacion))


def barra(draw: ImageDraw.ImageDraw, ctx: Contexto, color: str) -> Pieza:
    """Raya corta de color arriba del titular de la portada."""
    x = (ANCHO - 96) / 2 if ctx.carrusel.diseno.alineacion == "centro" else M
    return (10, 44, lambda y: draw.rectangle((x, y, x + 96, y + 10), fill=color))


def numero(draw: ImageDraw.ImageDraw, ctx: Contexto, valor: str, color: str, tam: int) -> Pieza:
    """Número grande de la serie («01», «02»…)."""
    f = fuente(ctx.carrusel.fuentes.titulo, tam)
    centrado = ctx.carrusel.diseno.alineacion == "centro"
    alto_cifra = -f.getbbox("0", anchor="ls")[1]
    def dibujar(y: float) -> None:
        x = ANCHO / 2 if centrado else M
        draw.text((x, y + alto_cifra), valor, font=f, fill=color, anchor="ms" if centrado else "ls")
    return (alto_cifra, int(tam * 0.26), dibujar)


def pie(draw: ImageDraw.ImageDraw, ctx: Contexto, n: int, pal: paletas.Paleta, portada: bool = False) -> None:
    """@usuario a la izquierda; «Desliza →» en la portada o «3/9» en las demás."""
    marca, fuentes = ctx.carrusel.marca, ctx.carrusel.fuentes
    firma = marca.get("usuario") or marca.get("nombre")
    f = fuente(fuentes.fuerte, 32)
    if firma:
        draw.text((M, PIE_Y), limpiar(firma, fuentes.fuerte)[0], font=f, fill=pal.suave, anchor="lm")
    if portada:
        largo = 46
        draw.text((ANCHO - M - largo - 18, PIE_Y), "Desliza", font=f, fill=pal.acento_chico, anchor="rm")
        flecha(draw, ANCHO - M - largo, PIE_Y + 1, largo, pal.acento_chico)
    elif ctx.carrusel.numerar:
        draw.text((ANCHO - M, PIE_Y), f"{n}/{ctx.total}", font=f, fill=pal.suave, anchor="rm")


def lienzo(color: str) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    imagen = Image.new("RGB", (ANCHO, ALTO), color)
    return imagen, ImageDraw.Draw(imagen)


def titulo(reg: Registro, ctx: Contexto, texto: str, tmax: float, tmin: float, alto: float,
           inter: float = 1.04, ancho: float = ANCHO_UTIL) -> Maqueta:
    d = ctx.carrusel.diseno
    return maq(reg, "titulo", texto, ctx.carrusel.fuentes.titulo, tmax * d.escala_titulo, tmin,
               ancho, alto, inter, d.mayusculas, 7)
