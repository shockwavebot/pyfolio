import threading
import time
import random
from contextlib import contextmanager

class ConnectionPool:
    """A thread-safe connection pool using bounded semaphore."""
    
    def __init__(self, max_connections=3):
        # Bounded semaphore prevents releasing more than max_connections
        self.semaphore = threading.BoundedSemaphore(max_connections)
        self.max_connections = max_connections
        self._connections = []
        
    @contextmanager
    def get_connection(self):
        """Context manager for acquiring/releasing connections safely."""
        print(f"[{threading.current_thread().name}] Waiting for connection...")
        
        # Acquire a connection (blocks if pool is full)
        self.semaphore.acquire()
        try:
            connection_id = len(self._connections) + 1
            connection = f"Connection-{connection_id}"
            self._connections.append(connection)
            
            print(f"[{threading.current_thread().name}] Acquired {connection}")
            print(f"Active connections: {len(self._connections)}/{self.max_connections}")
            
            yield connection
            
        finally:
            # Always release the connection
            if self._connections:
                released = self._connections.pop()
                print(f"[{threading.current_thread().name}] Released {released}")
            self.semaphore.release()

def worker(pool, worker_id, work_duration):
    """Simulate a worker that needs a database connection."""
    try:
        with pool.get_connection() as conn:
            print(f"[Worker-{worker_id}] Using {conn} for {work_duration}s")
            time.sleep(work_duration)
            print(f"[Worker-{worker_id}] Work completed")
    except Exception as e:
        print(f"[Worker-{worker_id}] Error: {e}")

def demonstrate_bounded_behavior():
    """Show what happens when trying to release too many resources."""
    print("\n--- Demonstrating Bounded Behavior ---")
    
    bounded_sem = threading.BoundedSemaphore(2)  # Max value is 2
    
    # This works fine
    bounded_sem.acquire()
    bounded_sem.release()
    print("Normal acquire/release: OK")
    
    # This will raise ValueError because we're trying to release 
    # more than the maximum value
    try:
        bounded_sem.release()  # This should fail
        bounded_sem.release()  # This would exceed the bound
    except ValueError as e:
        print(f"Bounded semaphore protection: {e}")

if __name__ == "__main__":
    # Create a connection pool with max 3 connections
    pool = ConnectionPool(max_connections=3)
    
    # Create 5 workers that will compete for 3 connections
    workers = []
    for i in range(5):
        work_time = random.uniform(1, 3)  # Random work duration
        worker_thread = threading.Thread(
            target=worker,
            args=(pool, i+1, work_time),
            name=f"Worker-{i+1}"
        )
        workers.append(worker_thread)
    
    print("Starting workers (5 workers, 3 max connections)...")
    
    # Start all workers
    for w in workers:
        w.start()
        time.sleep(0.1)  # Slight delay to see the queuing effect
    
    # Wait for all workers to complete
    for w in workers:
        w.join()
    
    print("\nAll workers completed!")
    
    # Demonstrate the bounded behavior
    demonstrate_bounded_behavior()