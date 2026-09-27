import os

from flask import Flask, jsonify

app = Flask(__name__)

CONFIG_KEY = os.environ.get("APP_CONFIG_KEY")
if not CONFIG_KEY:
    raise RuntimeError("APP_CONFIG_KEY environment variable is required")


@app.route("/")
def index():
    return jsonify(service="internal-tool", status="running")


@app.route("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
