FROM python:latest
FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y pip python-dev build-essential
RUN pip install flask
COPY main.py /
CMD [ "python3", "./main.py" ]