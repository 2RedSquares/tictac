from pyspark.sql import SparkSession


def test_dbconnect():
    spark = SparkSession.builder.getOrCreate()
    print("Testing simple count")  
    # The Spark code will execute on the Databricks cluster.
    print(spark.range(100).count())
    assert 1 == 1


