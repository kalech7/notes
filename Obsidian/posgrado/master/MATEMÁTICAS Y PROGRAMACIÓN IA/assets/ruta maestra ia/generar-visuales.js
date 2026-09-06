#!/usr/bin/env node

const fs = require("fs");
const os = require("os");
const path = require("path");
const { execFileSync } = require("child_process");

const OUT = __dirname;
const W = 1200;
const H = 700;
const C = {
  ink: "#172033", muted: "#56627A", line: "#C7D0E3", bg: "#F7F9FC",
  blue: "#2F6BFF", cyan: "#19A7AE", green: "#2AA876", orange: "#F59E42",
  red: "#E25555", purple: "#815AC0", white: "#FFFFFF", pale: "#EAF0FF",
};

function esc(value) {
  return String(value).replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;");
}

function shell(title, subtitle, content) {
  return `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="${C.muted}"/></marker>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="4" stdDeviation="5" flood-opacity="0.12"/></filter>
  </defs>
  <rect width="1200" height="700" rx="26" fill="${C.bg}"/>
  <text x="60" y="68" font-family="Helvetica,Arial,sans-serif" font-size="30" font-weight="700" fill="${C.ink}">${esc(title)}</text>
  <text x="60" y="100" font-family="Helvetica,Arial,sans-serif" font-size="17" fill="${C.muted}">${esc(subtitle)}</text>
  ${content}
</svg>`;
}

function box(x, y, w, h, title, lines = [], color = C.blue, active = false) {
  const fill = active ? color : C.white;
  const ink = active ? C.white : C.ink;
  const muted = active ? C.white : C.muted;
  return `<g filter="url(#shadow)">
    <rect x="${x}" y="${y}" width="${w}" height="${h}" rx="18" fill="${fill}" stroke="${color}" stroke-width="${active ? 4 : 2}"/>
    <text x="${x + 20}" y="${y + 34}" font-family="Helvetica,Arial,sans-serif" font-size="19" font-weight="700" fill="${ink}">${esc(title)}</text>
    ${lines.map((line, i) => `<text x="${x + 20}" y="${y + 64 + i * 24}" font-family="Helvetica,Arial,sans-serif" font-size="15" fill="${muted}">${esc(line)}</text>`).join("")}
  </g>`;
}

function arrow(x1, y1, x2, y2, label = "") {
  return `<g><line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${C.muted}" stroke-width="3" marker-end="url(#arrow)"/>${label ? `<text x="${(x1 + x2) / 2}" y="${(y1 + y2) / 2 - 10}" text-anchor="middle" font-family="Helvetica,Arial,sans-serif" font-size="14" fill="${C.muted}">${esc(label)}</text>` : ""}</g>`;
}

function footer(text) {
  return `<rect x="60" y="625" width="1080" height="42" rx="14" fill="${C.ink}"/><text x="600" y="652" text-anchor="middle" font-family="Helvetica,Arial,sans-serif" font-size="17" font-weight="700" fill="white">${esc(text)}</text>`;
}

function writeSvg(name, svg) {
  fs.mkdirSync(OUT, { recursive: true });
  fs.writeFileSync(path.join(OUT, name), svg);
}

function makeGif(name, frames, fps = 0.8) {
  const temp = fs.mkdtempSync(path.join(os.tmpdir(), "ia-visual-"));
  try {
    frames.forEach((svg, i) => {
      const stem = `frame-${String(i).padStart(2, "0")}`;
      const svgPath = path.join(temp, `${stem}.svg`);
      const pngPath = path.join(temp, `${stem}.png`);
      fs.writeFileSync(svgPath, svg);
      execFileSync("/usr/bin/sips", ["-s", "format", "png", svgPath, "--out", pngPath], { stdio: "ignore" });
    });
    execFileSync("ffmpeg", [
      "-y", "-loglevel", "error", "-framerate", String(fps), "-i", path.join(temp, "frame-%02d.png"),
      "-vf", "split[s0][s1];[s0]palettegen=max_colors=96[p];[s1][p]paletteuse=dither=bayer", "-loop", "0", path.join(OUT, name),
    ]);
  } finally {
    fs.rmSync(temp, { recursive: true, force: true });
  }
}

