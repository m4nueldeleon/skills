"""Vista previa del carrusel en un solo archivo HTML (sin Pillow).

Sirve para revisar el texto y el orden, o como respaldo si no se pudo instalar Pillow.
Los archivos para subir a Instagram son los PNG: este HTML solo se ve en el navegador.
"""
from __future__ import annotations

import base64
import html
import os
import re
from pathlib import Path

from . import paleta as paletas
from .datos import Carrusel

CSS = """
*{box-sizing:border-box;margin:0}
body{background:#d9dadc;font-family:X,system-ui,sans-serif;padding:24px;display:flex;flex-wrap:wrap;gap:24px}
.aviso{width:100%;font:16px/1.4 system-ui;color:#222}
.marco{width:540px;height:675px;overflow:hidden;flex:none;box-shadow:0 1px 4px rgba(0,0,0,.2)}
.lam{width:1080px;height:1350px;transform:scale(.5);transform-origin:0 0;position:relative;
  display:flex;flex-direction:column;padding:150px 96px 170px;background:var(--fondo);color:var(--texto)}
.lam.centro{text-align:center;align-items:center}
.cuerpo{flex:1;display:flex;flex-direction:column;justify-content:center;gap:40px;overflow:hidden;width:100%}
.serie .cuerpo{justify-content:flex-start;padding-top:170px}
.foto-arriba{margin:-150px -96px 60px;height:700px;background-size:cover;background-position:center;flex:none}
.titulo{font-family:T;font-size:var(--t,88px);line-height:1.05;letter-spacing:-.01em}
.mayus .titulo{text-transform:uppercase}
.texto{font-size:var(--x,50px);line-height:1.3;color:var(--suave)}
.numero{font-family:T;font-size:150px;line-height:.8;color:var(--acento)}
.acento{color:var(--acento)}
.resaltado .acento{background:var(--resaltado);color:var(--sobre);padding:0 .1em}
.barra{width:96px;height:10px;background:var(--acento)}
ol{list-style:none;padding:0;display:flex;flex-direction:column;gap:36px;font-family:F;font-size:48px}
ol li{display:flex;gap:40px;border-bottom:2px solid var(--linea);padding-bottom:36px}
ol li:last-child{border:0}
ol b{font-family:T;color:var(--acento);min-width:44px}
.nota{display:block;font-family:X;font-size:.8em;color:var(--suave)}
.pie{position:absolute;left:96px;right:96px;bottom:70px;display:flex;justify-content:space-between;
  font-family:F;font-size:32px;color:var(--suave)}
.boton{font-family:F;font-size:44px;background:var(--boton);color:var(--sobre-boton);border-radius:99px;
  padding:24px 48px;align-self:center}
.firma{font-family:F;font-size:46px}
.tipo-portada .titulo{font-size:128px}.tipo-cierre .titulo{font-size:104px}
.tipo-foto .titulo{font-size:72px}.tipo-foto .texto{font-size:42px}.tipo-foto .numero{font-size:84px}
.tipo-foto .cuerpo{justify-content:flex-start;gap:24px}
"""
AJUSTE = """
document.querySelectorAll('.cuerpo').forEach(function(c){
  var t=c.querySelector('.titulo'),x=c.querySelector('.texto'),n=0;
  while(c.scrollHeight>c.clientHeight&&n<40){n++;
    [t,x].forEach(function(e){if(!e)return;var s=parseFloat(getComputedStyle(e).fontSize);
      if(s>34)e.style.fontSize=(s-2)+'px';});}
});
"""


def _fuente_css(nombre: str, ruta: Path) -> str:
    datos = base64.b64encode(ruta.read_bytes()).decode("ascii")
    return f"@font-face{{font-family:{nombre};src:url(data:font/ttf;base64,{datos})}}"


def _marcado(texto: object) -> str:
    seguro = html.escape(str(texto or "")).replace("\n", "<br>")
    return re.sub(r"\*([^*]+)\*", r'<span class="acento">\1</span>', seguro)


def _vars(pal: paletas.Paleta) -> str:
    return (f"--fondo:{pal.fondo};--texto:{pal.texto};--suave:{pal.suave};--acento:{pal.acento};"
            f"--linea:{pal.linea};--resaltado:{pal.resaltado};--sobre:{pal.sobre_resaltado};"
            f"--boton:{pal.boton};--sobre-boton:{pal.sobre_boton}")


