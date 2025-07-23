import random 
from queue import Queue
from threading import Semaphore, Thread, Lock
from time import sleep


BUFFER_SIZE = 5
MUTEX = Lock()  # lock threading for buffer access

def producer(id: str, slot_sem: Semaphore, item_sem: Semaphore,buf: Queue):
    while True:
        print(f"[Producer {id}]: Waiting for slot")
        slot_sem.acquire()
        print(f"[Producer {id}]: Slot signal ackquired")
        rnd = round(random.uniform(0.01, 0.1),3)
        item = f"ITEM {rnd} from producer {id}"
        sleep(rnd)
        print(f"[Producer {id}]: Producing item: {item}")
        with MUTEX:
            buf.put(item)
        item_sem.release()

def consumer(id: str, slot_sem: Semaphore,item_sem: Semaphore, buf: Queue):
    while True:
        print(f"[Consumer {id}]: Waiting for slot")
        item_sem.acquire() 
        print(f"[Consumer {id}]: Item signal ackquired")
        with MUTEX:
            item = buf.get()
            print(f"[Consumer {id}]: Consuming item: {item}")
        rnd = round(random.uniform(0.01, 0.1), 3)
        sleep(rnd)
        slot_sem.release()

if __name__ == "__main__":
    print("Consumer-Producer example with Threading module Semaphore")
    buffer = Queue(BUFFER_SIZE)
    item_in_buffer = Semaphore(0)
    slot_in_buffer = Semaphore(BUFFER_SIZE)

    prod_consum_num = 2
    producers = []
    consumers = []
    for i in range(prod_consum_num):
        producer_thread = Thread(target=producer, args=(i,slot_in_buffer, item_in_buffer,buffer), daemon=True)
        producer_thread.start()
        producers.append(producer_thread)
        consumer_thread = Thread(target=consumer, args=(i,slot_in_buffer, item_in_buffer, buffer), daemon=True)
        consumer_thread.start()
        consumers.append(consumer_thread)

    sleep(1)
    print("End")
