import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";

const outDir = path.dirname(fileURLToPath(import.meta.url));
const tempDir = fs.mkdtempSync(path.join(os.tmpdir(), "llm-visuales-"));

const C = {
  bg: "#f8fafc",
  ink: "#0f172a",
  muted: "#475569",
  line: "#cbd5e1",
  blue: "#2563eb",
  blueSoft: "#dbeafe",
  purple: "#7c3aed",
  purpleSoft: "#ede9fe",
  green: "#16a34a",
  greenSoft: "#dcfce7",
  orange: "#ea580c",
  orangeSoft: "#ffedd5",
  red: "#dc2626",
  redSoft: "#fee2e2",
  white: "#ffffff",
};

function esc(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;");
}

function svgShell(title, body, width = 1200, height = 700) {
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}" viewBox="0 0 ${width} ${height}">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="${C.muted}"/></marker>
    <filter id="shadow" x="-10%" y="-10%" width="120%" height="120%"><feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.12"/></filter>
  </defs>
  <rect x="0" y="0" width="${width}" height="${height}" fill="${C.bg}"/>
  <text x="60" y="58" font-family="Arial, sans-serif" font-size="31" font-weight="700" fill="${C.ink}">${esc(title)}</text>
  ${body}
</svg>`;
}

function box(x, y, w, h, label, fill, stroke, size = 22) {
  return `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="16" fill="${fill}" stroke="${stroke}" stroke-width="2" filter="url(#shadow)"/>
  <text x="${x + w / 2}" y="${y + h / 2 + size / 3}" text-anchor="middle" font-family="Arial, sans-serif" font-size="${size}" font-weight="600" fill="${C.ink}">${esc(label)}</text>`;
}

function arrow(x1, y1, x2, y2, color = C.muted, width = 3) {
  return `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${color}" stroke-width="${width}" marker-end="url(#arrow)"/>`;
}

function writeSvg(name, content) {
  fs.writeFileSync(path.join(outDir, name), content, "utf8");
}

function makeGif(stem, frames, fps = "4/5") {
  const frameDir = path.join(tempDir, stem);
  fs.mkdirSync(frameDir, { recursive: true });
  frames.forEach((frame, index) => {
    const suffix = String(index).padStart(2, "0");
    const svgPath = path.join(frameDir, `frame-${suffix}.svg`);
    const pngPath = path.join(frameDir, `frame-${suffix}.png`);
    fs.writeFileSync(svgPath, frame, "utf8");
    const rendered = spawnSync(
      "sips",
      ["-s", "format", "png", svgPath, "--out", pngPath],
      { encoding: "utf8" },
    );
    if (rendered.status !== 0) {
      throw new Error(`sips no pudo renderizar ${svgPath}: ${rendered.stderr}`);
    }
  });
  const target = path.join(outDir, `${stem}.gif`);
  const result = spawnSync(
    "ffmpeg",
    [
      "-hide_banner",
      "-loglevel", "error",
      "-y",
      "-framerate", fps,
      "-i", path.join(frameDir, "frame-%02d.png"),
      "-filter_complex", "[0:v]split[a][b];[a]palettegen=max_colors=128[p];[b][p]paletteuse=dither=bayer",
      "-loop", "0",
      target,
    ],
    { encoding: "utf8" },
  );
  if (result.status !== 0) {
    throw new Error(`ffmpeg no pudo generar ${stem}: ${result.stderr}`);
  }
}

