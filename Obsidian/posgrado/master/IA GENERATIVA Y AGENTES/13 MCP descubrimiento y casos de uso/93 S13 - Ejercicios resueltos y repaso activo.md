---
title: "93 S13 - Ejercicios resueltos y repaso activo"
created: 2026-09-30
fecha: 2026-09-30
capitulo: 13
sesion: "13"
tags:
  - maestria/ia-generativa
  - agentes/mcp
  - estudio
---

# 93 S13 - Ejercicios resueltos y repaso activo

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/00 Índice - S13 MCP y casos de uso|Índice de la sesión 13]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

## Recordatorio de la sesión

MCP permite recibir capacidades en ejecución y conectar la aplicación con sus proveedores. El modelo sigue proponiendo llamadas; el programa valida y ejecuta. El desacople tiene valor cuando facilita reutilizar capacidades o incorporar nuevas sin modificar el bucle. La cuenta de integraciones ilustra una forma de crecimiento, no una medición de rendimiento.

## Veinte preguntas con solución

> [!question]- 1. Un agente utiliza tres herramientas. ¿El conteo justifica MCP?
> Con M=1,N=3: MN=3 y M+N=4. No lo justifica por reducción del conteo. Puede justificarlo desacoplar la siguiente capacidad o reutilizar proveedores.

> [!question]- 2. ¿Qué ocurre con dos aplicaciones y dos proveedores?
> MN=4 y M+N=4. Hay empate. La condición estricta da (2−1)(2−1)=1, que no es mayor que 1.

> [!question]- 3. Resuelve el caso M=2,N=3.
> MN=6; M+N=5. (M−1)(N−1)=1×2=2>1. El producto supera la suma en una unidad numérica; no se ha medido ahorro de dinero.

> [!question]- 4. Tres aplicaciones solo requieren cinco pares. ¿Hay doce integraciones?
> No. El supuesto de conexión completa ya no vale. Hay cinco pares requeridos; se debe contar la red real antes de usar M×N.

> [!question]- 5. Un servidor expone diez funciones. ¿N necesariamente vale diez?
> No. Si N cuenta proveedores separados, ese servidor es una unidad. Hay que fijar la unidad de integración y conservarla en ambas columnas.

> [!question]- 6. ¿Qué cambia entre importar un registro y descubrir un catálogo?
> En el caso de clase, el registro fija nombres al escribir o importar el código. El catálogo se recibe al ejecutar. El cliente debe conocer cómo comunicarse con el proveedor, no todas sus funciones de antemano.

> [!question]- 7. ¿Qué pieza coordina dos servidores?
> El host coordina los clientes. Cada cliente individual se comunica con un servidor. Un cliente agregado del simulador representa una capa de coordinación de proveedores, no una conexión MCP 1:a-varios.

> [!question]- 8. ¿En qué máquina se ejecuta la herramienta?
> En el entorno de su implementación: servidor local, servicio remoto o proceso del simulador. El modelo propone la operación; el programa la ejecuta.

> [!question]- 9. ¿Qué tres datos aporta el contrato de clase?
> Nombre para identificar la operación, descripción para decidir cuándo usarla y esquema de entrada para definir sus argumentos. La validación efectiva sigue siendo responsabilidad del programa.

> [!question]- 10. ¿Por qué el adaptador facilita añadir proveedores?
> Convierte los contratos publicados al formato estable que consume el agente. Si se conserva esa interfaz y el despacho dinámico, la lógica del agente no necesita conocer cada nueva tool. Su ubicación concreta es una decisión de diseño.

> [!question]- 11. ¿MCP reemplaza function calling?
> No. Function calling expresa la propuesta entre modelo y aplicación. MCP conecta cliente y proveedor. Puede haber function calling sin MCP o un cliente MCP determinista sin LLM.

> [!question]- 12. ¿Cómo distingues tools, resources y prompts?
> Una tool realiza una operación, un resource aporta contenido y un prompt ofrece una plantilla. Consultar ventas, leer un reporte y proponer una estructura de comparación son funciones distintas.

> [!question]- 13. ¿server/discover y tools/list hacen lo mismo?
> No. El primero informa de versiones, capacidades e identidad del servidor. El segundo lista herramientas. En la revisión de clase el servidor implementa discover, pero el cliente no está obligado a invocarlo antes de toda operación.

> [!question]- 14. ¿Qué cambió respecto de initialize?
> La revisión 2026-07-28 quitó el saludo initialize y usa metadatos por petición. La revisión anterior 2025-11-25 sí requiere un saludo. Se debe respetar la versión que hablan las partes.

