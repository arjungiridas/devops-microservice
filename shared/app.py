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

    # Set style based on version
    if version.lower() == 'blue':
        bg_color = "#001f3f"
        text_color = "#ffffff"
        title = "🌊 Welcome to the Blue Environment"
    elif version.lower() == 'green':
        bg_color = "#2ECC40"
        text_color = "#000000"
        title = "🌿 Welcome to the Green Environment"
    else:
        bg_color = "#eeeeee"
        text_color = "#000000"
        title = "🚀 Unknown Version"

    return f"""
    <html>
    <head><title>{title}</title></head>
    <body style="background-color:{bg_color}; color:{text_color}; font-family:sans-serif; text-align:center; padding-top:50px">
        <h1>{title}</h1>
        <p>🚀 Deployed with Docker and GitHub Actions!</p>
        <p><strong>Version:</strong> {version}</p>
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
