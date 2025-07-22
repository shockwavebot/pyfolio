import threading
import time
import random

# Create a semaphore with 3 available slots
semaphore = threading.Semaphore(3)

def worker(worker_id):
    print(f"Worker {worker_id} is waiting to acquire the semaphore.")
    with semaphore:  # Automatically acquires and releases the semaphore
        print(f"Worker {worker_id} has acquired the semaphore.")
        time.sleep(random.uniform(1, 3))  # Simulate work
        print(f"Worker {worker_id} is releasing the semaphore.")

# Launch multiple threads
threads = []
for i in range(10):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print("All workers have completed.")
