"""Cada tipo de lámina (portada, texto, lista, foto, cierre) en los tres estilos."""
from __future__ import annotations

from typing import Callable

from PIL import Image, ImageDraw

from . import paleta as paletas
from .composicion import (ABAJO, ANCHO_UTIL, ARRIBA, M, Contexto, Registro, apilar, barra, encajar,
                          lienzo, maq, numero, pie, pieza_texto, tinta, titulo)
from .datos import Carrusel
from .dibujo import ALTO, ANCHO, Maqueta, Tinta, circulo, foto_cubrir, fuente, pildora, pintar

ALTO_FOTO = 700            # foto arriba en los estilos claro y oscuro
INICIO_SERIE = ARRIBA + 170  # las láminas numeradas arrancan a la misma altura: se leen como serie


def _foto_arriba(imagen: Image.Image, lam: dict) -> None:
    imagen.paste(foto_cubrir(lam["foto"], (ANCHO, ALTO_FOTO), lam.get("enfoque", "centro")), (0, 0))


def _franja(imagen: Image.Image, draw: ImageDraw.ImageDraw, ctx: Contexto, lam: dict, reg: Registro,
            tam_titulo: float) -> None:
    """Estilo foto: la foto a sangre y una franja de color con el texto abajo."""
    pal, d, f = ctx.paleta, ctx.carrusel.diseno, ctx.carrusel.fuentes
    campo = "subtitulo" if lam["tipo"] == "portada" else "texto"
    def construir(prueba: Registro, escala: float) -> list:
        tit = titulo(prueba, ctx, lam.get("titulo", ""), tam_titulo * escala, 54, ALTO * 0.28)
        extra = lam.get(campo)
        cue = maq(prueba, campo, extra, f.texto, 46 * escala, 34, ANCHO_UTIL, ALTO * 0.16, 1.28) if extra else None
        return [numero(draw, ctx, str(lam["numero"]), pal.acento, int(84 * escala)) if lam.get("numero") else None,
                pieza_texto(draw, tit, tinta(ctx, pal), d.alineacion, 30),
                pieza_texto(draw, cue, Tinta(pal.suave, pal.acento), d.alineacion, 0) if cue else None]
    piezas = encajar(reg, construir, ALTO * 0.42)
    alto = sum(a + e for a, e, _ in piezas) - piezas[-1][1]
    y0 = ALTO - (76 + alto + 150)
    if lam.get("foto"):
        imagen.paste(foto_cubrir(lam["foto"], (ANCHO, int(y0) + 2), lam.get("enfoque", "centro")), (0, 0))
    draw.rectangle((0, y0, ANCHO, ALTO), fill=pal.fondo)
    apilar(piezas, y0 + 76, ALTO, 0.0)


def portada(ctx: Contexto, lam: dict, reg: Registro) -> Image.Image:
    pal, d, f = ctx.paleta, ctx.carrusel.diseno, ctx.carrusel.fuentes
    imagen, draw = lienzo(pal.fondo)
    con_foto = bool(lam.get("foto"))
    if ctx.carrusel.estilo == "foto" and con_foto:
        _franja(imagen, draw, ctx, lam, reg, 100)
        pie(draw, ctx, lam["n"], pal, portada=True)
        return imagen
    if con_foto:
        _foto_arriba(imagen, lam)
    arriba = ALTO_FOTO + 64 if con_foto else ARRIBA
    def construir(prueba: Registro, escala: float) -> list:
        tit = titulo(prueba, ctx, lam["titulo"], (100 if con_foto else 136) * escala, 60,
                     (ABAJO - arriba) * 0.75, 1.02)
        sub = lam.get("subtitulo")
        sub_m = maq(prueba, "subtitulo", sub, f.texto, 50 * escala, 36, ANCHO_UTIL, 260, 1.28) if sub else None
        return [None if con_foto else barra(draw, ctx, pal.acento),
                pieza_texto(draw, tit, tinta(ctx, pal), d.alineacion, 40),
                pieza_texto(draw, sub_m, Tinta(pal.suave, pal.acento), d.alineacion, 0) if sub_m else None]
    apilar(encajar(reg, construir, ABAJO - arriba), arriba, ABAJO, 0.0 if con_foto else 0.46)
    pie(draw, ctx, lam["n"], pal, portada=True)
    return imagen


