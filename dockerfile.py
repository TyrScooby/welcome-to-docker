dockerfile
# Use an official Python runtime as a parent image
FROM python:3-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Run the test when building/running
CMD ["python", "-m", "unittest", "test_app.py"]
