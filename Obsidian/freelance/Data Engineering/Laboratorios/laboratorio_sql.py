"""Ejemplos sintéticos de estudio. Solo usa una base SQLite en memoria."""
import sqlite3
from pathlib import Path

con = sqlite3.connect(':memory:')
con.executescript('''
CREATE TABLE partidos(id INTEGER PRIMARY KEY, grupo TEXT, partido TEXT, resultado TEXT);
INSERT INTO partidos VALUES
 (1,'A','Qatar vs. Ecuador','0,1'),
 (2,'A','Ecuador vs. Senegal','2,2'),
 (3,'A','Qatar vs. Senegal','1,1');
CREATE TABLE empleados(nombre TEXT PRIMARY KEY, salario INTEGER);
INSERT INTO empleados VALUES ('Ana',1000),('Luis',1000),('Pedro',900),('Carla',800);
CREATE TABLE clientes(id INTEGER PRIMARY KEY);
INSERT INTO clientes VALUES (1),(2),(3);
CREATE TABLE movimientos(cliente_id INTEGER);
INSERT INTO movimientos VALUES (1),(NULL);
CREATE TABLE scores(id INTEGER PRIMARY KEY, score INTEGER);
''')
con.executemany('INSERT INTO scores VALUES (?,?)', [(i, 100-i) for i in range(1,24)])

PIPELINE = '''
WITH separados AS (
 SELECT id, grupo,
 TRIM(SUBSTR(partido,1,INSTR(partido,' vs. ')-1)) AS local,
 TRIM(SUBSTR(partido,INSTR(partido,' vs. ')+5)) AS visitante,
 TRIM(SUBSTR(resultado,1,INSTR(resultado,',')-1)) AS gl_texto,
 TRIM(SUBSTR(resultado,INSTR(resultado,',')+1)) AS gv_texto
 FROM partidos
 WHERE (LENGTH(partido)-LENGTH(REPLACE(partido,' vs. ','')))=5
   AND (LENGTH(resultado)-LENGTH(REPLACE(resultado,',','')))=1
), validos AS (
 SELECT id,grupo,local,visitante,
 CAST(gl_texto AS INTEGER) AS gl, CAST(gv_texto AS INTEGER) AS gv
 FROM separados
 WHERE local <> '' AND visitante <> ''
   AND gl_texto <> '' AND gv_texto <> ''
   AND gl_texto NOT GLOB '*[^0-9]*' AND gv_texto NOT GLOB '*[^0-9]*'
   AND LENGTH(gl_texto) <= 2 AND LENGTH(gv_texto) <= 2
), perspectivas AS (
 SELECT id,grupo,local AS equipo,gl AS favor,gv AS contra FROM validos
 UNION ALL
 SELECT id,grupo,visitante,gv,gl FROM validos
), puntos AS (
 SELECT *,CASE WHEN favor>contra THEN 3 WHEN favor=contra THEN 1 ELSE 0 END AS puntos
 FROM perspectivas
), resumen AS (
 SELECT grupo,equipo,SUM(puntos) AS puntos,SUM(favor-contra) AS diferencia
 FROM puntos GROUP BY grupo,equipo
), ranking AS (
 SELECT *,ROW_NUMBER() OVER(PARTITION BY grupo ORDER BY puntos DESC,diferencia DESC,equipo) AS rn
 FROM resumen
)
'''

report = [f'SQLite {sqlite3.sqlite_version}', 'Datos sintéticos; base en memoria.']
def caso(nombre, sql, esperado):
    obtenido = con.execute(sql).fetchall()
    assert obtenido == esperado, (nombre, obtenido, esperado)
    report.append(f'OK {nombre}: {obtenido!r}')

caso('Puntos y ranking', PIPELINE+'SELECT equipo,puntos,diferencia,rn FROM ranking ORDER BY rn',
     [('Ecuador',4,1,1),('Senegal',2,0,2),('Qatar',1,-1,3)])