def _cuerpo_numerado(ctx: Contexto, draw: ImageDraw.ImageDraw, lam: dict, pal: paletas.Paleta,
                     tamanos: tuple, alto: float) -> Callable[[Registro, float], list]:
    """Número + titular + texto: lo comparten las láminas de texto y las de foto."""
    d, f = ctx.carrusel.diseno, ctx.carrusel.fuentes
    t_num, t_tit, t_cue = tamanos
    def construir(prueba: Registro, escala: float) -> list:
        tit = titulo(prueba, ctx, lam["titulo"], t_tit * escala, 48, alto * 0.6, 1.06) if lam.get("titulo") else None
        cue = maq(prueba, "texto", lam["texto"], f.texto, t_cue * escala, 34, ANCHO_UTIL, alto * 0.6, 1.32) \
            if lam.get("texto") else None
        color_cuerpo = pal.suave if tit else pal.texto
        return [numero(draw, ctx, str(lam["numero"]), pal.acento, int(t_num * escala)) if lam.get("numero") else None,
                pieza_texto(draw, tit, tinta(ctx, pal), d.alineacion, 40) if tit else None,
                pieza_texto(draw, cue, Tinta(color_cuerpo, pal.acento), d.alineacion, 0) if cue else None]
    return construir


def texto(ctx: Contexto, lam: dict, reg: Registro) -> Image.Image:
    pal = ctx.paleta
    imagen, draw = lienzo(pal.fondo)
    serie = bool(lam.get("numero"))
    inicio = INICIO_SERIE if serie else ARRIBA
    construir = _cuerpo_numerado(ctx, draw, lam, pal, (150, 88, 52), ABAJO - ARRIBA)
    piezas = encajar(reg, construir, ABAJO - inicio)
    apilar(piezas, inicio, ABAJO, 0.0 if serie else 0.42)
    pie(draw, ctx, lam["n"], pal)
    return imagen


def foto(ctx: Contexto, lam: dict, reg: Registro) -> Image.Image:
    pal = ctx.paleta
    imagen, draw = lienzo(pal.fondo)
    if ctx.carrusel.estilo == "foto":
        _franja(imagen, draw, ctx, lam, reg, 92)
        pie(draw, ctx, lam["n"], pal)
        return imagen
    _foto_arriba(imagen, lam)
    arriba = ALTO_FOTO + 60
    construir = _cuerpo_numerado(ctx, draw, lam, pal, (84, 76, 46), ABAJO - arriba)
    apilar(encajar(reg, construir, ABAJO - arriba), arriba, ABAJO, 0.0)
    pie(draw, ctx, lam["n"], pal)
    return imagen


def _fila(draw: ImageDraw.ImageDraw, pal: paletas.Paleta, f_idx: object, i: int, t: Maqueta,
          nm: Maqueta | None, separacion: float, ultima: bool) -> tuple:
    alto_fila = t.alto + (nm.alto + 12 if nm else 0)
    sangria = 84
    def dibujar(y: float) -> None:
        base = y + fuente(t.ruta, t.tam).getmetrics()[0]
        draw.text((M, base), str(i + 1), font=f_idx, fill=pal.acento_chico, anchor="ls")
        y2 = pintar(draw, t, M + sangria, y, ANCHO_UTIL - sangria, Tinta(pal.texto, pal.acento))
        if nm:
            pintar(draw, nm, M + sangria, y2 + 12, ANCHO_UTIL - sangria, Tinta(pal.suave, pal.acento))
        if not ultima:
            ly = y + alto_fila + separacion / 2
            draw.line((M, ly, ANCHO - M, ly), fill=pal.linea, width=2)
    return (alto_fila, separacion, dibujar)


def lista(ctx: Contexto, lam: dict, reg: Registro) -> Image.Image:
    pal, d, f = ctx.paleta, ctx.carrusel.diseno, ctx.carrusel.fuentes
    imagen, draw = lienzo(pal.fondo)
    def construir(prueba: Registro, escala: float) -> list:
        tam = max(32, int(50 * escala))
        tit = titulo(prueba, ctx, lam["titulo"], 84 * escala, 50, 330, 1.06) if lam.get("titulo") else None
        piezas = [pieza_texto(draw, tit, tinta(ctx, pal), d.alineacion, 60) if tit else None]
        items = lam["items"]
        for i, item in enumerate(items):
            dato = item if isinstance(item, dict) else {"texto": str(item)}
            t = maq(prueba, f"punto {i + 1}", dato.get("texto", ""), f.fuerte, tam, tam, ANCHO_UTIL - 84, 999, 1.2)
            nota = dato.get("nota")
            nm = maq(prueba, f"nota {i + 1}", nota, f.texto, tam * 0.8, tam * 0.8, ANCHO_UTIL - 84, 999, 1.3) \
                if nota else None
            f_idx = fuente(f.titulo, int(tam * 1.1))
            piezas.append(_fila(draw, pal, f_idx, i, t, nm, tam * 1.5, i == len(items) - 1))
        prueba.tamanos["items"] = tam
        return piezas
    apilar(encajar(reg, construir, ABAJO - ARRIBA), ARRIBA, ABAJO, 0.42)
    pie(draw, ctx, lam["n"], pal)
    return imagen


