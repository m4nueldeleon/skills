#!/usr/bin/env python3
"""Revisa una presentación de la skill presentacion-cinematografica sin abrir un navegador.

Uso:
    python3 revisar.py presentacion.html

Qué revisa: que el motor esté completo, que no queden láminas ni textos de la plantilla, cuántas
palabras lleva cada lámina, que la historia tenga sus cinco partes en orden, que haya una sola
acción al final, las notas, las imágenes, el contraste de los colores de marca y frases de relleno.
También lista las cifras en pantalla y los datos por llenar para confirmarlos con el usuario.

Sale con 0 si no hay errores y con 1 si hay errores. Solo usa Python 3 (sin instalar nada).
"""
from __future__ import annotations

import re
import sys
from html.parser import HTMLParser

TIPOS = {"portada", "frase", "palabra", "cifra", "lista", "contraste", "pasos", "cita", "foto", "pausa", "llamado"}
PARTES = ["gancho", "problema", "solucion", "prueba", "llamado"]
NOMBRE_PARTE = {"gancho": "gancho", "problema": "problema", "solucion": "solución", "prueba": "prueba", "llamado": "llamado"}
VACIOS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
RESTOS_PLANTILLA = [
    "Título que promete", "Para quién es y qué se lleva", "Una sola idea, dicha como", "Primer punto, corto",
    "Cómo se vive el problema", "Una frase corta para respirar", "La solución, en una línea", "Una línea que lo explica",
    "Qué mide este número", "Lo que dijo un cliente real", "Una frase sobre lo que se ve", "La única acción que quieres",
]
RELLENO = [
    "lorem ipsum", "todo:", "xxx", "[insertar", "[nombre", "aquí va", "placeholder",
]
FRASES_IA = [
    "al siguiente nivel", "desbloquea", "potencia tu", "en la era digital", "hoy en día", "en el mundo actual",
    "cambia las reglas del juego", "el secreto es", "la clave del éxito", "todo empieza con", "tú puedes",
    "el momento es ahora", "revoluciona", "sin precedentes",
]
LIMITE_PALABRAS_AVISO = 25
LIMITE_POR_TIPO = {"lista": 32, "pasos": 32}  # se revelan por partes
LIMITE_PALABRAS_ERROR = 40


class Lamina:
    def __init__(self, numero: int, attrs: dict[str, str]) -> None:
        self.numero = numero
        self.tipo = attrs.get("data-tipo", "")
        self.parte = attrs.get("data-parte", "")
        self.ejemplo = "data-ejemplo" in attrs
        self.fondo = attrs.get("data-fondo", "")
        self.texto = []
        self.texto_cifras = []
        self.notas = []
        self.pasos = 0
        self.resaltados = 0
        self.ems = []
        self.faltas = []
        self.imagenes = []
        self.ranuras = []
        self.primeros = []  # (etiqueta, texto) de los primeros hijos de .contenido

    @property
    def visible(self) -> str:
        return re.sub(r"\s+", " ", " ".join(self.texto)).strip()

    @property
    def palabras(self) -> int:
        return len([p for p in self.visible.split(" ") if p])


