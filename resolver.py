import time
from config import DNS_DB
from cache import get_cache, put_cache
from metrics import log_request


def resolve(domain):
    ip, hit = get_cache(domain)

    if hit:
        log_request(True)
        return ip

    # Simulate DNS delay
    time.sleep(0.1)
    ip = DNS_DB.get(domain, "0.0.0.0")

    put_cache(domain, ip)
    log_request(False)

    return ip
