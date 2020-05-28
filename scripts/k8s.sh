#!/bin/bash

cd `dirname $0`/k8s

# https://github.com/nigelpoulton/TheK8sBook
# https://kubernetes.io/docs/concepts/configuration/configmap/
# https://kubernetes.io/ja/docs/concepts/
# https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.13/
# kubectl delete all --all

# Workloads
# Networking
# Storage
# Configration

# postgres
# kubectl apply -f ./postgres.yml
# kubectl delete -f ./postgres.yml
# pgcli postgres://data_lake:password@localhost:5432/data_lake

# redis
# kubectl apply -f ./redis.yml
# kubectl delete -f ./redis.yml

# fake-gcs-server
# kubectl apply -f ./fake-gcs-server.yml
# kubectl delete -f ./fake-gcs-server.yml

# apisprout
kubectl create cm apisprout --from-file=../../openapi.yml --dry-run -o yaml | kubectl apply -f -
kubectl apply -f ./apisprout.yml
