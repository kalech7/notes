---
title: "Database Internals — Parte II · Del motor local al sistema distribuido"
created: 2026-09-30
libro: "Database Internals"
capitulo: 8
tags:
  - lecturas/database-internals
  - arquitectura/sistemas-distribuidos
---

# Parte II · Del motor local al sistema distribuido

[[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/00 Índice|Índice del capítulo 8]]

Hasta aquí, el libro explicó cómo guardar y recuperar datos dentro de un motor. Ahora cambia la escala: varios motores o procesos deben colaborar sin compartir una única memoria ni una única ejecución. Esa transición permite repartir capacidad, pero introduce incertidumbre sobre lo que hicieron los demás.

> «La falla de una computadora que desconocías puede inutilizar la tuya».
> — Leslie Lamport, epígrafe de la Parte II; traducción breve.

La frase presenta una dependencia oculta: una aplicación puede estar sana y fallar porque depende de un servicio lejano. No dice que todos los fallos produzcan ese efecto; explica por qué debemos estudiar las relaciones entre componentes.

## Escalar cambia dónde está el trabajo

**Escalar verticalmente** consiste en ejecutar el sistema en una máquina con más recursos: CPU, RAM o discos más rápidos. Simplifica algunas formas de coordinación porque los componentes permanecen en un mismo equipo, pero puede aumentar el costo y complicar su reemplazo. **Escalar horizontalmente** consiste en añadir máquinas y distribuir el trabajo entre ellas. La capacidad total puede aumentar, aunque aparece trabajo nuevo: enviar datos, coordinar decisiones y reconstruir información después de un fallo. Duplicar los nodos no garantiza duplicar rendimiento.

Un clúster es un conjunto de nodos que cooperan. **Nodo**, **proceso** y **réplica** son términos que el libro usa para participantes, pero conviene distinguirlos en un diseño: un nodo suele ser una máquina o instancia; un proceso es una ejecución de software; una réplica conserva una copia de cierta información. Una máquina puede ejecutar varios procesos y una base puede tener réplicas de solo parte de sus datos.

El libro recuerda que incluso cliente/servidor es distribuido: el cliente no puede inspeccionar directamente la memoria del servidor. Una aplicación de reservas que llama a una base de datos ya necesita cruzar esa frontera.

## Las piezas de un algoritmo

Un participante mantiene **estado local**, la información que conoce en ese momento. Envía mensajes a través de un **enlace de comunicación** y cambia su estado cuando ejecuta un paso o recibe información. Un algoritmo distribuido combina estas transiciones locales; no exige que todos los participantes den un paso al mismo tiempo.

Un **reloj físico** estima el tiempo del mundo. Un **reloj lógico** asigna valores para representar relaciones entre eventos; no es necesariamente una hora de calendario ni un contador que mida segundos. Los relojes lógicos serán útiles para hablar de orden sin exigir que las máquinas indiquen la misma hora.

Antes de prometer una garantía debemos expresar sus **supuestos**: qué mensajes pueden perderse, qué procesos pueden fallar, qué cotas de tiempo existen y qué memoria sobrevive a un reinicio. Dos algoritmos con la misma salida normal pueden comportarse de manera muy distinta cuando se rompe uno de esos supuestos.

| Propósito | Qué intenta conseguir | Ejemplo propio |
|---|---|---|
| Coordinación | Organizar acciones de varios trabajadores | Repartir archivos evitando que todos procesen el mismo |
| Cooperación | Combinar tareas de participantes | Varios nodos calculan partes de un informe |
| Diseminación | Difundir información | Propagar una configuración a los servidores |
| Consenso | Tomar una decisión compatible entre procesos correctos | Elegir el siguiente comando del registro replicado |

Difundir una propuesta no equivale a acordarla. La diseminación puede hacer llegar varios valores; el consenso necesita reglas para decidir uno y conservar la seguridad de esa decisión.

El recorrido de la Parte II empieza con abstracciones y enlaces sencillos, construye comunicación más fiable y termina abordando acuerdo. Los siguientes capítulos mencionados por el libro no están incluidos en este escaneo; esta carpeta explica los fundamentos presentes sin atribuirse su lectura.

**Referencia:** PDF 1–3 · introducción de la Parte II, folios impresos no visibles. [[Obsidian/lecturas/database internals/Materiales/08 Sistemas distribuidos.pdf#page=1|PDF de consulta]].

---

← [[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/00 Índice|Anterior]] · [[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/02 Concurrencia interleavings y estado compartido|Siguiente]] →
