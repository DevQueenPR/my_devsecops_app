# Use a slim-buster image for a smaller footprint
FROM python:3.8-slim-buster

# Install zlib1g-dev for Pillow compilation
RUN apt-get update && \
    apt-get install -y --no-install-recommends zlib1g-dev gcc libjpeg-dev && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY app.py .

# Command to run your application (assuming app.py runs a Flask/Django app, etc.)
# CMD ["python", "app.py"]
