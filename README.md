 🚀 Intelligent DNS Caching System with Adaptive TTL and Congestion Control

📌 Overview

This project implements an optimized DNS caching system that enhances traditional DNS resolution by introducing:

* Adaptive Time-To-Live (TTL) based on request frequency
* Token Bucket–based congestion control
* Efficient cache management with LFU eviction
* Multi-client simulation including DDoS-like traffic

The system is designed to reduce latency, improve cache hit ratio, and maintain performance under heavy network load.

 🧠 Key Features

 🔹 Adaptive TTL (Core Innovation)

* TTL dynamically adjusts based on domain access frequency
* Frequently accessed domains remain longer in cache
* Reduces redundant DNS lookups

 🔹 Congestion Control (Token Bucket Algorithm)

* Each client is assigned a token bucket
* Controls request rate dynamically
* Prevents system overload during high traffic or attack scenarios


🔹 LFU Cache Eviction

* Cache size is limited
* Least Frequently Used entries are removed
* Ensures efficient memory utilization


🔹 Multi-threaded Server

* Handles multiple client requests concurrently
* Uses thread pool for optimized performance

 🔹 Performance Metrics

* Total requests tracked
* Cache hit ratio calculated
* Used for comparative analysis


🔹 DDoS Simulation

* Simulates attacker clients sending rapid requests
* Validates effectiveness of congestion control

 ⚙️ How It Works

1. Client sends DNS request
2. Server checks congestion control
3. If allowed:

   * Check cache
   * If hit → return cached IP
   * If miss → resolve from DNS_DB
4. Cache updates:

   * Frequency increases
   * TTL adapts dynamically
5. Metrics updated

 ▶️ How to Run
 Step 1: Clone repository


git clone https://github.com/rajvee123/dns-optimizer.git
cd dns-optimizer

 Step 2: Run project


python main.py

 📊 Sample Output

[CACHE HIT] google.com | freq=30 | ttl=60
[ATTACKER] google.com -> {"status": "ok", "ip": "142.250.183.14"}
[BLOCKED] 10.0.0.1


 📈 Performance Insights

| Scenario     | Cache Hit Ratio | Latency    | Stability |
| ------------ | --------------- | ---------- | --------- |
| Static TTL   | Low (~0.6)      | High       | Moderate  |
| Adaptive TTL | High (~0.8+)    | Low        | High      |
| With DDoS    | Stable          | Controlled | High      |

 🔬 Innovations & Improvements

* Adaptive TTL improves caching efficiency
* Token bucket ensures fair resource allocation
* System remains stable under simulated attacks
* Demonstrates real-world DNS optimization techniques

 🎯 Applications

* DNS servers
* CDN optimization
* Network traffic management
* Distributed systems

 🧪 Future Enhancements

* Machine learning-based traffic prediction
* Real DNS integration
* Visualization dashboard
* Distributed cache nodes

