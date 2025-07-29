import queue
import threading

# Example 1: Basic FIFO Queue with Producer-Consumer
def fifo_queue_example():
    print("=== FIFO Queue Example ===")
    q = queue.Queue()

    def producer():
        for i in range(5):
            q.put(i)
            print(f"Produced: {i}")

    def consumer():
        while True:
            item = q.get()
            print(f"Consumed: {item}")
            q.task_done()

    # Create threads
    prod = threading.Thread(target=producer)
    cons = threading.Thread(target=consumer, daemon=True)

    # Start threads
    prod.start()
    cons.start()

    # Wait for producer to finish
    prod.join()
    # Wait for all tasks to be consumed
    q.join()

# Example 2: PriorityQueue
def priority_queue_example():
    print("\n=== PriorityQueue Example ===")
    q = queue.PriorityQueue()
    q.put((2, "Medium priority task"))
    q.put((1, "High priority task"))
    q.put((3, "Low priority task"))

    while not q.empty():
        print(q.get()[1])

# Example 3: LifoQueue (Stack-like behavior)
def lifo_queue_example():
    print("\n=== LifoQueue Example ===")
    q = queue.LifoQueue()
    for i in range(5):
        q.put(i)
        print(f"Pushed: {i}")

    while not q.empty():
        print(f"Popped: {q.get()}")

# Run all examples
if __name__ == "__main__":
    fifo_queue_example()
    priority_queue_example()
    lifo_queue_example()