from flask import Flask
from prometheus_client import start_http_server, Counter
import os

app = Flask(__name__)
REQUEST_COUNT = Counter('app_requests_total', 'Total number of requests')

@app.route('/')
def hello():
    REQUEST_COUNT.inc()
    version = os.getenv('VERSION', 'Blue')
    return f"""
    <html>
    <head>
        <title>Flask App - Blue</title>
        <style>
            body {{
                background: linear-gradient(to bottom right, #0f2027, #203a43, #2c5364);
                color: #ffffff;
                font-family: 'Segoe UI', sans-serif;
                text-align: center;
                padding-top: 100px;
            }}
            h1 {{
                font-size: 3em;
                color: #00bfff;
            }}
        </style>
    </head>
    <body>
        <h1>🚀 Blue Version: {version}</h1>
        <p>You're running the Blue environment of the Flask app.</p>
    </body>
    </html>
    """

@app.route('/version')
def version():
    return os.getenv('VERSION', 'Blue')

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000)
