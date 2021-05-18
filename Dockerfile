# python 3.8 image
#FROM registry.web.boeing.com/container/boeing-images/stack/rhel7-python38
FROM python:3.7.5-buster
#FROM ubuntu:latest

MAINTAINER Gopikrishna Yadam

#COPY . /app

# add the source code
WORKDIR /app

#add all files to app
ADD . /app

# install dependencies
RUN pip install -r requirements.txt

# expose port
EXPOSE 5000


# run the application:
CMD ["python", "app.py"]

