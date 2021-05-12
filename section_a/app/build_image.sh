#!/bin/bash

eval $(minikube docker-env)

docker build -t ingest_data .

kubectl apply -f ingestion_job.yaml