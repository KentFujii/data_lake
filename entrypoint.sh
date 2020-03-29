#!/bin/bash -xe
dockerize -wait-retry-interval 10s -wait tcp://postgres:5432 -timeout 1m
exec "$@"
