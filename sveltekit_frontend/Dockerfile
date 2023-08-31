FROM node:19 AS node-build

WORKDIR /usr/src/app

COPY sveltekit_frontend/package*.json ./
RUN npm install

COPY sveltekit_frontend/ .

RUN npm run build

EXPOSE 3000
CMD ["npm", "start"]
