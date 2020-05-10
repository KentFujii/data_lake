#!/bin/bash

cd `dirname $0`/k8s
kubectl apply -f ./
# kubectl delete -f ./