// 1. Ruta maestra
writeSvg("01-mapa-ruta-maestra.svg", shell("Ruta maestra para entender IA", "Cada capa responde una pregunta distinta; saltarse una deja huecos", `
  ${box(60, 145, 230, 150, "1 · Lenguaje", ["Python, objetos", "pruebas y contratos"], C.purple)}
  ${box(330, 145, 230, 150, "2 · Matemática", ["probabilidad, cálculo", "álgebra y numérica"], C.blue)}
  ${box(600, 145, 230, 150, "3 · Aprendizaje", ["pérdidas, métricas", "generalización"], C.cyan)}
  ${box(870, 145, 270, 150, "4 · Modelos", ["redes, atención", "RAG y anomalías"], C.green)}
  ${arrow(290, 220, 330, 220)}${arrow(560, 220, 600, 220)}${arrow(830, 220, 870, 220)}
  ${box(170, 380, 250, 135, "Representar", ["¿Cómo convierto el mundo", "en números y tensores?"], C.orange)}
  ${box(475, 380, 250, 135, "Aprender", ["¿Qué error minimizo y", "cómo cambian parámetros?"], C.red)}
  ${box(780, 380, 250, 135, "Evaluar", ["¿Generaliza, es seguro", "y sirve al objetivo?"], C.green)}
  ${arrow(420, 448, 475, 448)}${arrow(725, 448, 780, 448)}
  ${footer("Entender = definir → calcular → implementar → verificar → explicar límites")}
`));

// 2. Bayes y tasa base
const bayesStages = [
  ["Población", "1 000 casos", "10 enfermos · 990 sanos"],
  ["Test sensible", "Detecta 9 de 10", "1 falso negativo"],
  ["Falsos positivos", "Marca 50 de 990", "Aunque solo falla 5 %"],
  ["Posterior", "9 verdaderos / 59 positivos", "P(enfermo | +) = 15,3 %"],
];
makeGif("02-bayes-tasa-base.gif", bayesStages.map((_, active) => shell("Bayes: por qué importa la tasa base", "Sensibilidad alta no implica que un positivo sea casi seguro", `
  ${bayesStages.map((s, i) => box(60 + i * 280, 190, 240, 180, s[0], [s[1], s[2]], [C.blue, C.green, C.orange, C.red][i], i === active)).join("")}
  ${arrow(300, 280, 340, 280)}${arrow(580, 280, 620, 280)}${arrow(860, 280, 900, 280)}
  <text x="600" y="470" text-anchor="middle" font-family="Helvetica,Arial,sans-serif" font-size="28" font-weight="700" fill="${C.ink}">9 / (9 + 50) = 0,153</text>
  ${footer(`Paso ${active + 1}/4 · El denominador correcto incluye verdaderos y falsos positivos`)}`)), 0.7);

// 3. CLT
function bell(cx, cy, spread, color, opacity = 1) {
  const points = [];
  for (let x = -220; x <= 220; x += 4) {
    const y = -180 * Math.exp(-(x * x) / (2 * spread * spread));
    points.push(`${cx + x},${cy + y}`);
  }
  return `<polyline points="${points.join(" ")}" fill="none" stroke="${color}" stroke-width="6" opacity="${opacity}"/>`;
}
const clt = [
  { n: 1, spread: 150, se: "σ" }, { n: 10, spread: 85, se: "σ/√10" }, { n: 100, spread: 42, se: "σ/10" },
];
makeGif("03-clt-medias.gif", clt.map((stage, active) => shell("Ley de los grandes números y CLT", "Al promediar más observaciones, la media muestral fluctúa menos", `
  <line x1="150" y1="500" x2="1050" y2="500" stroke="${C.ink}" stroke-width="3"/>
  ${clt.map((s, i) => bell(600, 500, s.spread, [C.orange, C.cyan, C.blue][i], i <= active ? 1 : 0.12)).join("")}
  ${box(90, 155, 280, 120, `n = ${stage.n}`, [`Error estándar = ${stage.se}`, "La curva se estrecha"], C.blue, true)}
  <line x1="600" y1="300" x2="600" y2="520" stroke="${C.red}" stroke-width="3" stroke-dasharray="8 8"/>
  <text x="600" y="555" text-anchor="middle" font-family="Helvetica,Arial,sans-serif" font-size="16" fill="${C.muted}">media poblacional μ</text>
  ${footer(`Animación: n=${stage.n} · Más datos reducen incertidumbre, no corrigen sesgo`)}`)), 0.7);

