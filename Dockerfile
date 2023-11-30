# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /mysite

# Install dependencies
RUN apt-get update && apt-get install -y libpq-dev gcc
COPY requirements.txt /mysite/
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /code
COPY . /mysite/