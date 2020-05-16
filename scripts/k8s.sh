#!/bin/bash

cd `dirname $0`/k8s

# https://github.com/nigelpoulton/TheK8sBook
# https://kubernetes.io/docs/concepts/configuration/configmap/


# kubectl create configmap env --dry-run=true --output=yaml
# kubectl apply -f ./env.yml
# kubectl delete -f ./env.yml

# postgres
kubectl apply -f ./postgres/deployment.yml
kubectl delete -f ./postgres/deployment.yml
