son consultas que se ejecutan como parte de una consulta principal 
pueden estar ubicadas en trs distintos lugares de la consulta principal
* en la clausula select
* en la clausula from
* en la clausula where
Al igual que los parentesis en una expresion algebraica su resultado se calcula en primer lugar 
**Ejemplo**
cuales de los cliente que viven en una de las siguientes ciudaddes, han comrpado en la tienda 1? (('Oyo','Namibe','Jelets ','Pune'))

```sql
Select First_name
FROM (SELECT* FROM customer Cu,address Ad,city Cy
WHERE Cu.address_id=Ad.addres_id
AND Ad.city_id=Cy.city_id
AND city IN ('Oyo','Namibe','Jelets ','Pune'))Su,rental R
WHERE Su.customer=R.customer_id   
AND store_id = 1

```
[[SQL]]

## Notas relacionadas
- [[Comandos]]
- [[ejemplos]]
- [[ejercicios]]
- [[Vistas]]
