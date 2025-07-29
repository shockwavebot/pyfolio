import threading
import time

mutex = threading.Lock()

def critical_section(thread_id):
    print(f"Thread {thread_id} is waiting for the mutex...")
    with mutex:
        print(f"Thread {thread_id} has acquired the mutex.")
        time.sleep(0.1)  # Simulate critical section
        print(f"Thread {thread_id} is releasing the mutex.")

threads = []
for i in range(5):
    t = threading.Thread(target=critical_section, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All threads finished.")
