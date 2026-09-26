// Uso: node exportar_diagramas.cjs /ruta/a/mermaid.min.js
// Dependencia: playwright con Chrome instalado. No modifica las notas ni los .mmd.
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');
const sourceDirectory = path.join(__dirname, 'Diagramas');

(async () => {
  if (!process.argv[2]) throw new Error('Indica una copia local de mermaid.min.js');
  const browser = await chromium.launch({ channel: 'chrome', headless: true });
  try {
    const page = await browser.newPage({ viewport: { width: 1500, height: 1200 }, deviceScaleFactor: 2 });
    await page.setContent('<html><head><style>body{margin:0;background:#fff}#figure{box-sizing:content-box;width:1400px;padding:24px;background:#f6f8f8;border-radius:16px}#figure svg{display:block;width:1400px!important;max-width:1400px!important;height:auto}</style></head><body><div id="figure"></div></body></html>');
    await page.addScriptTag({ path: process.argv[2] });
    await page.evaluate(() => mermaid.initialize({
      startOnLoad: false, securityLevel: 'strict', theme: 'base',
      themeVariables: { fontFamily: 'Arial', fontSize: '20px', primaryColor: '#e6f3f3', primaryTextColor: '#16324f', primaryBorderColor: '#007f83', lineColor: '#2463a5', secondaryColor: '#e6edf7', tertiaryColor: '#fff1d8' },
      flowchart: { htmlLabels: true, curve: 'linear', padding: 20, nodeSpacing: 35, rankSpacing: 55 }
    }));
    let count = 0;
    for (const name of fs.readdirSync(sourceDirectory).filter(n => n.endsWith('.mmd')).sort()) {
      const source = fs.readFileSync(path.join(sourceDirectory, name), 'utf8');
      const svg = await page.evaluate(async ({ source, id }) => {
        const result = await mermaid.render(id, source);
        document.getElementById('figure').innerHTML = result.svg;
        await document.fonts.ready;
        return result.svg;
      }, { source, id: 'diagram' + (++count) });
      fs.writeFileSync(path.join(sourceDirectory, name.replace('.mmd', '.svg')), svg);
      await page.locator('#figure').screenshot({ path: path.join(sourceDirectory, name.replace('.mmd', '.png')) });
    }
    console.log(`Exportados ${count} diagramas en SVG y PNG a 2x.`);
  } finally { await browser.close(); }
})().catch(error => { console.error(error); process.exitCode = 1; });
