---
title: Fine-tuning eficiente - LoRA, QLoRA y PEFT
tags:
  - master/matematicas-programacion
  - llm
  - lora
  - fine-tuning
---

# Fine-tuning eficiente: LoRA, QLoRA y PEFT

## Qué cambia en fine-tuning

Partimos de pesos preentrenados $W_0$ y buscamos adaptar comportamiento. Fine-tuning completo actualiza todos los parámetros; PEFT actualiza una fracción pequeña.

## LoRA

En vez de aprender una matriz densa $\Delta W\in\mathbb R^{d_{out}\times d_{in}}$, factoriza:

$$\Delta W=BA,$$

$$A\in\mathbb R^{r\times d_{in}},\qquad
B\in\mathbb R^{d_{out}\times r},\qquad r\ll d.$$

La capa usa:

$$y=W_0x+\frac\alpha rBAx.$$

$W_0$ queda congelada; se entrenan $A,B$.

## Conteo

Matriz densa: $d_{out}d_{in}$ parámetros adaptables.

LoRA: $r(d_{in}+d_{out})$.

Con $d_{in}=d_{out}=4096$ y $r=16$:

$$16(4096+4096)=131072$$

frente a $4096^2=16777216$.

## Interpretación

LoRA supone que el cambio útil de la tarea vive aproximadamente en un subespacio de rango bajo. No reduce necesariamente el coste base de forward: reduce memoria de gradientes y optimizador para parámetros adaptables.

## Dónde aplicarla

Comúnmente a proyecciones de atención y, según presupuesto, FFN. La elección de módulos, rango, alpha y dropout es un hiperparámetro que debe validarse.

## QLoRA

Mantiene el modelo base cuantizado para ahorrar memoria y entrena adaptadores LoRA en mayor precisión. Conceptualmente:

```text
pesos base cuantizados y congelados
        +
adaptadores LoRA entrenables
```

La cuantización introduce aproximación y requisitos de kernels; los gradientes no convierten mágicamente todos los cálculos en 4 bits.

## Adapter lifecycle

- conservar tokenizador y plantilla de chat;
- registrar modelo base exacto;
- guardar configuración LoRA;
- evaluar antes/después;
- poder fusionar adaptador o cargarlo por separado;
- documentar licencia y datos.

## Riesgos

- sobreajuste a formatos pequeños;
- degradación de capacidades generales;
- memorizar datos sensibles;
- evaluación contaminada;
- confundir estilo obediente con veracidad;
- entrenar sin máscara correcta de tokens objetivo.

## Fine-tuning frente a RAG

| Necesidad | Mecanismo inicial |
|---|---|
| enseñar formato/estilo | SFT/LoRA |
| incorporar conocimiento cambiante y citable | RAG |
| cambiar comportamiento profundo | fine-tuning con evaluación amplia |
| responder una instrucción ocasional | prompting |

## Autoevaluación

1. ¿Qué rango tiene $BA$ como máximo?
2. ¿Qué memoria ahorra LoRA?
3. ¿Qué añade QLoRA?
4. ¿Por qué RAG suele ser mejor para documentos cambiantes?

---

Anterior: [[16 Tokenización práctica - BPE, WordPiece y SentencePiece]] · Siguiente: [[18 RAG - chunking, embeddings, recuperación y reranking]]

