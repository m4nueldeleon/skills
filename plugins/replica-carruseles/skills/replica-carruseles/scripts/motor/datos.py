"""Leer y revisar carrusel.json antes de dibujar.

Los errores (que impiden dibujar) salen como ErrorCarrusel con un mensaje claro.
Los avisos (que conviene corregir, pero no impiden dibujar) se devuelven en una lista.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from . import colores, paleta
from .fuentes import Fuentes, elegir

TIPOS = ("portada", "texto", "lista", "foto", "cierre")
ESTILOS = ("claro", "oscuro", "foto")
TAMANOS_TITULO = {"compacto": 0.88, "normal": 1.0, "grande": 1.14}
COLOR_POR_OMISION = "#1F3A5F"
MAX_LAMINAS = 20  # lo máximo que acepta Instagram en un carrusel
MAX_PALABRAS = 25
MAX_PALABRAS_LISTA = 35
LARGO_NOMBRE = 48  # caracteres del título que se citan en los avisos


class ErrorCarrusel(Exception):
    """Un problema en carrusel.json que impide dibujar."""


@dataclass(frozen=True)
class Diseno:
    alineacion: str = "izquierda"
    mayusculas: bool = False
    acento_modo: str = "color"
    escala_titulo: float = 1.0
    fondo: str | None = None


@dataclass(frozen=True)
class Carrusel:
    marca: dict
    estilo: str
    diseno: Diseno
    fuentes: Fuentes
    laminas: tuple
    base: Path
    numerar: bool = True
    caption: str = ""
    hashtags: tuple = field(default_factory=tuple)
    credito: str = ""


def contar_palabras(lamina: dict) -> int:
    partes = [lamina.get(k, "") for k in ("titulo", "subtitulo", "texto", "accion")]
    for item in lamina.get("items", []) or []:
        if isinstance(item, dict):
            partes += [item.get("texto", ""), item.get("nota", "")]
        else:
            partes.append(str(item))
    return sum(len(str(p).replace("*", " ").split()) for p in partes if p)


def nombre_lamina(lamina: dict) -> str:
    """Cómo se reconoce la lámina por su contenido: «03 · Te decides solo por la foto».

    El «03» es el número del punto (campo `numero`), que casi nunca coincide con la posición de la lámina.
    """
    texto = str(lamina.get("titulo") or lamina.get("texto") or "")
    texto = " ".join(texto.replace("*", "").split())
    if len(texto) > LARGO_NOMBRE:
        texto = texto[:LARGO_NOMBRE].rstrip() + "…"
    numero = str(lamina.get("numero") or "").strip()
    return " · ".join(p for p in (numero, texto) if p)


def etiqueta(lamina: dict, n: int, total: int) -> str:
    """«Lámina 5 de 9 («03 · Te decides solo por la foto»)»: la posición es la del archivo 05.png."""
    nombre = nombre_lamina(lamina) if isinstance(lamina, dict) else ""
    return f"Lámina {n} de {total}" + (f" («{nombre}»)" if nombre else "")


def _leer_json(ruta: Path) -> dict:
    if not ruta.is_file():
        raise ErrorCarrusel(f"No encuentro el archivo {ruta}")
    try:
        datos = json.loads(ruta.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ErrorCarrusel(f"carrusel.json no es JSON válido (línea {error.lineno}): {error.msg}") from error
    if not isinstance(datos, dict) or not isinstance(datos.get("laminas"), list):
        raise ErrorCarrusel("carrusel.json necesita una lista «laminas» con las láminas del carrusel")
    return datos


def _marca(datos: dict, avisos: list, estilo: str, fondo: str | None) -> dict:
    marca = dict(datos.get("marca") or {})
    colores_in = dict(marca.get("colores") or {})
    if not colores_in.get("principal"):
        avisos.append(f"No hay color principal de la marca: usé {COLOR_POR_OMISION}.")
    try:
        principal = colores.normalizar(colores_in.get("principal") or COLOR_POR_OMISION)
        acento = colores.normalizar(colores_in["acento"]) if colores_in.get("acento") else None
    except ValueError as error:
        raise ErrorCarrusel(f"Color de la marca: {error}") from error
    if paleta.acento_cambiado(estilo, principal, acento, fondo):
        avisos.append(f"El color de acento {acento} es casi tan oscuro como la letra y no resaltaría: en la palabra "
                      f"clave usé el principal {principal}. El acento es el color más vivo de la marca, no el más oscuro.")
    usuario = str(marca.get("usuario") or "").strip()
    if usuario and not usuario.startswith("@"):
        usuario = "@" + usuario
    return {**marca, "usuario": usuario, "nombre": str(marca.get("nombre") or "").strip(),
            "principal": principal, "acento": acento}


def _diseno(datos: dict, estilo: str) -> Diseno:
    pedido = dict(datos.get("diseno") or {})
    alineacion = pedido.get("alineacion", "izquierda")
    if alineacion not in ("izquierda", "centro"):
        raise ErrorCarrusel("diseno.alineacion debe ser «izquierda» o «centro»")
    modo = pedido.get("acento_modo", "resaltado" if estilo == "foto" else "color")
    if modo not in ("color", "resaltado"):
        raise ErrorCarrusel("diseno.acento_modo debe ser «color» o «resaltado»")
    tamano = pedido.get("tamano_titulo", "normal")
    if tamano not in TAMANOS_TITULO:
        raise ErrorCarrusel("diseno.tamano_titulo debe ser «compacto», «normal» o «grande»")
    fondo = pedido.get("fondo")
    if fondo and not colores.es_hex(fondo):
        raise ErrorCarrusel(f"diseno.fondo «{fondo}» no es un color en hexadecimal")
    return Diseno(alineacion=alineacion, mayusculas=bool(pedido.get("mayusculas", estilo == "foto")),
                  acento_modo=modo, escala_titulo=TAMANOS_TITULO[tamano],
                  fondo=colores.normalizar(fondo) if fondo else None)


def _ruta_foto(valor: object, base: Path, nombre: str, avisos: list) -> Path | None:
    if not valor:
        return None
    ruta = (base / str(valor)).expanduser()
    if ruta.is_file():
        return ruta
    avisos.append(f"{nombre}: no encontré la foto «{valor}»; la dibujé sin foto.")
    return None


def _lamina(cruda: object, n: int, total: int, base: Path, avisos: list) -> dict:
    nombre = etiqueta(cruda, n, total)
    if not isinstance(cruda, dict):
        raise ErrorCarrusel(f"{nombre} debe ser un objeto con «tipo»")
    tipo = cruda.get("tipo")
    if tipo not in TIPOS:
        raise ErrorCarrusel(f"{nombre}: el tipo «{tipo}» no existe. Usa: {', '.join(TIPOS)}")
    lamina = {**cruda, "n": n, "foto": _ruta_foto(cruda.get("foto"), base, nombre, avisos)}
    if tipo in ("portada", "cierre") and not lamina.get("titulo"):
        raise ErrorCarrusel(f"{nombre} ({tipo}) necesita «titulo»")
    if tipo == "texto" and not (lamina.get("titulo") or lamina.get("texto")):
        raise ErrorCarrusel(f"{nombre} (texto) necesita «titulo» o «texto»")
    if tipo == "lista" and not (2 <= len(lamina.get("items") or []) <= 6):
        raise ErrorCarrusel(f"{nombre} (lista) necesita entre 2 y 6 «items»")
    if tipo == "foto" and lamina["foto"] is None:
        lamina = {**lamina, "tipo": "texto"}
    tope = MAX_PALABRAS_LISTA if tipo == "lista" else MAX_PALABRAS
    palabras = contar_palabras(lamina)
    if palabras > tope:
        avisos.append(f"{nombre}: tiene {palabras} palabras; el tope es {tope}. Recórtala "
                      f"(es la que sale como {n:02d}.png).")
    return lamina


def _clave(valor: object) -> str:
    """El texto sin asteriscos, signos, mayúsculas ni espacios de más: para encontrar repetidos."""
    sin_signos = re.sub(r"[^\w\s]", " ", str(valor or "").replace("*", " ").lower())
    return " ".join(sin_signos.split())


def _revisar_repetidos(laminas: list, avisos: list) -> None:
    """Dos láminas con el mismo título o el mismo texto casi siempre son un error al copiar o recortar."""
    total = len(laminas)
    for campo, que in (("titulo", "el mismo título"), ("texto", "el mismo texto")):
        vistas: dict = {}
        for lam in laminas:
            clave = _clave(lam.get(campo))
            if not clave:
                continue
            if clave not in vistas:
                vistas[clave] = lam
                continue
            primera = vistas[clave]
            otra = etiqueta(lam, lam["n"], total)
            avisos.append(f"{etiqueta(primera, primera['n'], total)} y {otra[0].lower()}{otra[1:]} tienen {que}. "
                          "Cada lámina lleva su propia idea: corrige una de las dos.")


def _revisar_orden(laminas: list, avisos: list) -> None:
    total = len(laminas)
    if not 2 <= total <= MAX_LAMINAS:
        raise ErrorCarrusel(f"Un carrusel lleva de 2 a {MAX_LAMINAS} láminas; este tiene {total}")
    if not 6 <= total <= 10:
        avisos.append(f"Tiene {total} láminas; para un carrusel del día funcionan mejor de 6 a 10.")
    if laminas[0]["tipo"] != "portada":
        avisos.append("La primera lámina no es «portada»: la portada es la que hace que deslicen.")
    if laminas[-1]["tipo"] != "cierre":
        avisos.append("La última lámina no es «cierre»: ahí va la acción que le pides a la gente.")


def _revisar_texto_publicacion(caption: str, hashtags: list, avisos: list) -> None:
    primera = caption.strip().split("\n", 1)[0] if caption.strip() else ""
    if not primera:
        avisos.append("No hay «caption» (el texto de la publicación).")
    elif len(primera) > 125:
        avisos.append("La primera línea del caption pasa de 125 caracteres: Instagram la corta con «más».")
    if not 3 <= len(hashtags) <= 5:
        avisos.append(f"Lleva {len(hashtags)} hashtags; usa de 3 a 5 que describan el tema.")


def cargar(ruta_json: Path, estilo_forzado: str | None = None) -> tuple[Carrusel, list]:
    """Lee carrusel.json, lo revisa y devuelve (Carrusel, avisos)."""
    ruta_json = Path(ruta_json).expanduser().resolve()
    datos = _leer_json(ruta_json)
    base = ruta_json.parent
    avisos: list = []
    estilo = estilo_forzado or datos.get("estilo", "claro")
    if estilo not in ESTILOS:
        raise ErrorCarrusel(f"El estilo «{estilo}» no existe. Usa: {', '.join(ESTILOS)}")
    total = len(datos["laminas"])
    laminas = [_lamina(c, i + 1, total, base, avisos) for i, c in enumerate(datos["laminas"])]
    _revisar_orden(laminas, avisos)
    _revisar_repetidos(laminas, avisos)
    hashtags = [str(h).strip() for h in datos.get("hashtags") or [] if str(h).strip()]
    hashtags = [h if h.startswith("#") else "#" + h for h in hashtags]
    caption = str(datos.get("caption") or "")
    _revisar_texto_publicacion(caption, hashtags, avisos)
    try:
        fuentes = elegir(datos.get("fuentes"), estilo, base)
    except ValueError as error:
        raise ErrorCarrusel(str(error)) from error
    diseno = _diseno(datos, estilo)
    carrusel = Carrusel(marca=_marca(datos, avisos, estilo, diseno.fondo), estilo=estilo, diseno=diseno,
                        fuentes=fuentes, laminas=tuple(laminas), base=base,
                        numerar=bool(datos.get("numerar", True)), caption=caption,
                        hashtags=tuple(hashtags), credito=str(datos.get("credito") or "").strip())
    return carrusel, avisos
