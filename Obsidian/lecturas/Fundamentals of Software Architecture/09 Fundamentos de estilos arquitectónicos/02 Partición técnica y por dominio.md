---
title: "Partición técnica y por dominio"
created: 2026-09-28
capitulo: 9
tags:
  - lecturas/software-architecture
  - arquitectura/estilos
---

[[Obsidian/lecturas/Fundamentals of Software Architecture/09 Fundamentos de estilos arquitectónicos/00 Índice|← Índice del capítulo 9]]

# Partición técnica y por dominio

**Particionar es decidir qué criterio agrupa primero las responsabilidades.** El primer nivel importa porque establece dónde buscar cambios, qué se considera una unidad de trabajo y qué dependencias cruzan sus límites.

## 1. Dos maneras de organizar la misma aplicación

En una partición **técnica**, los contenedores principales representan capacidades de implementación: presentación, reglas de negocio, servicios, persistencia. Para localizar una consulta SQL, la categoría «persistencia» es una pista útil.

En una partición **por dominio**, los contenedores principales representan capacidades del negocio o flujos coherentes: compra, inventario, entrega. Para cambiar la política de reserva de existencias, «inventario» es una pista útil.

Las dos responden a preguntas diferentes: «¿qué clase de trabajo técnico hace este código?» y «¿qué responsabilidad de negocio atiende?». La elección no desaparece porque se usen carpetas con nombres elegantes; debe manifestarse en dependencias permitidas, propiedad de reglas y organización de datos.

![Partición técnica frente a partición por dominio](../Recursos%20visuales/Cap%C3%ADtulos%209%20y%2010/c09-01-particion.png)

La imagen compara dónde queda una modificación del proceso de compra. En la organización técnica, el cambio recorre varios grupos: interfaz, reglas y persistencia. En la organización por dominio queda agrupada alrededor de Compra, aunque internamente atraviese responsabilidades técnicas. Los recuadros representan agrupaciones lógicas, no máquinas ni servicios desplegados. Esta imagen es una elaboración propia basada en las figuras 9-2 a 9-4.

**Límite.** Localizar mejor un cambio no garantiza independencia. Si Compra escribe libremente tablas de Inventario o importa sus detalles internos, la frontera dibujada no protege el cambio.

**Fuente:** PDF pp. 8–11, impresas 137–140, figuras 9-2, 9-3 y 9-4.

## 2. Por qué importa el primer nivel

Imagina el requisito propio: «Al reservar un pedido, conservar el precio pactado aunque el catálogo cambie después». En una partición técnica, probablemente modificarás un formulario, una regla, una estructura persistente y una consulta. El conocimiento de «precio pactado» queda repartido entre capas.

En una partición por dominio, ese conocimiento puede quedar dentro de Pedidos. El módulo todavía tiene adaptación de entrada, reglas y almacenamiento, pero se trabaja primero con la responsabilidad que cambia. Si el requisito obliga además a consultar Catálogo, hace falta acordar un contrato entre ambas responsabilidades.

```text
Partición técnica                 Partición por dominio
presentación/                     pedidos/
  pedido                            entrada
  inventario                        reglas
negocio/                            persistencia
  pedido                            contrato público
  inventario                      inventario/
persistencia/                       entrada
  pedido                            reglas
  inventario                        persistencia
```

Esta disposición es didáctica. No hay que convertir cada etiqueta en un paquete obligatorio. La pregunta es qué dependencias protege y cómo facilita cambios reales.

## 3. Se pueden combinar sin perder la distinción

Un monolito modular puede tener módulos de dominio y capas internas. Eso sigue siendo partición por dominio en el primer nivel. Del mismo modo, una capa de negocio puede contener submódulos de compra e inventario, pero si las primeras divisiones del sistema son técnicas, su partición superior sigue siendo técnica.

Tampoco debe confundirse **partición por dominio** con **distribución**. Un sistema puede agrupar por dominio y desplegar todo junto. La separación física añade fallos de red, contratos remotos, operación y posiblemente coordinación de datos; no es necesaria para disfrutar de todas las ventajas de una frontera lógica.

## 4. Comparar por el tipo de cambio

| Cambio habitual | Partición técnica | Partición por dominio |
|---|---|---|
| Ajustar reglas de compra y su presentación | Puede tocar varias capas | Puede concentrarse en Compra |
| Sustituir una biblioteca común de persistencia | La especialidad técnica está localizada, aunque sus efectos pueden propagarse | Puede exigir coordinación entre módulos que usan la biblioteca |
| Separar equipos por capacidad de negocio | Requiere coordinación entre capas o propiedad transversal | El primer nivel facilita asignar responsabilidades completas |
| Aplicar una política compartida de personalización | Puede centralizar la política | Hay que distinguir política compartida de regla propia de cada dominio |
| Extraer una capacidad a otro despliegue | El dominio está repartido y exige reunir sus partes | Un límite de dominio facilita empezar, pero no resuelve datos ni operación |

Ninguna columna elimina todos los costos. «Fácil de encontrar» significa cosas distintas para un especialista técnico y para alguien que implementa un flujo de negocio.

## 5. Relación con el acoplamiento

Las capas pueden limitar dependencias cuando cada una conoce contratos estrechos. Esa ventaja se pierde si todas importan estructuras internas de todas. A su vez, los módulos de dominio pueden reducir la dispersión de reglas, pero se acoplan cuando comparten tablas, exigen transacciones globales o cambian contratos juntos.

**Procedimiento propio de revisión:** toma cinco cambios recientes; marca módulos, equipos, tablas y contratos afectados; distingue cambios inevitables por negocio de propagación accidental; compara una partición alternativa. Esto convierte «prefiero dominios» o «prefiero capas» en una hipótesis examinable.

> [!question] Si un cambio cruza tres capas, ¿el diseño es incorrecto?
> No necesariamente. Una función completa suele requerir presentación, reglas y datos. Hay que evaluar si las fronteras permiten comprender y probar el cambio, y si la coordinación resulta razonable para el equipo.

> [!question] ¿Una carpeta Pedidos basta para declarar un módulo de dominio?
> No. Necesita responsabilidad, interfaz y dependencias claras. Si todo puede modificar su estado sin pasar por sus reglas, su nombre no constituye encapsulación.

> [!question] ¿La partición elegida determina la organización del equipo?
> Influye en la colaboración necesaria, pero no la fija mecánicamente. Arquitectura y comunicación se condicionan; esa relación se desarrolla en la nota sobre Conway y equipos.

## Fuente principal

- [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/06 Fundamentos de estilos arquitectónicos.pdf#page=8|Fundamentals of Software Architecture, 2.ª ed., capítulo 9, PDF pp. 8–11; impresas 137–140]].

Las explicaciones, diagramas y ejemplos identificados como propios son elaboraciones didácticas; las páginas indicadas permiten contrastar los conceptos con el escaneo.

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/09 Fundamentos de estilos arquitectónicos/01 Estilos patrones y estructura|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/09 Fundamentos de estilos arquitectónicos/03 Silicon Sandwiches y decisiones de partición|Siguiente →]]
