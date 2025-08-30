import psutil, time

def monitor_performance():
    return {
        "cpu": psutil.cpu_percent(),
        "memory": psutil.virtual_memory().percent,
        "timestamp": time.time()
    }
