FROM node:6.1.0

MAINTAINER Enrique Garcia Navalon <garcianavalon@gmail.com>

RUN mkdir -p /app
WORKDIR /app

EXPOSE 3000
CMD [ "npm", "start" ]

# Install app dependencies
COPY ./nodejs/package.json /app/
RUN npm --quiet install

# Bundle app source
COPY ./nodejs /app
