"""Laboratorio sintético: usa SQLite en memoria, sin modificar una base existente."""
from pathlib import Path
import sqlite3
import math
base = Path(__file__).resolve().parent
conn = sqlite3.connect(":memory:")
conn.executescript((base / "m10-01-datos.sql").read_text())
def query(name):
    return conn.execute((base / name).read_text()).fetchall()
ranking = query("m10-02-ranking.sql")
assert ranking == [("d1", "A", 0.85, 2, 1), ("d1", "B", 0.85, 2, 1), ("d1", "D", 0.75, 2, 3)]
missing = query("m10-03-ausencias.sql")
assert missing == [("c22", "C", 22)]
coverage = query("m10-04-cobertura.sql")
assert coverage == [("C", 1, 2), ("E", 0, 2)]
print("RANKING (dataset, config, media, semillas, puesto)")
for row in ranking: print(row)
print("MÉTRICA AUSENTE", missing)
print("COBERTURA INCOMPLETA (config, observadas, esperadas)", coverage)
# Contrastar causa: el JOIN incorrecto multiplica filas.
wrong = conn.execute("SELECT COUNT(*) FROM runs r JOIN metrics m ON m.split='validation'").fetchone()[0]
right = conn.execute("SELECT COUNT(*) FROM runs r JOIN metrics m ON m.run_id=r.run_id AND m.split='validation'").fetchone()[0]
assert wrong == 132 and right == 11
print("JOIN sin identidad:", wrong, "filas; JOIN con identidad:", right)
# Corregir la ausencia conocida cambia la elegibilidad de C.
conn.execute("INSERT INTO metrics VALUES ('c22','validation','accuracy',0.80)")
updated = query("m10-02-ranking.sql")
assert updated[0] == ("d1", "C", 0.86, 2, 1)
assert query("m10-03-ausencias.sql") == []
print("AL AÑADIR LA MÉTRICA FALTANTE:", updated)
# Una accuracy inválida vuelve a excluir la semilla, no la cuenta completa.
conn.execute("UPDATE metrics SET metric_value=1.2 WHERE run_id='c22'")
assert query("m10-02-ranking.sql") == ranking
assert ("C",1,2) in query("m10-04-cobertura.sql")
# Las restricciones impiden duplicados y referencias a runs inexistentes.
for sql in ["INSERT INTO metrics VALUES ('a11','validation','accuracy',0.1)",
            "INSERT INTO metrics VALUES ('inexistente','validation','accuracy',0.1)"]:
    try:
        conn.execute(sql)
    except sqlite3.IntegrityError:
        pass
    else:
        raise AssertionError("Se aceptó una fila que debía violar la integridad")
print("Verificaciones correctas: población, empates, ausencia, cobertura cero, JOIN, rango y claves.")
conn.close()
