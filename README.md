# codemotion-docker-startups
Code samples for my 2016 Codemotion talk: Docker for Startups and Teams

## How to use this repo
The task folders contain both the final solution and the steps needed. Simple! :)

## Whats the main point?
Showing through with exemplification the benefits of building your proyect or product using Docker

- Easy to integrate other stuff
- Replicate production setup in development
- Easy to share shame environment with peers
- Fuck up proof: easy to clean and regenerate
- Unified interface for executing (run), updating (pull) and stoping
- Focus on your app, reuse everything

## Quick Reference
- `docker-compose up` creates and starts the stack. Use `-d`to run in background.
- `docker-compose down` destroys the stack. Use `-v` to also delete volumes.
- `docker-compose log [service]` shows the log of a service. No service logs all. Use `-f` for following.
- `docker-compose ps` shows the state of the active containers in the stack.
