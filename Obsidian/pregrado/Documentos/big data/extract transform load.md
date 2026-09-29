las organizaciones traen y consolidan datos de multiples fuente en un solo repositorio. en este proceso por ende se debe extraer los datos de su fuente original transformandolos combinandolos y asegurando la calidad para luego cargarlos en la base de datos de destino proporcionando una unica fuente de verdad lo que garantiza que todos los datos de la empresa 
sean coherentes 

# Extract
es el primer paso donde se recolecta toda la data desde un o mas fuentes. es mantenida en un almacenamiento temporal donde los dos pasos siguientes son ejecutados 
durante la extraccion, las reglas de validacion son aplicados. esto comprueba si los datos cumplen los requisitos de su destino. los datos que no superan la validacion se rechazan y no continuan 
* hojas de calculo
* archivos planos
* bases de datos sql y no sql 
* archivos separados por comas o tabuladores*
* paginas web 
* api
* archivos json (info esta en forma semiestructurada, es popular porque es usado por servicios web para comunicar datos)
___

# Transform
los datos se procesan para que sus valores y estructura se ajusten de forma coherente a su caso de uso previsto. el objetivo de la transformacion es hacer que todos los datos se ajusten a un esquema uniforme antes de pasar al ultimo paso 
Las transformaciones típicas incluyen agregadores, enmascaramiento de datos, expresión, unión, filtro, búsqueda, clasificación, enrutador, unión, XML, normalizador, H2R, R2H y servicio web. Esto ayuda a normalizar, estandarizar y filtrar los datos. También hace que los datos sean aptos para el consumo para análisis, funciones comerciales y otras actividades posteriores.
**Pasos:**
* reformatear los datos 
* limpiar datos irrelevantes 
* ordenar y filtrar datos 
* borrar la info duplicada 
## Notas relacionadas
- [[Caracteristicas del big data]]
- [[crisp-dm]]
- [[SQL]]
- [[Conexion a la base datos]]

# Carga
es cargar los conjuntos de datos transformados en la base de datos de destinopara su almacenamiento y analisis.
para cargar los datos se lo realiza mediante una rutina de insercion SQL donde la insercion de los datos se lleva a cabo de manera manual (este proceso toma mucho tiempo peor tiene mejor control de calidad ) otra forma es de manera masica(mucho mas rapido y reduce la posibilidad de errores sin embargo no realiza controles de calidad para cada registro lo que puede porvar problemas de integridad de los datos )

## Aplicación en Data Engineering freelance

- [[Obsidian/freelance/Data Engineering/Calidad/02 Validación Unicode y contratos|02 Validación Unicode y contratos]] — Contratos, validación de entrada y trazabilidad de rechazos.
