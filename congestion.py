import time
from config import RATE, BURST

CLIENT_BUCKET = {}

def allow_request(ip):
    now = time.time()

    if ip not in CLIENT_BUCKET:
        CLIENT_BUCKET[ip] = {
            "tokens": BURST,
            "last": now
        }

    bucket = CLIENT_BUCKET[ip]

    # Refill tokens
    elapsed = now - bucket["last"]
    bucket["tokens"] = min(BURST, bucket["tokens"] + elapsed * RATE)
    bucket["last"] = now

    if bucket["tokens"] >= 1:
        bucket["tokens"] -= 1
        return True
    else:
        return False
