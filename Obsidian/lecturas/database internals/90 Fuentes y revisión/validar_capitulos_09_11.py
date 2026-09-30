"""Validación estructural de la ampliación. Ejecutar con uv run --with pyyaml --with pymupdf."""
from pathlib import Path
import hashlib
import json
import re
import sys

import pymupdf
import yaml

BASE = Path(__file__).resolve().parent.parent
ROOT = BASE.parents[2]
CHAPTERS = {9: "09 Detección de fallas", 10: "10 Elección de líder", 11: "11 Replicación y consistencia"}
COVERAGE = BASE / "90 Fuentes y revisión/08 Cobertura y validación de detección liderazgo y replicación.md"
SOURCE = Path("/Users/alech/Downloads/CamScanner 2026-09-30 16.59.pdf")
PDF = BASE / "Materiales/09 a 11 Detección de fallas liderazgo y replicación.pdf"
SCRATCH = Path("/private/tmp/database-internals-09-11-validation")
SCRATCH.mkdir(exist_ok=True)

errors = []
notes = [p for folder in CHAPTERS.values() for p in sorted((BASE / folder).glob("*.md"))]
files = notes + [COVERAGE, BASE / "00 Empieza aquí.md", BASE / "README.md",
                 BASE / "90 Fuentes y revisión/00 Índice.md",
                 BASE / "90 Fuentes y revisión/01 Fuentes y cobertura.md",
                 BASE / "90 Fuentes y revisión/03 Procedencia de recursos visuales.md",
                 BASE / "08 Introducción a sistemas distribuidos/12 Laboratorio y repaso resuelto.md",
                 ROOT / "README.md", ROOT / "Obsidian/lecturas/00 Índice de lecturas.md"]
links = pdf_refs = mermaids = questions = 0
manifest = []
pdf_counts = {}

for file in files:
    if not file.exists():
        errors.append(f"Archivo inexistente: {file.relative_to(ROOT)}")
        continue
    s = file.read_text()
    label = str(file.relative_to(ROOT))
    fm = re.match(r"---\n(.*?)\n---\n", s, re.S)
    try:
        data = yaml.safe_load(fm.group(1)) if fm else {}
    except yaml.YAMLError as exc:
        errors.append(f"{label}: YAML inválido: {exc}")
        data = {}
    if file in notes or file == COVERAGE:
        for key in ("title", "created", "capitulo", "tags"):
            if key not in data:
                errors.append(f"{label}: falta propiedad {key}")
        if type(data.get("capitulo")) is not int:
            errors.append(f"{label}: capítulo debe ser entero")
        if "lecturas/database-internals" not in data.get("tags", []):
            errors.append(f"{label}: falta etiqueta del libro")
        if not any(t.startswith("arquitectura/") for t in data.get("tags", [])):
            errors.append(f"{label}: falta etiqueta temática")
        if str(data.get("created")) != "2026-09-30":
            errors.append(f"{label}: fecha incorrecta")
        if file in notes:
            expected = next(k for k, v in CHAPTERS.items() if file.parent.name == v)
            if data.get("capitulo") != expected:
                errors.append(f"{label}: número de capítulo incorrecto")
            if "←" not in s or "→" not in s:
                errors.append(f"{label}: falta navegación")
    if s.count("```") % 2:
        errors.append(f"{label}: bloque de código sin cerrar")
    if re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", s):
        errors.append(f"{label}: carácter de control")
    questions += s.count("> [!question]-")
    for block in re.findall(r"\[\[(.*?)\]\]", s):
        dest = block.replace("\\|", "|").split("|")[0]
        target, _, anchor = dest.partition("#")
        if not target:
            continue
        p = ROOT / target
        if not p.exists():
            p = Path(str(p) + ".md")
        if not p.exists():
            errors.append(f"{label}: destino inexistente {target}")
        links += 1
        if anchor.startswith("page="):
            pdf_refs += 1
            try:
                page = int(anchor.removeprefix("page="))
                if p not in pdf_counts:
                    pdf_counts[p] = len(pymupdf.open(p))
                if not 1 <= page <= pdf_counts[p]:
                    errors.append(f"{label}: página fuera del PDF {dest}")
            except Exception as exc:
                errors.append(f"{label}: referencia PDF inválida {dest}: {exc}")
    for _, target in re.findall(r"\[([^\[\]]+)\]\(([^)]+)\)", s):
        target = target.strip("<>")
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        target = target.partition("#")[0]
        p = ROOT / target if target.startswith("Obsidian/") else file.parent / target
        if not p.exists():
            errors.append(f"{label}: enlace Markdown inexistente {target}")
    for code in re.findall(r"```mermaid\n(.*?)\n```", s, re.S):
        mermaids += 1
        output = SCRATCH / f"mermaid-{mermaids:02}.mmd"
        output.write_text(code)
        manifest.append({"source": label, "input": str(output), "svg": str(output.with_suffix(".svg"))})

sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
source_hash = sha(SOURCE) if SOURCE.exists() else None
copy_hash = sha(PDF) if PDF.exists() else None
if source_hash and source_hash != copy_hash:
    errors.append("La copia del PDF difiere del original")
if not copy_hash:
    errors.append("Falta el PDF de referencia")
pngs = [p for k in CHAPTERS for p in sorted((BASE / f"Recursos visuales/Capítulo {k:02}").glob("*.png"))]
result = {
    "fecha": "2026-09-30",
    "notas_por_capitulo": {k: len(list((BASE / v).glob("*.md"))) for k, v in CHAPTERS.items()},
    "archivos_markdown_validados": len(files),
    "wikilinks_comprobados": links,
    "referencias_pdf_comprobadas": pdf_refs,
    "preguntas_plegables": questions,
    "png": len(pngs),
    "bloques_mermaid": mermaids,
    "pdf_paginas": len(pymupdf.open(PDF)) if PDF.exists() else None,
    "pdf_sha256": copy_hash,
    "copia_identica_al_original": source_hash == copy_hash if source_hash else None,
    "errores": errors,
}
(SCRATCH / "mermaid-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
(BASE / "90 Fuentes y revisión/validacion_capitulos_09_11.json").write_text(json.dumps(result, ensure_ascii=False, indent=2))
print(json.dumps(result, ensure_ascii=False, indent=2))
sys.exit(bool(errors))