// 4. Descenso por gradiente y Taylor
const pathPoints = [[930, 205], [810, 300], [700, 385], [620, 435], [585, 460]];
makeGif("04-gradiente-taylor.gif", pathPoints.map((_, active) => shell("Gradiente: dirección local de mayor aumento", "Descenso usa −∇L; Taylor predice el cambio para pasos pequeños", `
  <ellipse cx="570" cy="470" rx="420" ry="190" fill="none" stroke="#D9E1F2" stroke-width="3"/>
  <ellipse cx="570" cy="470" rx="310" ry="140" fill="none" stroke="#BCC9E3" stroke-width="3"/>
  <ellipse cx="570" cy="470" rx="200" ry="90" fill="none" stroke="#9DB0D7" stroke-width="3"/>
  <ellipse cx="570" cy="470" rx="90" ry="40" fill="none" stroke="${C.blue}" stroke-width="4"/>
  ${pathPoints.slice(0, active + 1).map((p, i) => `<circle cx="${p[0]}" cy="${p[1]}" r="${i === active ? 13 : 8}" fill="${i === active ? C.red : C.orange}"/>`).join("")}
  ${pathPoints.slice(0, active).map((p, i) => arrow(p[0] - 8, p[1] + 8, pathPoints[i + 1][0] + 8, pathPoints[i + 1][1] - 8)).join("")}
  ${box(70, 150, 340, 145, "Actualización", ["θₙ₊₁ = θₙ − η∇L(θₙ)", "η grande puede divergir"], C.purple)}
  ${footer(`Iteración ${active + 1}/${pathPoints.length} · El gradiente es local; el learning rate decide cuánto confiar`)}`)), 0.9);

// 5. Sesgo-varianza
writeSvg("05-bias-varianza.svg", shell("Sesgo, varianza y generalización", "La menor pérdida de training no garantiza el menor error futuro", `
  <line x1="130" y1="540" x2="1080" y2="540" stroke="${C.ink}" stroke-width="3" marker-end="url(#arrow)"/>
  <line x1="130" y1="540" x2="130" y2="155" stroke="${C.ink}" stroke-width="3" marker-end="url(#arrow)"/>
  <path d="M160 205 C420 300, 720 450, 1050 510" fill="none" stroke="${C.blue}" stroke-width="7"/>
  <path d="M160 205 C370 500, 680 520, 1050 240" fill="none" stroke="${C.red}" stroke-width="7"/>
  <line x1="610" y1="190" x2="610" y2="545" stroke="${C.green}" stroke-width="4" stroke-dasharray="10 9"/>
  <text x="910" y="500" font-family="Helvetica,Arial,sans-serif" font-size="18" font-weight="700" fill="${C.blue}">training</text>
  <text x="900" y="305" font-family="Helvetica,Arial,sans-serif" font-size="18" font-weight="700" fill="${C.red}">validation</text>
  <text x="610" y="175" text-anchor="middle" font-family="Helvetica,Arial,sans-serif" font-size="17" font-weight="700" fill="${C.green}">complejidad útil</text>
  <text x="600" y="590" text-anchor="middle" font-family="Helvetica,Arial,sans-serif" font-size="17" fill="${C.muted}">complejidad del modelo →</text>
  <text x="45" y="350" transform="rotate(-90 45 350)" text-anchor="middle" font-family="Helvetica,Arial,sans-serif" font-size="17" fill="${C.muted}">error esperado</text>
  ${footer("Subajuste ← sesgo alto · punto útil · varianza alta → sobreajuste")}
`));

