#!/usr/bin/env python3
"""Arma las láminas de un carrusel (PNG 1080x1350, listas para Instagram y Facebook).

Uso:
    python3 carrusel.py carrusel.json                 # PNG en ./laminas/ junto al JSON
    python3 carrusel.py carrusel.json --salida otra/  # en otra carpeta
    python3 carrusel.py carrusel.json --estilo oscuro # probar otro estilo sin tocar el JSON
    python3 carrusel.py carrusel.json --html          # además, una vista previa en HTML

Necesita Pillow. Si no está, intenta instalarla con pip; si no se puede, deja una vista previa
en HTML (carrusel.html) para que no te quedes sin nada.

Salida: 01.png, 02.png…, revision.jpg (todas juntas en chiquito) y caption.txt.
Código de salida: 0 todo bien · 1 algún texto no cupo (recórtalo) · 2 el JSON tiene un error.
"""
from __future__ import annotations

import argparse
import importlib
import re
import site
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from motor.datos import Carrusel, ErrorCarrusel, cargar  # noqa: E402

INTENTOS_PIP = (["--quiet"], ["--quiet", "--user"], ["--quiet", "--break-system-packages"])


def asegurar_pillow() -> bool:
    """¿Hay Pillow? Si no, intenta instalarla. Devuelve True si quedó lista."""
    try:
        importlib.import_module("PIL.Image")
        return True
    except ImportError:
        pass
    print("Instalando Pillow (la biblioteca que dibuja las imágenes)…", file=sys.stderr)
    for opciones in INTENTOS_PIP:
        hecho = subprocess.run([sys.executable, "-m", "pip", "install", *opciones, "pillow"],
                               capture_output=True, text=True)
        if hecho.returncode == 0:
            usuario = site.getusersitepackages()
            if "--user" in opciones and usuario not in sys.path:
                sys.path.append(usuario)  # lo instalado con --user no siempre está en la ruta todavía
            importlib.invalidate_caches()
            try:
                importlib.import_module("PIL.Image")
                return True
            except ImportError:
                continue
    return False


def _limpiar_salida(salida: Path) -> None:
    """Borra las láminas viejas (01.png, 02.png…) para que no se mezclen con las nuevas."""
    for viejo in salida.glob("*.png"):
        if re.fullmatch(r"\d{2}\.png", viejo.name):
            viejo.unlink()


def _hoja_revision(imagenes: list, destino: Path) -> None:
    """Todas las láminas en chiquito, como se ven al pasar el dedo en el celular."""
    from PIL import Image

    columnas, ancho, alto, aire = 3, 320, 400, 16
    filas = (len(imagenes) + columnas - 1) // columnas
    hoja = Image.new("RGB", (columnas * (ancho + aire) + aire, filas * (alto + aire) + aire), "#D9DADC")
    for i, imagen in enumerate(imagenes):
        x = aire + (i % columnas) * (ancho + aire)
        y = aire + (i // columnas) * (alto + aire)
        hoja.paste(imagen.resize((ancho, alto), Image.Resampling.LANCZOS), (x, y))
    hoja.save(destino, quality=86)


def dibujar_png(carrusel: Carrusel, salida: Path) -> list:
    from motor.laminas import dibujar

    _limpiar_salida(salida)
    resultado = dibujar(carrusel)
    for imagen, reg in resultado:
        imagen.save(salida / f"{reg.n:02d}.png", optimize=True)
    _hoja_revision([imagen for imagen, _ in resultado], salida / "revision.jpg")
    return [reg for _, reg in resultado]


def escribir_caption(carrusel: Carrusel, salida: Path) -> Path:
    partes = [carrusel.caption.strip()]
    if carrusel.credito:
        partes.append(f"Inspirado en {carrusel.credito}.")
    if carrusel.hashtags:
        partes.append(" ".join(carrusel.hashtags))
    destino = salida / "caption.txt"
    destino.write_text("\n\n".join(p for p in partes if p) + "\n", encoding="utf-8")
    return destino


def _reporte(carrusel: Carrusel, registros: list, avisos: list) -> int:
    from motor.datos import contar_palabras

    falla = False
    for lam, reg in zip(carrusel.laminas, registros):  # noqa: B905 (mismo largo; strict pide Python 3.10)
        tam = reg.tamanos.get("titulo") or reg.tamanos.get("items") or reg.tamanos.get("texto")
        detalle = f"letra del título {tam} px · " if tam else ""
        print(f"  {reg.n:02d}.png · {lam['tipo']} · {detalle}{contar_palabras(lam)} palabras")
        for aviso in dict.fromkeys(reg.avisos):
            print(f"     ! {aviso}")
        if reg.no_cupo:
            falla = True
            print(f"     ✖ No cupo ({', '.join(reg.no_cupo)}) ni con la letra más chica: recorta ese texto.")
    for aviso in avisos:
        print(f"  ! {aviso}")
    return 1 if falla else 0


def principal(argumentos: list[str] | None = None) -> int:
    lector = argparse.ArgumentParser(description="Arma las láminas PNG de un carrusel.json")
    lector.add_argument("json", type=Path, help="ruta a carrusel.json")
    lector.add_argument("--salida", type=Path, help="carpeta de las láminas (por omisión: laminas/ junto al JSON)")
    lector.add_argument("--estilo", choices=("claro", "oscuro", "foto"), help="usa otro estilo sin tocar el JSON")
    lector.add_argument("--html", action="store_true", help="además de los PNG, deja una vista previa HTML")
    lector.add_argument("--solo-html", action="store_true", help="solo la vista previa HTML (sin Pillow)")
    args = lector.parse_args(argumentos)
    try:
        carrusel, avisos = cargar(args.json, args.estilo)
    except ErrorCarrusel as error:
        print(f"✖ {error}", file=sys.stderr)
        return 2
    salida = (args.salida or carrusel.base / "laminas").expanduser().resolve()
    salida.mkdir(parents=True, exist_ok=True)
    caption = escribir_caption(carrusel, salida)
    if args.solo_html or not asegurar_pillow():
        from motor.respaldo_html import escribir_html

        vista = escribir_html(carrusel, salida)
        if not args.solo_html:
            print("✖ No pude instalar Pillow, así que no hay PNG.", file=sys.stderr)
        print(f"Vista previa: {vista}\nTexto de la publicación: {caption}")
        for aviso in avisos:
            print(f"  ! {aviso}")
        return 0 if args.solo_html else 1
    registros = dibujar_png(carrusel, salida)
    if args.html:
        from motor.respaldo_html import escribir_html

        escribir_html(carrusel, salida)
    print(f"Listo: {len(registros)} láminas en {salida}")
    codigo = _reporte(carrusel, registros, avisos)
    print(f"Revisa {salida / 'revision.jpg'} y el texto en {caption}")
    return codigo


if __name__ == "__main__":
    sys.exit(principal())
