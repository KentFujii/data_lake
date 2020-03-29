from builtins import range
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.models import DAG
from datetime import datetime, timedelta

args = {
    'owner': 'airflow',
    'start_date': datetime.today(),
}

dag = DAG(
    dag_id='test_dag', default_args=args,
    schedule_interval='0 4 * * *',
    dagrun_timeout=timedelta(minutes=60))


task = BashOperator(
    task_id='task',
    bash_command='echo "do task"',
    dag=dag)
