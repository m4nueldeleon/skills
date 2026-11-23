"""Pruebas del motor de carruseles. Corre con: python3 -m unittest scripts/test_carrusel.py (o pytest)."""
from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))

import carrusel  # noqa: E402
from motor import colores, datos, paleta  # noqa: E402
from motor.texto import envolver, palabras, quitar_emojis, unir  # noqa: E402

HAY_PILLOW = importlib.util.find_spec("PIL") is not None


def medir_fijo(texto: str) -> float:
    return len(texto) * 10.0


def carrusel_minimo(**cambios: object) -> dict:
    base = {
        "marca": {"nombre": "Panadería Prueba", "usuario": "panaderia.prueba", "colores": {"principal": "#B4432B"}},
        "estilo": "claro",
        "laminas": [
            {"tipo": "portada", "titulo": "Tu pan dura *más* así", "subtitulo": "3 trucos de mostrador"},
            {"tipo": "texto", "numero": "01", "titulo": "Guárdalo en *tela*",
             "texto": "La bolsa de plástico lo ablanda."},
            {"tipo": "lista", "titulo": "Resumen",
             "items": ["Tela", {"texto": "Rebanado", "nota": "Al momento"}, "Congela"]},
            {"tipo": "foto", "titulo": "Sin foto", "texto": "Se vuelve texto."},
            {"tipo": "cierre", "titulo": "¿Lo *pruebas*?", "texto": "Pide el tuyo.", "accion": "Escribe PAN"},
        ],
        "caption": "Tres trucos para que tu pan dure más.",
        "hashtags": ["pan", "#panaderia", "#trucos"],
    }
    base.update(cambios)
    return base


def escribir(directorio: Path, contenido: dict) -> Path:
    ruta = directorio / "carrusel.json"
    ruta.write_text(json.dumps(contenido, ensure_ascii=False), encoding="utf-8")
    return ruta


class Colores(unittest.TestCase):
    def test_contraste_extremos(self) -> None:
        self.assertAlmostEqual(colores.contraste("#FFFFFF", "#000000"), 21.0, places=1)

    def test_asegurar_contraste_cumple(self) -> None:
        for color, fondo in (("#FFE14D", "#FFFFFF"), ("#1A2B3C", "#101010"), ("#0E7C7B", "#FFFFFF")):
            self.assertGreaterEqual(colores.contraste(colores.asegurar_contraste(color, fondo), fondo), 4.5)

    def test_color_invalido(self) -> None:
        with self.assertRaises(ValueError):
            colores.normalizar("rojo")

    def test_paletas_legibles(self) -> None:
        for estilo in ("claro", "oscuro", "foto"):
            for principal in ("#0E7C7B", "#FFD400", "#1B1B1B", "#F2F2F2"):
                p = paleta.para(estilo, principal, None)
                self.assertGreaterEqual(colores.contraste(p.texto, p.fondo), 4.5, (estilo, principal))
                self.assertGreaterEqual(colores.contraste(p.suave, p.fondo), 4.5, (estilo, principal))
                c = paleta.para_cierre(estilo, principal, None)
                self.assertGreaterEqual(colores.contraste(c.texto, c.fondo), 4.5, (estilo, principal))
                self.assertGreaterEqual(colores.contraste(c.sobre_boton, c.boton), 3.0, (estilo, principal))


class Texto(unittest.TestCase):
    def test_acentos(self) -> None:
        (parrafo,) = palabras("No esperes a que te *duela la* muela")
        self.assertEqual([p.texto for p in parrafo if p.acento], ["duela", "la"])

    def test_signo_pegado_al_acento(self) -> None:
        (parrafo,) = palabras("¿Te pasa *esto*? Sí")
        self.assertEqual(unir(parrafo), "¿Te pasa esto? Sí")

    def test_envolver_respeta_ancho(self) -> None:
        renglones, partida = envolver("una dos tres cuatro cinco seis siete ocho", medir_fijo, 120)
        self.assertFalse(partida)
        self.assertTrue(all(medir_fijo(unir(r)) <= 120 for r in renglones))

    def test_palabra_larguisima_se_parte(self) -> None:
        _, partida = envolver("supercalifragilisticoespialidoso", medir_fijo, 100)
        self.assertTrue(partida)

    def test_sin_viuda(self) -> None:
        renglones, _ = envolver("uno dos tres cuatro cinco", medir_fijo, 190)
        self.assertGreater(len(renglones[-1]), 1)

    def test_quitar_emojis(self) -> None:
        limpio, habia = quitar_emojis("Hola 😀 mundo ✨")
        self.assertTrue(habia)
        self.assertEqual(limpio, "Hola mundo")


