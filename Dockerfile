# Define the base image
FROM ubuntu:18.04

# Install required packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.5 \
    python3-pip \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy this repo to a folder in the Docker container
COPY . .

# Set the work directory
WORKDIR .

# Run unittests
CMD python3 -m unittest unit.py

# Run Main
CMD python3 main.py

EXPOSE 22