function attentionFrame(step) {
  const tokens = ["El", "banco", "cerró", "temprano"];
  const xs = [105, 315, 525, 735];
  let body = `<text x="60" y="100" font-family="Arial, sans-serif" font-size="20" fill="${C.muted}">Ejemplo: la consulta del token «cerró» busca contexto útil sin mirar el futuro.</text>`;
  tokens.forEach((token, i) => {
    const active = i === 2;
    body += box(xs[i], 145, 150, 62, token, active ? C.purpleSoft : C.white, active ? C.purple : C.line, 22);
  });

  if (step >= 1) {
    body += arrow(600, 220, 600, 278);
    body += box(105, 290, 250, 76, "Q: qué busco", C.purpleSoft, C.purple, 21);
    body += box(475, 290, 250, 76, "K: qué ofrezco", C.blueSoft, C.blue, 21);
    body += box(845, 290, 250, 76, "V: contenido", C.greenSoft, C.green, 21);
  }
  if (step >= 2) {
    body += `<text x="60" y="430" font-family="Arial, sans-serif" font-size="24" font-weight="700" fill="${C.ink}">Puntajes QKᵀ / √H</text>`;
    const scores = [0.7, 2.2, 1.4, 3.0];
    scores.forEach((score, i) => {
      const masked = i > 2;
      const w = masked ? 25 : score * 85;
      body += `<text x="65" y="${475 + i * 43}" font-family="Arial, sans-serif" font-size="19" fill="${C.ink}">${esc(tokens[i])}</text>`;
      body += `<rect x="170" y="${454 + i * 43}" width="${w}" height="28" rx="6" fill="${masked ? C.redSoft : C.blueSoft}"/>`;
      body += `<text x="${180 + w}" y="${475 + i * 43}" font-family="Arial, sans-serif" font-size="18" fill="${masked ? C.red : C.blue}">${masked ? "−∞ por máscara" : score.toFixed(1)}</text>`;
    });
  }
  if (step >= 3) {
    body += `<rect x="565" y="430" width="2" height="210" fill="${C.line}"/>`;
    body += `<text x="610" y="430" font-family="Arial, sans-serif" font-size="24" font-weight="700" fill="${C.ink}">Softmax: pesos que suman 1</text>`;
    const probs = [0.14, 0.63, 0.23, 0.0];
    probs.forEach((p, i) => {
      body += `<text x="615" y="${475 + i * 43}" font-family="Arial, sans-serif" font-size="19" fill="${C.ink}">${esc(tokens[i])}</text>`;
      body += `<rect x="720" y="${454 + i * 43}" width="${p * 430}" height="28" rx="6" fill="${i === 1 ? C.green : C.greenSoft}"/>`;
      body += `<text x="${730 + p * 430}" y="${475 + i * 43}" font-family="Arial, sans-serif" font-size="18" fill="${C.green}">${p.toFixed(2)}</text>`;
    });
  }
  if (step >= 4) {
    body += `<rect x="60" y="645" width="1080" height="2" fill="${C.line}"/>`;
    body += `<text x="600" y="680" text-anchor="middle" font-family="Arial, sans-serif" font-size="22" font-weight="700" fill="${C.ink}">Salida = 0.14·V(El) + 0.63·V(banco) + 0.23·V(cerró)</text>`;
  }
  return svgShell(`${step + 1}. Atención: de una pregunta a una mezcla de información`, body);
}

function ropeFrame(position) {
  const cx1 = 330;
  const cx2 = 835;
  const cy = 390;
  const radius = 150;
  const theta = 0.42;
  const a = position * theta;
  const b = Math.max(0, position - 2) * theta;
  const point = (cx, angle) => [cx + radius * Math.cos(-angle), cy + radius * Math.sin(-angle)];
  const [qx, qy] = point(cx1, a);
  const [kx, ky] = point(cx2, b);
  let body = `<text x="60" y="100" font-family="Arial, sans-serif" font-size="20" fill="${C.muted}">Cada par de dimensiones gira. El producto Q·K conserva información de la distancia relativa.</text>`;
  for (const cx of [cx1, cx2]) {
    body += `<circle cx="${cx}" cy="${cy}" r="${radius}" fill="${C.white}" stroke="${C.line}" stroke-width="2"/>`;
    body += `<line x1="${cx - 185}" y1="${cy}" x2="${cx + 185}" y2="${cy}" stroke="${C.line}" stroke-width="2" marker-end="url(#arrow)"/>`;
    body += `<line x1="${cx}" y1="${cy + 185}" x2="${cx}" y2="${cy - 185}" stroke="${C.line}" stroke-width="2" marker-end="url(#arrow)"/>`;
  }
  body += `<line x1="${cx1}" y1="${cy}" x2="${qx}" y2="${qy}" stroke="${C.purple}" stroke-width="7" marker-end="url(#arrow)"/>`;
  body += `<line x1="${cx2}" y1="${cy}" x2="${kx}" y2="${ky}" stroke="${C.blue}" stroke-width="7" marker-end="url(#arrow)"/>`;
  body += `<text x="${cx1}" y="180" text-anchor="middle" font-family="Arial, sans-serif" font-size="24" font-weight="700" fill="${C.purple}">Q en posición m=${position}</text>`;
  body += `<text x="${cx2}" y="180" text-anchor="middle" font-family="Arial, sans-serif" font-size="24" font-weight="700" fill="${C.blue}">K en posición n=${Math.max(0, position - 2)}</text>`;
  body += `<rect x="405" y="610" width="390" height="58" rx="14" fill="${C.greenSoft}" stroke="${C.green}" stroke-width="2"/>`;
  body += `<text x="600" y="647" text-anchor="middle" font-family="Arial, sans-serif" font-size="22" font-weight="700" fill="${C.ink}">ángulo relativo = (m − n)θ = 2θ</text>`;
  return svgShell("RoPE: la posición se codifica como una rotación", body);
}