class Lector(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.pila = []  # (etiqueta, banderas)
        self.titulo = ""
        self.generador = ""
        self.cuerpo = {}
        self.escenario = False
        self.motor = False
        self.laminas = []
        self.en_titulo = False
        self.guion = []

    def _bandera(self, nombre: str) -> bool:
        return any(nombre in b for _, b in self.pila)

    def handle_starttag(self, tag: str, attrs_lista: list[tuple[str, str | None]]) -> None:
        attrs = {k: (v if v is not None else "") for k, v in attrs_lista}
        clases = set(attrs.get("class", "").split())
        banderas = set()
        if tag == "meta" and attrs.get("name") == "generator":
            self.generador = attrs.get("content", "")
        if tag == "title":
            self.en_titulo = True
        if tag == "body":
            self.cuerpo = attrs
        if tag in ("script", "style"):
            banderas.add("codigo")
        if attrs.get("id") == "escenario":
            self.escenario = True
            banderas.add("escenario")
        if tag == "section" and "lamina" in clases and self._bandera("escenario") and not self._bandera("lamina"):
            self.laminas.append(Lamina(len(self.laminas) + 1, attrs))
            banderas.add("lamina")
        lam = self.laminas[-1] if self._bandera("lamina") or "lamina" in banderas else None
        if lam is not None:
            if "notas" in clases:
                banderas.add("notas")
            if "contenido" in clases:
                banderas.add("contenido")
            if "paso" in clases:
                lam.pasos += 1
            if "n" in clases:
                banderas.add("numero-paso")
            if tag == "em" and not self._bandera("notas"):
                lam.resaltados += 1
                banderas.add("em")
                lam.ems.append("")
            if tag == "mark" and "falta" in clases:
                banderas.add("falta")
                lam.faltas.append("")
            if "data-imagen" in attrs:
                lam.ranuras.append(attrs.get("data-imagen"))
            if tag == "img":
                lam.imagenes.append(attrs.get("src", ""))
            padre = self.pila[-1] if self.pila else None
            if padre and "contenido" in padre[1] and tag not in VACIOS:
                banderas.add("hijo-directo")
                lam.primeros.append([tag, clases, ""])
        if tag not in VACIOS:
            self.pila.append((tag, banderas))

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.en_titulo = False
        for i in range(len(self.pila) - 1, -1, -1):
            if self.pila[i][0] == tag:
                del self.pila[i:]
                break

    def handle_data(self, data: str) -> None:
        if self.en_titulo:
            self.titulo += data
        if self._bandera("codigo"):
            if "MOTOR · presentacion-cinematografica" in data:
                self.motor = True
            return
        if not self._bandera("lamina") or not self.laminas:
            return
        lam = self.laminas[-1]
        if self._bandera("notas"):
            lam.notas.append(data)
            return
        lam.texto.append(data)
        if not self._bandera("numero-paso"):
            lam.texto_cifras.append(data)
        if self._bandera("em") and lam.ems:
            lam.ems[-1] += data
        if self._bandera("falta") and lam.faltas:
            lam.faltas[-1] += data
        if self._bandera("hijo-directo") and lam.primeros:
            lam.primeros[-1][2] += data


def luminancia(hexa: str) -> float | None:
    hexa = hexa.lstrip("#")
    if len(hexa) == 3:
        hexa = "".join(c * 2 for c in hexa)
    if not re.fullmatch(r"[0-9a-fA-F]{6}", hexa):
        return None
    canales = []
    for i in (0, 2, 4):
        c = int(hexa[i:i + 2], 16) / 255
        canales.append(c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * canales[0] + 0.7152 * canales[1] + 0.0722 * canales[2]


def contraste(a: str, b: str) -> float | None:
    la, lb = luminancia(a), luminancia(b)
    if la is None or lb is None:
        return None
    alto, bajo = max(la, lb), min(la, lb)
    return (alto + 0.05) / (bajo + 0.05)


def revisar(ruta: str) -> tuple[list[str], list[str], list[Lamina], Lector]:
    with open(ruta, encoding="utf-8") as f:
        fuente = f.read()
    lector = Lector()
    lector.feed(fuente)
    laminas = lector.laminas
    errores, avisos = [], []

    if "presentacion-cinematografica" not in lector.generador or not lector.escenario or not lector.motor:
        errores.append("Falta el motor de la plantilla o está incompleto: copia el <style> y el <script> de plantilla/presentacion.html sin cambiarlos.")
    titulo = lector.titulo.strip()
    if not titulo or titulo == "Título de tu presentación":
        errores.append("El <title> sigue vacío o es el de la plantilla: pon el nombre de la presentación.")
    if not laminas:
        errores.append("No encontré láminas (<section class=\"lamina\"> dentro de <main id=\"escenario\">).")
        return errores, avisos, laminas, lector

    look = lector.cuerpo.get("data-look", "")
    if look not in {"cine", "estudio", "bosque", "marca"}:
        errores.append(f"El <body> debe llevar data-look=\"cine\", \"estudio\", \"bosque\" o \"marca\" (lleva «{look}»).")
    if look == "marca":
        estilo = lector.cuerpo.get("style", "")
        var = dict(re.findall(r"--([a-z-]+)\s*:\s*(#[0-9a-fA-F]{3,6})", estilo))
        if not {"fondo", "texto", "acento"} <= set(var):
            avisos.append("Look «marca»: pon en el <body> style=\"--fondo:#…;--texto:#…;--suave:#…;--acento:#…;--sobre-acento:#…\".")
        else:
            c1 = contraste(var["texto"], var["fondo"])
            c2 = contraste(var["acento"], var["fondo"])
            if c1 is not None and c1 < 4.5:
                errores.append(f"Look «marca»: el texto casi no se lee sobre el fondo (contraste {c1:.1f}; mínimo 4.5).")
            if c2 is not None and c2 < 3:
                avisos.append(f"Look «marca»: el color de acento se pierde sobre el fondo (contraste {c2:.1f}; mínimo 3). Úsalo de fondo en la lámina de revelación y no para texto.")

    secuencia = []
    seguidas = 1
    for i, lam in enumerate(laminas):
        id_ = f"Lámina {lam.numero}"
        bajo = lam.visible.lower()
        if lam.ejemplo:
            errores.append(f"{id_}: es una lámina de ejemplo de la plantilla (data-ejemplo). Bórrala o escríbela de nuevo.")
        for resto in RESTOS_PLANTILLA:
            if resto.lower() in bajo:
                errores.append(f"{id_}: quedó texto de la plantilla («{resto}…»).")
                break
        for r in RELLENO:
            if r in bajo:
                errores.append(f"{id_}: tiene texto de relleno («{r}»).")
                break
        if lam.tipo not in TIPOS:
            errores.append(f"{id_}: data-tipo «{lam.tipo}» no existe. Usa: {', '.join(sorted(TIPOS))}.")
        if lam.parte not in PARTES:
            avisos.append(f"{id_}: falta data-parte (gancho, problema, solucion, prueba o llamado).")
        else:
            secuencia.append((lam.numero, lam.parte))
        limite = LIMITE_POR_TIPO.get(lam.tipo, LIMITE_PALABRAS_AVISO)
        if lam.palabras > LIMITE_PALABRAS_ERROR:
            errores.append(f"{id_}: {lam.palabras} palabras en pantalla. Es más de una idea: pártela en dos láminas.")
        elif lam.palabras > limite:
            avisos.append(f"{id_}: {lam.palabras} palabras en pantalla; procura {limite} o menos.")
        if not "".join(lam.notas).strip():
            avisos.append(f"{id_}: no tiene notas (<aside class=\"notas\">) con lo que se dice.")
        if lam.resaltados > 1:
            avisos.append(f"{id_}: tiene {lam.resaltados} resaltados (<em>); deja uno para que destaque.")
        for em in lam.ems:
            if len(em.split()) > 4:
                avisos.append(f"{id_}: el resaltado «{em.strip()}» es largo; deja 4 palabras o menos (no se parte entre renglones).")
        for src in lam.imagenes:
            if not src.strip():
                errores.append(f"{id_}: hay una <img> sin imagen. Quítala: la ranura vacía ya se esconde sola.")
            elif src.startswith(("http://", "https://")):
                avisos.append(f"{id_}: la imagen viene de internet ({src[:60]}…); sin conexión no se verá.")
            elif not src.startswith("data:"):
                avisos.append(f"{id_}: la imagen «{src[:60]}» es un archivo aparte; corre empaquetar.py para meterla en el HTML.")
        if lam.tipo == "foto" and "foto" not in lam.ranuras:
            errores.append(f"{id_}: es de tipo foto pero no tiene <figure data-imagen=\"foto\">.")
        if lam.tipo in {"portada", "frase", "lista", "llamado"} and lam.primeros:
            etiqueta, clases, texto = lam.primeros[0]
            palabras = len(texto.split())
            if etiqueta not in {"h1", "h2"} and 0 < palabras <= 5 and not clases & {"gigante", "numero"}:
                avisos.append(f"{id_}: «{texto.strip()}» va encima del título como rótulo chico; quítalo o intégralo al título.")
        for frase in FRASES_IA:
            if frase in bajo:
                avisos.append(f"{id_}: «{frase}» suena a frase de folleto; cámbiala por un dato o una acción concreta.")
        if "—" in lam.visible:
            avisos.append(f"{id_}: tiene raya larga (—); usa punto o dos puntos.")
        if i and lam.tipo == laminas[i - 1].tipo:
            seguidas += 1
            if seguidas == 3:
                avisos.append(f"Láminas {lam.numero - 2} a {lam.numero}: tres «{lam.tipo}» seguidas; alterna con otro tipo.")
        else:
            seguidas = 1

    antitesis = len(re.findall(r"\bno es\b[^.!?]{1,60}\.\s*es\b", " ".join(l.visible.lower() for l in laminas)))
    if antitesis > 1:
        avisos.append(f"Hay {antitesis} frases «No es X. Es Y.»; deja una como máximo.")
    presentes = [p for p in PARTES if any(parte == p for _, parte in secuencia)]
    for p in PARTES:
        if p not in presentes:
            avisos.append(f"La historia no tiene {NOMBRE_PARTE[p]}: revisa el guion (gancho → problema → solución → prueba → llamado).")
    for (n1, p1), (n2, p2) in zip(secuencia, secuencia[1:]):
        if PARTES.index(p2) < PARTES.index(p1):
            avisos.append(f"La historia regresa: la lámina {n2} ({NOMBRE_PARTE[p2]}) va después de la {n1} ({NOMBRE_PARTE[p1]}).")
            break
    llamados = [l.numero for l in laminas if l.tipo == "llamado"]
    if len(llamados) != 1:
        avisos.append(f"Debe haber una sola lámina de llamado y hay {len(llamados)}: una presentación pide una sola acción.")
    if laminas[-1].tipo not in {"llamado", "pausa", "frase", "palabra"}:
        avisos.append("La última lámina no es el llamado: termina con la acción que quieres que hagan.")
    if sum(1 for l in laminas if l.fondo == "acento") > 2:
        avisos.append("Más de dos láminas con fondo de acento: guárdalo para revelar la solución.")
    if sum(1 for l in laminas if l.tipo == "pausa") > 2:
        avisos.append("Más de dos pausas: pierden fuerza si se repiten.")
    return errores, avisos, laminas, lector


def resumen_historia(laminas: list[Lamina]) -> str:
    tramos = []
    for lam in laminas:
        if not lam.parte:
            continue
        if tramos and tramos[-1][0] == lam.parte:
            tramos[-1][2] = lam.numero
        else:
            tramos.append([lam.parte, lam.numero, lam.numero])
    partes = []
    for parte, a, b in tramos:
        rango = f"{a}" if a == b else f"{a}-{b}"
        partes.append(f"{NOMBRE_PARTE.get(parte, parte)} ({rango})")
    return " → ".join(partes)


def main() -> None:
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    ruta = sys.argv[1]
    try:
        errores, avisos, laminas, lector = revisar(ruta)
    except (OSError, UnicodeDecodeError) as e:
        print(f"No pude leer {ruta}: {e}")
        sys.exit(2)
    look = lector.cuerpo.get("data-look", "?")
    print(f"\nRevisión · {ruta.split('/')[-1]} · {len(laminas)} láminas · look {look}\n")
    if laminas:
        print("Historia: " + (resumen_historia(laminas) or "sin partes marcadas"))
        print("Palabras por lámina: " + ", ".join(f"{l.numero}:{l.palabras}" for l in laminas))
        print(f"Revelados (clics extra): {sum(l.pasos for l in laminas)}\n")
    for e in errores:
        print("  ✖ " + e)
    for a in avisos:
        print("  ⚠ " + a)
    cifras = []
    for lam in laminas:
        for c in re.findall(r"[$€]?\d[\d.,]*\s?%?", " ".join(lam.texto_cifras)):
            c = c.strip(" .,")
            if c:
                cifras.append(f"{c} (lámina {lam.numero})")
    if cifras:
        print("\nCifras en pantalla. Confirma que cada una salió del usuario o de una fuente real:")
        print("  " + " · ".join(cifras))
    faltas = [f"{t.strip() or '[sin texto]'} (lámina {l.numero})" for l in laminas for t in l.faltas]
    if faltas:
        print("\nDatos por llenar (salen en amarillo hasta que los cambies):")
        print("  " + " · ".join(faltas))
    print("\n" + ("Lista para entregar." if not errores else f"Corrige {len(errores)} error(es) antes de entregar.") + "\n")
    sys.exit(1 if errores else 0)


if __name__ == "__main__":
    main()
