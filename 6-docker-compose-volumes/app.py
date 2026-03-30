from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

redis_host = os.environ.get("REDIS_HOST", "redis")
redis_port = int(os.environ.get("REDIS_PORT", 6379))

r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)


@app.route("/")
def index():
    return "Hello from Flask! Visit /counter to see the persistent counter."


@app.route("/counter")
def counter():
    count = r.incr("page_views")
    return jsonify(
        {
            "page_views": count,
            "message": "This counter persists across container restarts!",
        }
    )


@app.route("/counter/reset")
def reset_counter():
    r.set("page_views", 0)
    return jsonify({"message": "Counter reset to 0"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)
