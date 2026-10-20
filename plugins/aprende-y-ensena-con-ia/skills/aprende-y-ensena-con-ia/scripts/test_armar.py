"""Pruebas de armar.py. Correr con: python3 -m unittest discover -s scripts -p "test_*.py" """
from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import armar  # noqa: E402

EJEMPLOS = Path(__file__).resolve().parent.parent / "ejemplos"


PLANTILLAS = Path(__file__).resolve().parent.parent / "plantillas"


def datos_de_pagina(html: str) -> dict:
    bloque = armar.BLOQUE_DATOS.search(html)
    assert bloque, "la página no tiene bloque de datos"
    return json.loads(bloque.group(2))


def sin_datos(html: str) -> str:
    return armar.BLOQUE_DATOS.sub("", html, count=1)


def examen_minimo() -> dict:
    tarjetas = [{"tema": "Cobro", "pregunta": f"Pregunta {i}", "respuesta": f"Respuesta {i}"} for i in range(6)]
    examen = [
        {"tema": "Cobro", "tipo": "opcion", "pregunta": f"P{i}", "opciones": ["a", "b", "c"], "correcta": i % 3, "explicacion": "x"}
        for i in range(4)
    ] + [{"tema": "Cobro", "tipo": "vf", "pregunta": "Afirmación", "correcta": False, "explicacion": "x"}]
    return {"titulo": "Examen", "temas": ["Cobro"], "tarjetas": tarjetas, "examen": examen, "minimo": 80}


class RevisionTest(unittest.TestCase):
    def test_ejemplos_publicados_pasan_sin_errores(self) -> None:
        casos = {
            "examen-del-equipo": "examen-del-equipo-restaurante.json",
            "mapa-del-libro": "mapa-del-libro-habitos-atomicos.json",
            "apuntes": "apuntes-margen-de-ganancia.json",
        }
        for tipo, archivo in casos.items():
            with self.subTest(tipo=tipo):
                datos = json.loads((EJEMPLOS / archivo).read_text(encoding="utf-8"))
                self.assertEqual(armar.revisar(tipo, datos).errores, [])

    def test_examen_valido(self) -> None:
        self.assertEqual(armar.revisar("examen-del-equipo", examen_minimo()).errores, [])

    def test_correcta_fuera_de_rango_es_error(self) -> None:
        datos = examen_minimo()
        datos["examen"][0] = {**datos["examen"][0], "correcta": 5}
        errores = armar.revisar("examen-del-equipo", datos).errores
        self.assertTrue(any("correcta" in e for e in errores))

    def test_tema_inexistente_es_error(self) -> None:
        datos = examen_minimo()
        datos["tarjetas"][0] = {**datos["tarjetas"][0], "tema": "Otro"}
        errores = armar.revisar("examen-del-equipo", datos).errores
        self.assertTrue(any("Otro" in e for e in errores))

    def test_verdadero_falso_exige_booleano(self) -> None:
        datos = examen_minimo()
        datos["examen"][4] = {**datos["examen"][4], "correcta": "falso"}
        self.assertTrue(armar.revisar("examen-del-equipo", datos).errores)

    def test_misma_letra_siempre_da_aviso(self) -> None:
        datos = examen_minimo()
        datos["examen"] = [{**q, "correcta": 0} if q["tipo"] == "opcion" else q for q in datos["examen"]]
        avisos = armar.revisar("examen-del-equipo", datos).avisos
        self.assertTrue(any("misma letra" in a for a in avisos))

    def test_mapa_tipo_desconocido_es_error(self) -> None:
        datos = json.loads((EJEMPLOS / "mapa-del-libro-habitos-atomicos.json").read_text(encoding="utf-8"))
        errores = armar.revisar("mapa-del-libro", {**datos, "tipo": "pelicula"}).errores
        self.assertTrue(any("tipo" in e for e in errores))

    def test_mapa_con_pocas_ramas_es_error(self) -> None:
        datos = {"titulo": "Libro", "idea_central": "Idea", "ramas": [{"titulo": "A", "puntos": ["x"]}], "preguntas": ["a", "b"]}
        self.assertTrue(armar.revisar("mapa-del-libro", datos).errores)


class ArmadoTest(unittest.TestCase):
    def test_solo_cambia_el_bloque_de_datos(self) -> None:
        for tipo, archivo in armar.PLANTILLAS.items():
            with self.subTest(tipo=tipo):
                plantilla = (PLANTILLAS / archivo).read_text(encoding="utf-8")
                self.assertEqual(len(armar.BLOQUE_DATOS.findall(plantilla)), 1)
                html = armar.armar(tipo, examen_minimo())
                self.assertEqual(sin_datos(html), sin_datos(plantilla))

    def test_texto_peligroso_no_cierra_el_script(self) -> None:
        datos = examen_minimo()
        datos["titulo"] = "Cuidado </script><script>alert(1)</script> <!-- x"
        html = armar.armar("examen-del-equipo", datos)
        self.assertEqual(html.count("</script>"), 2)  # solo los dos cierres de la plantilla
        self.assertEqual(datos_de_pagina(html)["titulo"], datos["titulo"])

    def test_tarjetas_quita_el_examen(self) -> None:
        html = armar.armar("tarjetas", examen_minimo())
        self.assertEqual(datos_de_pagina(html)["examen"], [])

    def test_linea_de_comandos_escribe_la_pagina(self) -> None:
        with tempfile.TemporaryDirectory() as carpeta:
            entrada = Path(carpeta) / "datos.json"
            salida = Path(carpeta) / "salida.html"
            entrada.write_text(json.dumps(examen_minimo()), encoding="utf-8")
            proceso = subprocess.run(
                [sys.executable, str(Path(armar.__file__)), "examen-del-equipo", str(entrada), str(salida)],
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(proceso.returncode, 0, proceso.stderr)
            self.assertTrue(salida.exists())

    def test_linea_de_comandos_con_errores_no_escribe(self) -> None:
        with tempfile.TemporaryDirectory() as carpeta:
            entrada = Path(carpeta) / "datos.json"
            salida = Path(carpeta) / "salida.html"
            entrada.write_text(json.dumps({"titulo": "x"}), encoding="utf-8")
            proceso = subprocess.run(
                [sys.executable, str(Path(armar.__file__)), "mapa-del-libro", str(entrada), str(salida)],
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(proceso.returncode, 1)
            self.assertFalse(salida.exists())


if __name__ == "__main__":
    unittest.main()
