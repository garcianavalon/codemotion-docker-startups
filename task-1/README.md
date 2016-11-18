## TASK 1 - Casualy making your own IaaS
In this task we will improve our dockerized adding load balancing.

### Learning points
- Advanced composing with Docker Compose
- Exposing and mapping ports

### Steps
0. Create a `task-1` folder in your working environment and go into it
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
    ports:
      - "6767:80"
```

2. Start the up
- `$docker-compose up -d`
- Visit http://localhost:6767 and watch it work.

3. Scale the app for loadbalancing!
- `$docker-compose scale web=3`
- Reload http://localhost:6767 and watch the hostname change!

4. Scale down, we are not rich
- `$docker-compose scale web=1`

5. Clean up
- `$ docker-compose down -v`
