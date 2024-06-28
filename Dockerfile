# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install virtualenv
RUN pip install --no-cache-dir virtualenv

# Create a virtual environment
RUN virtualenv venv

# Activate the virtual environment and install the required dependencies
RUN . venv/bin/activate && pip install --no-cache-dir -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV PORT=8080

# Ensure the virtual environment is activated when running the application
CMD ["sh", "-c", ". venv/bin/activate && python app.py"]
