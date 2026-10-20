"""Pruebas de revisar_pagina.py. Corre con:  python3 -m unittest scripts/test_revisar_pagina.py"""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from revisar_pagina import a_markdown, colores_en, es_crema, es_morado, main, revisar  # noqa: E402

EJEMPLOS = Path(__file__).resolve().parent.parent / "ejemplos" / "panaderia"

BUENA = """<!doctype html><html lang="es-MX"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>:root{--acento:#1F6B4A} body{font-family:'Bricolage Grotesque',sans-serif}
.revela{transition:opacity .5s ease-out}
@media (prefers-reduced-motion: reduce){*{transition:none}}</style></head>
<body><h1>Tacos al pastor desde las 7 de la noche</h1>
<a href="https://wa.me/523300000000?text=Hola">Pedir por WhatsApp</a>
<a href="tel:+523300000000">Llamar</a>
<a href="https://www.google.com/maps/search/?api=1&query=Centro">Cómo llegar</a>
<img src="foto.jpg" alt="Trompo de pastor" width="800" height="600">
<a href="aviso-de-privacidad.html">Aviso de privacidad</a></body></html>"""

MALA = """<!doctype html><html><head><meta charset="utf-8">
<style>.hero{background:linear-gradient(135deg,#7c3aed,#db2777)} .btn{box-shadow:0 0 30px #a855f7;transition:all .3s ease-in}
.eyebrow{text-transform:uppercase;letter-spacing:.3em;font-size:12px} h1{font-family:'Playfair Display'}
.x{animation:flotar 6s infinite} @keyframes entrar{from{transform:scale(0)}}</style></head>
<body><h1>Bienvenidos</h1><span class="eyebrow">Servicios</span><section></section>
<span class="eyebrow">Proceso</span><section></section><span class="eyebrow">Contacto</span><section></section>
<p>Transformamos tu experiencia con soluciones innovadoras. Lorem ipsum. +10,000 clientes felices.</p>
<form><input placeholder="Fecha de nacimiento"></form>
<a href="https://wa.me/+52 33 0000 0000">WhatsApp</a><a href="#">Saber más</a>
<img src="https://images.unsplash.com/photo-1.jpg"></body></html>"""


def _revisar_texto(html, extras=("aviso-de-privacidad.html",)):
    with tempfile.TemporaryDirectory() as d:
        ruta = Path(d) / "index.html"
        ruta.write_text(html, encoding="utf-8")
        for nombre in extras:
            (Path(d) / nombre).write_text("<p>aviso</p>", encoding="utf-8")
        return revisar(ruta)


def _mensajes(reporte, nivel=None):
    return " | ".join(h["mensaje"] for h in reporte.hallazgos if nivel is None or h["nivel"] == nivel)


class PruebasColor(unittest.TestCase):
    def test_morado_y_crema(self):
        self.assertTrue(es_morado(colores_en("#7c3aed")[0]))
        self.assertFalse(es_morado(colores_en("#1F6B4A")[0]))
        self.assertTrue(es_crema(colores_en("#f5f1ea")[0]))
        self.assertFalse(es_crema(colores_en("#F4F6F2")[0]))

    def test_formatos(self):
        self.assertEqual(len(colores_en("rgb(10, 20, 30) hsl(280 60% 50%) purple #abc")), 4)


