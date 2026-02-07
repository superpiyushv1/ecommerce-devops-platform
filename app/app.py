from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = "1.0.0"

@app.route("/health")
def health():
    return jsonify(status="UP")

@app.route("/version")
def version():
    return jsonify(version=APP_VERSION)

@app.route("/order", methods=["POST"])
def create_order():
    return jsonify(message="Order created successfully")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
