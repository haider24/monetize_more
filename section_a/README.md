# Section A
##### Write a simple data ingestion boilerplate application that ingest the bid data provided above and bulk insert in elasticsearch. Ensure the data schema is designed using OOP or YAML. Can you make it deployable using docker and kubernetes?


## Application
The details of the importtant application code files listed below:
- bid.py
    - Contains the data schema as the Bid class. [elasticsearch-dsl](https://github.com/elastic/elasticsearch-dsl-py) python lobrary is used which allows defining documents as Python objects.
- driver.py
    - The entrypoint of the Docker image which starts the ingestion process
- build_image.sh
    - Bash script that builds the application image. The application was tested on [minikube](https://minikube.sigs.k8s.io/docs/start/) which provides a local kubernetes environment for testing and development purposes. The line eval "$(minikube docker-env)" in the bash script makes sure that the minikube cluster gets the Docker image from local machine rather than try to pull from DockerHub


###### Note: The application reads Elasticsearch endpoint from the "ES_ENDPOINT" environment variable

## Kubernetes Deployment
The file "ingestion_job.yaml" contains the Kubernetes deployment configuration. The application is deployed on Kubernetes in the form of a [Kubernetes Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/). The job contains ES_HOST as environment variable.