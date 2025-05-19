FROM node:lts-slim

RUN mkdir /app
WORKDIR /app

COPY yarn.lock package.json ./
RUN yarn install

COPY . .
CMD ["yarn", "dev", "--host"]
