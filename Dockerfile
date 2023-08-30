FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /usr/src/app

# Install any required Python packages
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Install any required Node.js packages
COPY sveltekit_frontend/package.json sveltekit_frontend/package-lock.json ./
# RUN cd sveltekit_frontend/
# Copy the source code into the Docker image
COPY . .

RUN apt-get update && \
    apt-get install -y curl && \
    curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs
RUN npm install
RUN npm run build
# Expose ports 8000 and 3000
# EXPOSE 8000
EXPOSE 3000

CMD ["npm", "run", "start"]

# Define the command to run when the Docker container is started
# CMD ["npm", "run", "dev"]
# CMD ["python", "manage.py", "runserver"]


# Install Node.js and npm
# Install the required Node.js packages
RUN npm install

# Build the SvelteKit app

# Expose the port that the app will run on
EXPOSE 3000

# Start the app