def _sello(imagen: Image.Image, ctx: Contexto, lam: dict, escala: float) -> tuple | None:
    """Foto redonda (o logo) arriba del cierre, si la hay."""
    if lam.get("foto"):
        diametro = int(220 * escala)
        disco = circulo(foto_cubrir(lam["foto"], (600, 600), lam.get("enfoque", "centro")), diametro)
        return (diametro, 48, lambda y: imagen.paste(disco, (int((ANCHO - diametro) / 2), int(y)), disco))
    logo = ctx.carrusel.marca.get("logo")
    ruta = (ctx.carrusel.base / str(logo)) if logo else None
    if not ruta or not ruta.is_file():
        return None
    with Image.open(ruta) as abierto:
        marca = abierto.convert("RGBA")
    marca.thumbnail((int(360 * escala), int(150 * escala)), Image.Resampling.LANCZOS)
    return (marca.height, 48, lambda y: imagen.paste(marca, (int((ANCHO - marca.width) / 2), int(y)), marca))


def cierre(ctx: Contexto, lam: dict, reg: Registro) -> Image.Image:
    pal, f = ctx.cierre, ctx.carrusel.fuentes
    imagen, draw = lienzo(pal.fondo)
    marca = ctx.carrusel.marca
    def construir(prueba: Registro, e: float) -> list:
        def bloque(campo: str, valor: object, ruta: object, tmax: float, tmin: float, color: Tinta,
                   espacio: float, inter: float = 1.2) -> tuple | None:
            if not valor:
                return None
            m = maq(prueba, campo, str(valor), ruta, tmax * e, tmin, ANCHO_UTIL, 400, inter)
            return pieza_texto(draw, m, color, "centro", espacio)
        tit = titulo(prueba, ctx, lam["titulo"], 112 * e, 60, 420, 1.04)
        acc = maq(prueba, "accion", lam["accion"], f.fuerte, 44 * e, 32, ANCHO_UTIL - 140, 170) \
            if lam.get("accion") else None
        boton = (acc.alto + acc.tam * 1.1, 64, lambda y: pildora(draw, acc, ANCHO / 2, y, ANCHO_UTIL, pal.boton,
                                                                 pal.sobre_boton)) if acc else None
        return [_sello(imagen, ctx, lam, e),
                pieza_texto(draw, tit, tinta(ctx, pal), "centro", 36),
                bloque("texto", lam.get("texto"), f.texto, 50, 36, Tinta(pal.suave, pal.acento), 60, 1.3),
                boton,
                bloque("usuario", marca.get("usuario"), f.fuerte, 46, 32, Tinta(pal.texto, pal.texto), 10),
                bloque("nombre", marca.get("nombre"), f.texto, 34, 26, Tinta(pal.suave, pal.suave), 0)]
    apilar(encajar(reg, construir, ALTO - 220), 110, ALTO - 110, 0.5)
    return imagen


DIBUJANTES: dict[str, Callable] = {"portada": portada, "texto": texto, "lista": lista,
                                   "foto": foto, "cierre": cierre}


def contexto(carrusel: Carrusel) -> Contexto:
    marca, d = carrusel.marca, carrusel.diseno
    return Contexto(carrusel=carrusel,
                    paleta=paletas.para(carrusel.estilo, marca["principal"], marca.get("acento"), d.fondo),
                    cierre=paletas.para_cierre(carrusel.estilo, marca["principal"], marca.get("acento")),
                    total=len(carrusel.laminas))


def dibujar(carrusel: Carrusel) -> list[tuple[Image.Image, Registro]]:
    ctx = contexto(carrusel)
    salida = []
    for lam in carrusel.laminas:
        reg = Registro(lam["n"])
        salida.append((DIBUJANTES[lam["tipo"]](ctx, lam, reg), reg))
    return salida
