import os
from flask import Flask
import redis

app = Flask(__name__)

try:
    redis_client = redis.Redis(
        host=os.environ.get("REDIS_HOST", "localhost"),
        port=6379,
        decode_responses=True
    )
    redis_client.ping()
except:
    redis_client = None


@app.route("/")
def home():
    return "Ecommerce DevOps Platform Running!"


@app.route("/health")
def health():
    if redis_client:
        return {"status": "healthy", "redis": "connected"}
    else:
        return {"status": "healthy", "redis": "not available"}
