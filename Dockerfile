FROM python:3.6

# Set the working directory to /app
WORKDIR /usr/src/app

# Install any required Python packages
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install psycopg2-binary
RUN pip install -r requirements.txt

COPY . .

FROM node:14

WORKDIR /usr/src/app

COPY package.json .
COPY package-lock.json .
RUN npm install


COPY . .

RUN npm run build
# Expose ports 8000 and 3000
# EXPOSE 3000

# CMD ["npm", "run", "start"]

# Define the command to run when the Docker container is started
# CMD ["npm", "run", "dev"]
# CMD ["python", "manage.py", "runserver"]


# Install Node.js and npm
# Install the required Node.js packages
# RUN npm install

# Build the SvelteKit app

# Expose the port that the app will run on
# EXPOSE 3000

# Start the app
