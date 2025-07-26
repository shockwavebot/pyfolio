import threading
import time

shared_counter = [0]
iterations = 100_000

def increment_counter():
    global shared_counter
    for _ in range(iterations):
        val = shared_counter[0]
        time.sleep(0.00001)  # simulate delay between read and write
        shared_counter[0] = val + 1


# Create multiple threads to increment the counter
threads = []
thread_num = 10
for _ in range(thread_num):
    thread = threading.Thread(target=increment_counter)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

expected = thread_num * iterations
print(f"Expected value: {expected}")
print(f"Actual value: {shared_counter}")
difference = expected - shared_counter[0]
print(f"Difference: {difference}")


# Expected value: 1000000
# Actual value: [100004]
# Difference: 899996
