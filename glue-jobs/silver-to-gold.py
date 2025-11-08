import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, to_date, sum as _sum, countDistinct


## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

silver= spark.read.parquet("s3://retail-pipeline-data-lake/silver/transactions/")

silver_agg= silver.withColumn("sale_amount", col("qty")*col("price")) \
            .withColumn("date", to_date(col("ts")))


# Aggregation-1: daily sales summary
daily_sales = silver_agg.groupBy("date", "store_id") \
                .agg(
                    _sum("sale_amount").alias("total_sales"), 
                    countDistinct("transaction_id").alias("total_transactions")
                )
daily_sales.write.mode("overwrite").parquet("s3://retail-pipeline-data-lake/gold/daily-sales-summary/")


# Aggregation-2: Product Performance
prod_perf= silver_agg.groupBy("product_id").agg(
    _sum(col("qty")).alias("total_sold"),
    _sum(col("sale_amount")).alias("total_sales"))

prod_perf.write.mode("overwrite").parquet("s3://retail-pipeline-data-lake/gold/product-performance/")

job.commit()
