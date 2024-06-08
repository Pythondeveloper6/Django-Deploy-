# start docker with kernal + python
FROM python:3.11.9-slim-bullseye

# show logs 
ENV PYTHONUNBUFFERED = 1

# update kernal + install dependencies 
RUN apt-get update && apt-get -y install gcc libpq-dev

# create project folder 
WORKDIR /app

# copy requirments.txt --> app
COPY requirments.txt /app/requirments.txt

# install requirements
RUN pip install -r /app/requirments.txt

# copy all project files --> app
COPY . /app/