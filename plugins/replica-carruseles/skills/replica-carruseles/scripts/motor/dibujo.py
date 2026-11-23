"""Piezas de dibujo con Pillow: fuentes, bloques de texto que se ajustan solos, fotos y adornos."""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

from .texto import SUSTITUTOS, envolver, quitar_emojis, unir

ANCHO, ALTO = 1080, 1350
ENFOQUES = {"centro": (0.5, 0.5), "arriba": (0.5, 0.2), "abajo": (0.5, 0.8),
            "izquierda": (0.25, 0.5), "derecha": (0.75, 0.5)}


@lru_cache(maxsize=256)
def fuente(ruta: Path, tam: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(ruta), max(8, int(tam)))


def _huella(ruta: Path, letra: str) -> bytes:
    lienzo = Image.new("L", (96, 96), 0)
    ImageDraw.Draw(lienzo).text((16, 8), letra, font=fuente(ruta, 48), fill=255)
    return lienzo.tobytes()


@lru_cache(maxsize=4096)
def _tiene_glifo(ruta: Path, letra: str) -> bool:
    """Si la letra se dibuja igual que un signo inexistente, la fuente no la tiene."""
    return _huella(ruta, letra) != _huella(ruta, "\U0010FFFD")


def limpiar(texto: str, ruta: Path) -> tuple[str, list[str]]:
    """Quita emojis y cambia los signos que la fuente no tiene. Devuelve (texto, avisos)."""
    avisos = []
    texto, habia = quitar_emojis(str(texto))
    if habia:
        avisos.append("quité emojis (en las láminas se ven como cuadritos; ponlos en el caption)")
    salida = []
    for letra in texto:
        if letra.isspace() or letra == "*" or _tiene_glifo(ruta, letra):
            salida.append(letra)
            continue
        cambio = SUSTITUTOS.get(letra, "")
        salida.append(cambio)
        avisos.append(f"la fuente no tiene «{letra}»" + (f", usé «{cambio}»" if cambio else ", lo quité"))
    return "".join(salida), avisos


@dataclass(frozen=True)
class Maqueta:
    renglones: tuple
    ruta: Path
    tam: int
    paso: float
    alto: float
    cupo: bool
    tam_max: int

    @property
    def encogida(self) -> bool:
        return self.tam < self.tam_max


def _alto_bloque(n: int, f: ImageFont.FreeTypeFont, paso: float) -> float:
    asc, desc = f.getmetrics()
    return 0 if n == 0 else (n - 1) * paso + asc + desc


def _balancear(texto: str, medir: object, ancho: float, renglones: list) -> list:
    """Renglones parejos (como `text-wrap: balance`): el ancho más chico que no agrega renglones."""
    if len(renglones) < 2:
        return renglones
    bajo, alto, mejor = ancho * 0.45, ancho, renglones
    for _ in range(12):
        medio = (bajo + alto) / 2
        prueba, partida = envolver(texto, medir, medio)
        if len(prueba) == len(renglones) and not partida:
            mejor, alto = prueba, medio
        else:
            bajo = medio
    return mejor


def _sueltas(renglones: list) -> bool:
    """¿Hay un renglón con una sola palabra en un texto de varias? (se ve descuidado)."""
    if sum(1 for r in renglones for p in r if not p.pegada) < 3:
        return False
    return any(sum(1 for p in r if not p.pegada) == 1 for r in renglones)


def _intentar(texto: str, ruta: Path, tam: int, ancho: float, interlineado: float,
              balancear: bool) -> tuple[list, bool, float, float]:
    f = fuente(ruta, tam)
    renglones, partida = envolver(texto, f.getlength, ancho)
    if balancear:
        renglones = _balancear(texto, f.getlength, ancho, renglones)
    paso = tam * interlineado
    return renglones, partida, paso, _alto_bloque(len(renglones), f, paso)


def maquetar(texto: str, ruta: Path, tam_max: int, tam_min: int, ancho: float, alto_max: float,
             interlineado: float = 1.1, mayus: bool = False, max_renglones: int = 99,
             titular: bool = False) -> Maqueta:
    """Busca el tamaño de letra más grande con el que el texto cabe en la caja.

    En titulares (`titular=True`) además empareja los renglones y, si puede bajando la letra
    hasta un 25 %, evita que una palabra quede sola en un renglón.
    """
    texto = texto.upper() if mayus else texto
    primero = None
    for tam in range(int(tam_max), int(tam_min) - 1, -2):
        renglones, partida, paso, alto = _intentar(texto, ruta, tam, ancho, interlineado, titular)
        cabe = alto <= alto_max and len(renglones) <= max_renglones and not partida
        if not cabe:
            continue
        maqueta = Maqueta(tuple(tuple(r) for r in renglones), ruta, tam, paso, alto, True, int(tam_max))
        primero = primero or maqueta
        if not titular or not _sueltas(renglones) or tam <= tam_max * 0.75:
            return primero if titular and _sueltas(renglones) else maqueta
    if primero:
        return primero
    renglones, _, paso, alto = _intentar(texto, ruta, int(tam_min), ancho, interlineado, titular)
    return Maqueta(tuple(tuple(r) for r in renglones), ruta, int(tam_min), paso, alto, False, int(tam_max))


