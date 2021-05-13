FROM python:3.7

ARG ENV

WORKDIR /app

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY ./ ./

ENTRYPOINT python driver.py