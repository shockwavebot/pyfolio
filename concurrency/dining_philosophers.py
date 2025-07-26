import threading
import time
import random

# Number of philosophers
N = 5

# Chopsticks (mutexes)
chopsticks = [threading.Lock() for _ in range(N)]

def philosopher(id):
    # Determine left and right chopsticks
    left = id
    right = (id + 1) % N
    
    # Asymmetric pickup: even philosophers pick left first, odd pick right first
    first, second = (left, right) if id % 2 == 0 else (right, left)
    
    while True:
        # Thinking
        print(f"Philosopher {id} is thinking.")
        time.sleep(random.uniform(0.1, 1))  # Simulate thinking time
        
        # Attempt to eat
        print(f"Philosopher {id} is hungry.")
        with chopsticks[first]:  # Pick up first chopstick
            print(f"Philosopher {id} picked up chopstick {first}.")
            time.sleep(random.uniform(0.01, 0.1))  # Simulate delay
            with chopsticks[second]:  # Pick up second chopstick
                print(f"Philosopher {id} picked up chopstick {second} and is eating.")
                time.sleep(random.uniform(0.1, 1))  # Simulate eating time
                print(f"Philosopher {id} finished eating.")
            print(f"Philosopher {id} released chopstick {second}.")
        print(f"Philosopher {id} released chopstick {first}.")

# Create philosopher threads
philosophers = [threading.Thread(target=philosopher, args=(i,)) for i in range(N)]

# Set threads as daemons so they exit when the main program ends
for p in philosophers:
    p.daemon = True
    p.start()

# Keep the program running for 5 seconds
time.sleep(5)
print("Main program exiting.")
