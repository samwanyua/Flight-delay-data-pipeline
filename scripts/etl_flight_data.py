from pyspark.sql import SparkSession
from pyspark.sql.functions import col, year,month, sum as spark_sum

def main():
    spark = SparkSession.builder\
        .appName("FlightDelayETL")\
        .getOrCreate()
    
    # read parquet file
    df = spark.read.parquet("data/raw/flight_data.parquet")

    print(f"Initial record count: {df.count()}")
    print(f"Schema:\n")

    df.printSchema()

    print("=" * 40)

    print(f"Columns, {df.columns}")

    # df.describe().show()
    print("=" * 40)

    # check for rows with any nulls
    null_counts = df.select([spark_sum(col(c).isNull().cast("int")).alias(c) for c in df.columns])
    
    non_zero_nulls = null_counts.select([
        c for c in null_counts.columns if null_counts.first()[c] > 0
    ])

    non_zero_nulls.show(truncate=False)
    print("=" * 40)

if __name__ == "__main__":
    main()