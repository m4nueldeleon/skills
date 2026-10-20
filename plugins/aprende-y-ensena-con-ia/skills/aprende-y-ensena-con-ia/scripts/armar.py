#!/usr/bin/env python3
"""Arma una página de la skill aprende-y-ensena-con-ia con una plantilla y un archivo de datos.

Uso:
    python3 scripts/armar.py mapa-del-libro    datos.json salida.html
    python3 scripts/armar.py apuntes           datos.json salida.html
    python3 scripts/armar.py tarjetas          datos.json salida.html
    python3 scripts/armar.py examen-del-equipo datos.json salida.html

Revisa los datos (campos obligatorios, cantidades y largos), escribe la página lista para abrir
en el navegador y avisa lo que conviene corregir. Si hay errores, no escribe nada y sale con
código 1. Solo usa la biblioteca estándar de Python 3.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PLANTILLAS = {
    "mapa-del-libro": "mapa-del-libro.html",
    "apuntes": "apuntes.html",
    "tarjetas": "tarjetas-y-examen.html",
    "examen-del-equipo": "tarjetas-y-examen.html",
}
ICONOS = {
    "idea", "check", "alerta", "reloj", "dinero", "persona", "equipo", "chat", "calendario",
    "grafica", "corazon", "estrella", "libro", "escudo", "carrito", "telefono", "flecha", "meta",
}
# El bloque real empieza al inicio de un renglón (así no lo confunde con una mención en un comentario).
MAX_PALABRAS_COLUMNA_MAPA = 230
BLOQUE_DATOS = re.compile(
    r'^(<script type="application/json" id="datos">)(.*?)(</script>)', re.DOTALL | re.MULTILINE
)


class Revision:
    """Junta errores (impiden armar la página) y avisos (conviene corregir)."""

    def __init__(self) -> None:
        self.errores: list[str] = []
        self.avisos: list[str] = []

    def error(self, mensaje: str) -> None:
        self.errores.append(mensaje)

    def aviso(self, mensaje: str) -> None:
        self.avisos.append(mensaje)


def palabras(texto: object) -> int:
    return len(str(texto).split()) if isinstance(texto, str) else 0


def texto_obligatorio(rev: Revision, datos: dict, campo: str, donde: str = "") -> str:
    valor = datos.get(campo)
    if not isinstance(valor, str) or not valor.strip():
        rev.error(f"Falta «{campo}»{donde}.")
        return ""
    return valor


def largo(rev: Revision, texto: object, maximo: int, donde: str) -> None:
    if palabras(texto) > maximo:
        rev.aviso(f"{donde} tiene {palabras(texto)} palabras (lo ideal: {maximo} o menos).")


def lista(rev: Revision, datos: dict, campo: str, minimo: int, maximo: int, obligatoria: bool = True) -> list:
    valor = datos.get(campo)
    if valor is None and not obligatoria:
        return []
    if not isinstance(valor, list):
        rev.error(f"«{campo}» tiene que ser una lista.")
        return []
    if not minimo <= len(valor) <= maximo:
        rev.error(f"«{campo}» lleva {len(valor)} elementos; tienen que ser de {minimo} a {maximo}.")
    return valor


def revisar_mapa(datos: dict, rev: Revision) -> None:
    texto_obligatorio(rev, datos, "titulo")
    if datos.get("tipo", "libro") not in ("libro", "otro"):
        rev.error("«tipo» tiene que ser «libro» u «otro» (curso, conferencia o tema).")
    largo(rev, texto_obligatorio(rev, datos, "idea_central"), 25, "La idea central")
    ramas = lista(rev, datos, "ramas", 4, 8)
    for i, rama in enumerate(ramas, 1):
        if not isinstance(rama, dict):
            rev.error(f"La rama {i} no tiene el formato correcto.")
            continue
        largo(rev, texto_obligatorio(rev, rama, "titulo", f" en la rama {i}"), 6, f"El título de la rama {i}")
        puntos = rama.get("puntos", [])
        if not isinstance(puntos, list) or not 1 <= len(puntos) <= 3:
            rev.error(f"La rama {i} necesita de 1 a 3 puntos.")
        else:
            for p in puntos:
                largo(rev, p, 14, f"Un punto de la rama {i}")
        largo(rev, rama.get("en_tu_negocio", ""), 22, f"«En tu negocio» de la rama {i}")
    # Medido al imprimir: una columna de ~230 palabras todavía cabe en una hoja carta horizontal.
    validas = [r for r in ramas if isinstance(r, dict)]
    mitad = -(-len(validas) // 2)
    for columna in (validas[:mitad], validas[mitad:]):
        total = sum(palabras(r.get("titulo")) + palabras(r.get("en_tu_negocio"))
                    + sum(palabras(p) for p in r.get("puntos", []) if isinstance(r.get("puntos"), list))
                    for r in columna)
        if total > MAX_PALABRAS_COLUMNA_MAPA:
            rev.aviso(f"Una columna del mapa lleva {total} palabras: puede no caber en una hoja. Recorta puntos.")
    for p in lista(rev, datos, "preguntas", 2, 4):
        if not isinstance(p, str) or not p.strip():
            rev.error("Hay una pregunta vacía.")
    if not str(datos.get("fuente", "")).strip():
        rev.aviso("Falta «fuente»: di si sale de lo que pegó el usuario, de lo que se conoce del libro o de ambos.")


def revisar_apuntes(datos: dict, rev: Revision) -> None:
    largo(rev, texto_obligatorio(rev, datos, "tema"), 8, "El tema")
    largo(rev, texto_obligatorio(rev, datos, "en_una_frase"), 30, "La frase principal")
    for i, paso in enumerate(lista(rev, datos, "pasos", 2, 5), 1):
        if not isinstance(paso, dict):
            rev.error(f"El paso {i} no tiene el formato correcto.")
            continue
        largo(rev, texto_obligatorio(rev, paso, "titulo", f" en el paso {i}"), 4, f"El título del paso {i}")
        largo(rev, paso.get("texto", ""), 16, f"El texto del paso {i}")
    for i, clave in enumerate(lista(rev, datos, "claves", 2, 4), 1):
        if not isinstance(clave, dict):
            rev.error(f"La clave {i} no tiene el formato correcto.")
            continue
        texto_obligatorio(rev, clave, "titulo", f" en la clave {i}")
        largo(rev, clave.get("texto", ""), 28, f"El texto de la clave {i}")
        if clave.get("icono") not in ICONOS:
            rev.aviso(f"El ícono «{clave.get('icono')}» de la clave {i} no existe; se usará «idea».")
    ejemplo = datos.get("ejemplo")
    if ejemplo is not None:
        if not isinstance(ejemplo, dict):
            rev.error("«ejemplo» no tiene el formato correcto.")
        else:
            largo(rev, ejemplo.get("texto", ""), 45, "El texto del ejemplo")
            cuentas = ejemplo.get("cuentas", [])
            if not isinstance(cuentas, list) or len(cuentas) > 5:
                rev.error("«cuentas» del ejemplo tiene que ser una lista de 0 a 5 renglones.")
    largo(rev, datos.get("cuidado", ""), 35, "«Cuidado con esto»")
    for i, p in enumerate(lista(rev, datos, "palabras", 0, 6, obligatoria=False), 1):
        if not isinstance(p, dict) or not str(p.get("palabra", "")).strip():
            rev.error(f"La palabra clave {i} no tiene el formato correcto.")
    for i, p in enumerate(lista(rev, datos, "preguntas", 2, 4), 1):
        if not isinstance(p, dict):
            rev.error(f"La pregunta {i} no tiene el formato correcto.")
            continue
        texto_obligatorio(rev, p, "pregunta", f" en la pregunta {i}")
        texto_obligatorio(rev, p, "respuesta", f" en la pregunta {i}")


def revisar_tarjetas_y_examen(datos: dict, rev: Revision, con_examen: bool) -> None:
    texto_obligatorio(rev, datos, "titulo")
    minimo = datos.get("minimo", 80)
    if not isinstance(minimo, (int, float)) or not 1 <= minimo <= 100:
        rev.error("«minimo» tiene que ser un número de 1 a 100.")
    temas = lista(rev, datos, "temas", 1, 6)
    temas_validos = {t for t in temas if isinstance(t, str) and t.strip()}
    vistas: set[str] = set()
    for i, t in enumerate(lista(rev, datos, "tarjetas", 6, 30), 1):
        if not isinstance(t, dict):
            rev.error(f"La tarjeta {i} no tiene el formato correcto.")
            continue
        pregunta = texto_obligatorio(rev, t, "pregunta", f" en la tarjeta {i}")
        largo(rev, pregunta, 18, f"La pregunta de la tarjeta {i}")
        largo(rev, texto_obligatorio(rev, t, "respuesta", f" en la tarjeta {i}"), 30, f"La respuesta de la tarjeta {i}")
        if t.get("tema") not in temas_validos:
            rev.error(f"La tarjeta {i} usa el tema «{t.get('tema')}», que no está en «temas».")
        if pregunta.strip().lower() in vistas:
            rev.aviso(f"La tarjeta {i} repite una pregunta.")
        vistas.add(pregunta.strip().lower())

    examen = datos.get("examen") or []
    if not con_examen:
        if examen:
            rev.aviso("/tarjetas no lleva examen: se ignorarán las preguntas de «examen».")
        return
    examen = lista(rev, datos, "examen", 5, 20)
    posiciones = []
    for i, q in enumerate(examen, 1):
        if not isinstance(q, dict):
            rev.error(f"La pregunta {i} del examen no tiene el formato correcto.")
            continue
        texto_obligatorio(rev, q, "pregunta", f" en la pregunta {i} del examen")
        if q.get("tema") not in temas_validos:
            rev.error(f"La pregunta {i} del examen usa el tema «{q.get('tema')}», que no está en «temas».")
        tipo = q.get("tipo")
        if tipo == "opcion":
            opciones = q.get("opciones")
            if not isinstance(opciones, list) or not 3 <= len(opciones) <= 4:
                rev.error(f"La pregunta {i} necesita de 3 a 4 opciones.")
                continue
            correcta = q.get("correcta")
            if not isinstance(correcta, int) or isinstance(correcta, bool) or not 0 <= correcta < len(opciones):
                rev.error(f"En la pregunta {i}, «correcta» tiene que ser la posición de la opción buena (de 0 a {len(opciones) - 1}).")
            else:
                posiciones.append(correcta)
            if not str(q.get("explicacion", "")).strip():
                rev.aviso(f"La pregunta {i} no trae explicación.")
        elif tipo == "vf":
            if not isinstance(q.get("correcta"), bool):
                rev.error(f"En la pregunta {i} (verdadero o falso), «correcta» tiene que ser true o false.")
        elif tipo == "abierta":
            texto_obligatorio(rev, q, "respuesta_modelo", f" en la pregunta {i} del examen")
            menciones = q.get("debe_mencionar")
            if not isinstance(menciones, list) or not menciones:
                rev.error(f"La pregunta abierta {i} necesita «debe_mencionar» con al menos una idea.")
        else:
            rev.error(f"La pregunta {i} tiene un tipo desconocido «{tipo}» (usa opcion, vf o abierta).")
    if len(posiciones) >= 4 and len(set(posiciones)) == 1:
        rev.aviso("Todas las respuestas correctas están en la misma letra: cambia el orden de algunas opciones.")
    temas_examen = {q.get("tema") for q in examen if isinstance(q, dict)}
    for tema in temas_validos - temas_examen:
        rev.aviso(f"El tema «{tema}» no tiene preguntas en el examen.")


def revisar(tipo: str, datos: object) -> Revision:
    rev = Revision()
    if not isinstance(datos, dict):
        rev.error("Los datos tienen que ser un objeto JSON ({ … }).")
        return rev
    if tipo == "mapa-del-libro":
        revisar_mapa(datos, rev)
    elif tipo == "apuntes":
        revisar_apuntes(datos, rev)
    else:
        revisar_tarjetas_y_examen(datos, rev, con_examen=(tipo == "examen-del-equipo"))
    return rev


def json_para_html(datos: dict) -> str:
    """JSON legible que no puede cerrar la etiqueta <script> antes de tiempo."""
    texto = json.dumps(datos, ensure_ascii=False, indent=2)
    return texto.replace("</", "<\\/").replace("<!--", "\\u003c!--")


def armar(tipo: str, datos: dict) -> str:
    plantilla = (RAIZ / "plantillas" / PLANTILLAS[tipo]).read_text(encoding="utf-8")
    if tipo == "tarjetas":
        datos = {**datos, "examen": []}
    bloque = "\n" + json_para_html(datos) + "\n"
    resultado, cambios = BLOQUE_DATOS.subn(lambda m: m.group(1) + bloque + m.group(3), plantilla, count=1)
    if cambios != 1:
        raise ValueError("La plantilla no tiene el bloque de datos.")
    return resultado


def main(argumentos: list[str]) -> int:
    if len(argumentos) != 3 or argumentos[0] not in PLANTILLAS:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    tipo, ruta_datos, ruta_salida = argumentos
    try:
        datos = json.loads(Path(ruta_datos).read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"✖ No encuentro el archivo de datos: {ruta_datos}", file=sys.stderr)
        return 1
    except json.JSONDecodeError as e:
        print(f"✖ El archivo de datos no es JSON válido (renglón {e.lineno}, columna {e.colno}): {e.msg}", file=sys.stderr)
        return 1
    rev = revisar(tipo, datos)
    for aviso in rev.avisos:
        print(f"• Aviso: {aviso}")
    if rev.errores:
        print(f"✖ {len(rev.errores)} error(es); no se escribió la página:", file=sys.stderr)
        for error in rev.errores:
            print(f"  - {error}", file=sys.stderr)
        return 1
    salida = Path(ruta_salida)
    if not re.fullmatch(r"[A-Za-z0-9._-]+", salida.name):
        print("• Aviso: el nombre del archivo lleva espacios, acentos o símbolos; uno como «examen-meseros.html» se abre más fácil.")
    salida.parent.mkdir(parents=True, exist_ok=True)
    salida.write_text(armar(tipo, datos), encoding="utf-8")
    print(f"✔ Página lista: {salida}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
