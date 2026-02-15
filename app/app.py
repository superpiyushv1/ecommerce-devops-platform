import os
import redis
from flask import Flask

app = Flask(__name__)

def get_redis():
    """
    Redis factory function.
    Easy to mock in tests.
    """
    redis_host = os.getenv("REDIS_HOST", "localhost")
    redis_port = int(os.getenv("REDIS_PORT", 6379))
    return redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route("/")
def home():
    r = get_redis()
    r.incr("hits")
    return "Hello from Ecommerce DevOps Platform!", 200

@app.route("/health")
def heallth():
    return {"status": "ok"}, 200
