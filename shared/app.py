from flask import Flask
from prometheus_client import start_http_server, Counter
import os

app = Flask(__name__)
REQUEST_COUNT = Counter('app_requests_total', 'Total number of requests')

@app.route('/')
def hello():
    REQUEST_COUNT.inc()
    version = os.getenv('VERSION', 'unknown')
    bg_color = "green" if version == "green" else "blue"
    return f"""
    <html>
    <head><title>Flask App - {version}</title></head>
    <body style="background-color:{bg_color}; color:white; font-family:Arial;">
    <h1>🚀 Hello from version: <strong>{version}</strong></h1>
    </body></html>
    """

@app.route('/health')
def health():
    return "OK", 200

@app.route('/version')
def version():
    return os.getenv('VERSION', 'unknown')

if __name__ == '__main__':
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000)
