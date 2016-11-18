FROM nginx:1.9.14

MAINTAINER Enrique Garcia Navalon "garcianavalon@gmail.com"

RUN  mkdir -p  /etc/nginx

COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf

COPY ./nginx/servers/ /etc/nginx/servers

# OPTIONAL SSL
#COPY ./path/to/certs  /etc/nginx/ssl
