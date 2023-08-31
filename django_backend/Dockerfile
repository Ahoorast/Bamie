FROM python:3.8

# Set the working directory to /app
WORKDIR /usr/src/app

# Install any required Python packages
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install psycopg2-binary
RUN pip install -r requirements.txt

COPY . .

