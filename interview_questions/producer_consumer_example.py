import threading
import time
import random

# Shared buffer and its size
BUFFER_SIZE = 5
buffer = []
mutex = threading.Lock()  # Mutex for exclusive buffer access
items = threading.Semaphore(0)  # Tracks items in buffer
spaces = threading.Semaphore(BUFFER_SIZE)  # Tracks available spaces

def producer(id):
    while True:
        item = random.randint(1, 100)  # Produce a random item
        spaces.acquire()  # Wait for available space
        with mutex:  # Lock the buffer
            buffer.append(item)
            print(f"Producer {id} produced {item}. Buffer: {buffer}")
        items.release()  # Signal that an item is available
        time.sleep(random.uniform(0.1, 1))  # Simulate varying production time

def consumer(id):
    while True:
        items.acquire()  # Wait for available items
        with mutex:  # Lock the buffer
            item = buffer.pop(0)
            print(f"Consumer {id} consumed {item}. Buffer: {buffer}")
        spaces.release()  # Signal that space is available
        time.sleep(random.uniform(0.1, 1))  # Simulate varying consumption time

if __name__ == "__main__":
    # Create producer and consumer threads
    producers = [threading.Thread(target=producer, args=(i,)) for i in range(2)]
    consumers = [threading.Thread(target=consumer, args=(i,)) for i in range(2)]

    # Set threads as daemons so they exit when the main program ends
    for p in producers:
        p.daemon = True
        p.start()
    for c in consumers:
        c.daemon = True
        c.start()

    # Keep the program running for 5 seconds
    time.sleep(5)
    print("Main program exiting.")
