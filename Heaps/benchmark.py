from heaps import Heap
import gc
import time
from timeit import timeit
from random import randint

numbers = [randint(1, 300000) for i in range(100000)]

def creating_2ary_heap(numbers, quantity):
    new_heap = Heap(2)
    for number in numbers[:quantity]:
        new_heap.push(number)
    return new_heap

def creating_3ary_heap(numbers, quantity):
    new_heap = Heap(3)
    for number in numbers[:quantity]:
        new_heap.push(number)
    return new_heap

def creating_4ary_heap(numbers, quantity):
    new_heap = Heap(4)
    for number in numbers[:quantity]:
        new_heap.push(number)
    return new_heap
    
def benchmark_creating_2ary_heap(numbers):
    results = []
    quantity = 0
    for i in range(11):
        gc.disable()
        creating_time = timeit(lambda: creating_2ary_heap(numbers, quantity), number=10)
        gc.enable()
        results.append(creating_time)
        quantity += 10000
    return results

def benchmark_creating_3ary_heap(numbers):
    results = []
    quantity = 0
    for i in range(11):
        gc.disable()
        creating_time = timeit(lambda: creating_3ary_heap(numbers, quantity), number=10)
        gc.enable()
        results.append(creating_time)
        quantity += 10000
    return results

def benchmark_creating_4ary_heap(numbers):
    results = []
    quantity = 0
    for i in range(11):
        gc.disable()
        creating_time = timeit(lambda: creating_4ary_heap(numbers, quantity), number=10)
        gc.enable()
        results.append(creating_time)
        quantity += 10000
    return results


def removing_roots(heap:Heap, quantity):
    for i in range (quantity):
        heap.pop()
    
def benchmark_removing_root_2ary_heap():
    results = []
    quantity = 0
    for i in range(11):
        big_heap2 = Heap(2)
        for number in numbers:
            big_heap2.push(number)
        gc.disable()
        removing_time = timeit(lambda: removing_roots(big_heap2, quantity), number=1)
        gc.enable()
        results.append(removing_time)
        quantity += 9999
    return results

def benchmark_removing_root_3ary_heap():
    results = []
    quantity = 0
    for i in range(11):
        big_heap3 = Heap(3)
        for number in numbers:
            big_heap3.push(number)
        gc.disable()
        removing_time = timeit(lambda: removing_roots(big_heap3, quantity), number=1)
        gc.enable()
        results.append(removing_time)
        quantity += 9999
    return results

def benchmark_removing_root_4ary_heap():
    results = []
    quantity = 0
    for i in range(11):
        big_heap4 = Heap(4)
        for number in numbers:
            big_heap4.push(number)
        gc.disable()
        removing_time = timeit(lambda: removing_roots(big_heap4, quantity), number=1)
        gc.enable()
        results.append(removing_time)
        quantity += 9999
    return results
