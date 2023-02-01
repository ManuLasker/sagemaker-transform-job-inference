#!/usr/bin/env bash

echo "building docker container with name transform_job"

docker build -t transform_job -f $1 .
