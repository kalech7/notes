---
tags:
  - machine-learning
  - poo
  - python
  - matematicas-programacion-ia
---

# POO aplicada a Machine Learning — índice de estudio

Esta carpeta reorganiza la nota completa [[Programación orientada a objetos aplicada a Machine Learning]] en sesiones más pequeñas. La idea es estudiar primero cómo funciona la POO y después construir una clase `Scalar` capaz de conservar la historia de sus operaciones.

## Ruta recomendada

1. [[01 Fundamentos de POO]]
2. [[02 Herencia y composición]]
3. [[03 Métodos dunder]]
4. [[04 Buenas prácticas y assert]]
5. [[05 Scalar y autodiferenciación]]
6. [[06 Grafo computacional y neurona]]

Después continúa con [[../ingenieria de software para machine learning/00 Índice y recordatorio - Ingeniería de software para ML|Ingeniería de software para ML]] para convertir clases aisladas en experimentos reproducibles, validados y probados.

## Mapa de conceptos

```text
Clase e instancia
        │
        ├── self, __init__ y métodos
        ├── herencia y composición
        └── dunder y sobrecarga de operadores
                          │
                          ▼
                 clase Scalar
                          │
                          ├── valor numérico
                          ├── padres y operación
                          └── grafo computacional
                                      │
                                      ├── orden topológico
                                      └── backpropagation
```

## Cómo estudiar cada nota

- Lee la teoría y explica el concepto con tus propias palabras.
- Ejecuta los ejemplos en un notebook o archivo Python.
- Modifica una línea y predice el resultado antes de ejecutar.
- Responde las preguntas de repaso al final de cada nota.

> [!tip] Idea central del módulo
> La POO no deriva por sí sola: organiza los objetos, sus relaciones y la historia computacional que harán posible la autodiferenciación.

## Nota de referencia

La nota original se conserva completa aquí: [[Programación orientada a objetos aplicada a Machine Learning]].

## Grafo con el resto del posgrado

La ruta completa del material puede leerse así:

```text
[[UV]]
   ↓ prepara el entorno reproducible
[[Estructuras de Python en un experimento de IA]]
   ↓ define estructuras e invariantes de los datos
[[Programación orientada a objetos aplicada a Machine Learning]]
   ↓ encapsula comportamiento y construye Scalar
[[numpy pandas parquet arrow]]
   ↓ transforma y conserva datos con contexto
[[funcion de perdida]]
   ↓ mide el error y guía el entrenamiento
```

Enlaces directos:

- [[UV]] — entorno, dependencias y reproducibilidad.
- [[Estructuras de Python en un experimento de IA]] — `list`, `tuple`, `dict`, aliasing y copias defensivas.
- [[numpy pandas parquet arrow]] — representación, validación y almacenamiento de datos.
- [[funcion de perdida]] — *feature engineering*, pérdida, gradientes y entrenamiento.
- [[../ingenieria de software para machine learning/00 Índice y recordatorio - Ingeniería de software para ML|Ingeniería de software para ML]] — contratos, configuración, pruebas, logs y artefactos.

## Lista de comprobación

- [ ] Puedo distinguir clase, instancia, atributo y método.
- [ ] Puedo explicar `self`, `__init__` y `super()`.
- [ ] Sé decidir entre herencia y composición.
- [ ] Entiendo `self` y `other` en `__add__`.
- [ ] Sé diferenciar `__repr__` de `__str__`.
- [ ] Entiendo por qué `Scalar` guarda padres y operaciones.
- [ ] Puedo recorrer un grafo en orden topológico.
