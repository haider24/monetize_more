# Section A
##### Write a simple data ingestion boilerplate application that ingest the bid data provided above and bulk insert in elasticsearch. Ensure the data schema is designed using OOP or YAML. Can you make it deployable using docker and kubernetes?


## Application
The application code resides in the app/ directory. The contents of app/ directory along with their details are listed below:
- bid.py
    - Contains the data schema as the Bid class. [elasticsearch-dsl](https://github.com/elastic/elasticsearch-dsl-py) python lobrary is used which allows defining documents as Python objects.
- driver.py
    - The entrypoint of the Docker image which starts the ingestion process
- build_image.sh
    - Bash script that builds the application image. The application was tested on [minikube](https://minikube.sigs.k8s.io/docs/start/) which provides a local kubernetes environment for testing and development purposes. The line eval "$(minikube docker-env)" in the bash script makes sure that the minikube cluster gets the Docker image from local machine rather than try to pull from DockerHub


##### Note: The application reads Elasticsearch endpoint from the "ES_HOST" environment variable