function kvFrame(step) {
  const tokens = ["La", "IA", "aprende", "con", "datos", "útiles"];
  let body = `<text x="60" y="100" font-family="Arial, sans-serif" font-size="20" fill="${C.muted}">Paso ${step + 1}: se incorpora «${tokens[step]}».</text>`;
  body += `<text x="285" y="155" text-anchor="middle" font-family="Arial, sans-serif" font-size="25" font-weight="700" fill="${C.orange}">Sin KV cache</text>`;
  body += `<text x="900" y="155" text-anchor="middle" font-family="Arial, sans-serif" font-size="25" font-weight="700" fill="${C.green}">Con KV cache</text>`;
  body += `<line x1="600" y1="135" x2="600" y2="610" stroke="${C.line}" stroke-width="2"/>`;
  for (let i = 0; i <= step; i++) {
    body += box(75 + i * 82, 220, 70, 55, tokens[i], C.orangeSoft, C.orange, 16);
    body += `<text x="${110 + i * 82}" y="315" text-anchor="middle" font-family="Arial, sans-serif" font-size="16" fill="${C.orange}">K,V ↻</text>`;
    const isNew = i === step;
    body += box(655 + i * 82, 220, 70, 55, tokens[i], isNew ? C.greenSoft : C.blueSoft, isNew ? C.green : C.blue, 16);
    body += `<text x="${690 + i * 82}" y="315" text-anchor="middle" font-family="Arial, sans-serif" font-size="16" fill="${isNew ? C.green : C.blue}">${isNew ? "K,V +" : "cache"}</text>`;
  }
  body += `<rect x="85" y="390" width="410" height="120" rx="18" fill="${C.white}" stroke="${C.line}" stroke-width="2"/>`;
  body += `<text x="290" y="430" text-anchor="middle" font-family="Arial, sans-serif" font-size="20" fill="${C.ink}">Recalcula K y V de todo el prefijo</text>`;
  body += `<text x="290" y="470" text-anchor="middle" font-family="Arial, sans-serif" font-size="25" font-weight="700" fill="${C.orange}">${step + 1} proyecciones por capa</text>`;
  body += `<rect x="705" y="390" width="390" height="120" rx="18" fill="${C.white}" stroke="${C.line}" stroke-width="2"/>`;
  body += `<text x="900" y="430" text-anchor="middle" font-family="Arial, sans-serif" font-size="20" fill="${C.ink}">Reutiliza K y V anteriores</text>`;
  body += `<text x="900" y="470" text-anchor="middle" font-family="Arial, sans-serif" font-size="25" font-weight="700" fill="${C.green}">1 proyección nueva por capa</text>`;
  body += `<text x="600" y="610" text-anchor="middle" font-family="Arial, sans-serif" font-size="20" fill="${C.muted}">La memoria del cache sí crece con la longitud: O(B·S·L·K·H).</text>`;
  return svgShell("Generación autoregresiva: evitar trabajo repetido", body);
}

