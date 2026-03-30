import redis
import sys

try:
    r = redis.Redis(host="redis", port=6379, decode_responses=True)
    r.ping()
    print("SUCCESS: Connected to Redis at redis:6379")

    # Test write/read
    r.set("test_key", "test_value")
    value = r.get("test_key")
    print(f"SUCCESS: Write/Read test - test_key = {value}")

except redis.ConnectionError as e:
    print(f"FAILED: Could not connect to Redis - {e}")
    sys.exit(1)
except Exception as e:
    print(f"FAILED: {e}")
    sys.exit(1)
