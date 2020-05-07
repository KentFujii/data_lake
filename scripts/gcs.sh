#!/bin/bash

BODY=`curl http://0.0.0.0:4443/storage/v1/b/data_lake_test/o | jq .items[].name`
echo $BODY
