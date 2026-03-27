import time
from config import BASE_TTL, MAX_TTL, MAX_CACHE_SIZE

CACHE = {}

class CacheEntry:
    def __init__(self, ip):
        self.ip = ip
        self.timestamp = time.time()
        self.freq = 1
        self.ttl = BASE_TTL

    def update_ttl(self):
        # Adaptive TTL based on frequency
        self.ttl = min(MAX_TTL, BASE_TTL + self.freq * 5)

    def is_valid(self):
        return (time.time() - self.timestamp) < self.ttl


def get_cache(domain):
    if domain in CACHE:
        entry = CACHE[domain]

        if entry.is_valid():
            entry.freq += 1
            entry.update_ttl()
            print(f"[CACHE HIT] {domain} | freq={entry.freq} | ttl={entry.ttl}")
            return entry.ip, True
        else:
            del CACHE[domain]

    return None, False


def put_cache(domain, ip):
    if len(CACHE) >= MAX_CACHE_SIZE:
        # Remove least frequently used (LFU)
        least_used = min(CACHE, key=lambda k: CACHE[k].freq)
        print(f"[EVICT] {least_used}")
        del CACHE[least_used]

    CACHE[domain] = CacheEntry(ip)
    print(f"[CACHE STORE] {domain}")
