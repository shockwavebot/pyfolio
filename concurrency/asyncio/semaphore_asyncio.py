import asyncio
import random

semaphore = asyncio.Semaphore(3)

async def worker(worker_id):
    print(f"Worker {worker_id} is waiting to acquire the semaphore.")
    async with semaphore:
        print(f"Worker {worker_id} has acquired the semaphore.")
        await asyncio.sleep(random.uniform(1, 2))
        print(f"Worker {worker_id} is releasing the semaphore.")

async def main():
    tasks = [asyncio.create_task(worker(i)) for i in range(10)]
    await asyncio.gather(*tasks)

asyncio.run(main())
