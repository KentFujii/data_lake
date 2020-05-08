import json
import pathlib

import airflow.utils.dates
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

from clients.twitter_client import TwitterClient
from storages.gcloud_storage import GcloudStorage

dag = DAG(
    dag_id="twitter",
    description="Download twitter posts and store in GCS",
    start_date=airflow.utils.dates.days_ago(2),
    schedule_interval='*/15 * * * *',
    catchup=False
)

def _download(**context):
    client = TwitterClient()
    client.fetch()
    return client.load()

download = PythonOperator(
    task_id="download",
    python_callable=_download,
    provide_context=True,
    dag=dag,
)

def _store(**context):
    downloaded = context['ti'].xcom_pull(task_ids='download')
    storage = GcloudStorage()
    storage.put(context['ts'] + '.json', downloaded)

store = PythonOperator(
    task_id="store",
    python_callable=_store,
    provide_context=True,
    dag=dag,
)

download >> store
