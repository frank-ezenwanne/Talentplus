FROM node:14.21-alpine

WORKDIR /dt_frontend

COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD npm run start




