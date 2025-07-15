# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files
COPY ../shared/app.py .
COPY ../shared/requirements.txt /app/requirements.txt


# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000
EXPOSE 8000

# Set version
ENV VERSION=blue


# Run the app
CMD ["python", "app.py"]
