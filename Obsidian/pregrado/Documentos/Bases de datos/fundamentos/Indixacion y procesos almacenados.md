## Índices (Indexing)

> [!info] Explicación
> Los índices son estructuras de datos especiales asociadas a tablas o vistas que mejoran significativamente la velocidad de búsqueda y recuperación de registros (como el índice de un libro). Sin embargo, ocupan espacio en disco y pueden ralentizar las operaciones de inserción, actualización y borrado (`INSERT`, `UPDATE`, `DELETE`), ya que el índice también debe actualizarse.

Mejoran la búsqueda de un registro en una tabla mediante una estructura de acceso rápido.

```mermaid
flowchart TD
    subgraph Sin Índice
        A1[Consulta SELECT] --> B1[Escaneo de Tabla Completa\nTable Scan]
        B1 --> C1[Fila Encontrada\nTiempo O de N]
    end
    
    subgraph Con Índice
        A2[Consulta SELECT] --> B2[Búsqueda en Árbol B\nIndex Seek]
        B2 --> C2[Fila Encontrada\nTiempo O de log N]
    end
```

## Procesos almacenados (Stored Procedures)

> [!info] Explicación
> Un proceso (o procedimiento) almacenado es un conjunto de instrucciones SQL que se compilan y almacenan en el propio motor de base de datos. Sirve para encapsular lógica de negocio compleja, reducir el tráfico de red (al no enviar comandos largos repetidamente) y mejorar la seguridad (previniendo inyecciones SQL y controlando permisos a nivel de procedimiento).

En la base de datos se realiza un proceso almacenado donde el cliente de la aplicación solo manda a ejecutar (por ejemplo con `EXEC proc_nombre`) y ya no es necesario enviar toda la consulta SQL estructurada desde el código de la aplicación.

```mermaid
sequenceDiagram
    participant App as Aplicación Cliente
    participant BD as Base de Datos

    App->>BD: EXEC proc_crear_usuario(datos)
    Note over BD: El proceso almacenado<br/>ejecuta múltiples INSERTs<br/>y validaciones internamente
    BD-->>App: Resultado (Éxito o Error)
```

## Notas relacionadas
- [[SQL]]
- [[Comandos]]
- [[Vistas]]

## Aplicación en Data Engineering freelance

- [[Obsidian/freelance/Data Engineering/SQL/02 Índices y filtros eficientes|02 Índices y filtros eficientes]] — Ampliación de SARGability, tipos de índices y costos.
