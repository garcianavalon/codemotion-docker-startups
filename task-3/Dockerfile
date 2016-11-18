FROM python:2.7
MAINTAINER Enrique Garcia Navalon <garcianavalon@gmail.com>

RUN mkdir -p /app
WORKDIR /app

EXPOSE "5000"
CMD python app.py

# Install app dependencies
COPY ./python/requirements.txt /app/
RUN pip install -r requirements.txt

# Bundle app source
COPY ./python /app
