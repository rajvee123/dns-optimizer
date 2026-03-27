total_requests = 0
cache_hits = 0


def log_request(hit):
    global total_requests, cache_hits
    total_requests += 1
    if hit:
        cache_hits += 1


def print_stats():
    if total_requests == 0:
        return

    print("\n==== PERFORMANCE METRICS ====")
    print(f"Total Requests: {total_requests}")
    print(f"Cache Hits: {cache_hits}")
    print(f"Cache Hit Ratio: {cache_hits / total_requests:.2f}")
