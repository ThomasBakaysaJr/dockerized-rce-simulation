FROM node:24-alpine
WORKDIR /client

COPY package.json .
RUN npm install

COPY . .
# runs nodemon to autoreload changes
CMD ["npm", "run", "dev"]