> [!question]- 15. ¿Qué hace el cliente tras input_required?
> Obtiene la entrada necesaria y reintenta la petición con un nuevo id y sus respuestas, conservando el estado explícito que corresponda. No inventa el dato faltante ni entra en un bucle ilimitado.

> [!question]- 16. ¿Sin sesión significa sin memoria o base persistente?
> No. El host puede mantener historial y el servicio datos persistentes. Las peticiones del protocolo son autosuficientes y la continuidad necesaria se expresa con argumentos o identificadores.

> [!question]- 17. ¿Descubrir una tool autoriza utilizar todos sus datos?
> No. La presencia en el catálogo y la autorización son asuntos distintos. Alcance, identidad y permisos se comprueban al realizar la acción.

> [!question]- 18. Diez tools de 80 tokens se ofrecen en cuatro decisiones. ¿Qué cuenta resulta?
> Bajo esos supuestos didácticos: 10×80×4=3200 tokens de catálogo incluidos en llamadas. No es una factura ni una medición del PDF; faltan entradas, salidas y políticas reales de caché.

> [!question]- 19. Abril suma 1670 y marzo 2695. ¿Cuál es la variación y qué no demuestra?
> Diferencia: 1670−2695=−1025. Variación respecto de marzo: −1025/2695×100≈−38,03 %. No demuestra la causa de la caída ni que la cobertura de ambos meses sea comparable sin comprobarlo.

> [!question]- 20. Una conversión funciona tras agregar un servidor. ¿Qué falta para decir que hay MCP real?
> La práctica local demuestra catálogo, rutas y función del agente conservada. Faltan transporte, mensajes y reglas de revisión, validación completa y pruebas de interoperabilidad. Si no hubo LLM, tampoco se demostró su selección de herramientas.

## Un caso integrado resuelto

Una organización tiene tres aplicaciones: agente analista, IDE y chat de soporte. Quiere ofrecer cuatro sistemas: ventas, documentos, calendario e incidencias. Supongamos que las tres aplicaciones necesitan los cuatro sistemas.

1. **Conteo:** MN=3×4=12 pares específicos; M+N=3+4=7 componentes reutilizables bajo la simplificación de clase. La condición es (3−1)(4−1)=6>1.
2. **Arquitectura:** cada host coordina clientes hacia los proveedores. Un servidor de ventas puede exponer varias operaciones sin multiplicar el número de sistemas.
3. **Descubrimiento:** los clientes reciben contratos y guardan la relación entre nombre público y proveedor.
4. **Decisión:** el analista ofrece los contratos pertinentes y pide al modelo resolver la comparación.
5. **Verificación:** los totales y el denominador se recalculan; la respuesta no agrega causas no observadas.
6. **Cambio:** se publica una operación de conversión y se refresca el catálogo. La configuración puede cambiar; la lógica genérica del agente se conserva.
7. **Límite:** el protocolo no demuestra que las descripciones sean fiables, ni concede permisos ni define la calidad del verificador.

La propuesta es razonable por compartir capacidades y por la incorporación esperada de nuevas operaciones. Para decidir sobre una implementación concreta también hacen falta costo operativo, compatibilidad y restricciones del entorno.

## Errores que ya deberías poder corregir

| Frase | Corrección |
| --- | --- |
| «El modelo ejecuta MCP» | El modelo propone; la implementación ejecuta |
| «MCP ahorra exactamente 60 % de costo» | La cuenta compara unidades distintas y no mide costos |
| «Framework significa registro fijo» | Depende del diseño; puede incorporar descubrimiento |
| «Está en catálogo, entonces está autorizado» | La autorización se comprueba aparte |
| «Cacheé tools/list, ya no hay tokens de tools» | Caché del servidor y contexto del LLM son distintos |
| «Los tests pasan, toda la tarea está bien» | La fuerza de la conclusión depende del contrato y la cobertura |
| «Descubrir basta» | Faltan adaptación, despacho y retorno de resultados al historial |

Fuente de clase: PDF 1–26 · numeración visible igual a la página PDF · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/sesion-13.pdf#page=1|Sesión 13]].

Las preguntas, soluciones y el caso integrado son elaboración propia. El ejercicio organizacional se inspira en la página 17; los requisitos del taller se explican como contexto docente.

---

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/92 S13 - Laboratorio local de descubrimiento y extensión B|Anterior]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/00 Índice - S13 MCP y casos de uso|Índice]] →
