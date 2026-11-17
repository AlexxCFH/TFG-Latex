"""Convierte cada mockup (mockups.py) en un PNG en PlantillaTFG/img con Chrome sin ventana.

Uso: python render.py [nombre ...]   (sin nombres, todos)
"""
import os
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import mockups  # noqa: E402

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SALIDA = os.path.normpath(os.path.join(AQUI, "..", ".."))   # PlantillaTFG/img
HTML = os.path.join(AQUI, "html")
os.makedirs(HTML, exist_ok=True)

elegidos = sys.argv[1:] or list(mockups.MOCKUPS)
for nombre in elegidos:
    html, (ancho, alto) = mockups.MOCKUPS[nombre]()
    ruta_html = os.path.join(HTML, nombre + ".html")
    with open(ruta_html, "w", encoding="utf-8") as f:
        f.write(html)
    png = os.path.join(SALIDA, nombre + ".png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    "--allow-file-access-from-files", "--force-device-scale-factor=2",
                    f"--window-size={ancho},{alto}", f"--screenshot={png}",
                    "file:///" + ruta_html.replace("\\", "/")],
                   check=True, capture_output=True)
    print("ok", nombre)
