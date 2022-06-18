# Define the base image
FROM ubuntu:18.04

# Install required packages
RUN yum update \
 && yum upgrade\
 && yum install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-setuptools
 
# Copy this repo to a folder in the Docker container
COPY . .
 
# Set the work directory
WORKDIR .

# Run unittests
RUN python -m unittest unit.py

# Define entry
ENTRYPOINT ["python", "main.py"]

