import sys
from awsglue.context import GlueContext
from pyspark.context import SparkContext

sc= SparkContext()
glueContext= GlueContext(sc)
spark= glueContext.spark_session

jdbc_url= "jdbc:postgresql://retaildb.cwhoa0u4yglg.us-east-1.rds.amazonaws.com:5432/retail_db"
props= {'user': 'postgres', 'password': 'postgres123', 'driver':'org.postgresql.Driver'}

df = spark.read.jdbc(url= jdbc_url, table= "public.transactions", properties= props)
df.write.mode("overwrite").parquet("s3://retail-pipeline-data-lake/raw/transactions/")