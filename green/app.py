from flask import Flask
from prometheus_client import start_http_server, Counter
import os

app = Flask(__name__)

# Prometheus metric
REQUEST_COUNT = Counter('app_requests_total', 'Total number of requests')

@app.route('/')
def hello():
    REQUEST_COUNT.inc()
    version = os.getenv('VERSION', 'Unknown')
    return f"""
    <html>
    <body style="background-color:green; color:white; font-family:Arial; text-align:center; padding-top:100px;">
        <h1>🚀 Hello from version: {version}</h1>
        <h2>This is the GREEN environment!</h2>
    </body>
    </html>
    """

@app.route('/version')
def version():
    return os.getenv('VERSION', 'Unknown')

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000)
