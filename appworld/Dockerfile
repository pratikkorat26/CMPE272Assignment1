# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt /app

# Install the neccesary libraries to run the application
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the files
COPY . /app

# setup the flask environment variable
ENV FLASK_ENV=developmentworldenv

# this commands runs the application
CMD [ "python3", "main.py"]

# docker run command
# first port is our machine's port and second port it where application runs