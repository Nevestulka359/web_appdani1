from flask import Flask
import redis
import os

app = Flask(__name__)

# Configure Redis connection from environment variables
redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))

# Connect to Redis
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/')
def home():
    return "OK", 200

@app.route('/visit')
def visit():
    try:
        count = r.incr('visits')
        return f"Visit count: {count}"
    except redis.exceptions.ConnectionError:
        return "Cannot connect to Redis", 500

@app.route('/health')
def health():
    try:
        return "OK", 200
    except redis.exceptions.ConnectionError:
        return "Redis unavailable", 500