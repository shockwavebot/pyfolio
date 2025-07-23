import threading

def demonstrate_regular_semaphore():
    """Show how regular semaphore can lead to resource leaks."""
    print("=== REGULAR SEMAPHORE ===")
    
    regular_sem = threading.Semaphore(3)  # Initial value: 3
    print("Initial semaphore value: 3")
    
    # Normal usage
    regular_sem.acquire()
    regular_sem.acquire()
    print("After 2 acquires: 1 remaining")
    
    regular_sem.release()
    regular_sem.release()
    print("After 2 releases: back to 3")
    
    # The dangerous part - accidental extra releases
    print("\n--- Accidental extra releases ---")
    regular_sem.release()  # Now internal counter is 4!
    print("Extra release #1: counter now 4 (should be max 3)")
    
    regular_sem.release()  # Now internal counter is 5!
    print("Extra release #2: counter now 5 (should be max 3)")
    
    # This creates a resource leak - more "resources" available than actually exist
    print("\nNow we can acquire more than our original limit:")
    for i in range(5):
        if regular_sem.acquire(blocking=False):
            print(f"  Acquired #{i+1} (this shouldn't be possible beyond 3!)")
        else:
            print(f"  Failed to acquire #{i+1}")

def demonstrate_bounded_semaphore():
    """Show how bounded semaphore prevents resource leaks."""
    print("\n=== BOUNDED SEMAPHORE ===")
    
    bounded_sem = threading.BoundedSemaphore(3)  # Max value: 3
    print("Initial semaphore value: 3")
    
    # Normal usage
    bounded_sem.acquire()
    bounded_sem.acquire()
    print("After 2 acquires: 1 remaining")
    
    bounded_sem.release()
    bounded_sem.release()
    print("After 2 releases: back to 3")
    
    # Try the same accidental extra releases
    print("\n--- Attempting accidental extra releases ---")
    try:
        bounded_sem.release()  # This will raise ValueError
        print("Extra release #1: Should not see this!")
    except ValueError as e:
        print(f"Extra release #1 BLOCKED: {e}")
    
    # Semaphore state is protected - counter stays at 3
    print("Semaphore counter remains at safe maximum of 3")
    
    acquired_count = 0
    print("\nCan only acquire up to the original limit:")
    for i in range(5):
        if bounded_sem.acquire(blocking=False):
            acquired_count += 1
            print(f"  Acquired #{i+1}")
        else:
            print(f"  Failed to acquire #{i+1} (correctly blocked)")
    
    # Clean up
    for _ in range(acquired_count):
        bounded_sem.release()

class FlawedConnectionPool:
    """Example showing how regular semaphore can cause issues."""
    
    def __init__(self, max_connections):
        self.semaphore = threading.Semaphore(max_connections)  # Regular semaphore
        self.max_connections = max_connections
    
    def buggy_method(self):
        """Simulate a bug where release() is called twice."""
        self.semaphore.acquire()
        print("Acquired connection")
        
        # Simulate some bug where release gets called twice
        self.semaphore.release()
        print("Released connection (first time)")
        
        # Bug: accidental second release
        self.semaphore.release()
        print("Released connection (second time) - BUG: This creates a leak!")

class SafeConnectionPool:
    """Example showing how bounded semaphore prevents the issue."""
    
    def __init__(self, max_connections):
        self.semaphore = threading.BoundedSemaphore(max_connections)  # Bounded semaphore
        self.max_connections = max_connections
    
    def buggy_method(self):
        """Same buggy code, but bounded semaphore catches the error."""
        self.semaphore.acquire()
        print("Acquired connection")
        
        self.semaphore.release()
        print("Released connection (first time)")
        
        try:
            # The same bug, but now it's caught!
            self.semaphore.release()
            print("Released connection (second time) - This shouldn't print")
        except ValueError as e:
            print(f"BUG CAUGHT: {e}")

def demonstrate_real_world_scenario():
    """Show practical difference in connection pool scenario."""
    print("\n=== REAL WORLD SCENARIO ===")
    
    print("\n1. Flawed pool with regular semaphore:")
    flawed_pool = FlawedConnectionPool(2)
    flawed_pool.buggy_method()
    
    print("\n2. Safe pool with bounded semaphore:")
    safe_pool = SafeConnectionPool(2)
    safe_pool.buggy_method()

if __name__ == "__main__":
    demonstrate_regular_semaphore()
    demonstrate_bounded_semaphore()
    demonstrate_real_world_scenario()
