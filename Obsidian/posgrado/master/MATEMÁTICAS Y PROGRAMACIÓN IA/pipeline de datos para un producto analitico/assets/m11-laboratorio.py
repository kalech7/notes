"""Laboratorio didáctico M11: SQLite en memoria, sin dependencias externas.
No usa ni modifica los experimentos del curso. No ejecuta dbt.
Ejecutar: python3 m11-laboratorio.py
"""
import json
import sqlite3


def construir(omitir=False, duplicar=False, vaciar=False):
    con = sqlite3.connect(':memory:')
    con.executescript('''
    CREATE TABLE expected(config_id TEXT, seed INTEGER,
                          PRIMARY KEY(config_id, seed));
    CREATE TABLE runs(run_id TEXT PRIMARY KEY, config_id TEXT, seed INTEGER);
    CREATE TABLE metrics(run_id TEXT PRIMARY KEY, accuracy REAL);
    CREATE TABLE metadata(dataset_key TEXT);
    INSERT INTO expected VALUES ('A',11),('A',22),('B',11),('B',22);
    INSERT INTO runs VALUES ('r1','A',11),('r2','A',22),
                            ('r3','B',11),('r4','B',22);
    INSERT INTO metrics VALUES ('r1',0.6),('r2',0.8),('r3',0.7),('r4',0.9);
    INSERT INTO metadata VALUES ('origen_demo');
    ''')
    if omitir:
        con.execute("DELETE FROM metrics WHERE run_id='r2'")
    if vaciar:
        con.execute('DELETE FROM metrics')
    if duplicar:
        con.execute("INSERT INTO metadata VALUES ('origen_demo')")
    # Todas las ejecuciones del ejemplo pertenecen al mismo origen fijo.
    # Omitimos versión, estado y split para aislar cobertura y multiplicidad.
    con.executescript('''
    CREATE VIEW staging AS
    SELECT r.run_id,r.config_id,r.seed,m.accuracy
    FROM runs r JOIN metrics m ON m.run_id=r.run_id
    JOIN expected e ON e.config_id=r.config_id AND e.seed=r.seed
    JOIN metadata d ON d.dataset_key='origen_demo';
    ''')
    rows, ids = con.execute('SELECT COUNT(*),COUNT(DISTINCT run_id) FROM staging').fetchone()
    bad = con.execute('''
      SELECT e.config_id,e.seed,COUNT(s.run_id)
      FROM expected e LEFT JOIN staging s
      ON s.config_id=e.config_id AND s.seed=e.seed
      GROUP BY e.config_id,e.seed HAVING COUNT(s.run_id)<>1
      ORDER BY e.config_id,e.seed
    ''').fetchall()
    key_ok = con.execute('SELECT COUNT(*)=COUNT(DISTINCT dataset_key) FROM metadata').fetchone()[0]
    non_null = con.execute('SELECT COUNT(*) FROM staging WHERE accuracy IS NULL').fetchone()[0] == 0
    domain_ok = con.execute('SELECT COUNT(*) FROM staging WHERE accuracy IS NULL OR accuracy<0 OR accuracy>1').fetchone()[0] == 0
    rank = None
    if not bad and key_ok and non_null and domain_ok:
        rank = con.execute('''
          WITH summary AS (
            SELECT config_id,AVG(accuracy) mean_accuracy,COUNT(*) seeds
            FROM staging GROUP BY config_id
          ) SELECT config_id,ROUND(mean_accuracy,6),seeds,
            RANK() OVER (ORDER BY mean_accuracy DESC) position
          FROM summary ORDER BY position,config_id
        ''').fetchall()
    result = dict(filas=rows,ejecuciones_distintas=ids,
                  clave_metadatos_valida=bool(key_ok),not_null_pasa=non_null,
                  cobertura_fallos=bad,ranking=rank)
    con.close()
    return result


def main():
    a,b=construir(),construir()
    missing=construir(omitir=True)
    dup=construir(duplicar=True)
    empty=construir(vaciar=True)
    assert a==b
    assert a['ranking']==[('B',0.8,2,1),('A',0.7,2,2)]
    assert missing['cobertura_fallos']==[('A',22,0)]
    assert missing['not_null_pasa'] and missing['ranking'] is None
    assert dup['filas']==8 and dup['ejecuciones_distintas']==4
    assert len(dup['cobertura_fallos'])==4 and dup['ranking'] is None
    assert empty['not_null_pasa'] and len(empty['cobertura_fallos'])==4
    print(json.dumps(dict(caso_correcto=a,metrica_omitida=missing,
                         metadatos_duplicados=dup,metricas_vacias=empty,
                         reconstrucciones_iguales=a==b),indent=2,ensure_ascii=False))

if __name__=='__main__':
    main()