class PruebasRevision(unittest.TestCase):
    def test_pagina_buena_sin_faltas(self):
        r = _revisar_texto(BUENA)
        self.assertEqual(r.conteo()["falta"], 0, _mensajes(r, "falta"))
        self.assertIn("WhatsApp bien escrito", _mensajes(r, "ok"))

    def test_pagina_mala_detecta_rasgos(self):
        r = _revisar_texto(MALA)
        todo = _mensajes(r)
        for esperado in ("viewport", "degradado", "resplandor", "Playfair", "MAYÚSCULAS", "prefers-reduced-motion",
                         "scale(0)", "ease-in", "no paran nunca", "lorem ipsum", "Frases vacías", "+10,000 clientes",
                         "solo dígitos", "aviso de privacidad", "nacimiento", "sin texto alternativo",
                         "Fotos de banco", "transition: all", "href=\"#\""):
            self.assertIn(esperado.lower(), todo.lower(), f"no detectó: {esperado}")

    def test_whatsapp_sin_lada(self):
        r = _revisar_texto(BUENA.replace("523300000000?text", "3300000000?text"))
        self.assertIn("clave del país", _mensajes(r, "falta"))

    def test_sin_contacto(self):
        html = "<html lang='es'><head><meta name='viewport' content='width=device-width'></head><body><h1>Hola</h1></body></html>"
        self.assertIn("ningún botón", _mensajes(_revisar_texto(html), "falta"))

    def test_reserva_no_confunde_derechos_reservados(self):
        r = _revisar_texto(BUENA.replace("</body>", "<p>Todos los derechos reservados.</p></body>"))
        self.assertNotIn("términos y condiciones", _mensajes(r))

    def test_ocultar_sin_js_se_detecta(self):
        html = BUENA.replace("</style>", ".aparece{opacity:0}</style>").replace(
            "</body>", "<div class='aparece'>a</div><div class='aparece'>b</div><div class='aparece'>c</div></body>")
        self.assertIn("empieza invisible", _mensajes(_revisar_texto(html)))

    def test_enlace_legal_a_archivo_que_no_existe(self):
        r = _revisar_texto(BUENA, extras=())
        self.assertIn("todavía no existe", _mensajes(r, "falta"))

    def test_pendientes_en_atributos_y_largos(self):
        largo = "[PENDIENTE: foto de la fachada de frente, horizontal, con luz de día, sin coches estacionados enfrente y con el letrero]"
        html = BUENA.replace("</body>", f'<img src="x.jpg" alt="{largo}" width="1" height="1"><p>{largo}</p></body>')
        self.assertIn("2 marca(s) [PENDIENTE]", _mensajes(_revisar_texto(html), "falta"))

    def test_espanol_normal_no_es_texto_de_ejemplo(self):
        html = BUENA.replace("</body>", "<p>Llevamos la contabilidad de tu empresa. Te lo explicamos todo: C.P. Juan Pérez.</p></body>")
        self.assertNotIn("Textos de relleno o de ejemplo", _mensajes(_revisar_texto(html)))

    def test_whatsapp_business_y_diagonal(self):
        corto = _revisar_texto(BUENA.replace("https://wa.me/523300000000?text=Hola", "https://wa.me/message/ABC123"))
        self.assertIn("WhatsApp Business", _mensajes(corto, "ok"))
        diagonal = _revisar_texto(BUENA.replace("523300000000?text=Hola", "523300000000/"))
        self.assertIn("WhatsApp bien escrito", _mensajes(diagonal, "ok"))

    def test_partes_de_tarjeta_no_cuentan(self):
        partes = "".join('<div class="card"><h3 class="card-title">a</h3><p class="card-text">b</p></div>' for _ in range(3))
        self.assertNotIn("tarjetas", _mensajes(_revisar_texto(BUENA.replace("</body>", partes + "</body>"))))

    def test_reducir_movimiento_en_comentario_no_cuenta(self):
        html = BUENA.replace("@media (prefers-reduced-motion: reduce){*{transition:none}}", "/* prefers-reduced-motion */")
        self.assertIn("prefers-reduced-motion", _mensajes(_revisar_texto(html), "falta"))

    def test_markdown_y_main(self):
        r = _revisar_texto(BUENA)
        self.assertIn("# Revisión automática", a_markdown(r, "index.html"))
        self.assertEqual(main([]), 2)
        self.assertEqual(main(["no-existe.html"]), 1)


class PruebasEjemplos(unittest.TestCase):
    def test_ejemplo_antes_tiene_muchos_rasgos(self):
        r = revisar(EJEMPLOS / "antes-cara-de-ia.html")
        rasgos = [h for h in r.hallazgos if h["grupo"].startswith("Rasgos") and h["nivel"] == "aviso"]
        self.assertGreaterEqual(len(rasgos), 8)

    def test_ejemplo_despues_solo_pendientes(self):
        r = revisar(EJEMPLOS / "despues" / "index.html")
        faltas = [h["mensaje"] for h in r.hallazgos if h["nivel"] == "falta"]
        self.assertEqual(len(faltas), 3, faltas)  # pendientes del dueño + aviso y términos que prepara su abogado
        self.assertIn("[PENDIENTE]", faltas[0])
        self.assertTrue(all("todavía no existe" in f for f in faltas[1:]))
        self.assertFalse([h for h in r.hallazgos if h["grupo"].startswith("Rasgos") and h["nivel"] == "aviso"])


if __name__ == "__main__":
    unittest.main()
