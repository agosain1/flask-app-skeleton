FROM python:alpine3.7

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY . /appServer
WORKDIR /appServer

ENV FLASK_APP=appServer

ENTRYPOINT ["./gunicorn_starter.sh"]