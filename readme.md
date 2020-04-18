## cli

### postgres

fig exec postgres bash -c "psql -U airflow -l"


### redis

fig exec redis redis-cli

## memo

https://aws.amazon.com/jp/big-data/datalakes-and-analytics/what-is-a-data-lake/

### data catalog

https://www.ataccama.com/resources/4-reasons-your-data-lake-needs-a-data-catalog

https://jp.drinet.co.jp/blog/datamanagement/data-catalog-trend

### airflow

https://dev.classmethod.jp/articles/airflow-gs-arch-learn/

https://airflow.apache.org/docs/stable/configurations-ref.html?highlight=celery

https://stackoverflow.com/questions/44780736/setting-up-s3-for-logs-in-airflow/44796247#44796247

#### logging

https://stackoverflow.com/questions/60252680/how-to-programmatically-set-up-airflow-1-10-logging-with-localstack-s3-endpoint

https://airflow.readthedocs.io/en/stable/howto/write-logs.html#write-logs-amazon

https://airflow.readthedocs.io/en/stable/howto/connection/aws.html

https://github.com/apache/airflow/blob/master/airflow/providers/amazon/aws/hooks/s3.py#L581

https://github.com/apache/airflow/blob/68d1714f296989b7aad1a04b75dc033e76afb747/airflow/providers/amazon/aws/hooks/base_aws.py#L101

```
worker_1     | [2020-04-19 00:34:24,376] {settings.py:253} INFO - settings.configure_orm(): Using pool settings. pool_size=5, max_overflow=10, pool_recycle=1800, pid=263
worker_1     | [2020-04-19 00:34:24,984] {settings.py:253} INFO - settings.configure_orm(): Using pool settings. pool_size=5, max_overflow=10, pool_recycle=1800, pid=266
worker_1     | [2020-04-19 00:34:25,015] {s3_task_handler.py:180} ERROR - Could not write logs to s3://data_lake/chapter2_download_rocket_launches/download_launches/2015-07-07T00:00:00+00:00/1.log
worker_1     | Traceback (most recent call last):
worker_1     |   File "/usr/local/lib/python3.6/site-packages/airflow/utils/log/s3_task_handler.py", line 177, in s3_write
worker_1     |     encrypt=conf.getboolean('core', 'ENCRYPT_S3_LOGS'),
worker_1     |   File "/usr/local/lib/python3.6/site-packages/airflow/hooks/S3_hook.py", line 380, in load_string
worker_1     |     self._upload_file_obj(file_obj, key, bucket_name, replace, encrypt)
worker_1     |   File "/usr/local/lib/python3.6/site-packages/airflow/hooks/S3_hook.py", line 451, in _upload_file_obj
worker_1     |     client.upload_fileobj(file_obj, bucket_name, key, ExtraArgs=extra_args)
worker_1     |   File "/usr/local/lib/python3.6/site-packages/boto3/s3/inject.py", line 539, in upload_fileobj
worker_1     |     return future.result()
worker_1     |   File "/usr/local/lib/python3.6/site-packages/s3transfer/futures.py", line 106, in result
worker_1     |     return self._coordinator.result()
worker_1     |   File "/usr/local/lib/python3.6/site-packages/s3transfer/futures.py", line 265, in result
worker_1     |     raise self._exception
worker_1     |   File "/usr/local/lib/python3.6/site-packages/s3transfer/tasks.py", line 126, in __call__
worker_1     |     return self._execute_main(kwargs)
worker_1     |   File "/usr/local/lib/python3.6/site-packages/s3transfer/tasks.py", line 150, in _execute_main
worker_1     |     return_value = self._main(**kwargs)
worker_1     |   File "/usr/local/lib/python3.6/site-packages/s3transfer/upload.py", line 692, in _main
worker_1     |     client.put_object(Bucket=bucket, Key=key, Body=body, **extra_args)
worker_1     |   File "/usr/local/lib/python3.6/site-packages/botocore/client.py", line 316, in _api_call
worker_1     |     return self._make_api_call(operation_name, kwargs)
worker_1     |   File "/usr/local/lib/python3.6/site-packages/botocore/client.py", line 613, in _make_api_call
worker_1     |     operation_model, request_dict, request_context)
worker_1     |   File "/usr/local/lib/python3.6/site-packages/botocore/client.py", line 632, in _make_request
worker_1     |     return self._endpoint.make_request(operation_model, request_dict)
worker_1     |   File "/usr/local/lib/python3.6/site-packages/botocore/endpoint.py", line 102, in make_request
worker_1     |     return self._send_request(request_dict, operation_model)
worker_1     |   File "/usr/local/lib/python3.6/site-packages/botocore/endpoint.py", line 132, in _send_request
worker_1     |     request = self.create_request(request_dict, operation_model)
worker_1     |   File "/usr/local/lib/python3.6/site-packages/botocore/endpoint.py", line 116, in create_request
worker_1     |     operation_name=operation_model.name)
worker_1     |   File "/usr/local/lib/python3.6/site-packages/botocore/hooks.py", line 356, in emit
worker_1     |     return self._emitter.emit(aliased_event_name, **kwargs)
worker_1     |   File "/usr/local/lib/python3.6/site-packages/botocore/hooks.py", line 228, in emit
worker_1     |     return self._emit(event_name, kwargs)
worker_1     |   File "/usr/local/lib/python3.6/site-packages/botocore/hooks.py", line 211, in _emit
worker_1     |     response = handler(**kwargs)
worker_1     |   File "/usr/local/lib/python3.6/site-packages/botocore/signers.py", line 90, in handler
worker_1     |     return self.sign(operation_name, request)
worker_1     |   File "/usr/local/lib/python3.6/site-packages/botocore/signers.py", line 160, in sign
worker_1     |     auth.add_auth(request)
worker_1     |   File "/usr/local/lib/python3.6/site-packages/botocore/auth.py", line 357, in add_auth
worker_1     |     raise NoCredentialsError
worker_1     | botocore.exceptions.NoCredentialsError: Unable to locate credentials
worker_1     | [2020-04-19 00:34:25,242] {__init__.py:51} INFO - Using executor CeleryExecutor
worker_1     | [2020-04-19 00:34:25,244] {dagbag.py:403} INFO - Filling up the DagBag from /data_lake/airflow/get_picture.py
worker_1     | [2020-04-19 00:34:25,319: INFO/ForkPoolWorker-3] Task airflow.executors.celery_executor.execute_command[4d6205cf-1892-4a54-ad1c-2ff15df0f75b] succeeded in 17.51859030000196s: None
worker_1     | Running %s on host %s <TaskInstance: chapter2_download_rocket_launches.get_pictures 2015-07-07T00:00:00+00:00 [queued]> 07d5ec9d261b
```
