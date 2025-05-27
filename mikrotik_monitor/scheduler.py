import threading, time
from mikrotik_client import get_nat_stats
from csv_writer import save_stats

def start_monitoring(routers, interval):
    def task():
        while True:
            for r in routers:
                stats = get_nat_stats(r)
                save_stats(r.ip, stats)
            time.sleep(interval)
    thread = threading.Thread(target=task, daemon=True)
    thread.start()
