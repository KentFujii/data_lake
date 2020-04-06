FROM python:3.6.6-stretch

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo
ENV PYTHONDONTWRITEBYTECODE 1
ENV AIRFLOW_HOME /data_lake
ENV C_FORCE_ROOT true
ENV DOCKERIZE_VERSION v0.6.1

RUN apt-get update && apt-get install -y wget
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

WORKDIR /data_lake
ADD requirements.txt /data_lake/requirements.txt
RUN python3 -m pip install --upgrade pip \
        && python3 -m pip install -r /data_lake/requirements.txt
ADD . /data_lake
ENTRYPOINT ["./entrypoint.sh"]
