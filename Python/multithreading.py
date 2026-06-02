'''
mulithreading in Python allows you to run multiple threads (smaller units of a process) concurrently, which can be useful for tasks that are I/O-bound or require waiting for external resources. However, due to the Global Interpreter Lock (GIL), Python threads may not be effective for CPU-bound tasks. For CPU-bound tasks, you might want to consider using multiprocessing instead.

'''

import threading
import time



def worker(number):
    print(f"Worker {number} is starting.")
    time.sleep(2)
    print(f"Worker {number} is finishing.")


threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()


for t in threads:
    t.join()

print("All workers have finished.")