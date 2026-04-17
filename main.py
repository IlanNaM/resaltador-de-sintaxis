import os
from scripts.parser import parser

ruta_html = os.path.join(os.getcwd())
print(f"RUTA HTML OBJETIVO: {ruta_html}")

parser(ruta_html=ruta_html, nombre_html="resalta_sintaxis")
