---
title: "103 S14 - Presupuestos repetición y costo del historial"
created: 2026-10-02
fecha: 2026-10-01
capitulo: 14
sesion: "14"
tags:
  - maestria/ia-generativa
  - agentes/robustez
  - estudio
---

# 103 S14 - Presupuestos repetición y costo del historial

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/00 Índice - S14 Multiagente LangGraph y robustez|Índice de S14]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Los tres frenos del jueves vigilan cosas diferentes. Un paso limita duración lógica; un presupuesto limita consumo; un contador de repetición detecta acciones idénticas. **Progreso** significa acercarse a la respuesta, y ninguna de esas tres métricas lo demuestra por sí sola.

![[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Recursos visuales/Capítulo 14/05-tres-frenos.png]]

Las cajas describen la señal que observa cada freno y lo que deja fuera. Las flechas convergen en una autorización: si cualquiera falla, la siguiente acción se detiene. Una llamada cara puede agotar presupuesto en un paso; una consulta barata puede repetirse sin aportar información. Los tres límites se complementan.

## Repetición exacta y paráfrasis

La clave propuesta por la sesión es `(tool, json.dumps(entrada, sort_keys=True))`. Ordenar las claves del JSON hace que dos diccionarios equivalentes no parezcan distintos por su orden. No convierte estos textos en equivalentes:

| Entrada de buscar | Conteo por esa entrada |
| --- | ---: |
| precio NimbusSoft | 1 |
| precio de NimbusSoft | 1 |
| NimbusSoft precio | 1 |

Con `max_repetidas=2`, las tres entradas pasan. Una cuarta paráfrasis nueva también pasa; repetir por tercera vez una entrada idéntica cruza ese umbral. Un límite global de pasos o gasto corta aunque las frases cambien.

La repetición global conserva todas las ocurrencias de la tarea. Si `permitir()` mira el máximo histórico y una clave llegó a 3, cambiar de estrategia no borra ese bloqueo. Un detector de repeticiones consecutivas o una ventana reciente tendría otra política. En las notas y la práctica se distingue qué definición se está utilizando.

## Registrar después y revisar antes

La consigna del notebook pide `registrar` y luego `permitir`: permite observar si el consumo acumulado ya alcanzó un límite. Si registras después de ejecutar, la llamada que excedió el gasto ya ocurrió. Si solo comparas «gastado < máximo» antes de la próxima llamada, puedes autorizar una operación individual demasiado cara.

El complemento local agrega `autorizar(tool, entrada, costo_estimado)`: verifica el próximo consumo y reserva antes del efecto simulado. En un servicio real, hay que conciliar la reserva con el uso devuelto por el proveedor y acotar salida, reintentos y tiempos. Una estimación menor que el costo real no es una garantía dura de dinero.

## Por qué cada paso puede costar más

![[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Recursos visuales/Capítulo 14/06-historial-reenviado.png]]

S es el contexto inicial. A, B y C son mensajes incorporados después. La segunda llamada vuelve a procesar S, la tercera vuelve a procesar S y A, y las posteriores arrastran más historial. La figura representa el mecanismo con cuatro llamadas ilustrativas, sin precios ni mediciones de un modelo.

Supón un contexto inicial de S tokens y T tokens nuevos por vuelta. La llamada k recibe `S + (k−1)T`. En N llamadas, la suma de entrada es:

$$\text{entrada total}=NS+T\frac{N(N-1)}{2}.$$

El término triangular suma `0+1+...+(N−1)`. Para N=8 da 28T; para 16 da 120T; para 20 da 190T. `120/28 ≈ 4,286`, pero **ese factor aplica solo al término del historial**, no al costo total. Con S=1 000 y T=200: 8 llamadas reciben 13 600 tokens en total, y 16 reciben 40 000; la relación es aproximadamente 2,94.

Para calcular dinero necesitas tokens de entrada y salida, tarifas correspondientes y política de caché, si existe. El ejemplo supone crecimiento uniforme y reenvío completo; truncar, resumir o recuperar memoria selectiva cambia la cuenta. La H200 puede no facturar tokens al alumno, pero sigue consumiendo cómputo y tiempo.

Fuente: PDF 22–24 y 31 · numeración visible = página PDF · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/sesion-14.pdf#page=22|sesion-14.pdf]].

---

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/102 S14 - Pausas aprobación humana y contrato de salida|Anterior]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/104 S14 - Inyección indirecta mínimo privilegio y responsabilidad|Siguiente]] →
