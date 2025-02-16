import threading
import time

from lib import logger


def wait_for_event(e, name):
    logger.info(f"{name}: Waiting for the event to be set...")
    e.wait(5)  # Blocks until event is set
    logger.info(f"{name}: Event is set! Resuming work...")


def set_event_after_delay(e, delay):
    logger.info("Setter Thread: Doing some work before setting the event...")
    time.sleep(delay)
    logger.info("Setter Thread: Work done. Setting the event now.")
    e.set()


if __name__ == "__main__":
    # Create an Event object
    event = threading.Event()

    # Create two threads that will wait for the event
    t1 = threading.Thread(target=wait_for_event, args=(event, "Thread-1"))

    # Create a thread that will set the event after a delay
    setter_thread = threading.Thread(target=set_event_after_delay, args=(event, 3))

    # Start all threads
    t1.start()
    setter_thread.start()

    time.sleep(4)
    event.clear()  # Reset the event
    t2 = threading.Thread(target=wait_for_event, args=(event, "Thread-2"))
    t2.start()

    # Wait for all threads to finish
    t1.join()
    setter_thread.join()
    t2.join()

    logger.info("Main: All threads have finished.")
