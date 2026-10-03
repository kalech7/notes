"""Validación reproducible: uv run --with pyyaml --with pillow --with pypdf python validar_notas.py."""
from pathlib import Path
import ast, hashlib, json, re
import yaml
from PIL import Image
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[6]
B = ROOT/'Obsidian/posgrado/master/IA GENERATIVA Y AGENTES'
C = B/'14 Multiagente LangGraph y robustez'
OUT = Path(__file__).resolve().parent
FUENTE = B/'90 Referencias/17 FUENTES - Sesión 14 tutorial y robustez.md'
notes = sorted(C.glob('*.md')) + [FUENTE]
nav = [ROOT/'README.md',B/'00 Inicio/00 INICIO - Ruta de aprendizaje.md',
       B/'90 Referencias/14 FUENTES - Materiales y mapa de cobertura.md',
       B/'06 Talleres y práctica/00 Índice - Prácticas de la semana 3.md']
errors=[];links=0;pdf_anchors=0;code=0;mermaid=[];formulas=[]

def resolve(target):
    p=ROOT/target
    if p.exists():return p
    if p.suffix=='':
        p=p.with_suffix('.md')
        if p.exists():return p
    return None

for f in notes:
    s=f.read_text()
    try:
        fm=yaml.safe_load(s.split('---',2)[1])
        assert all(k in fm for k in ['title','created','capitulo','tags'])
        assert fm['capitulo']==14 and isinstance(fm['tags'],list)
    except Exception as e:errors.append(f'{f.name}: YAML {e}')
    for ch in s:
        if ord(ch)<32 and ch not in '\n\t\r':errors.append(f'{f.name}: carácter de control {ord(ch)}')
    for raw in re.findall(r'\[\[(.*?)\]\]',s):
        target=raw.replace('\\|','|').split('|')[0]
        path,sep,anchor=target.partition('#');p=resolve(path)
        links+=1
        if not p:errors.append(f'{f.name}: enlace ausente {target}');continue
        if anchor.startswith('page='):
            pdf_anchors+=1
            n=int(anchor.split('=')[1]);pages=len(PdfReader(p).pages)
            if not 1<=n<=pages:errors.append(f'{f.name}: ancla PDF inválida {target}')
    for kind,block in re.findall(r'```(\w+)\s*\n(.*?)```',s,re.S):
        if kind=='mermaid':mermaid.append({'file':str(f.relative_to(ROOT)),'source':block})
        if kind in ['python','json']:
            code+=1
            try:ast.parse(block) if kind=='python' else json.loads(block)
            except Exception as e:errors.append(f'{f.name}: {kind} {e}')
    formulas.extend(re.findall(r'\$\$(.*?)\$\$',s,re.S))
    for embed in re.finditer(r'!\[\[[^\n]+\.png\]\]',s):
        after=s[embed.end():].strip()
        if not after or after.startswith(('#','!','```')):errors.append(f'{f.name}: imagen sin prosa')

# En navegación se comprueban solo enlaces de S14, sin volver a auditar todo el vault.
for f in nav:
    s=f.read_text()
    if s.startswith('---'):yaml.safe_load(s.split('---',2)[1])
    for raw in re.findall(r'\[\[(.*?)\]\]',s):
        if 'S14' not in raw and 'Multiagente LangGraph' not in raw and 's3-jue' not in raw and 's14_' not in raw:continue
        links+=1
        target=raw.replace('\\|','|').split('|')[0].split('#')[0]
        if not resolve(target):errors.append(f'{f.name}: nuevo enlace ausente {target}')

hashes={}
for name in ['sesion-14.pdf','tutorial-langgraph.pdf','s3-jue-estudiante.ipynb']:
    original=Path('/Users/alech/Downloads')/name;copy=B/'Materiales'/name
    assert original.read_bytes()==copy.read_bytes(),name
    hashes[name]=hashlib.sha256(copy.read_bytes()).hexdigest()
original=json.loads((B/'Materiales/s3-jue-estudiante.ipynb').read_text())
notebook=json.loads((C/'Practica/s3-jue-resuelto.ipynb').read_text())
assert notebook['nbformat']==4
counts={'markdown':0,'code':0}
for c in notebook['cells']:
    counts[c['cell_type']]+=1
    if c['cell_type']=='code':
        ast.parse(''.join(c['source']))
        assert c['execution_count'] and c['outputs']
        assert not any(o['output_type']=='error' for o in c['outputs'])
assert len(original['cells'])==13
assert counts['code']==6
for p in [C/'Practica/s14_robustez_local.py', B/'Recursos visuales/Capítulo 14/generar_diagramas.py']:
    ast.parse(p.read_text())
images=sorted((B/'Recursos visuales/Capítulo 14').glob('*.png'))
assert len(images)==9
for f in images:
    with Image.open(f) as im:assert im.size==(1600,1000);im.verify()
result=json.loads((C/'Practica/s14_resultados_verificados.json').read_text());assert result['total']==17
guard = json.loads((OUT/'guard_textual.json').read_text())
def filtro_textual(q):
    q = q.strip().lower()
    return q.startswith('select') and not any(t in q for t in [' insert ',' update ',' delete ',' drop ',' alter '])
assert not filtro_textual(guard['consulta_A']['texto'])
assert filtro_textual(guard['consulta_B']['texto'])
renders = json.loads((OUT/'mermaid_resultados.json').read_text())
assert len(renders)==5 and all(r['correcto'] for r in renders)
katex = json.loads((OUT/'katex_resultados.json').read_text())
assert katex['correcto'] and katex['formulas']==1

# Se reserva el destino del informe antes de resolver sus enlaces circulares.
(OUT/'formulas.json').write_text(json.dumps(formulas,ensure_ascii=False,indent=2))
(OUT/'mermaid_fuentes.json').write_text(json.dumps(mermaid,ensure_ascii=False,indent=2))
report={'fecha_validacion':'2026-10-02','notas_nuevas':len(notes),
        'enlaces_comprobados':links,'anclas_pdf':pdf_anchors,'fragmentos_python_json':code,
        'diagramas_mermaid':len(mermaid),'formulas':len(formulas),'png':len(images),
        'original_notebook_celdas':len(original['cells']),'notebook_resuelto':counts,
        'comprobaciones_practica':result['total'],'sha256_originales':hashes,
        'mermaid_renderizado':renders,'katex':katex,'guard_textual':guard,
        'errores':errors,'revision_visual_png':'9 PNG inspeccionados; figura 06 corregida y revisada',
        'alcance':'Capítulo S14, fuentes S14 y enlaces nuevos de navegación; LangGraph no ejecutado'}
(OUT/'validacion_s14.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