def _foto(lam: dict, salida: Path) -> str:
    if not lam.get("foto"):
        return ""
    ruta = os.path.relpath(lam["foto"], salida).replace(os.sep, "/")
    return f'<div class="foto-arriba" style="background-image:url(\'{html.escape(ruta)}\')"></div>'


def _contenido(lam: dict) -> str:
    partes = []
    if lam.get("numero"):
        partes.append(f'<div class="numero">{html.escape(str(lam["numero"]))}</div>')
    if lam["tipo"] == "portada":
        partes.insert(0, '<div class="barra"></div>')
    partes.append(f'<div class="titulo">{_marcado(lam.get("titulo"))}</div>')
    extra = lam.get("subtitulo") or lam.get("texto")
    if extra:
        partes.append(f'<div class="texto">{_marcado(extra)}</div>')
    if lam["tipo"] == "lista":
        filas = []
        for i, item in enumerate(lam["items"], 1):
            dato = item if isinstance(item, dict) else {"texto": item}
            nota = f'<span class="nota">{_marcado(dato.get("nota"))}</span>' if dato.get("nota") else ""
            filas.append(f"<li><b>{i}</b><span>{_marcado(dato.get('texto'))}{nota}</span></li>")
        partes.append(f"<ol>{''.join(filas)}</ol>")
    return "".join(partes)


def _cierre(lam: dict, carrusel: Carrusel) -> str:
    marca = carrusel.marca
    partes = [f'<div class="titulo">{_marcado(lam["titulo"])}</div>']
    if lam.get("texto"):
        partes.append(f'<div class="texto">{_marcado(lam["texto"])}</div>')
    if lam.get("accion"):
        partes.append(f'<div class="boton">{html.escape(str(lam["accion"]))}</div>')
    if marca.get("usuario"):
        partes.append(f'<div class="firma">{html.escape(marca["usuario"])}</div>')
    return "".join(partes)


def _lamina(lam: dict, carrusel: Carrusel, salida: Path, total: int) -> str:
    d = carrusel.diseno
    es_cierre = lam["tipo"] == "cierre"
    pal = paletas.para_cierre(carrusel.estilo, carrusel.marca["principal"], carrusel.marca.get("acento")) \
        if es_cierre else paletas.para(carrusel.estilo, carrusel.marca["principal"],
                                       carrusel.marca.get("acento"), d.fondo)
    clases = ["lam", f"tipo-{lam['tipo']}", "centro" if es_cierre or d.alineacion == "centro" else "",
              "mayus" if d.mayusculas else "", "resaltado" if d.acento_modo == "resaltado" else "",
              "serie" if lam.get("numero") and lam["tipo"] == "texto" else ""]
    cuerpo = _cierre(lam, carrusel) if es_cierre else _contenido(lam)
    derecha = "Desliza →" if lam["tipo"] == "portada" else (f"{lam['n']}/{total}" if carrusel.numerar else "")
    pie = "" if es_cierre else (f'<div class="pie"><span>{html.escape(carrusel.marca.get("usuario", ""))}'
                                f"</span><span>{derecha}</span></div>")
    return (f'<div class="marco"><section class="{" ".join(c for c in clases if c)}" style="{_vars(pal)}">'
            f'{_foto(lam, salida) if not es_cierre else ""}<div class="cuerpo">{cuerpo}</div>{pie}</section></div>')


def escribir_html(carrusel: Carrusel, salida: Path) -> Path:
    """Escribe carrusel.html en `salida` y devuelve su ruta."""
    f = carrusel.fuentes
    fuentes = "".join(_fuente_css(n, r) for n, r in (("T", f.titulo), ("X", f.texto), ("F", f.fuerte)))
    total = len(carrusel.laminas)
    laminas = "".join(_lamina(lam, carrusel, salida, total) for lam in carrusel.laminas)
    pagina = (
        '<!doctype html><html lang="es"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1"><title>Vista previa del carrusel</title>'
        f"<style>{fuentes}{CSS}</style></head><body>"
        '<p class="aviso">Vista previa a la mitad de tamaño. Para subir a Instagram usa los PNG '
        "(1080 × 1350) que arma <code>carrusel.py</code>.</p>"
        f"{laminas}<script>{AJUSTE}</script></body></html>"
    )
    destino = salida / "carrusel.html"
    destino.write_text(pagina, encoding="utf-8")
    return destino
