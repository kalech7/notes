# Reproducir la revisión de las sesiones 17 y 18

Desde la raíz de este repositorio se puede ejecutar:

```bash
uv run --with pymupdf --with pyyaml python "Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/90 Referencias/Validación S17 S18/validar_notas.py"
```

El script valida las notas y sus recursos usando las rutas del repositorio. No requiere la carpeta Descargas del autor: `fuentes.json` conserva las huellas SHA-256 y el número de páginas de los PDF originales. Si se dispone de los dos originales, `--original-dir /ruta/a/carpeta` permite compararlos otra vez.

`resultado.json` registra las comprobaciones. El recuento aproximado de palabras excluye YAML, bloques de código y rutas de enlaces; mide texto de lectura, no tamaño del archivo. Los registros de ejercicios usan datos ficticios y no acreditan calidad de un modelo real.

Para renderizar los diagramas se requiere Node.js y Chrome o Chromium. Desde esta carpeta:

```bash
npx --yes --package @mermaid-js/mermaid-cli mmdc -i diagramas.md -o diagramas-renderizados.md -e png -p puppeteer.json -j 2
```

El validador genera `puppeteer.json` si encuentra el navegador; este archivo es local y está ignorado por Git. Si el navegador está en otra ubicación, se puede indicar su ejecutable mediante `NOTAS_CHROME_PATH` antes de ejecutar el validador. Cuando se utiliza el navegador administrado por Puppeteer, se omite `-p puppeteer.json`.

Los PNG renderizados y `renderizado.json` son evidencia de la revisión guardada, no sustituyen una nueva ejecución si se cambian los bloques Mermaid.

Las imágenes educativas pueden regenerarse con Pillow ejecutando `Recursos visuales/S17/generar_imagenes.py` desde la raíz de la materia. El programa busca Arial o DejaVu Sans en la máquina y genera también las imágenes S18. El script de `Recursos visuales/S18/` regenera únicamente esa sesión.
