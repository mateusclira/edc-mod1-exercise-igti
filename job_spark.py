from pyspark.sql.functions import mean, max, min, col, count
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("ExerciseSpark")
    .getOrCreate()
)

enem = (
    spark
    .read
    .format("csv")
    .option("header",True)
    .option("inferSchema",True)
    .option("delimiter",";")
    .load("s3://datalake-mateus-6086-3608-0729/raw-data/MICRODADOS_ENEM_2020")
)

(
    enem
    .write
    .mode("overwrite")
    .format("parquet")
    .partitionBy("TP_FAIXA_ETARIA")
    .save("s3://datalake-mateus-6086-3608-0729/consumer-zone/MICRODADOS_ENEM_2020")
)