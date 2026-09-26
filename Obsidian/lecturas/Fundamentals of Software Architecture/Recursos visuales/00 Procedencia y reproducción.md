---
title: "Procedencia de las ilustraciones y gráficos"
created: 2026-09-25
tags:
  - lecturas/software-architecture
  - recursos-visuales
---

# Procedencia de las ilustraciones y gráficos

[[Obsidian/lecturas/Fundamentals of Software Architecture/06 Atlas visual explicado|← Atlas visual]]

## Ilustración generada

`03-modularidad.png` fue creada para esta guía con la herramienta integrada de generación de imágenes. Se inspeccionaron sus títulos y la distinción visual entre separación lógica y física. Es una analogía conceptual, no una medición. El archivo final se conserva en esta carpeta.

Prompt utilizado:

```text
Use case: scientific-educational. Asset type: original conceptual illustration for a Spanish software architecture study guide. Create one wide illustration with three clearly separated panels, polished isometric educational illustration on warm white background, navy teal and coral palette, generous whitespace, no tiny text. Exact titles above panels: 'MONOLITO MODULAR', 'MICROSERVICIOS', 'MONOLITO DISTRIBUIDO'. First panel: one large transparent enclosure containing three distinct neatly grouped functional modules teal blue amber, clear interfaces connecting them, one enclosing deployment boundary. Second panel: three separate smaller enclosures each containing one functional module and its own small data cylinder, thin explicit communication bridges between enclosures. Third panel: three separate enclosures entangled with many crossing red cables and one shared external data cylinder, suggest costly coordination, no fire or melodrama. Illustration explains that physical separation alone does not remove coupling; distinguish modularity from deployment. All three panels equally sized. Render titles verbatim and no other text. No logos, no watermark. High resolution landscape.
```

La generación tuvo un límite temporal durante la primera entrega. En la ampliación posterior se generaron nuevas ilustraciones con la misma herramienta integrada. No se utilizó un servicio alternativo de pago. Los prompts adicionales se conservan en `prompts-ilustraciones.md`.

## Figuras vectoriales y gráficos

Los archivos `01`, `02`, `04`, `05`, `06`, `07` y `08` en formato SVG son dibujos originales elaborados mediante `generar_graficos.py`. No dependen de la generación de imágenes. Los PNG con los mismos nombres son representaciones de esos mismos gráficos, no ilustraciones adicionales.

La figura `04` calcula coordenadas de A e I; la `05` presenta un conteo de pares verificable; la `06` usa series sintéticas identificadas como tales; la `07` representa un incidente hipotético. Las demás figuras representan relaciones conceptuales. Los colores acompañan texto, formas o trazos distintos, de manera que no son la única forma de distinguir elementos.

Para regenerar los SVG, ejecuta el script con Python 3. Las versiones PNG ya están incluidas para otros lectores. Los veinte diagramas Mermaid se conservan como archivos `.mmd` dentro de `Diagramas`, junto con sus SVG y PNG. Cada capítulo inserta el PNG mediante un enlace Markdown relativo y enlaza la fuente editable; así las imágenes también se ven en GitHub sin depender de la sintaxis de embeds de Obsidian.

Todos los recursos se explican en el atlas y se relacionan con sus capítulos. No se requiere conectividad para leer las notas, ver los archivos conservados o consultar los PDF locales.
