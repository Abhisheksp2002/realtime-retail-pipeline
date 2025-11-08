from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql.functions import explode, col, to_timestamp


sc= SparkContext()
glueContext= GlueContext(sc)
spark= glueContext.spark_session

raw= spark.read.json("s3://retail-pipeline-data-lake/raw/transactions/")
flat= raw.selectExpr("transaction_id", "store_id", "timestamp", "explode(items) as item")
clean= float.select("transaction_id", "store_id", to_timestamp("timestamp").alias(ts),
                    col("item.product_id").alias("product_id"),
                    col("item.qty").alias("qty"),
                    col("price").alias("price"))

clean.write.mode("overwrite").parquet("s3://retail-pipeline-data-lake/silver/transactions")