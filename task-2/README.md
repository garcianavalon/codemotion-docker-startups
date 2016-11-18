## TASK 2 - `if(development==production) happines=true`

In this task we will use NGINX to use custom .localhost domains

### Learning points
- Networking between components
- Using a production like setup


### Steps
0. Create a `task-2` folder in your working environment and go into it
1. Create a `docker-compose.yml` file with the following contents
```
version: '2'
services:
  web:
    image: garcianavalon/task0-web
    depends_on:
     - redis
  redis:
    image: redis
  lb:
    image: dockercloud/haproxy
    links:
      - web
    # For Docker Machine guys
    #environment:
    #  - DOCKER_HOST
    volumes:
      # For linux and Docker for Mac guys
      - /var/run/docker.sock:/var/run/docker.sock
  nginx:
    build: .
    image: garcianavalon/task2-nginx
    volumes:
      - ./nginx/default.conf:/etc/nginx/conf.d/default.conf
      - ./nginx/servers:/etc/nginx/servers
      # OPTIONAL SSL
      # - ./path/to/certs:/etc/nginx/ssl
    links:
      - lb
    ports:
      - "80:80"
      - "443:443"
```
2. Create a `Dockerfile` file with the following contents
```
FROM nginx:1.9.14

MAINTAINER Enrique Garcia Navalon "garcianavalon@gmail.com"

RUN  mkdir -p  /etc/nginx

COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf

COPY ./nginx/servers/ /etc/nginx/servers

# OPTIONAL SSL
#COPY ./path/to/certs  /etc/nginx/ssl
```
3. Copy the NGINX folder from this repo :)

4. Get the images ready
- `$ docker-compose build`
- `$ docker-compose pull`

4. Edit your /etc/hosts ()
- If you are using chrome, skip this step
- On windows C:/Windows/System32/drivers/etc/hosts
- Add `127.0.0.1 *.localhost`

5. Test it!
- Visit http://mywebsite.localhost

6. Bonus point
- Try scaling up and down the web service

7. Clean up
- `$ docker-compose down -v`
