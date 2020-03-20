# Dockerfile
FROM node:10

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package*.json ./
COPY webpack.config.js ./

RUN npm install

COPY src ./src

EXPOSE 8080
CMD ["npm", "start"]