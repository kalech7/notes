"""Laboratorio sintético. Requiere PySpark compatible y Java; ejecutar con spark-submit.
Crea una ruta nueva temporal. No usa fuentes ni infraestructura de producción.
"""
import math
import tempfile
from pathlib import Path
from pyspark.sql import SparkSession, functions as F, Window
from pyspark.sql.types import DoubleType

spark = SparkSession.builder.master('local[2]').appName('LaboratorioDE').getOrCreate()
salida = Path(tempfile.mkdtemp(prefix='estudio-de-spark-'))
try:
    centros = spark.createDataFrame([
        ('PUBLICO','A',0.0,0.0), ('PUBLICO','B',2.0,0.0),
        ('PUBLICO','C',1.0,3.0), ('PRIVADO','D',10.0,10.0),
        ('PRIVADO','E',None,5.0), ('PRIVADO','F',float('nan'),2.0),
    ], 'titularidad string, id string, x double, y double')
    valido = F.col('titularidad').isNotNull()
    for nombre in ('x', 'y'):
        valido = valido & F.col(nombre).isNotNull() & ~F.isnan(nombre) & (F.abs(F.col(nombre)) != float('inf'))
    etiquetado = centros.withColumn('valido', F.coalesce(valido, F.lit(False)))
    limpios = etiquetado.filter('valido').drop('valido')
    rechazados = etiquetado.filter('NOT valido')
    assert limpios.count() == 4 and rechazados.count() == 2
    medias = limpios.groupBy('titularidad').agg(F.avg('x').alias('mx'), F.avg('y').alias('my'))
    enriquecido = limpios.join(medias, 'titularidad')
    assert enriquecido.count() == limpios.count()
    nativo = enriquecido.withColumn('distancia', F.sqrt(
        F.pow(F.col('x')-F.col('mx'),2)+F.pow(F.col('y')-F.col('my'),2)))

    @F.udf(DoubleType())
    def distancia_python(x,y,mx,my):
        if any(v is None for v in (x,y,mx,my)):
            return None
        return float(math.hypot(x-mx,y-my))

    ambos = nativo.withColumn('distancia_python', distancia_python('x','y','mx','my'))
    assert ambos.filter(F.abs(F.col('distancia')-F.col('distancia_python')) > 1e-10).count() == 0
    w = Window.partitionBy('titularidad').orderBy('distancia','id')
    elegidos = ambos.withColumn('rn',F.row_number().over(w)).filter('rn=1')
    # collect permitido aquí: se esperan exactamente dos filas sintéticas.
    assert {r.id for r in elegidos.select('id').collect()} == {'A','D'}
    empates = nativo.withColumn('r', F.rank().over(Window.partitionBy('titularidad').orderBy('distancia'))).filter('r=1')
    assert {r.id for r in empates.select('id').collect()} == {'A','B','D'}
    agrupado = nativo.groupBy('titularidad').agg(F.sort_array(F.collect_list(F.struct('id','distancia'))).alias('centros'))
    agrupado.createOrReplaceTempView('resumen_centros')
    spark.sql("SELECT titularidad, TRANSFORM(centros, c -> c.id) AS ids FROM resumen_centros").show(truncate=False)
    ambos.explain('formatted')
    plano = elegidos.select('titularidad','id','x','y','mx','my','distancia')
    plano.write.mode('errorifexists').parquet(str(salida/'parquet'))
    plano.write.mode('errorifexists').json(str(salida/'json'))
    plano.write.mode('errorifexists').option('header',True).option('sep','|').csv(str(salida/'csv'))
    leidos = [spark.read.parquet(str(salida/'parquet')),
              spark.read.schema(plano.schema).json(str(salida/'json')),
              spark.read.schema(plano.schema).option('header',True).option('sep','|').csv(str(salida/'csv'))]
    for df in leidos:
        assert df.count() == 2
        assert {r.id for r in df.select('id').collect()} == {'A','D'}
    print('Comprobaciones Spark completadas. Resultados en:', salida)
finally:
    spark.stop()
