import os
from flask import Flask
import redis

app = Flask(__name__)

redis_client = None

redis_url = os.environ.get("REDIS_URL")

if redis_url:
    try:
        redis_client = redis.from_url(redis_url, decode_responses=True)
        redis_client.ping()
        print("Connected to Redis")
    except Exception as e:
        print("Redis connection failed:", e)
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