// 6. Forward y backward
const nnSteps = [
  ["Entrada x", ["features", "forma: B×d"]], ["Forward", ["z = Wx+b", "a = ReLU(z)"]],
  ["Pérdida", ["L(ŷ,y)", "mide el error"]], ["Backward", ["∂L/∂W", "regla de cadena"]],
  ["Update", ["W ← W−ηg", "repetir"]],
];
makeGif("06-red-forward-backward.gif", nnSteps.map((_, active) => shell("Una red aprende en un ciclo", "Forward calcula; backward atribuye responsabilidad; el optimizador cambia parámetros", `
  ${nnSteps.map((s, i) => box(35 + i * 232, 215, 200, 175, s[0], s[1], [C.purple, C.blue, C.orange, C.red, C.green][i], i === active)).join("")}
  ${[0,1,2,3].map(i => arrow(235 + i * 232, 300, 267 + i * 232, 300)).join("")}
  <path d="M1065 410 C1040 540, 260 560, 150 420" fill="none" stroke="${C.muted}" stroke-width="3" stroke-dasharray="8 7" marker-end="url(#arrow)"/>
  ${footer(`Paso ${active + 1}/5 · Sin loss no hay señal; sin backward no hay crédito; sin update no hay aprendizaje`)}`)), 0.9);

// 7. Condicionamiento
writeSvg("07-condicionamiento.svg", shell("Condicionamiento: cuánto amplifica un problema el ruido", "Estabilidad habla del algoritmo; condicionamiento habla del problema", `
  ${box(70, 175, 300, 160, "Bien condicionado", ["entrada cambia 0,1 %", "salida cambia ≈0,1 %"], C.green)}
  ${box(450, 175, 300, 160, "Mal condicionado", ["entrada cambia 0,1 %", "salida cambia 100× o más"], C.red)}
  ${box(830, 175, 300, 160, "Qué hacer", ["QR/SVD, regularizar", "escalar y medir κ(A)"], C.blue)}
  ${arrow(370, 255, 450, 255)}${arrow(750, 255, 830, 255)}
  <text x="600" y="455" text-anchor="middle" font-family="Helvetica,Arial,sans-serif" font-size="30" font-weight="700" fill="${C.ink}">error relativo de salida ≤ κ(A) × error relativo de entrada</text>
  ${footer("Evita formar A⁻¹ y AᵀA sin necesidad: pueden amplificar redondeo y condición")}
`));

// 8. Particiones sin fuga
const splitSteps = [
  ["Agrupar", ["por persona/sesión", "unidad indivisible"]], ["Training", ["ajusta parámetros", "y scaler"]],
  ["Validation", ["elige umbral", "e hiperparámetros"]], ["Test", ["estima desempeño", "una sola vez"]],
];
makeGif("08-particiones-sin-fuga.gif", splitSteps.map((_, active) => shell("Particiones sin fuga de información", "Primero agrupa; después divide. Ninguna identidad o sesión debe cruzar fronteras", `
  ${splitSteps.map((s, i) => box(70 + i * 280, 210, 230, 185, s[0], s[1], [C.purple, C.blue, C.orange, C.green][i], i === active)).join("")}
  ${arrow(300, 302, 350, 302)}${arrow(580, 302, 630, 302)}${arrow(860, 302, 910, 302)}
  <text x="600" y="500" text-anchor="middle" font-family="Helvetica,Arial,sans-serif" font-size="22" font-weight="700" fill="${C.red}">Fuga = información del futuro o del test influye en el entrenamiento</text>
  ${footer(`Paso ${active + 1}/4 · La unidad de independencia manda: usuario, sesión, paciente o tiempo`)}`)), 0.75);

