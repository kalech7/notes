> [!info] Explicación
> Las subconsultas (o *subqueries*) son consultas SQL anidadas dentro de otra consulta principal. Se utilizan para resolver problemas donde primero se necesita obtener un resultado intermedio antes de poder realizar la consulta definitiva. Al igual que los paréntesis en una expresión algebraica matemática, su resultado se calcula y resuelve en primer lugar, y luego ese resultado es utilizado por la consulta exterior.

Las subconsultas pueden estar ubicadas en tres distintos lugares de la consulta principal:
* En la cláusula `SELECT`
* En la cláusula `FROM`
* En la cláusula `WHERE`

```mermaid
flowchart TD
    subgraph Consulta Principal (Externa)
        O[SELECT columnas\nFROM tabla\nWHERE condicion]
    end
    
    subgraph Subconsulta (Interna)
        I[SELECT columna_intermedia\nFROM otra_tabla]
    end
    
    I -->|"Retorna valor(es) o tabla virtual"| O
    O -.->|"Si es correlacionada, evalúa fila por fila"| I
```

**Ejemplo**
¿Cuáles son los clientes que viven en una de las siguientes ciudades y han comprado en la tienda 1? (`'Oyo'`, `'Namibe'`, `'Jelets'`, `'Pune'`)

```sql
SELECT first_name
FROM (
    -- Esta es la subconsulta en la cláusula FROM actuando como una tabla virtual 'Su'
    SELECT * 
    FROM customer Cu, address Ad, city Cy
    WHERE Cu.address_id = Ad.address_id
    AND Ad.city_id = Cy.city_id
    AND city IN ('Oyo', 'Namibe', 'Jelets', 'Pune')
) Su, rental R
WHERE Su.customer_id = R.customer_id   
AND store_id = 1;
```

[[SQL]]

## Notas relacionadas
- [[Comandos]]
- [[ejemplos]]
- [[ejercicios]]
- [[Vistas]]
