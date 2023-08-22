# Use a Node base image
FROM node:20

# Set working directory
WORKDIR /usr/src/app

# Install app dependencies
COPY package*.json ./
RUN npm install

# Bundle app source
COPY . ./

# Specify the command to run on container start
CMD [ "node", "screen_server.js" ]
