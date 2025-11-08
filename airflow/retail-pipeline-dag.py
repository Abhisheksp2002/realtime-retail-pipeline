from airflow import DAG
from airflow.providers.amazon.aws.operators.glue import AwsGlueJobOperator
from airflow.providers.amazon.aws.operators.lambda_function import AwsLambdaInvokeFunctionOperator
from datetime import datetime, timedelta

default_args= {"owner": "data_team", "retries":1, "retry_delay": timedelta(minutes=5)}

with DAG("retail_pipeline", start_date= datetime(2025, 11, 6), schedule_interval= "@hourly", catchup= False) as dag:
    fetch_products= AwsLambdaInvokeFunctionOperator(
        task_id= "fetch_products", function_name= "product-api-fetcher"
    )

    extract_pg= AwsGlueJobOperator(
        task_id= "extract_postgres", job_name= "extract-postgres"
    )

    transform_silver= AwsGlueJobOperator(
        task_id= "to_silver", job_name= "bronze-to-silver"
    )

    transform_gold= AwsGlueJobOperator(
        task_id= "to_gold", job_name= "silver_to_gold"
    )

    fetch_products >> extract_pg >> transform_silver >> transform_gold