#!/usr/bin/env python3
"""Revisa la carpeta de un equipo de agentes antes de usarlo en Claude Code.

Uso:  python3 revisar_equipo.py [carpeta-del-equipo]   (por omisión, la carpeta actual)

Revisa que cada archivo de .claude/agents tenga su encabezado bien escrito, que ningún agente
tenga herramientas peligrosas, que el coordinador nombre a agentes que existen, que exista la
ficha del negocio (CLAUDE.md), que los archivos de datos citados existan y que no haya llaves ni
números de tarjeta. Solo lee archivos: no cambia nada. Sale con código 1 si encuentra errores.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

NOMBRE_VALIDO = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MODELOS = {"inherit", "sonnet", "opus", "haiku", "fable"}
COLORES = {"red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"}
PELIGROSAS = {"Bash": "puede correr comandos en tu computadora"}
SECRETOS = [
    re.compile(p)
    for p in (
        r"sk-ant-[A-Za-z0-9_-]{20,}",
        r"\bsk-[A-Za-z0-9]{32,}",
        r"AKIA[0-9A-Z]{16}",
        r"\bgh[pousr]_[A-Za-z0-9]{30,}",
        r"AIza[0-9A-Za-z_-]{35}",
        r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
    )
]
CUENTA = re.compile(r"\b(?:\d[ -]?){14,17}\d\b")  # tarjeta (15-16) o CLABE (18)
RUTA_DATOS = re.compile(r"`(datos/[^`\s]+)`")


def leer_encabezado(texto: str) -> tuple[dict[str, str] | None, str]:
    """Devuelve (campos, cuerpo) de un archivo con encabezado entre líneas '---'."""
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?(.*)$", texto, re.S)
    if not m:
        return None, texto
    campos: dict[str, str] = {}
    for linea in m.group(1).splitlines():
        if not linea.strip() or linea.lstrip().startswith("#"):
            continue
        clave, sep, valor = linea.partition(":")
        if sep and not linea.startswith((" ", "\t")):
            campos[clave.strip()] = valor.strip().strip('"').strip("'")
    return campos, m.group(2)


def separar_herramientas(valor: str) -> list[str]:
    """'Agent(a, b), Read, Write' -> ['Agent(a, b)', 'Read', 'Write']"""
    partes: list[str] = []
    actual, nivel = "", 0
    for c in valor.strip("[]"):
        nivel += (c == "(") - (c == ")")
        if c == "," and nivel == 0:
            partes.append(actual.strip())
            actual = ""
        else:
            actual += c
    if actual.strip():
        partes.append(actual.strip())
    return [p.strip("'\"") for p in partes]


def revisar_agente(
    archivo: Path, carpeta: Path, errores: list[str], avisos: list[str]
) -> tuple[str | None, list[str]]:
    texto = archivo.read_text(encoding="utf-8")
    campos, cuerpo = leer_encabezado(texto)
    nombre_archivo = archivo.stem
    if campos is None:
        errores.append(f"{archivo.name}: falta el encabezado entre líneas '---' al inicio.")
        return None, []
    nombre = campos.get("name", "")
    if not nombre:
        errores.append(f"{archivo.name}: falta 'name'.")
    elif nombre != nombre_archivo:
        errores.append(f"{archivo.name}: 'name' dice «{nombre}» y el archivo se llama «{nombre_archivo}»; deben ser iguales.")
    elif not NOMBRE_VALIDO.match(nombre):
        errores.append(f"{archivo.name}: 'name' solo puede llevar minúsculas, números y guiones (sin acentos ni espacios).")
    descripcion = campos.get("description", "")
    if not descripcion:
        errores.append(f"{archivo.name}: falta 'description' (es lo que Claude lee para saber cuándo usarlo).")
    elif len(descripcion) < 40:
        avisos.append(f"{archivo.name}: la 'description' es muy corta; di qué tareas le tocan.")
    herramientas = separar_herramientas(campos.get("tools", ""))
    if not campos.get("tools"):
        avisos.append(f"{archivo.name}: no tiene 'tools'; heredaría TODAS las herramientas (incluidas las de correr comandos).")
    for h in herramientas:
        base = h.split("(")[0]
        if base in PELIGROSAS:
            errores.append(f"{archivo.name}: tiene «{base}», que {PELIGROSAS[base]}. Quítala en esta primera versión.")
        if base.startswith("mcp__"):
            avisos.append(f"{archivo.name}: tiene un conector ({base}); revisa que solo pueda leer y redactar.")
    modelo = campos.get("model")
    if modelo and modelo not in MODELOS and not modelo.startswith("claude-"):
        avisos.append(f"{archivo.name}: 'model: {modelo}' no es un valor conocido; usa 'inherit'.")
    color = campos.get("color")
    if color and color not in COLORES:
        avisos.append(f"{archivo.name}: 'color: {color}' no es válido; usa uno de {', '.join(sorted(COLORES))}.")
    if len(cuerpo.strip()) < 200:
        errores.append(f"{archivo.name}: casi no tiene instrucciones debajo del encabezado.")
    if "[" in cuerpo and re.search(r"\[(?:Negocio|Departamento|nombre del dueño|tarea)[^\]]*\]", cuerpo):
        errores.append(f"{archivo.name}: quedaron huecos de la plantilla sin llenar (como [Negocio] o [tarea]).")
    if "borrador" not in cuerpo.lower():
        avisos.append(f"{archivo.name}: no dice que trabaja en borrador; agrégalo a sus reglas.")
    for ruta in sorted(set(RUTA_DATOS.findall(cuerpo))):
        if not (carpeta / ruta).exists():
            avisos.append(f"{archivo.name}: menciona `{ruta}`, pero ese archivo no existe todavía.")
    return nombre or nombre_archivo, herramientas


def revisar_coordinador(
    herramientas: list[str], nombres: set[str], errores: list[str], avisos: list[str]
) -> None:
    agente = next((h for h in herramientas if h.startswith("Agent")), None)
    if agente is None:
        errores.append("coordinador.md: le falta «Agent(...)» en 'tools'; sin eso no puede repartir trabajo.")
        return
    m = re.match(r"Agent\((.*)\)", agente)
    lista = [n.strip() for n in m.group(1).split(",")] if m else []
    if not lista:
        avisos.append("coordinador.md: «Agent» sin lista; podría llamar a cualquier agente de tu computadora.")
        return
    departamentos = nombres - {"coordinador"}
    for n in lista:
        if n not in departamentos:
            errores.append(f"coordinador.md: nombra a «{n}», pero no existe .claude/agents/{n}.md.")
    for n in sorted(departamentos - set(lista)):
        avisos.append(f"coordinador.md: no incluye a «{n}» en su lista; no podrá pasarle trabajo.")


def buscar_secretos(carpeta: Path, errores: list[str]) -> None:
    for archivo in carpeta.rglob("*"):
        if not archivo.is_file() or archivo.suffix.lower() not in {".md", ".txt", ".json", ".csv"}:
            continue
        texto = archivo.read_text(encoding="utf-8", errors="ignore")
        rel = archivo.relative_to(carpeta)
        if any(p.search(texto) for p in SECRETOS):
            errores.append(f"{rel}: parece tener una llave o contraseña. Bórrala.")
        if CUENTA.search(texto):
            errores.append(f"{rel}: parece tener un número de tarjeta o cuenta. Bórralo.")


def main() -> int:
    carpeta = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    errores: list[str] = []
    avisos: list[str] = []
    dir_agentes = carpeta / ".claude" / "agents"
    sin_punto = carpeta / "claude" / "agents"
    if not dir_agentes.is_dir() and sin_punto.is_dir():
        avisos.append(
            "Encontré claude/agents/ sin punto (así viene en el ejemplo). En tu carpeta real tiene que llamarse "
            ".claude/agents/ para que Claude Code cargue los agentes."
        )
        dir_agentes = sin_punto
    if not dir_agentes.is_dir():
        print(f"✖ No encontré {carpeta / '.claude' / 'agents'}. ¿Es la carpeta correcta del equipo?")
        return 1
    if not (carpeta / "CLAUDE.md").is_file():
        errores.append("Falta CLAUDE.md (la ficha del negocio que leen todos los agentes).")
    if not (carpeta / "entregables").is_dir():
        avisos.append("Falta la carpeta entregables/ (ahí dejan sus borradores).")
    archivos = sorted(dir_agentes.glob("*.md"))
    if not archivos:
        errores.append("No hay agentes en .claude/agents/.")
    nombres: set[str] = set()
    herramientas_coordinador: list[str] | None = None
    for archivo in archivos:
        nombre, herramientas = revisar_agente(archivo, carpeta, errores, avisos)
        if nombre:
            nombres.add(nombre)
        if archivo.stem == "coordinador":
            herramientas_coordinador = herramientas
    if herramientas_coordinador is not None:
        revisar_coordinador(herramientas_coordinador, nombres, errores, avisos)
    else:
        avisos.append("No hay coordinador.md; puedes llamar a cada agente por su nombre.")
    buscar_secretos(carpeta, errores)

    print(f"Equipo en {carpeta}")
    print(f"Agentes encontrados: {', '.join(sorted(nombres)) or 'ninguno'}")
    for e in errores:
        print(f"✖ {e}")
    for a in avisos:
        print(f"⚠ {a}")
    if errores:
        print(f"\n✖ {len(errores)} error(es) por corregir antes de usar el equipo.")
        return 1
    print(f"\n✔ Equipo listo ({len(nombres)} agentes)" + (f", con {len(avisos)} aviso(s)." if avisos else "."))
    return 0


if __name__ == "__main__":
    sys.exit(main())