function ringFrame(step) {
  const devices = [
    { x: 600, y: 180, name: "GPU 0" },
    { x: 930, y: 365, name: "GPU 1" },
    { x: 600, y: 550, name: "GPU 2" },
    { x: 270, y: 365, name: "GPU 3" },
  ];
  const phase = step < 4 ? "Reduce-scatter: sumar y repartir resultados" : "All-gather: distribuir los fragmentos reducidos";
  let body = `<text x="600" y="100" text-anchor="middle" font-family="Arial, sans-serif" font-size="22" fill="${C.muted}">${phase}</text>`;
  devices.forEach((d, i) => {
    const active = i === step % 4;
    body += `<circle cx="${d.x}" cy="${d.y}" r="78" fill="${active ? C.purpleSoft : C.white}" stroke="${active ? C.purple : C.line}" stroke-width="4" filter="url(#shadow)"/>`;
    body += `<text x="${d.x}" y="${d.y - 8}" text-anchor="middle" font-family="Arial, sans-serif" font-size="22" font-weight="700" fill="${C.ink}">${d.name}</text>`;
    body += `<text x="${d.x}" y="${d.y + 27}" text-anchor="middle" font-family="Arial, sans-serif" font-size="18" fill="${active ? C.purple : C.muted}">fragmento ${String.fromCharCode(65 + i)}</text>`;
  });
  for (let i = 0; i < devices.length; i++) {
    const a = devices[i];
    const b = devices[(i + 1) % devices.length];
    const dx = b.x - a.x;
    const dy = b.y - a.y;
    const len = Math.hypot(dx, dy);
    const ux = dx / len;
    const uy = dy / len;
    body += arrow(a.x + ux * 90, a.y + uy * 90, b.x - ux * 90, b.y - uy * 90, C.blue, 5);
  }
  body += `<rect x="455" y="315" width="290" height="100" rx="18" fill="${step < 4 ? C.orangeSoft : C.greenSoft}" stroke="${step < 4 ? C.orange : C.green}" stroke-width="2"/>`;
  body += `<text x="600" y="350" text-anchor="middle" font-family="Arial, sans-serif" font-size="20" fill="${C.ink}">paso ${step + 1} de 8</text>`;
  body += `<text x="600" y="385" text-anchor="middle" font-family="Arial, sans-serif" font-size="22" font-weight="700" fill="${step < 4 ? C.orange : C.green}">${step < 4 ? "sumar" : "copiar"}</text>`;
  body += `<text x="600" y="675" text-anchor="middle" font-family="Arial, sans-serif" font-size="20" fill="${C.muted}">Al final, todas las GPU poseen el mismo resultado reducido.</text>`;
  return svgShell("Ring all-reduce = reduce-scatter + all-gather", body);
}

function softmax(values, temperature) {
  const scaled = values.map((v) => v / temperature);
  const m = Math.max(...scaled);
  const exps = scaled.map((v) => Math.exp(v - m));
  const total = exps.reduce((a, b) => a + b, 0);
  return exps.map((v) => v / total);
}

function temperatureChart() {
  const logits = [2.5, 1.2, 0.2, -0.4];
  const labels = ["gato", "perro", "ave", "pez"];
  const temps = [0.5, 1, 2];
  let body = `<text x="60" y="100" font-family="Arial, sans-serif" font-size="20" fill="${C.muted}">Mismos logits [2.5, 1.2, 0.2, −0.4]; solo cambia T.</text>`;
  temps.forEach((temp, panel) => {
    const x0 = 75 + panel * 380;
    const probs = softmax(logits, temp);
    body += `<text x="${x0 + 140}" y="160" text-anchor="middle" font-family="Arial, sans-serif" font-size="25" font-weight="700" fill="${panel === 0 ? C.orange : panel === 1 ? C.blue : C.purple}">T = ${temp}</text>`;
    body += `<line x1="${x0}" y1="580" x2="${x0 + 300}" y2="580" stroke="${C.line}" stroke-width="2"/>`;
    labels.forEach((label, i) => {
      const h = probs[i] * 390;
      const color = panel === 0 ? C.orange : panel === 1 ? C.blue : C.purple;
      body += `<rect x="${x0 + 8 + i * 72}" y="${580 - h}" width="50" height="${h}" rx="7" fill="${color}" opacity="${0.95 - i * 0.12}"/>`;
      body += `<text x="${x0 + 33 + i * 72}" y="610" text-anchor="middle" font-family="Arial, sans-serif" font-size="16" fill="${C.ink}">${label}</text>`;
      body += `<text x="${x0 + 33 + i * 72}" y="${Math.max(190, 565 - h)}" text-anchor="middle" font-family="Arial, sans-serif" font-size="16" font-weight="700" fill="${C.ink}">${probs[i].toFixed(2)}</text>`;
    });
  });
  body += `<text x="600" y="665" text-anchor="middle" font-family="Arial, sans-serif" font-size="20" fill="${C.muted}">T baja concentra probabilidad; T alta aplana la distribución. No añade conocimiento al modelo.</text>`;
  return svgShell("Temperatura: cambia la forma de la distribución", body);
}

makeGif("03-atencion-paso-a-paso", [0, 1, 2, 3, 4, 4].map(attentionFrame));
makeGif("04-rope-rotaciones", [0, 1, 2, 3, 4, 5, 6, 7].map(ropeFrame), "1");
makeGif("06-kv-cache-generacion", [0, 1, 2, 3, 4, 5, 5].map(kvFrame), "1");
makeGif("12-ring-allreduce", Array.from({ length: 8 }, (_, i) => ringFrame(i)), "1");
writeSvg("07-temperatura-sampling.svg", temperatureChart());

fs.rmSync(tempDir, { recursive: true, force: true });
console.log("Visuales generados en", outDir);
