---
title: Validación, excepciones, assert y tipos
tags:
  - master/matematicas-programacion
  - python
  - validacion
---

# Validación, excepciones, `assert` y tipos

## Tres mecanismos diferentes

| Mecanismo | Para qué sirve | Ejemplo |
|---|---|---|
| type hints | contrato estático/documental | `scores: list[float]` |
| excepción | entrada o estado inválido en producción | `ValueError` |
| assert | invariante interno o prueba | `assert train.isdisjoint(test)` |

## No validar al usuario con assert

Python puede desactivar `assert` con optimización. Para datos externos:

```python
if not 0 < fraction < 1:
    raise ValueError("fraction debe estar entre 0 y 1")
```

## Excepciones específicas

- `ValueError`: valor incompatible;
- `TypeError`: tipo de uso incorrecto;
- `FileNotFoundError`: recurso ausente;
- excepción de dominio propia: cuando añade significado y recuperación.

No captures `Exception` silenciosamente. Si no puedes resolver el error, añade contexto y vuelve a elevar.

## Validar fronteras

Al leer datos verifica:

- columnas requeridas;
- tipos convertibles;
- timestamps monotónicos o política de orden;
- identificadores no vacíos;
- valores finitos;
- unidades y rangos plausibles.

## Invariantes semánticos

```python
assert not set(train_users) & set(test_users)
assert len(scores) == len(labels)
assert all(math.isfinite(x) for x in scores)
```

Una forma correcta no garantiza semántica correcta. Añade pruebas que rompan accidentes: tamaños distintos para ejes distintos, grupos repetidos y casos extremos.

## Tipos no sustituyen validación

`float` no expresa “probabilidad en [0,1]”. Los tipos previenen categorías de errores; las restricciones de dominio requieren comprobaciones.

## Autoevaluación

1. ¿Por qué no usar `assert` para validar una ruta del usuario?
2. ¿Qué diferencia hay entre forma y semántica?
3. ¿Cuándo crear una excepción propia?
4. ¿Qué contexto debe conservar un error de lectura?

---

Anterior: [[02 Configuración, dataclasses, contratos y composición]] · Siguiente: [[04 Pruebas unitarias, integración y pruebas semánticas]]

