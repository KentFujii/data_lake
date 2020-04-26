## cli

### postgres

fig exec postgres bash -c "psql -U airflow -l"


### redis

fig exec redis redis-cli

## memo

https://aws.amazon.com/jp/big-data/datalakes-and-analytics/what-is-a-data-lake/

https://github.com/apache/airflow/blob/master/airflow/contrib/hooks/gcs_hook.py

AIRFLOW_CONN_AWS_DEFAULT=aws://?aws_access_key_id=data_lake&aws_secret_access_key=password&host=http%3A%2F%2Fminio%3A9000

AIRFLOW_CONN_GOOGLE_CLOUD_DEFAULT='google-cloud-platform://?extra__google_cloud_platform__key_path=%2Fkeys%2Fkey.json&extra__google_cloud_platform__scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcloud-platform&extra__google_cloud_platform__project=airflow&extra__google_cloud_platform__num_retries=5'

### airflow

https://airflow.apache.org/docs/stable/howto/write-logs.html#writing-logs-to-google-cloud-storage

https://github.com/googleapis/python-storage/issues/102

https://github.com/apache/airflow/blob/79d3f33c1b65c9c7e7b1a75e25d38cab9aa4517f/airflow/providers/google/cloud/hooks/gcs.py

https://googleapis.dev/python/storage/latest/index.html
