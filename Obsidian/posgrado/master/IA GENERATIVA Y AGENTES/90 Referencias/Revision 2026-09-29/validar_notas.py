from pathlib import Path
import json,re,ast,urllib.parse,xml.etree.ElementTree as ET,hashlib
from PIL import Image
import yaml
from pypdf import PdfReader
BASE=Path('/Users/alech/Documents/notes');C=BASE/'Obsidian/posgrado/master/IA GENERATIVA Y AGENTES'
notas=sorted(p for d in C.iterdir() if d.is_dir() and re.match(r'^\d',d.name) for p in d.glob('*.md'))
files=[p for p in C.rglob('*') if p.is_file() and '.venv' not in p.parts]
lookup={}
for p in files:
 for key in (p.name,p.stem):lookup.setdefault(key,set()).add(p)
issues=[];links=0;embeds=0;meta=[];pdfcache={};charts=[];mdlinks=0;mdimages=0
for p in notas:
 t=p.read_text()
 if not t.startswith('---\n'):issues.append({'file':str(p),'type':'YAML ausente'})
 else:
  try:
   y=yaml.safe_load(t.split('---',2)[1]);assert isinstance(y,dict);assert isinstance(y.get('tags'),list)
  except Exception as e:issues.append({'file':str(p),'type':'YAML inválido','detail':str(e)})
 for m in re.finditer(r'(!?)\[\[([^\]]+)\]\]',t):
  dest=m[2].split('|',1)[0];name,sep,anchor=dest.partition('#');links+=1;embeds+=bool(m[1])
  if not name:found=[p]
  else:
   q=BASE/name;found=[k for k in [q,Path(str(q)+'.md')] if k.is_file()]
   if not found:found=list(lookup.get(name,[]))
  if not found:issues.append({'file':str(p),'type':'link ausente','detail':dest});continue
  if len(found)>1:issues.append({'file':str(p),'type':'link ambiguo','detail':dest});continue
  target=found[0]
  if sep:
   if target.suffix=='.pdf' and anchor.startswith('page='):
    if target not in pdfcache:pdfcache[target]=len(PdfReader(target).pages)
    try:assert 1<=int(anchor[5:])<=pdfcache[target]
    except Exception:issues.append({'file':str(p),'type':'pagina PDF inválida','detail':dest})
   elif target.suffix=='.md' and not anchor.startswith('^'):
    hs=re.findall(r'^#+\s+(.+?)\s*$',target.read_text(),re.M)
    if anchor not in hs:issues.append({'file':str(p),'type':'ancla ausente','detail':dest})
 for m in re.finditer(r'(!?)\[[^\]\n]*\]\((?:<([^>]+)>|([^\s)]+))\)',t):
  dest=m[2] or m[3]
  if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',dest):continue
  name=urllib.parse.unquote(dest.split('#',1)[0]);mdlinks+=1;mdimages+=bool(m[1])
  if not name:continue
  q=Path(name) if name.startswith('/') else p.parent/name
  if not q.is_file():issues.append({'file':str(p),'type':'enlace Markdown ausente','detail':dest})
 for i,body in enumerate(re.findall(r'```mermaid\n(.*?)\n```',t,re.S)):
  charts.append({'file':str(p),'index':i,'source':body})
 if t.count('```')%2:issues.append({'file':str(p),'type':'bloque sin cierre'})
for canvas in (C/'00 Inicio').glob('*.canvas'):
 data=json.loads(canvas.read_text());ids=[n['id'] for n in data['nodes']]+[e['id'] for e in data['edges']]
 if len(ids)!=len(set(ids)):issues.append({'file':str(canvas),'type':'ids duplicados'})
 nodes={n['id'] for n in data['nodes']}
 for e in data['edges']:
  if e['fromNode'] not in nodes or e['toNode'] not in nodes:issues.append({'file':str(canvas),'type':'arista rota'})
 for n in data['nodes']:
  if n['type']=='file' and not (BASE/n['file']).is_file():issues.append({'file':str(canvas),'type':'archivo canvas ausente','detail':n['file']})
svgcount=0;pngcount=0
for f in (C/'Recursos visuales').glob('*.svg'):
 try:ET.parse(f);svgcount+=1
 except Exception as e:issues.append({'file':str(f),'type':'SVG inválido','detail':str(e)})
for f in (C/'Recursos visuales').glob('*.png'):
 try:
  with Image.open(f) as im:im.verify()
  pngcount+=1
 except Exception as e:issues.append({'file':str(f),'type':'PNG inválido','detail':str(e)})
originales=[]
for n in ['s3-lun-estudiante.ipynb','s3-mar-estudiante.ipynb','sesion-12.pdf','sesion-07.pdf']:
 a=Path('/Users/alech/Downloads')/n;b=C/'Materiales'/n
 same=a.read_bytes()==b.read_bytes()
 originales.append({'archivo':n,'coincide_con_Descargas':same,'sha256':hashlib.sha256(b.read_bytes()).hexdigest()})
 if not same:issues.append({'file':str(b),'type':'copia fuente diferente'})
sessions=sorted((C/'Materiales').glob('sesion-*.pdf'))
revisados=[{'archivo':p.name,'paginas':len(PdfReader(p).pages)} for p in sessions]
report={'notas':len(notas),'wikilinks':links,'embeds':embeds,'mermaid':len(charts),'enlaces_Markdown_locales':mdlinks,'imagenes_Markdown':mdimages,'SVG_validos':svgcount,'PNG_validos':pngcount,'fuentes_copiadas':originales,'sesiones':revisados,'paginas_sesiones':sum(s['paginas'] for s in revisados),'PDFs_con_anclas_verificados':len(pdfcache),'errores':issues}
Path('/tmp/ia-auditoria/estructura.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
Path('/tmp/ia-auditoria/mermaid-mapa.json').write_text(json.dumps(charts,ensure_ascii=False,indent=2))
Path('/tmp/ia-auditoria/mermaid-todos.md').write_text('\n\n'.join(f"## {i} {Path(c['file']).name}\n\n```mermaid\n{c['source']}\n```" for i,c in enumerate(charts)))
Path('/tmp/ia-auditoria/puppeteer.json').write_text(json.dumps({'executablePath':'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome','args':['--no-sandbox']}))
print(json.dumps(report,ensure_ascii=False,indent=2))
