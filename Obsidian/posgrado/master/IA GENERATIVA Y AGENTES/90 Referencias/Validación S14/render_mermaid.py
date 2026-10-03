"""Render de Mermaid con la CLI disponible y Chrome del sistema."""
from pathlib import Path
import json, subprocess, concurrent.futures
P=Path(__file__).resolve().parent
P.joinpath('puppeteer.json').write_text(json.dumps({'executablePath':'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome','args':['--no-sandbox']}))
items=json.loads((P/'mermaid_fuentes.json').read_text())
cli=Path('/Users/alech/.npm/_npx/668c188756b835f3/node_modules/@mermaid-js/mermaid-cli/src/cli.js')
def render(pair):
    i,item=pair;src=P/f'mermaid-{i}.mmd';out=P/f'mermaid-{i}.svg';src.write_text(item['source'])
    r=subprocess.run(['node',str(cli),'-i',str(src),'-o',str(out),'-p',str(P/'puppeteer.json')],capture_output=True,text=True,timeout=60)
    return {'file':item['file'],'render':out.name,'correcto':r.returncode==0,'error':r.stderr[-2000:] if r.returncode else ''}
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
    results=list(ex.map(render,enumerate(items,1)))
(P/'mermaid_resultados.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(results,ensure_ascii=False,indent=2))
raise SystemExit(any(not r['correcto'] for r in results))
