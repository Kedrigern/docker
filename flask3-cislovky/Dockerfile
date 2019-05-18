FROM tiangolo/uwsgi-nginx-flask:latest

COPY ./app /app

ENV STATIC_PATH /app/cislovky/static/

RUN mkdir /app/instance 
RUN chmod 777 /app/instance
VOLUME /app/instance