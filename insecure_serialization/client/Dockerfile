FROM node:24-alpine
WORKDIR /app

COPY package.json .
RUN npm install

COPY server.js .
# runs nodemon to autoreload changes
CMD ["npm", "run", "dev"]