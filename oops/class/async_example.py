"""
ASYNCIO CONCURRENCY vs MULTI-THREADING - FUTURE REFERENCE

ASYNCIO (What this example demonstrates):
- Single-threaded with event loop
- Cooperative multitasking - tasks yield control with 'await'
- Non-blocking I/O - while one task waits, others can run
- Perfect for I/O-bound tasks (network calls, file reads)
- No thread switching overhead
- Concurrency = doing multiple things (not simultaneously, but efficiently)

MULTI-THREADING (Different approach):
- Multiple threads running simultaneously  
- Preemptive multitasking - OS controls thread switching
- True parallelism but with overhead and complexity
- Better for CPU-bound tasks
- Parallelism = doing multiple things simultaneously

KEY DIFFERENCE:
- Sequential: 2s + 3s + 1s = 6 seconds total
- Concurrent (asyncio): max(2s, 3s, 1s) = 3 seconds total
- Same thread, but tasks yield during I/O waits

WHEN TO USE ASYNCIO:
- Web scraping, API calls, database queries
- File I/O operations
- Any task that involves waiting for external resources

VISUAL COMPARISON:

Asyncio (Concurrent - Single Thread):
Thread 1: Task A ----wait---- Task B ----wait---- Task C
          (yields)            (yields)            (yields)
          
Multi-threading (Parallel - Multiple Threads):
Thread 1: Task A ████████████████████████████████
Thread 2: Task B ████████████████████████████████  
Thread 3: Task C ████████████████████████████████

EXECUTION FLOW IN THIS EXAMPLE:
Sequential:
  API 1 (2s) → API 2 (3s) → API 3 (1s) = 6 seconds total

Concurrent (asyncio.gather):
  API 1 (2s) ┐
  API 2 (3s) ├─ All start together = 3 seconds total (max time)
  API 3 (1s) ┘
"""

import asyncio
import time

async def fetch_data(name: str, delay: int):
    print(f"Starting to fetch {name}...")
    await asyncio.sleep(delay)  # Simulate network request
    print(f"Finished fetching {name}")
    return f"Data from {name}"

async def main():
    print("Sequential execution:")
    start_time = time.time()
    
    # Sequential - takes 6 seconds total
    result1 = await fetch_data("API 1", 2)
    result2 = await fetch_data("API 2", 3)
    result3 = await fetch_data("API 3", 1)
    
    sequential_time = time.time() - start_time
    print(f"Sequential time: {sequential_time:.2f} seconds\n")
    
    print("Concurrent execution:")
    start_time = time.time()
    
    # Concurrent - takes 3 seconds total (max of all delays)
    results = await asyncio.gather(
        fetch_data("API 1", 2),
        fetch_data("API 2", 3),
        fetch_data("API 3", 1)
    )
    
    concurrent_time = time.time() - start_time
    print(f"Concurrent time: {concurrent_time:.2f} seconds")
    print(f"Results: {results}")

# Run the async function
if __name__ == "__main__":
    asyncio.run(main())