// 9. FAR/FRR
writeSvg("09-far-frr-umbral.svg", shell("FAR, FRR y el umbral biométrico", "Mover el umbral intercambia seguridad y comodidad; no existe un valor universal", `
  <line x1="130" y1="545" x2="1080" y2="545" stroke="${C.ink}" stroke-width="3" marker-end="url(#arrow)"/>
  <line x1="130" y1="545" x2="130" y2="160" stroke="${C.ink}" stroke-width="3" marker-end="url(#arrow)"/>
  <path d="M155 500 C380 470, 600 340, 1040 180" fill="none" stroke="${C.red}" stroke-width="7"/>
  <path d="M155 180 C400 250, 660 410, 1040 510" fill="none" stroke="${C.blue}" stroke-width="7"/>
  <circle cx="600" cy="355" r="13" fill="${C.green}"/><line x1="600" y1="355" x2="600" y2="545" stroke="${C.green}" stroke-width="4" stroke-dasharray="8 7"/>
  <text x="900" y="230" font-family="Helvetica,Arial,sans-serif" font-size="20" font-weight="700" fill="${C.red}">FAR: impostores aceptados</text>
  <text x="820" y="490" font-family="Helvetica,Arial,sans-serif" font-size="20" font-weight="700" fill="${C.blue}">FRR: legítimos rechazados</text>
  <text x="620" y="340" font-family="Helvetica,Arial,sans-serif" font-size="17" font-weight="700" fill="${C.green}">EER aproximado</text>
  <text x="600" y="590" text-anchor="middle" font-family="Helvetica,Arial,sans-serif" font-size="17" fill="${C.muted}">umbral de rechazo →</text>
  ${footer("El EER compara sistemas; producción elige umbral según el costo de cada error")}
`));

// 10. RAG
const ragSteps = [
  ["Pregunta", ["intención", "y restricciones"]], ["Recuperar", ["chunks candidatos", "vector + léxico"]],
  ["Rerank", ["ordena por", "relevancia real"]], ["Generar", ["usa evidencia", "y cita fuentes"]],
  ["Evaluar", ["recall + fidelidad", "y respuesta"]],
];
makeGif("10-rag-pipeline.gif", ragSteps.map((_, active) => shell("RAG no es solo buscar y pegar", "Cada etapa puede fallar y necesita su propia métrica", `
  ${ragSteps.map((s, i) => box(35 + i * 232, 215, 200, 175, s[0], s[1], [C.purple, C.blue, C.cyan, C.orange, C.green][i], i === active)).join("")}
  ${[0,1,2,3].map(i => arrow(235 + i * 232, 300, 267 + i * 232, 300)).join("")}
  ${footer(`Paso ${active + 1}/5 · Si no recuperas evidencia correcta, el generador no puede inventar confiabilidad`)}`)), 0.85);

// 11. Proyecto mouse
writeSvg("11-proyecto-mouse.svg", shell("Proyecto: autenticación continua por dinámica de mouse", "Del evento crudo a una decisión auditable, sin usar el test para calibrar", `
  ${box(45, 170, 190, 160, "Eventos", ["t, x, y", "botón, estado"], C.purple)}
  ${box(275, 170, 190, 160, "Sesión", ["trayectoria", "unidad indivisible"], C.blue)}
  ${box(505, 170, 190, 160, "17 features", ["velocidad, pausas", "ángulos, distancia"], C.cyan)}
  ${box(735, 170, 190, 160, "Perfil", ["RMS-z", "Isolation Forest"], C.orange)}
  ${box(965, 170, 190, 160, "Decisión", ["score ≥ τ", "alarma"], C.red)}
  ${arrow(235, 250, 275, 250)}${arrow(465, 250, 505, 250)}${arrow(695, 250, 735, 250)}${arrow(925, 250, 965, 250)}
  ${box(235, 425, 300, 120, "Validation legítimo", ["elige τ sin mirar test"], C.green)}
  ${box(665, 425, 300, 120, "Test público", ["mide FAR, FRR, F1"], C.blue)}
  ${arrow(535, 485, 665, 485, "umbral fijo")}
  ${footer("Score alto significa anomalía; anomalía no prueba intención maliciosa")}
`));

