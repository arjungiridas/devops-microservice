# blue/Dockerfile or green/Dockerfile

FROM python:3.9-slim

WORKDIR /app

# Copy shared app.py into container
COPY ../shared/app.py .

# Copy requirements if needed
COPY ../requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000 8000

CMD ["python", "app.py"]
