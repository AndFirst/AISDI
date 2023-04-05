import pytest

from heaps import Heap

def test_create_empty_binary_heap():
    heap = Heap(2)
    assert heap.get_raw_data() == []
    assert heap._k == 2

def test_create_empty_n_ary_heap():
    n = 1500100900
    heap = Heap(n)
    assert heap.get_raw_data() == []
    assert heap._k == n

def test_create_one_ary_heap():
    with pytest.raises(ValueError):
        heap = Heap(1)

def test_check_correctly():
    heap = Heap(2)
    for value in [4, 3, 2, 1]:
        heap.push(value)
    assert heap.check() is True
    heap._values[0] = -1
    assert heap.check() is False

def test_insert():
    heap = Heap(3)
    heap.push(1)
    assert heap.get_raw_data() == [1]
    heap.push(2)
    assert heap.get_raw_data() == [2, 1]
    heap.push(1)
    assert heap.get_raw_data() == [2, 1, 1]
    heap.push(3)
    assert heap.get_raw_data() == [3, 1, 1, 2]
    heap.push(4)
    assert heap.get_raw_data() == [4, 3, 1, 2, 1]
    assert heap.check() is True

def test_remove_root():
    heap = Heap(2)
    for number in [4, 3, 2, 1]:
        heap.push(number)
    heap.pop()
    assert heap.peek() == 3
    assert len(heap.get_raw_data()) == 3
    assert heap.check() is True
