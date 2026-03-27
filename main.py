import threading
import time
from server import start_server
from client import simulate
from metrics import print_stats

if __name__ == "__main__":
    threading.Thread(target=start_server, daemon=True).start()

    time.sleep(1)

    simulate()

    print_stats()
