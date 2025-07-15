from airflow import DAG
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import subprocess

default_args = {
    'owner': 'data_engineer',
    'start_date': days_ago(1),
    'depends_on_past': False,
    'retries': 1,
}

def run_dbt_models():
    subprocess.run(["dbt", "run"], check=True)

with DAG(
    'retail_sales_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
) as dag:

    load_data = SnowflakeOperator(
        task_id='load_data',
        sql='''COPY INTO raw.retail_sales FROM @my_stage/retail_sales_sample.csv FILE_FORMAT = (TYPE = 'CSV' FIELD_OPTIONALLY_ENCLOSED_BY = '"')''',
        snowflake_conn_id='my_snowflake_conn',
    )

    transform_data = PythonOperator(
        task_id='transform_data',
        python_callable=run_dbt_models,
    )

    load_data >> transform_data