// 12. Experimento reproducible
writeSvg("12-experimento-reproducible.svg", shell("Anatomía de un experimento reproducible", "Un número sin contexto no es un resultado científico", `
  ${box(70, 160, 300, 145, "Entradas", ["datos + versión", "código + entorno"], C.blue)}
  ${box(450, 160, 300, 145, "Configuración", ["seed, split, features", "modelo, hiperparámetros"], C.purple)}
  ${box(830, 160, 300, 145, "Ejecución", ["logs y validaciones", "errores visibles"], C.orange)}
  ${arrow(370, 232, 450, 232)}${arrow(750, 232, 830, 232)}
  ${box(210, 415, 330, 130, "Artefactos", ["modelo, predicciones", "hashes y métricas"], C.cyan)}
  ${box(660, 415, 330, 130, "Explicación", ["supuestos, límites", "y decisión resultante"], C.green)}
  ${arrow(540, 480, 660, 480)}
  ${footer("Reproducible = otra persona puede reconstruir qué ocurrió y por qué")}
`));

// 13. Resultados reales del baseline, si ya existe el reporte.
const reportPath = path.resolve(OUT, "../../proyecto/notebook/reports/baseline_metrics.json");
if (fs.existsSync(reportPath)) {
  const report = JSON.parse(fs.readFileSync(reportPath, "utf8"));
  const rms = report.aggregate.rms_z;
  const forest = report.aggregate.isolation_forest;
  const metrics = [
    ["F1 impostor ↑", rms.f1_impostor, forest.f1_impostor],
    ["Accuracy ↑", rms.accuracy, forest.accuracy],
    ["FAR ↓", rms.far, forest.far],
    ["FRR ↓", rms.frr, forest.frr],
  ];
  const bars = metrics.map((m, i) => {
    const x = 120 + i * 265;
    const base = 535;
    const hr = 280 * m[1];
    const hf = 280 * m[2];
    return `<text x="${x + 80}" y="190" text-anchor="middle" font-family="Helvetica,Arial,sans-serif" font-size="17" font-weight="700" fill="${C.ink}">${m[0]}</text>
      <rect x="${x}" y="${base - hr}" width="65" height="${hr}" rx="8" fill="${C.cyan}"/>
      <rect x="${x + 90}" y="${base - hf}" width="65" height="${hf}" rx="8" fill="${C.orange}"/>
      <text x="${x + 32}" y="${base - hr - 10}" text-anchor="middle" font-family="Helvetica,Arial,sans-serif" font-size="15" font-weight="700" fill="${C.cyan}">${m[1].toFixed(3)}</text>
      <text x="${x + 122}" y="${base - hf - 10}" text-anchor="middle" font-family="Helvetica,Arial,sans-serif" font-size="15" font-weight="700" fill="${C.orange}">${m[2].toFixed(3)}</text>`;
  }).join("");
  writeSvg("13-baseline-resultados.svg", shell("Baseline real: qué dicen las métricas", "816 sesiones públicas; el resultado sirve para diagnosticar, no para declarar éxito", `
    <line x1="90" y1="535" x2="1110" y2="535" stroke="${C.ink}" stroke-width="3"/>
    ${bars}
    <rect x="330" y="565" width="18" height="18" rx="4" fill="${C.cyan}"/><text x="358" y="580" font-family="Helvetica,Arial,sans-serif" font-size="16" fill="${C.muted}">RMS-z</text>
    <rect x="500" y="565" width="18" height="18" rx="4" fill="${C.orange}"/><text x="528" y="580" font-family="Helvetica,Arial,sans-serif" font-size="16" fill="${C.muted}">Isolation Forest</text>
    ${footer("Hallazgo: ambos umbrales rechazan demasiados legítimos; toca mejorar calibración y protocolo")}
  `));
}

console.log("Generados los recursos visuales en", OUT);
