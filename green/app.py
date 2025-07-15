from flask import Flask
from prometheus_client import start_http_server, Counter
import time

app = Flask(__name__)

# Define a counter metric
REQUEST_COUNT = Counter('app_requests_total', 'Total number of requests')

@app.route('/')
def hello():
    REQUEST_COUNT.inc()
    return "🚀 Hello from the UPDATED Flask app via Blue-Green Deployment(green)!"

if __name__ == '__main__':
    # Start Prometheus metrics server on port 8000
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000)

