---
title: Laboratorio - mini Transformer causal en PyTorch
tags:
  - master/matematicas-programacion
  - pytorch
  - transformer
  - laboratorio
related:
  - "[[python/mini_transformer_pytorch.py]]"
  - "[[python/atencion_desde_cero.py]]"
---

# Laboratorio: mini Transformer causal en PyTorch

## Objetivo

Construir y auditar la ruta:

```text
token IDs → embedding → bloques → logits → CE desplazada → backward
```

Archivos:

- [[python/atencion_desde_cero.py]]: atención causal sin dependencias;
- [[python/mini_transformer_pytorch.py]]: mini LLM con PyTorch.

## Parte A: atención sin dependencias

Ejecuta:

```bash
python3 "python/atencion_desde_cero.py"
```

La salida verificada en este vault es:

```text
Pesos de atención:
[1.0, 0.0, 0.0]
[0.5423, 0.4577, 0.0]
[0.2491, 0.3123, 0.4386]

Salida ponderada:
[10.0, 0.0]
[5.4232, 9.1535]
[4.6838, 8.4397]
```

### Qué comprobar

1. cada fila de pesos suma 1;
2. el triángulo superior vale 0 después de softmax;
3. la primera salida coincide exactamente con $v_1$;
4. la última salida mezcla los tres valores.

## Parte B: modelo PyTorch

El modelo usa:

- `nn.Embedding`;
- atención causal con `scaled_dot_product_attention`;
- arquitectura pre-norm;
- `nn.RMSNorm`;
- FFN SwiGLU;
- weight tying entre embedding y salida;
- pérdida next-token desplazada.

## Formas del caso de prueba

```text
batch token IDs     (3, 8)
embedding           (3, 8, 24)
Q, K, V             (3, 4, 8, 6)
atención             (3, 4, 8, 6)
unir cabezas         (3, 8, 24)
logits               (3, 8, 32)
targets desplazados  (3, 7)
pérdida              ()
```

## Atención

Fragmento central:

```python
qkv = self.qkv(x)
qkv = qkv.reshape(batch, seq_len, 3, self.num_heads, self.head_dim)
q, k, v = qkv.unbind(dim=2)

q = q.transpose(1, 2)
k = k.transpose(1, 2)
v = v.transpose(1, 2)

attended = F.scaled_dot_product_attention(
    q, k, v,
    dropout_p=0.0,
    is_causal=True,
)
```

`transpose(1, 2)` pasa de `(B,S,N,H)` a `(B,N,S,H)`.

## Volver a $D$

```python
attended = attended.transpose(1, 2).contiguous()
attended = attended.reshape(batch, seq_len, d_model)
```

Después de transponer, `contiguous()` produce una disposición física compatible con el aplanado esperado. `reshape` puede copiar si hace falta; hacerlo explícito facilita la auditoría.

## SwiGLU

```python
return self.down(F.silu(self.gate(x)) * self.up(x))
```

Formas:

```text
x                 (B,S,D)
gate(x), up(x)    (B,S,F)
producto          (B,S,F)
down              (B,S,D)
```

## Residuales pre-norm

```python
x = x + self.attn(self.attn_norm(x))
x = x + self.ffn(self.ffn_norm(x))
```

Ambas ramas vuelven a forma $(B,S,D)$ antes de sumar.

## Weight tying

```python
self.lm_head.weight = self.embedding.weight
```

No copia valores: ambos módulos referencian el mismo parámetro. Por eso el gradiente de embedding recibe contribuciones del lookup de entrada y de la proyección de salida.

## Pérdida desplazada

```python
predictions = logits[:, :-1, :]
targets = token_ids[:, 1:]

loss = F.cross_entropy(
    predictions.reshape(-1, predictions.size(-1)),
    targets.reshape(-1),
)
```

Hay $B(S-1)$ decisiones de clasificación.

## Ejecución

Desde esta carpeta, en un entorno con PyTorch:

```bash
python3 "python/mini_transformer_pytorch.py"
```

Se comprueba:

- `logits.shape == (3, 8, 32)`;
- la pérdida es escalar;
- existe gradiente para `embedding.weight`.

El archivo fue verificado sintácticamente en este entorno. La ejecución completa requiere PyTorch, que no está instalado en el intérprete actual del vault.

## Experimentos guiados

### 1. Romper causalidad

Cambia `is_causal=True` por `False`. No concluyas solo mirando la pérdida inicial. Entrena en una secuencia pequeña y observa que el modelo puede usar tokens futuros.

### 2. Prueba de prefijo

Para dos entradas con el mismo prefijo y distinto futuro, los logits de las posiciones del prefijo deben ser iguales en modo evaluación.

```python
x1 = torch.tensor([[1, 2, 3, 4, 5]])
x2 = torch.tensor([[1, 2, 3, 9, 9]])

with torch.inference_mode():
    z1 = model(x1)
    z2 = model(x2)

assert torch.allclose(z1[:, :3], z2[:, :3], atol=1e-6)
```

Esta prueba detecta fugas del futuro.

### 3. Inspección de parámetros compartidos

```python
assert model.embedding.weight is model.lm_head.weight
```

### 4. Un paso de optimización

Predice primero qué debe ocurrir con la pérdida; luego ejecuta varias iteraciones y registra:

- pérdida;
- norma del gradiente;
- norma de parámetros;
- token accuracy del lote.

### 5. Añadir RoPE

Implementa una función sobre $Q,K$ y comprueba que:

- conserva forma;
- conserva norma de cada par salvo redondeo;
- no modifica $V$.

### 6. Añadir KV cache

Separa `prefill` de `decode` y verifica igualdad numérica entre:

1. forward completo del prefijo extendido;
2. un paso nuevo usando cache.

## Pruebas semánticas mínimas

| Prueba | Invariante |
|---|---|
| formas QKV | $D=NH$ |
| máscara causal | futuro no cambia logits previos |
| softmax | suma 1 sobre claves |
| residual | entrada y rama tienen misma forma |
| CE | posición $t$ predice $t+1$ |
| tying | mismo objeto parámetro |
| backward | gradiente existe y es finito |

> [!tip] Método del laboratorio
> Antes de ejecutar, escribe la forma esperada y una propiedad numérica. Una salida sin excepción no demuestra que el modelo sea semánticamente correcto.

---

Anterior: [[13 Multimodalidad - ViT, CLIP y LLaVA]] · Siguiente: [[15 Resumen, mapa mental y autoevaluación]]
