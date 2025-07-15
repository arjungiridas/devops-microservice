from flask import Flask, render_template
from prometheus_client import start_http_server, Counter
import os

app = Flask(__name__)

# Prometheus metric
REQUEST_COUNT = Counter('app_requests_total', 'Total number of requests')

@app.route('/')
def home():
    REQUEST_COUNT.inc()
    version = os.getenv('VERSION', 'Unknown')
    return render_template("index.html", version=version)

@app.route('/version')
def version():
    return os.getenv('VERSION', 'Unknown')

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    # Start Prometheus metrics server on port 8000
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000)
