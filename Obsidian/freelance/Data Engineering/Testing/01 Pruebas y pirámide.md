---
title: "Pruebas: niveles, objetivos y pirámide"
created: 2026-09-07
tags:
  - freelance/data-engineering
  - estudio
---

# Pruebas: niveles, objetivos y pirámide

## Dos preguntas diferentes

El **nivel** indica qué parte del sistema pruebas. El **tipo u objetivo** indica qué propiedad estás comprobando. Una prueba puede ser de sistema y funcional; otra, de sistema y rendimiento. No pongas «unitaria» y «no funcional» como alternativas excluyentes.

| Nivel | Qué observa | Ejemplo de ingeniería de datos |
|---|---|---|
| Unidad o componente | Pieza delimitada | Regla que asigna puntos |
| Integración | Colaboración entre piezas | Lector, esquema y transformación conectados |
| Sistema | Sistema completo bajo prueba | Carga de archivo hasta reporte final |
| Aceptación | Necesidad del negocio y aptitud para uso | El responsable valida criterios del ranking |

«Componente» y «unidad» pueden solaparse según la organización. Una prueba end-to-end recorre una cadena representativa y puede atravesar varios sistemas. Aceptación no significa solo «no se cayó»: requiere criterios verificables acordados.

## Funcional frente a no funcional

Una prueba funcional pregunta si el sistema cumple el comportamiento requerido: un empate suma un punto. Una prueba no funcional observa cualidades: procesa un volumen acordado dentro del tiempo objetivo, protege accesos o sigue disponible bajo ciertas condiciones. Seguridad también puede tener comprobaciones de funciones concretas, como rechazar una acción sin permiso.

## La pirámide como economía de retroalimentación

```text
              /  E2E  \            pocas: flujo completo
             /---------\
            /Integración\          varias: uniones entre piezas
           /-------------\
          /   Unitarias   \        muchas: reglas pequeñas
         /_________________\
```

Las unitarias suelen ser rápidas y localizan bien el error. Las E2E suelen costar más, depender de más cosas y dificultar el diagnóstico. La pirámide no fija porcentajes universales: elige una distribución que detecte riesgos reales a un costo razonable. Un pipeline cuyo principal riesgo es el esquema de una fuente necesita buenas pruebas de integración, aunque su lógica Python sea sencilla.

```python
def puntos(favor, contra):
    if favor < 0 or contra < 0:
        raise ValueError("Los goles no pueden ser negativos")
    return 3 if favor > contra else 1 if favor == contra else 0

# Entradas y salidas decididas a partir de la regla del negocio.
assert puntos(2, 0) == 3
assert puntos(1, 1) == 1
assert puntos(0, 2) == 0
```

La unidad no necesita conectarse a una base real. Un mock puede sustituir una dependencia, pero no verifica que la dependencia real tenga el mismo comportamiento: eso se comprueba en integración.

## Error común y ejercicio

Tener muchos tests no demuestra cobertura de riesgos. Si todos prueban victorias, falta la regla de empate y el manejo de valores inválidos. Diseña un test de cada nivel para «recibir partidos y entregar clasificados». En aceptación especifica si deben salir exactamente dos equipos o todos los empatados: esa diferencia cambia el código.

> [!tip] Regla para recordar
> Nivel: qué parte pruebas. Objetivo: qué propiedad verificas.

## Comprueba que lo entendiste

> [!question]- ¿Unit testing significa probar contra todos los servicios reales?
> No. Delimita una unidad y controla dependencias para obtener retroalimentación rápida. La interacción real corresponde a pruebas de integración.

## Conexiones

- [[Obsidian/freelance/Data Engineering/Testing/02 Regresión y pruebas de datos|02 Regresión y pruebas de datos]] — clasifica pruebas después de modificar una regla.
- [[Obsidian/posgrado/master/MATEMÁTICAS Y PROGRAMACIÓN IA/ingenieria de software para machine learning/04 Pruebas unitarias, integración y pruebas semánticas|04 Pruebas unitarias, integración y pruebas semánticas]] — ya contiene ejemplos de invariantes y tolerancias para ML.
- [[Obsidian/pregrado/Documentos/Software 2/tecnicas pruebas|tecnicas pruebas]] — conecta TDD y BDD con niveles y criterios de aceptación.

Volver a [[Obsidian/freelance/Data Engineering/00 Empieza aquí|la ruta de estudio]].
