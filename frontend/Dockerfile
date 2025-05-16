FROM node:20-slim

WORKDIR /app

# Copy package.json and package-lock.json separately to leverage Docker cache
COPY package*.json ./
RUN npm install

# Copy the rest of the app
COPY . .

# Expose port
EXPOSE 5173

# Command is defined in docker-compose.yml for flexibility
CMD ["npm", "run", "dev"]