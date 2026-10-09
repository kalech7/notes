"""Regenera los dos esquemas S18 con Pillow y las funciones compartidas S17."""
from pathlib import Path
import runpy

shared = Path(__file__).resolve().parents[1] / 'S17/generar_imagenes.py'
functions = runpy.run_path(str(shared))
functions['bordes']()
functions['costos']()
print('Dos imágenes S18 regeneradas')
