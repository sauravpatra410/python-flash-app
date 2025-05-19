FROM python:3.9-slim

# Copy app files into the container
COPY . /app

# Set the working directory
WORKDIR /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the Flask app
CMD ["python3", "app.py"]
