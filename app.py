import os
import redis
from flask import Flask

app = Flask(__name__)

# Initialize Redis client
r = redis.Redis(host=os.getenv("REDIS_HOST", "localhost"), port=os.getenv("REDIS_PORT", 6379))

@app.route('/')
def home():
    return "Welcome to my simple web app!"

@app.route('/about')
def about():
    return "This is the about page."

@app.route('/health')
def health():
    try:
        r.ping()
        return "OK", 200
    except redis.exceptions.ConnectionError:
        return "Redis unavailable", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
