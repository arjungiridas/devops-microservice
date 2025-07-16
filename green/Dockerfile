FROM python:3.9-slim

WORKDIR /app

COPY ../shared/app.py .
COPY ../requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000 8000

CMD ["python", "app.py"]
