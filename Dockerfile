# Start with a Python base image
FROM python:3.13.0-alpine3.20

# Install Sphinx and any other required dependencies for your Python script
RUN pip install sphinx

# Install any dependencies needed for the Python script (e.g., numpy, requests, etc.)
RUN pip install --no-cache-dir some-package

# Set up the working directory for the application
WORKDIR /app

# Copy the sum.py script into the container
COPY sum.py /app/

# Create a directory for the Sphinx documentation
COPY ./docs /app/docs

# Set the working directory to where the sum.py script and docs are located
WORKDIR /app

# Optionally, run Sphinx to initialize the documentation (you can do this in Jenkins too)
# RUN sphinx-quickstart /app/docs
