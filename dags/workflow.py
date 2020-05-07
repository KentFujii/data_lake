import json
import pathlib

import airflow.utils.dates
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

from data_lake import clients
from twitter_client import TwitterClient
from gcloud_storage import GcloudStorage

dag = DAG(
    dag_id="twitter",
    description="Download twitter posts and store in GCS",
    start_date=airflow.utils.dates.days_ago(2),
    schedule_interval='*/15 * * * *',
    catchup=False
)

# download = PythonOperator(
#     task_id="download",
#     python_callable=_get_pictures,
#     dag=dag,
# )

download = BashOperator(
    task_id="store",
    bash_command="echo aaaaaaaaaaaaaaaaaaaaaaaaaa",
    dag=dag,
)

download
