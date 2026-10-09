"""Valida notas S17/S18, rutas, YAML y páginas; extrae Mermaid para renderizar."""
from pathlib import Path
import re, json, hashlib, os, shutil, argparse
from datetime import datetime
from zoneinfo import ZoneInfo
import yaml
import pymupdf

VAULT=Path(__file__).resolve().parents[6]
COURSE=VAULT/'Obsidian/posgrado/master/IA GENERATIVA Y AGENTES'
OUT=Path(__file__).resolve().parent
FOLDERS=[COURSE/'17 Observabilidad y versionado de prompts',COURSE/'18 Guardrails costo y latencia']
NOTES=sorted(p for folder in FOLDERS for p in folder.rglob('*.md'))
NOTES += [COURSE/'00 Inicio/01 Guía - Entender las sesiones 17 y 18.md',COURSE/'00 Inicio/02 Caso resuelto - Diagnosticar y mejorar un asistente de ventas.md',COURSE/'90 Referencias/18 FUENTES - Sesiones 17 y 18 integración.md',COURSE/'90 Referencias/19 REVISIÓN - Profundidad y comprensión S17 S18.md']
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--original-dir',type=Path,help='Carpeta opcional con sesion-17.pdf y sesion-18.pdf originales')
args=parser.parse_args()
errors=[]; links=0; diagrams=[]; words=0; questions=0
for note in NOTES:
    if not note.exists():
        errors.append(f'Falta nota: {note}');continue
    raw=note.read_text();questions+=raw.count('[!question]')
    readable=re.sub(r'^---\n.*?\n---\n','',raw,flags=re.S)
    readable=re.sub(r'```.*?```','',readable,flags=re.S)
    readable=re.sub(r'!\[\[.*?\]\]','',readable)
    readable=re.sub(r'\[\[([^\]]+)\]\]',lambda m:m.group(1).split('|')[-1].split('/')[-1],readable)
    readable=re.sub(r'\[([^\]]+)\]\([^)]*\)',r'\1',readable)
    words+=len(readable.split())
    try:
        front=raw.split('---',2)[1]; data=yaml.safe_load(front)
        for key in ['title','created','capitulo','tags']:
            if key not in data:errors.append(f'{note.name}: falta YAML {key}')
        if not isinstance(data.get('capitulo'),int):errors.append(f'{note.name}: capitulo no entero')
    except Exception as ex:errors.append(f'{note.name}: YAML {ex}')
    for full in re.findall(r'\[\[([^\]]+)\]\]',raw):
        target=full.split('|',1)[0]; path,_,anchor=target.partition('#');links+=1
        if not path:continue
        absolute=VAULT/path
        resolved=absolute if absolute.exists() else absolute.with_suffix('.md')
        if not resolved.exists():
            relative=note.parent/path
            resolved=relative if relative.exists() else relative.with_suffix('.md')
        if not resolved.exists():errors.append(f'{note.name}: enlace roto {target}')
        elif anchor.startswith('page='):
            n=int(anchor.split('=',1)[1])
            if resolved.suffix!='.pdf' or not 1<=n<=len(pymupdf.open(resolved)):
                errors.append(f'{note.name}: página inválida {target}')
    for label,target in re.findall(r'(?<!!)\[([^\]]+)\]\(([^)]+)\)',raw):
        if re.match(r'^(https?://|mailto:)',target):continue
        target=target.strip('<>').split('#')[0]
        if target and not (note.parent/target).exists() and not Path(target).exists():
            errors.append(f'{note.name}: Markdown roto {target}')
    for body in re.findall(r'```mermaid\s*\n(.*?)```',raw,re.S):
        diagrams.append((str(note.relative_to(VAULT)),body))
        if 'sequenceDiagram' in body and ';' in body:errors.append(f'{note.name}: punto y coma secuencia')
    if raw.count('```')%2:errors.append(f'{note.name}: bloque sin cierre')

bundle='\n\n'.join(f'## Diagrama {i}: {name}\n\n```mermaid\n{body}\n```' for i,(name,body) in enumerate(diagrams,1))
(OUT/'diagramas.md').write_text(bundle)
chrome_candidates=[os.environ.get('NOTAS_CHROME_PATH'),
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    shutil.which('google-chrome'),shutil.which('chromium'),shutil.which('chromium-browser'),
    'C:/Program Files/Google/Chrome/Application/chrome.exe']
chrome=next((str(p) for p in chrome_candidates if p and Path(p).is_file()),None)
if chrome:
    (OUT/'puppeteer.json').write_text(json.dumps({'executablePath':chrome,'args':['--no-sandbox']}))
manifest=json.loads((OUT/'fuentes.json').read_text())
copies={}
for ses,entry in manifest.items():
    target=COURSE/'Materiales'/entry['file']
    sha=lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    with pymupdf.open(target) as doc:
        pages=len(doc)
    copies[ses]={'pages':pages,'identical':sha(target)==entry['sha256']}
    if pages!=entry['pages']:errors.append(f'Páginas PDF {ses} alteradas')
    if not copies[ses]['identical']:errors.append(f'Copia PDF {ses} alterada')
    if args.original_dir:
        source=args.original_dir/f'sesion-{ses}.pdf'
        if not source.exists():errors.append(f'Falta original solicitado {source.name}')
        else:
            copies[ses]['original_identical']=sha(source)==sha(target)
            if not copies[ses]['original_identical']:errors.append(f'PDF {ses} no coincide con original')
result={'date':datetime.now(ZoneInfo('America/Guayaquil')).date().isoformat(),'notes':len(NOTES),'words_approx':words,'word_count_method':'Texto de lectura, sin YAML, código, rutas ni URLs de enlaces','wikilinks':links,'mermaid':len(diagrams),'questions':questions,'pdf_copies':copies,'errors':errors}
(OUT/'resultado.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
