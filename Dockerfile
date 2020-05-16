FROM python:3.6.6-stretch

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo
ENV AIRFLOW_HOME /etc/airflow
ENV PYTHONPATH /data_lake
ENV PYTHONDONTWRITEBYTECODE 1
ENV C_FORCE_ROOT true

WORKDIR /data_lake
ADD requirements.txt /data_lake/requirements.txt
RUN python3 -m pip install --upgrade pip \
        && python3 -m pip install -r /data_lake/requirements.txt
ADD airflow.cfg /etc/airflow/airflow.cfg
ADD . /data_lake
