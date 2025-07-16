FROM python:3.9-slim

WORKDIR /app

# Copy requirements first to use Docker cache efficiently
COPY ../requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# NOW copy the latest app.py
COPY ../shared/app.py .

EXPOSE 5000
EXPOSE 8000

CMD ["python", "app.py"]