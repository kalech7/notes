---
title: Estructura, entornos y reproducibilidad
tags:
  - master/matematicas-programacion
  - reproducibilidad
---

# Estructura, entornos y reproducibilidad

## Estructura mínima

```text
proyecto/
├── pyproject.toml
├── uv.lock
├── README.md
├── src/mi_proyecto/
├── tests/
├── notebooks/
└── reports/
```

- `src/` contiene lógica reutilizable;
- notebooks exploran y presentan, no esconden toda la implementación;
- tests fijan invariantes;
- reports conserva resultados derivados;
- data y `.venv` se reconstruyen o descargan y normalmente no se versionan.

## Entorno reproducible

```bash
uv sync --locked
uv run pytest
```

`pyproject.toml` declara lo deseado; `uv.lock` fija la solución exacta. Versiona ambos, no `.venv`.

## Semillas

Una semilla ayuda a repetir una secuencia pseudoaleatoria, pero no garantiza reproducibilidad universal:

- hardware y kernels pueden diferir;
- paralelismo cambia orden de operaciones;
- versiones cambian defaults;
- datos externos pueden cambiar.

Registra versión de Python, dependencias, plataforma, semilla y hash o versión del dataset.

## Configuración como dato

No disperses hiperparámetros por el código. Reúne:

```python
@dataclass(frozen=True)
class TrainConfig:
    seed: int
    learning_rate: float
    epochs: int
```

La configuración debe poder serializarse junto a resultados.

## Funciones puras y efectos

Separa:

- transformar datos: entrada → salida;
- leer/escribir archivos;
- entrenar;
- evaluar;
- presentar resultados.

Las funciones puras son más fáciles de probar. Los efectos deben estar en bordes explícitos.

## Notebook reproducible

Un notebook sano:

1. parte de un entorno limpio;
2. ejecuta de arriba abajo;
3. no depende de variables ocultas;
4. llama funciones de `src/`;
5. registra entradas y genera salidas deterministas cuando corresponde.

## Autoevaluación

1. ¿Qué diferencia hay entre `pyproject.toml`, `uv.lock` y `.venv`?
2. ¿Por qué una semilla no garantiza identidad en cualquier máquina?
3. ¿Qué lógica debe salir de un notebook?
4. ¿Por qué los efectos en los bordes facilitan tests?

---

Anterior: [[00 Índice y recordatorio - Ingeniería de software para ML]] · Siguiente: [[02 Configuración, dataclasses, contratos y composición]]

