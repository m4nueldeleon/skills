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


class Acento(unittest.TestCase):
    """El acento es el color más vivo de la marca; si es casi tan oscuro como la letra, va el principal."""

    def test_acento_oscuro_usa_el_principal(self) -> None:
        p = paleta.para("claro", "#E85D8F", "#2D2A32")
        self.assertEqual(p.acento, colores.asegurar_contraste("#E85D8F", "#FFFFFF", 4.0))
        self.assertGreaterEqual(colores.contraste(p.acento, p.texto), 3.0)
        self.assertEqual(paleta.para("oscuro", "#E85D8F", "#2D2A32").acento, "#E85D8F")

    def test_acento_vivo_se_respeta(self) -> None:
        claro = paleta.para("claro", "#1F3A5F", "#F2B705")
        self.assertEqual(claro.acento, colores.asegurar_contraste("#F2B705", "#FFFFFF", 4.0))
        self.assertEqual(paleta.para("oscuro", "#B4432B", "#F2B705").acento, "#F2B705")
        self.assertFalse(paleta.acento_cambiado("oscuro", "#B4432B", "#FFD400"))

    def test_se_pierde(self) -> None:
        self.assertTrue(paleta.se_pierde("#2D2A32", "#FFFFFF", paleta.TINTA_CLARA))
        self.assertTrue(paleta.se_pierde("#101820", paleta.FONDO_OSCURO, paleta.TINTA_OSCURA))
        self.assertFalse(paleta.se_pierde("#0E7C7B", "#FFFFFF", paleta.TINTA_CLARA))

    def test_aviso_de_acento_oscuro(self) -> None:
        oscuro = carrusel_minimo()
        oscuro["marca"]["colores"] = {"principal": "#E85D8F", "acento": "#2D2A32"}
        vivo = carrusel_minimo()
        vivo["marca"]["colores"] = {"principal": "#1F3A5F", "acento": "#F2B705"}
        with tempfile.TemporaryDirectory() as tmp:
            _, avisos_oscuro = datos.cargar(escribir(Path(tmp), oscuro))
            _, avisos_vivo = datos.cargar(escribir(Path(tmp), vivo))
        self.assertTrue(any("#2D2A32" in a and "más vivo" in a for a in avisos_oscuro))
        self.assertFalse(any("acento" in a for a in avisos_vivo))


class ContrasteCierre(unittest.TestCase):
    """Toda letra sobre un color sólido queda en 4.5:1 o más, también con colores de marca medios."""

    MEDIOS = ("#E85D8F", "#C8507A", "#7A7A7A", "#D9558A", "#E0533A", "#2E86C1", "#0E7C7B", "#FFD400", "#1B1B1B")

    def test_todo_par_de_colores_llega_a_45(self) -> None:
        for estilo in ("claro", "oscuro", "foto"):
            for principal in self.MEDIOS:
                for acento in (None, "#2D2A32", "#F2B705"):
                    for p in (paleta.para(estilo, principal, acento), paleta.para_cierre(estilo, principal, acento)):
                        caso = (estilo, principal, acento)
                        self.assertGreaterEqual(colores.contraste(p.texto, p.fondo), 4.5, caso)
                        self.assertGreaterEqual(colores.contraste(p.suave, p.fondo), 4.5, caso)
                        self.assertGreaterEqual(colores.contraste(p.sobre_resaltado, p.resaltado), 4.5, caso)
                        self.assertGreaterEqual(colores.contraste(p.sobre_boton, p.boton), 4.5, caso)

    def test_rosa_medio_lleva_letra_casi_negra(self) -> None:
        cierre = paleta.para_cierre("claro", "#E85D8F", None)
        self.assertEqual(cierre.fondo, "#E85D8F")
        self.assertEqual(cierre.texto, colores.NEGRO)
        caja = paleta.para_cierre("foto", "#E85D8F", None)  # el caso de la prueba: blanco sobre rosa a 3.3:1
        self.assertNotEqual(caja.sobre_resaltado, colores.BLANCO)

    def test_color_sin_letra_legible_oscurece_el_fondo(self) -> None:
        self.assertLess(max(colores.contraste(colores.BLANCO, "#C8507A"),
                            colores.contraste(colores.NEGRO, "#C8507A")), 4.5)
        cierre = paleta.para_cierre("oscuro", "#C8507A", None)
        self.assertEqual(cierre.texto, colores.BLANCO)
        self.assertLess(colores.luminancia(cierre.fondo), colores.luminancia("#C8507A"))
        self.assertLess(colores.contraste(cierre.fondo, "#C8507A"), 1.3)  # sigue pareciéndose a la marca


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

    def test_aviso_de_largo_nombra_posicion_y_titulo(self) -> None:
        # La prueba real: «Lámina 5» se confundió con el punto «05». El aviso dice posición, total y título.
        largo = carrusel_minimo()
        largo["laminas"][3] = {"tipo": "texto", "numero": "05", "titulo": "Te decides solo por la *foto*",
                               "texto": " ".join(["palabra"] * 30)}
        with tempfile.TemporaryDirectory() as tmp:
            _, avisos = datos.cargar(escribir(Path(tmp), largo))
        (aviso,) = [a for a in avisos if "palabras" in a and "tope" in a]
        self.assertTrue(aviso.startswith("Lámina 4 de 5 («05 · Te decides solo por la foto»): tiene 36 palabras"))
        self.assertIn("el tope es 25", aviso)
        self.assertIn("04.png", aviso)

    def test_titulo_repetido_avisa(self) -> None:
        repetido = carrusel_minimo()
        repetido["laminas"][3]["titulo"] = "guárdalo en tela."
        with tempfile.TemporaryDirectory() as tmp:
            _, avisos = datos.cargar(escribir(Path(tmp), repetido))
        self.assertTrue(any(a.startswith("Lámina 2 de 5 («01 · Guárdalo en tela») y lámina 4 de 5")
                            and "mismo título" in a for a in avisos), avisos)

    def test_texto_repetido_avisa(self) -> None:
        repetido = carrusel_minimo()
        repetido["laminas"][4]["texto"] = "La bolsa de *plástico* lo ablanda"
        with tempfile.TemporaryDirectory() as tmp:
            _, avisos = datos.cargar(escribir(Path(tmp), repetido))
        self.assertTrue(any("Lámina 2 de 5" in a and "lámina 5 de 5" in a and "mismo texto" in a for a in avisos))

    def test_sin_repetidos_no_avisa(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            _, avisos = datos.cargar(escribir(Path(tmp), carrusel_minimo()))
        self.assertFalse(any("mismo" in a for a in avisos))

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

    def test_cierre_con_color_medio_se_dibuja_legible(self) -> None:
        from PIL import Image

        medio = carrusel_minimo()
        medio["marca"]["colores"] = {"principal": "#C8507A"}
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(carrusel.principal([str(escribir(Path(tmp), medio))]), 0)
            with Image.open(Path(tmp) / "laminas" / "05.png") as imagen:
                esquina = imagen.convert("RGB").getpixel((8, 8))
        fondo = paleta.para_cierre("claro", "#C8507A", None).fondo
        self.assertEqual(esquina, colores.a_rgb(fondo))
        self.assertGreaterEqual(colores.contraste(colores.BLANCO, fondo), 4.5)

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
