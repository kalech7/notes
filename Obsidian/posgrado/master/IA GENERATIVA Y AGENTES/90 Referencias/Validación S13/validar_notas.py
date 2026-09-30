from pathlib import Path
import re, json, hashlib, ast, xml.etree.ElementTree as ET, datetime
import yaml
from PIL import Image
from pypdf import PdfReader
ROOT=Path('/Users/alech/Documents/notes')
C=ROOT/'Obsidian/posgrado/master/IA GENERATIVA Y AGENTES'
CH=C/'13 MCP descubrimiento y casos de uso'
DEST=Path(__file__).parent
TMP=Path('/tmp/s13-review');TMP.mkdir(exist_ok=True)
new=list(sorted(CH.glob('*.md')))+[C/'90 Referencias/16 FUENTES - Sesión 13 MCP y validación.md']
modified=[C/'00 Inicio/00 INICIO - Ruta de aprendizaje.md', C/'90 Referencias/14 FUENTES - Materiales y mapa de cobertura.md', C/'90 Referencias/12 GLOSARIO - Diccionario explicado para estas sesiones.md', C/'12 Patrones de agentes y diseño del toolset/78 S12 - Ejercicios resueltos y repaso activo.md']
lookup={}
for p in C.rglob('*'):
 if p.is_file():
  for key in (p.name,p.stem):lookup.setdefault(key,set()).add(p)
issues=[];links=0;images=0;mdlinks=0;diagrams=[];anchors=0
for p in new+modified:
 t=p.read_text();y=yaml.safe_load(t.split('---',2)[1])
 if p in new:
  assert isinstance(y['title'],str) and isinstance(y['tags'],list)
  assert y['capitulo']==13 and y['created']==datetime.date(2026,9,30)
 if any(ord(ch)<32 and ch!='\n' for ch in t):issues.append({'file':p.name,'error':'Carácter de control en Markdown'})
 if t.count('```')%2:issues.append({'file':p.name,'error':'Bloque sin cierre'})
 for m in re.finditer(r'(!?)\[\[([^\]]+)\]\]',t):
  target=m[2].split('|')[0];name,_,anchor=target.partition('#');links+=1;images+=bool(m[1])
  q=ROOT/name
  found=[v for v in [q,Path(str(q)+'.md')] if v.is_file()] or list(lookup.get(name,[]))
  if not name:found=[p]
  if len(found)!=1:issues.append({'file':p.name,'error':'Destino ausente o ambiguo','target':target});continue
  if anchor.startswith('page='):
   anchors+=1
   assert found[0].suffix=='.pdf'
   if not 1<=int(anchor[5:])<=len(PdfReader(found[0]).pages):issues.append({'file':p.name,'error':'Página inválida','target':target})
  elif anchor and found[0].suffix=='.md':
   headings=re.findall(r'^#+\s+(.+)$',found[0].read_text(),re.M)
   if anchor not in headings:issues.append({'file':p.name,'error':'Ancla ausente','target':target})
 for m in re.finditer(r'(?<!!)\[[^\]\n]+\]\(([^)]+)\)',t):
  url=m[1];mdlinks+=1
  if url.startswith(('https://','http://')):continue
  q=Path(url) if url.startswith('/') else p.parent/url
  if not q.is_file():issues.append({'file':p.name,'error':'Enlace Markdown ausente','target':url})
 for body in re.findall(r'```mermaid\n(.*?)\n```',t,re.S):
  if p in new:diagrams.append({'file':p.name,'source':body})
 for lang,body in re.findall(r'```(json|python)\n(.*?)\n```',t,re.S):
  if p not in new:continue
  try:
   if lang=='json':json.loads(body)
   else:ast.parse(body)
  except Exception as e:issues.append({'file':p.name,'error':f'Código {lang} inválido: {e}'})
PNG=list((C/'Recursos visuales/Capítulo 13').glob('*.png'))
SVG=list((C/'Recursos visuales/Capítulo 13').glob('*.svg'))
for p in PNG:
 with Image.open(p) as im:im.verify()
for p in SVG:ET.parse(p)
orig=Path('/Users/alech/Downloads/sesion-13.pdf').read_bytes();copy=(C/'Materiales/sesion-13.pdf').read_bytes()
assert orig==copy and len(PdfReader(C/'Materiales/sesion-13.pdf').pages)==26
practice=json.loads((CH/'Practica/s13_resultados_verificados.json').read_text())
assert practice['fuente_agente_igual'] and practice['rutas_distinguidas'] and len(practice['rechazos_verificados'])==6
report={'fecha':'2026-09-30','notas_S13':9,'nota_fuentes':1,'notas_existentes_actualizadas':4,'archivos_markdown_validados':len(new+modified),'wikilinks':links,'embeds':images,'enlaces_markdown':mdlinks,'anclas_pdf_validas':anchors,'png_validos':len(PNG),'svg_validos':len(SVG),'mermaid_extraidos':len(diagrams),'pdf_paginas':26,'sha256_pdf':hashlib.sha256(copy).hexdigest(),'pdf_identico_original':orig==copy,'practica_verificada':True,'errores':issues}
(DEST/'validacion_s13.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
(TMP/'mermaid-todos.md').write_text('\n\n'.join('## '+d['file']+'\n\n```mermaid\n'+d['source']+'\n```' for d in diagrams))
(TMP/'puppeteer.json').write_text(json.dumps({'executablePath':'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome','args':['--no-sandbox']}))
print(json.dumps(report,ensure_ascii=False,indent=2))
if issues:raise SystemExit(1)
