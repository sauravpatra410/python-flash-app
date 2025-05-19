FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy app files
COPY . /app

# Install system packages (procps gives you `ps`)
RUN apt-get update && \
    apt-get install -y procps && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Expose Flask port
EXPOSE 5000

# Run the app
CMD ["python3", "app.py"]
