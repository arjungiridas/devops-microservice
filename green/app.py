from flask import Flask
from prometheus_client import start_http_server, Counter
import os

app = Flask(__name__)
REQUEST_COUNT = Counter('app_requests_total', 'Total number of requests')

@app.route('/')
def hello():
    REQUEST_COUNT.inc()
    version = os.getenv('VERSION', 'Green')
    return f"""
    <html>
    <head>
        <title>Flask App - Green</title>
        <style>
            body {{
                background: linear-gradient(to bottom right, #56ab2f, #a8e063);
                color: #1b1b1b;
                font-family: 'Verdana', sans-serif;
                text-align: center;
                padding-top: 100px;
            }}
            h1 {{
                font-size: 3em;
                color: #145a32;
            }}
        </style>
    </head>
    <body>
        <h1>✅ Green Version: {version}</h1>
        <p>This is the Green environment of the Flask app.</p>
    </body>
    </html>
    """

@app.route('/version')
def version():
    return os.getenv('VERSION', 'Green')

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000)
