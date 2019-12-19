FROM python:3.7

RUN apt-get update  && apt-get install -y python3-pip libpoppler-cpp-dev
# TODO: verify below works, if works, uncomment
# RUN chmod 777 app/setup.sh
WORKDIR /usr/src/app
COPY . .