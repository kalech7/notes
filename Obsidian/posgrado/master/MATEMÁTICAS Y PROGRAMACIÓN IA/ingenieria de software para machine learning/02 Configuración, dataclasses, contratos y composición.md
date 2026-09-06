---
title: Configuración, dataclasses, contratos y composición
tags:
  - master/matematicas-programacion
  - python
  - arquitectura
---

# Configuración, dataclasses, contratos y composición

## Dataclass

Una `dataclass` expresa un registro con campos conocidos:

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class SplitConfig:
    validation_fraction: float = 0.2
    seed: int = 7
```

`frozen=True` evita cambios accidentales después de iniciar una corrida.

## Contrato estructural con Protocol

```python
from typing import Protocol, Sequence

class Scorer(Protocol):
    def fit(self, X: Sequence[Sequence[float]]) -> None: ...
    def score(self, X: Sequence[Sequence[float]]) -> list[float]: ...
```

Cualquier clase que cumpla esas operaciones puede participar sin heredar de una base concreta.

## ABC cuando necesitas una jerarquía nominal

Una clase abstracta sirve cuando quieres compartir implementación y exigir métodos. `Protocol` favorece bajo acoplamiento; ABC expresa pertenencia explícita a una familia.

## Composición

```python
@dataclass
class Experiment:
    loader: DataLoader
    features: FeatureExtractor
    model: Scorer
    evaluator: Evaluator
```

El experimento **tiene** componentes. No necesita heredar de todos.

## Inyección de dependencias

Recibir componentes desde afuera permite:

- reemplazar el modelo sin cambiar carga de datos;
- usar dobles de prueba;
- probar cada pieza;
- evitar variables globales.

## API pequeña

Prefiere métodos con contratos claros:

```text
fit(train) → estado aprendido
transform(data) → misma semántica, nueva representación
predict(data) → etiquetas
score(data) → puntajes continuos
evaluate(y, score) → métricas
```

No mezcles `score` como “métrica del modelo” y “puntaje por observación” sin nombres explícitos.

## Autoevaluación

1. ¿Cuándo usar `dataclass(frozen=True)`?
2. ¿Qué diferencia Protocol de ABC?
3. ¿Por qué composición reduce acoplamiento?
4. ¿Qué aporta inyectar un modelo falso en tests?

---

Anterior: [[01 Estructura, entornos y reproducibilidad]] · Siguiente: [[03 Validación, excepciones, assert y tipos]]

