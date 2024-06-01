# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

# Define environment variable
ENV FLASK_APP=app.py

# Make the script executable
RUN chmod +x /app/start.sh

# Set the entrypoint to the shell script
ENTRYPOINT ["/app/start.sh"]
