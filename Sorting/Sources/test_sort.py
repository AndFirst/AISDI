from bubble_sort import bubble_sort
from selection_sort import selection_sort
from merge_sort import merge_sort
from quick_sort import quick_sort

def test_bubble_sort():
    list = [2, 6, 4, 8, 1]
    sorted_list = [1, 2, 4, 6, 8]
    assert bubble_sort(list) == sorted_list
    
def test_bubble_sort_repetetive_numbers():
    list = [2, 6, 4, 8, 1, 1, 1, 4]
    sorted_list = [1, 1, 1, 2, 4, 4, 6, 8]
    assert bubble_sort(list) == sorted_list
    
def test_selection_sort():
    list = [2, 6, 4, 8, 1]
    sorted_list = [1, 2, 4, 6, 8]
    assert selection_sort(list) == sorted_list
    
def test_selection_sort_repetetive_numbers():
    list = [2, 6, 4, 8, 1, 1, 1, 4]
    sorted_list = [1, 1, 1, 2, 4, 4, 6, 8]
    assert selection_sort(list) == sorted_list
    
def test_merge_sort_even_length():
    list = [2, 6, 4, 8, 1]
    sorted_list = [1, 2, 4, 6, 8]
    assert merge_sort(list) == sorted_list
    
def test_merge_sort_odd_length():
    list = [2, 6, 4, 8, 1, 5]
    sorted_list = [1, 2, 4, 5, 6, 8]
    assert merge_sort(list) == sorted_list
    
def test_quick_sort():
    list = [2, 6, 4, 8, 3, 1, 12, 13, 0, 3]
    sorted_list = [0, 1, 2, 3, 3, 4, 6, 8, 12, 13]
    assert quick_sort(list) == sorted_list
    
def test_sort_empty_list():
    l = []
    assert bubble_sort(l) == merge_sort(l) == quick_sort(l) == selection_sort(l) == l

def test_sort_words():
    list = ["ala", "ma", "kota"] 
    sorted_list = ["ala", "kota", "ma"]
    assert bubble_sort(list) == sorted_list
    assert selection_sort(list) == sorted_list
    assert merge_sort(list) == sorted_list
    assert quick_sort(list) == sorted_list