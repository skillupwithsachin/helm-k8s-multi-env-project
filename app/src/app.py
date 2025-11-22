# app/src/app.py
import os
from flask import Flask, jsonify

app = Flask(__name__)

ENV = os.getenv("APP_ENV", "dev")
GREETING = os.getenv("GREETING", "Hello")
VERSION = os.getenv("APP_VERSION", "v0.0.1")

@app.route("/")
def root():
    return jsonify({
        "message": f"{GREETING} from Flask API ({ENV})",
        "version": VERSION,
        "env": ENV
    })

@app.route("/health")
def health():
    return jsonify({"status": "ok", "env": ENV})

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
