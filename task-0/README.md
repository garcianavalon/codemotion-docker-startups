## TASK 0 - Building your primerita Dockerfile

In this task we will go through the basics of dockerizing your code and running it.

### Learning points
- Dockerfile syntax and build process
- Layering images for efficency
- Basic orchestration with Docker Compose
- Using volumes for live reloading on containers

### Steps
0. Set up
- Create a task-0 folder in your working environment
- Go inside
1. Create your app
- Create a python folder and go inside
- Create an `app.py` file with the following contents:
```python
import socket

from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
 redis.incr('hits')
 hostname = socket.gethostname()
 return 'Hello World, I am %s! I have been seen %s times.' % (hostname,redis.get('hits'))

if __name__ == "__main__":
 app.run(host="0.0.0.0", debug=True)

```
- Create a `requirements.txt` file
```
flask
redis
```
2. Create a `Dockerfile` in task-0
```
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
```
3. Create a `docker-compose.yml file` in task-0
```
version: '2'
services:
  web:
    build: .
    image: garcianavalon/task0-web
    ports:
     - "5000:5000"
    depends_on:
     - redis
  redis:
    image: redis

```
6. Pull the redis image
- `$ docker-compose pull`

5.  Run it!
- `$ docker-compose up`
- Go to http://localhost:5000 and watch it live!

6. Extra! Code reloading directly with out building
- Add this to your `docker-compose.yml` in the python service sections
```
volumes:
 - ./python:/app
```
7. Clean up
- `$ docker-compose down -v`