caso('Top 2', PIPELINE+'SELECT equipo FROM ranking WHERE rn<=2 ORDER BY rn', [('Ecuador',),('Senegal',)])
caso('Dos participaciones por partido', PIPELINE+'SELECT COUNT(*) FROM perspectivas', [(6,)])
caso('Conservacion de diferencia', PIPELINE+'SELECT SUM(favor-contra) FROM perspectivas', [(0,)])
caso('Ranking empates', '''SELECT nombre,RANK() OVER(ORDER BY salario DESC),
 DENSE_RANK() OVER(ORDER BY salario DESC),ROW_NUMBER() OVER(ORDER BY salario DESC,nombre)
 FROM empleados ORDER BY salario DESC,nombre''',
 [('Ana',1,1,1),('Luis',1,1,2),('Pedro',3,2,3),('Carla',4,3,4)])
caso('Percent rank', '''SELECT nombre,PERCENT_RANK() OVER(ORDER BY salario DESC)
 FROM empleados ORDER BY salario DESC,nombre''', [('Ana',0.0),('Luis',0.0),('Pedro',2/3),('Carla',1.0)])
caso('NTILE 23 filas', '''WITH q AS (SELECT NTILE(5) OVER(ORDER BY score DESC,id) AS bucket FROM scores)
 SELECT bucket,COUNT(*) FROM q GROUP BY bucket ORDER BY bucket''', [(1,5),(2,5),(3,5),(4,4),(5,4)])
caso('Anti join robusto', '''SELECT id FROM clientes c WHERE NOT EXISTS
 (SELECT 1 FROM movimientos m WHERE m.cliente_id=c.id) ORDER BY id''', [(2,),(3,)])
caso('NOT IN con NULL', 'SELECT id FROM clientes WHERE id NOT IN (SELECT cliente_id FROM movimientos)', [])
caso('UNION ALL conserva', 'SELECT 1 UNION ALL SELECT 1', [(1,),(1,)])
caso('UNION deduplica', 'SELECT 1 UNION SELECT 1', [(1,)])
caso('EXCEPT', 'SELECT 1 EXCEPT SELECT 2', [(1,)])
caso('INTERSECT', 'SELECT 1 INTERSECT SELECT 1', [(1,)])
caso('CAST no valida', "SELECT CAST('abc' AS INTEGER),CAST('3x' AS INTEGER)", [(0,3)])
caso('NBSP explicito', "SELECT UPPER(TRIM(REPLACE(CHAR(160)||'Ecuador',CHAR(160),' ')))", [('ECUADOR',)])
caso('Parser flecha', '''WITH t(evento) AS (VALUES ('Juan -> Maria'),('Pedro -> Ana '),('Lucía->Carlos'))
 SELECT TRIM(SUBSTR(evento,1,INSTR(evento,'->')-1)),TRIM(SUBSTR(evento,INSTR(evento,'->')+2)) FROM t''',
 [('Juan','Maria'),('Pedro','Ana'),('Lucía','Carlos')])
# Casos inválidos: no deben convertirse en goles válidos silenciosamente.
con.executemany('INSERT INTO partidos VALUES (?,?,?,?)', [
 (4,'A','Sin delimitador','1,0'), (5,'A','A vs. B','x,2'),
 (6,'A','A vs. B','3x,2'), (7,'A','A vs. B','1,2,3'),
 (8,'A','A vs. B','-1,0'), (9,'A','A vs. B','100,0'),
 (10,'A','A vs. B',' ,0'), (11,'A','A vs. B vs. C','1,0')])
caso('Solo entradas validas', PIPELINE+'SELECT id FROM validos ORDER BY id', [(1,),(2,),(3,)])
caso('Rechazos identificados', PIPELINE+'SELECT id FROM partidos WHERE id NOT IN (SELECT id FROM validos) ORDER BY id',
 [(i,) for i in range(4,12)])
report.append('Regla didactica del parser: goles de uno o dos digitos, sin signo; no es una regla universal.')
report.append(f'Total: {sum(x.startswith("OK ") for x in report)} comprobaciones correctas.')
output='\n'.join(report)+'\n'
print(output)
Path(__file__).with_name('resultados_sql.txt').write_text(output)
con.close()
