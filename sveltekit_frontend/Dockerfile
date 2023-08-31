FROM node:19 AS node-build

WORKDIR /usr/src/app

COPY sveltekit_frontend/package*.json ./
RUN npm i && npm run build

COPY . .

RUN npm run build
CMD [ "node build/index.js" ]
