## memo

https://aws.amazon.com/jp/big-data/datalakes-and-analytics/what-is-a-data-lake/

```
webserver_1  | [2020-04-02 15:13:02 +0000] [21] [INFO] Handling signal: ttin
webserver_1  | [2020-04-02 15:13:02 +0000] [153] [INFO] Booting worker with pid: 153
webserver_1  | [2020-04-02 15:13:03,455] {__init__.py:51} INFO - Using executor CeleryExecutor
webserver_1  | [2020-04-02 15:13:03,457] {dagbag.py:403} INFO - Filling up the DagBag from /data_lake/airflow
webserver_1  | [2020-04-02 15:13:03 +0000] [21] [INFO] Handling signal: ttou
webserver_1  | [2020-04-02 15:13:03 +0000] [137] [INFO] Worker exiting (pid: 137)
```

```
[2020-04-02 15:17:54,477] {scheduler_job.py:153} INFO - Started process (PID=2340) to work on /data_lake/airflow/get_picture.py
[2020-04-02 15:17:54,480] {scheduler_job.py:1560} INFO - Processing file /data_lake/airflow/get_picture.py for tasks to queue
[2020-04-02 15:17:54,481] {logging_mixin.py:112} INFO - [2020-04-02 15:17:54,480] {dagbag.py:403} INFO - Filling up the DagBag from /data_lake/airflow/get_picture.py
[2020-04-02 15:17:54,498] {scheduler_job.py:1572} INFO - DAG(s) dict_keys(['chapter2_download_rocket_launches']) retrieved from /data_lake/airflow/get_picture.py
[2020-04-02 15:17:54,532] {scheduler_job.py:1282} INFO - Processing chapter2_download_rocket_launches
[2020-04-02 15:17:54,544] {scheduler_job.py:446} INFO - Skipping SLA check for <DAG: chapter2_download_rocket_launches> because no tasks in DAG have SLAs
[2020-04-02 15:17:54,549] {scheduler_job.py:161} INFO - Processing /data_lake/airflow/get_picture.py took 0.072 seconds
[2020-04-02 15:17:55,487] {logging_mixin.py:112} INFO - [2020-04-02 15:17:55,486] {settings.py:253} INFO - settings.configure_orm(): Using pool settings. pool_size=5, max_overflow=10, pool_recycle=1800, pid=2342
```

```
File Path                            PID  Runtime      # DAGs    # Errors  Last Runtime    Last Run
---------------------------------  -----  ---------  --------  ----------  --------------  -------------------
/data_lake/airflow/sample.py        2125  0.00s             0           0  1.02s           2020-04-02T15:16:05
/data_lake/airflow/get_picture.py   2124  0.01s             1           0  1.02s           2020-04-02T15:16:05
================================================================================
[2020-04-02 15:16:15,249] {dag_processing.py:1292} INFO - Finding 'running' jobs without a recent heartbeat
[2020-04-02 15:16:15,251] {dag_processing.py:1296} INFO - Failing jobs without heartbeat after 2020-04-02 15:11:15.251343+00:00
[2020-04-02 15:16:25,366] {dag_processing.py:1292} INFO - Finding 'running' jobs without a recent heartbeat
[2020-04-02 15:16:25,368] {dag_processing.py:1296} INFO - Failing jobs without heartbeat after 2020-04-02 15:11:25.368166+00:00
[2020-04-02 15:16:35,496] {dag_processing.py:1292} INFO - Finding 'running' jobs without a recent heartbeat
[2020-04-02 15:16:35,498] {dag_processing.py:1296} INFO - Failing jobs without heartbeat after 2020-04-02 15:11:35.498452+00:00
[2020-04-02 15:16:35,512] {dag_processing.py:1029} INFO - 
================================================================================
DAG File Processing Stats
```

### data catalog

https://www.ataccama.com/resources/4-reasons-your-data-lake-needs-a-data-catalog

https://jp.drinet.co.jp/blog/datamanagement/data-catalog-trend

### airflow

https://dev.classmethod.jp/articles/airflow-gs-arch-learn/

https://airflow.apache.org/docs/stable/configurations-ref.html?highlight=celery
