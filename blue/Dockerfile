FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy app.py from shared folder (now possible from root context)
COPY shared/app.py .

EXPOSE 5000
CMD ["python", "app.py"]
