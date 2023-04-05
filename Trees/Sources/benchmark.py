from trees import (BST, AVL)
import gc
import time
from timeit import timeit
import matplotlib.pyplot as plt
from random import randint

numbers = [randint(1, 3000) for i in range(1000)]
print(numbers)
sorted_numbers = [i+1 for i in range(1000)]
print(sorted_numbers)
avl_tree = AVL(numbers)
bst_tree = BST(numbers)

def creating_BST(numbers, quantity):
    if quantity == 0:
        new_bst = BST([0])
    else:
        new_bst = BST(numbers[:quantity])
    return new_bst

def creating_AVL(numbers, quantity):
    if quantity == 0:
        new_avl = AVL([0])
    else:
        new_avl = AVL(numbers[:quantity])
    return new_avl
    
def benchmark_creating_BST(numbers):
    results = []
    quantity = 0
    for i in range(11):
        gc.disable()
        creating_time = timeit(lambda: creating_BST(numbers, quantity), number=10)
        gc.enable()
        results.append(creating_time)
        quantity += 100
    return results

def benchmark_creating_AVL(numbers):
    results = []
    quantity = 0
    for i in range(11):
        gc.disable()
        creating_time = timeit(lambda: creating_AVL(numbers, quantity), number=10)
        gc.enable()
        results.append(creating_time)
        quantity += 100
    return results

def searching_BST(quantity):
    list = []
    for i in numbers[:quantity]:
        list.append(bst_tree.search(i))
    return list

def searching_AVL(quantity):
    list = []
    for i in numbers[:quantity]:
        list.append(avl_tree.search(i))
    return list

def benchmark_searching_BST():
    results = []
    quantity = 1
    for i in range(11):
        gc.disable()
        searching_time = timeit(lambda: searching_BST(quantity), number=10)
        gc.enable()
        results.append(searching_time)
        quantity += 100
    return results

def benchmark_searching_AVL():
    results = []
    quantity = 1
    for i in range(11):
        gc.disable()
        searching_time = timeit(lambda: searching_AVL(quantity), number=10)
        gc.enable()
        results.append(searching_time)
        quantity += 100
    return results

def removing_BST_benchmark():
    results = []
    quantity = 0
    for i in range(11):
        bst_tree = BST(numbers)
        gc.disable()
        start = time.time()
        for i in numbers[:quantity]:
            bst_tree.delete(i)
        stop = time.time()
        gc.enable()
        results.append(stop - start)
        quantity +=100
    return results

def removing_AVL_benchmark():
    results = []
    quantity = 0
    for i in range(11):
        avl_tree = AVL(numbers)
        gc.disable()
        start = time.time()
        for i in numbers[:quantity]:
            avl_tree.delete(i)
        stop = time.time()
        gc.enable()
        results.append(stop - start)
        quantity +=100
    return results


def s_creating_BST(sorted_numbers, quantity):
    if quantity == 0:
        new_bst = BST([0])
    else:
        new_bst = BST(sorted_numbers[:quantity])
    return new_bst

def s_creating_AVL(sorted_numbers, quantity):
    if quantity == 0:
        new_avl = AVL([0])
    else:
        new_avl = AVL(sorted_numbers[:quantity])
    return new_avl
    
def s_benchmark_creating_BST(sorted_numbers):
    results = []
    quantity = 0
    for i in range(11):
        gc.disable()
        creating_time = timeit(lambda: s_creating_BST(sorted_numbers, quantity), number=10)
        gc.enable()
        results.append(creating_time)
        quantity += 100
    return results

def s_benchmark_creating_AVL(sorted_numbers):
    results = []
    quantity = 0
    for i in range(11):
        gc.disable()
        creating_time = timeit(lambda: s_creating_AVL(sorted_numbers, quantity), number=10)
        gc.enable()
        results.append(creating_time)
        quantity += 100
    return results

def s_searching_BST(quantity):
    list = []
    for i in sorted_numbers[:quantity]:
        list.append(bst_tree.search(i))
    return list

def s_searching_AVL(quantity):
    list = []
    for i in sorted_numbers[:quantity]:
        list.append(avl_tree.search(i))
    return list

def s_benchmark_searching_BST():
    results = []
    quantity = 1
    for i in range(11):
        gc.disable()
        searching_time = timeit(lambda: s_searching_BST(quantity), number=10)
        gc.enable()
        results.append(searching_time)
        quantity += 100
    return results

def s_benchmark_searching_AVL():
    results = []
    quantity = 1
    for i in range(11):
        gc.disable()
        searching_time = timeit(lambda: s_searching_AVL(quantity), number=10)
        gc.enable()
        results.append(searching_time)
        quantity += 100
    return results

def s_removing_BST_benchmark():
    results = []
    quantity = 0
    for i in range(11):
        bst_tree = BST(sorted_numbers)
        gc.disable()
        start = time.time()
        for i in sorted_numbers[:quantity]:
            bst_tree.delete(i)
        stop = time.time()
        gc.enable()
        results.append(stop - start)
        quantity +=100
    return results

def s_removing_AVL_benchmark():
    results = []
    quantity = 0
    for i in range(11):
        avl_tree = AVL(sorted_numbers)
        gc.disable()
        start = time.time()
        for i in sorted_numbers[:quantity]:
            avl_tree.delete(i)
        stop = time.time()
        gc.enable()
        results.append(stop - start)
        quantity +=100
    return results
