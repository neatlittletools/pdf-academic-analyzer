FROM python:3.7

RUN apt-get update  && apt-get install -y python3-pip libpoppler-cpp-dev

WORKDIR /usr/src/app
COPY . .