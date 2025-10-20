# Use a lightweight official Python base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy all project files into the container
COPY . /app

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask’s default port
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
