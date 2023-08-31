FROM node:19 AS node-build

WORKDIR /usr/src/app

COPY sveltekit_frontend/package*.json ./
RUN npm i && npm run build

COPY sveltekit_frontend sveltekit_frontend

RUN npm run build
