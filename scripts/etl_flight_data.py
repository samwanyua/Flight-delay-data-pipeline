from pyspark.sql import SparkSession
from pyspark.sql.functions import col, year,month

def main():
    spark = SparkSession.builder\
        .appName("FlightDelayETL")\
        .getOrCreate()