def _tramos(renglon: tuple) -> list[tuple[str, bool, bool]]:
    """Agrupa palabras seguidas con el mismo acento: se dibujan juntas y conservan el kerning.

    Cada tramo es (texto, ¿acento?, ¿va pegado al anterior?).
    """
    tramos: list[tuple[str, bool, bool]] = []
    for palabra in renglon:
        if tramos and tramos[-1][1] == palabra.acento:
            previo = tramos[-1]
            tramos[-1] = (previo[0] + ("" if palabra.pegada else " ") + palabra.texto, previo[1], previo[2])
        else:
            tramos.append((palabra.texto, palabra.acento, palabra.pegada and bool(tramos)))
    return tramos


@dataclass(frozen=True)
class Tinta:
    color: str
    acento: str
    modo: str = "color"          # "color" pinta la palabra; "resaltado" le pone una caja detrás
    sobre_resaltado: str = "#FFFFFF"


def _pintar_renglon(draw: ImageDraw.ImageDraw, renglon: tuple, f: ImageFont.FreeTypeFont,
                    x: float, y: float, tinta: Tinta) -> None:
    espacio = f.getlength(" ")
    asc = f.getmetrics()[0]
    alto_mayus = -f.getbbox("H", anchor="ls")[1]
    for i, (texto, es_acento, pegado) in enumerate(_tramos(renglon)):
        if i and not pegado:
            x += espacio
        ancho = f.getlength(texto)
        color = tinta.acento if es_acento else tinta.color
        resaltar = es_acento and tinta.modo == "resaltado"
        margen_x = f.size * 0.1 if resaltar else 0
        x += margen_x  # la caja no se come el espacio con la palabra vecina
        if resaltar:
            base = y + asc
            draw.rectangle((x - margen_x, base - alto_mayus - f.size * 0.16, x + ancho + margen_x,
                            base + f.size * 0.2), fill=tinta.acento)
            color = tinta.sobre_resaltado
        draw.text((x, y), texto, font=f, fill=color, anchor="la")
        x += ancho + margen_x


def pintar(draw: ImageDraw.ImageDraw, maqueta: Maqueta, x: float, y: float, ancho: float,
           tinta: Tinta, alineacion: str = "izquierda") -> float:
    """Dibuja la maqueta con su esquina superior izquierda en (x, y). Devuelve la y final."""
    f = fuente(maqueta.ruta, maqueta.tam)
    for i, renglon in enumerate(maqueta.renglones):
        largo = f.getlength(unir(renglon))
        inicio = x + (ancho - largo) / 2 if alineacion == "centro" else x
        _pintar_renglon(draw, renglon, f, inicio, y + i * maqueta.paso, tinta)
    return y + maqueta.alto


def foto_cubrir(ruta: Path, tam: tuple[int, int], enfoque: object = "centro") -> Image.Image:
    """Recorta la foto para llenar `tam` sin deformarla (como «cubrir»), respetando la rotación."""
    with Image.open(ruta) as original:
        imagen = ImageOps.exif_transpose(original).convert("RGB")
    if isinstance(enfoque, (list, tuple)) and len(enfoque) == 2:
        centro = (float(enfoque[0]), float(enfoque[1]))
    else:
        centro = ENFOQUES.get(str(enfoque), ENFOQUES["centro"])
    return ImageOps.fit(imagen, tam, method=Image.Resampling.LANCZOS, centering=centro)


def circulo(imagen: Image.Image, diametro: int) -> Image.Image:
    """La imagen recortada en círculo, con fondo transparente."""
    cuadrada = ImageOps.fit(imagen.convert("RGBA"), (diametro * 2, diametro * 2), Image.Resampling.LANCZOS)
    mascara = Image.new("L", cuadrada.size, 0)
    ImageDraw.Draw(mascara).ellipse((0, 0, *cuadrada.size), fill=255)
    cuadrada.putalpha(mascara)
    return cuadrada.resize((diametro, diametro), Image.Resampling.LANCZOS)


def flecha(draw: ImageDraw.ImageDraw, x: float, y: float, largo: float, color: str, grosor: int = 5) -> None:
    """Flecha hacia la derecha dibujada con líneas (no depende de que la fuente tenga «→»)."""
    punta = largo * 0.36
    draw.line((x, y, x + largo, y), fill=color, width=grosor)
    draw.line((x + largo - punta, y - punta, x + largo, y), fill=color, width=grosor)
    draw.line((x + largo - punta, y + punta, x + largo, y), fill=color, width=grosor)


def pildora(draw: ImageDraw.ImageDraw, maqueta: Maqueta, centro_x: float, y: float, ancho_max: float,
            fondo: str, color: str) -> float:
    """Botón redondeado con el texto de la acción. Devuelve la y final."""
    f = fuente(maqueta.ruta, maqueta.tam)
    largo = max(f.getlength(unir(r)) for r in maqueta.renglones)
    relleno_x, relleno_y = f.size * 0.9, f.size * 0.55
    ancho = min(ancho_max, largo + 2 * relleno_x)
    alto = maqueta.alto + 2 * relleno_y
    x0 = centro_x - ancho / 2
    draw.rounded_rectangle((x0, y, x0 + ancho, y + alto), radius=alto / 2 if alto < 140 else 36, fill=fondo)
    pintar(draw, maqueta, x0 + relleno_x, y + relleno_y, ancho - 2 * relleno_x, Tinta(color, color), "centro")
    return y + alto