class Datos(unittest.TestCase):
    def test_carga_y_avisos(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            c, avisos = datos.cargar(escribir(Path(tmp), carrusel_minimo()))
        self.assertEqual(c.marca["usuario"], "@panaderia.prueba")
        self.assertEqual(c.hashtags[0], "#pan")
        self.assertEqual(c.laminas[3]["tipo"], "texto")  # foto sin archivo -> texto
        self.assertTrue(any("6 a 10" in a for a in avisos))

    def test_tipo_inexistente(self) -> None:
        malo = carrusel_minimo(laminas=[{"tipo": "video", "titulo": "x"}, {"tipo": "cierre", "titulo": "y"}])
        with tempfile.TemporaryDirectory() as tmp, self.assertRaises(datos.ErrorCarrusel):
            datos.cargar(escribir(Path(tmp), malo))

    def test_color_malo(self) -> None:
        malo = carrusel_minimo(marca={"colores": {"principal": "azulito"}})
        with tempfile.TemporaryDirectory() as tmp, self.assertRaises(datos.ErrorCarrusel):
            datos.cargar(escribir(Path(tmp), malo))

    def test_lamina_larga_avisa(self) -> None:
        largo = carrusel_minimo()
        largo["laminas"][1]["texto"] = " ".join(["palabra"] * 40)
        with tempfile.TemporaryDirectory() as tmp:
            _, avisos = datos.cargar(escribir(Path(tmp), largo))
        self.assertTrue(any("Lámina 2" in a and "Recórtala" in a for a in avisos))

    def test_json_roto(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ruta = Path(tmp) / "carrusel.json"
            ruta.write_text("{ no es json", encoding="utf-8")
            self.assertEqual(carrusel.principal([str(ruta)]), 2)


@unittest.skipUnless(HAY_PILLOW, "Pillow no está instalada")
class Dibujo(unittest.TestCase):
    def test_los_tres_estilos(self) -> None:
        from PIL import Image

        for estilo in ("claro", "oscuro", "foto"):
            with tempfile.TemporaryDirectory() as tmp:
                ruta = escribir(Path(tmp), carrusel_minimo(estilo=estilo))
                self.assertEqual(carrusel.principal([str(ruta)]), 0, estilo)
                pngs = sorted((Path(tmp) / "laminas").glob("*.png"))
                self.assertEqual(len(pngs), 5)
                for png in pngs:
                    with Image.open(png) as imagen:
                        self.assertEqual(imagen.size, (1080, 1350))
                self.assertTrue((Path(tmp) / "laminas" / "revision.jpg").is_file())
                self.assertIn("#panaderia", (Path(tmp) / "laminas" / "caption.txt").read_text(encoding="utf-8"))

    def test_texto_que_no_cabe_devuelve_1(self) -> None:
        enorme = carrusel_minimo()
        enorme["laminas"][1]["texto"] = " ".join(["desbordado"] * 160)
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(carrusel.principal([str(escribir(Path(tmp), enorme))]), 1)

    def test_foto_y_cierre_con_foto(self) -> None:
        from PIL import Image

        with tempfile.TemporaryDirectory() as tmp:
            Image.new("RGB", (800, 1200), "#557766").save(Path(tmp) / "f.jpg")
            con_foto = carrusel_minimo()
            con_foto["laminas"][3]["foto"] = "f.jpg"
            con_foto["laminas"][4]["foto"] = "f.jpg"
            self.assertEqual(carrusel.principal([str(escribir(Path(tmp), con_foto))]), 0)

    def test_logo_en_cierre_y_diseno(self) -> None:
        from PIL import Image

        with tempfile.TemporaryDirectory() as tmp:
            Image.new("RGBA", (600, 200), (20, 40, 200, 255)).save(Path(tmp) / "logo.png")
            con_logo = carrusel_minimo(diseno={"alineacion": "centro", "mayusculas": True,
                                               "acento_modo": "resaltado", "tamano_titulo": "grande"},
                                       fuentes={"titulo": "oswald", "texto": "montserrat"})
            con_logo["marca"] = {**con_logo["marca"], "logo": "logo.png"}
            self.assertEqual(carrusel.principal([str(escribir(Path(tmp), con_logo)), "--html"]), 0)
            self.assertTrue((Path(tmp) / "laminas" / "carrusel.html").is_file())


class VistaPrevia(unittest.TestCase):
    def test_html_sin_pillow(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ruta = escribir(Path(tmp), carrusel_minimo())
            self.assertEqual(carrusel.principal([str(ruta), "--solo-html"]), 0)
            pagina = (Path(tmp) / "laminas" / "carrusel.html").read_text(encoding="utf-8")
        self.assertEqual(pagina.count('class="marco"'), 5)
        self.assertIn('<span class="acento">más</span>', pagina)


if __name__ == "__main__":
    unittest.main()
