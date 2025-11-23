from threading import Thread
from time import time
from enum import Enum

niter = 5 * 1000 * 1000

class BarDescriptor:
    def __get__(self, instance, owner):
        return 2
    
    def __set__(self, instance, value):
        pass

class Bar:
    X = BarDescriptor()

def benchmark(n):
    items = [Bar()] * n
    for i in range(n):
        # Bar.X
        items[i].X = 1

for nth in (1, 4):
    t0 = time()
    threads = [Thread(target=benchmark, args=(niter,)) for _ in range(nth)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"{nth=} {(time() - t0) / nth}")