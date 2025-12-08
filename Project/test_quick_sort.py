"""
Unit tests for Quick Sort
Written by: Thongchai_595-6
"""
from quick_sort import quick_sort

def test_empty():
    assert quick_sort([]) == []

def test_single():
    assert quick_sort([7]) == [7]

def test_sorted():
    assert quick_sort([1, 2, 3]) == [1, 2, 3]

def test_reverse():
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_negative():
    assert quick_sort([0, -3, 5, -1]) == [-3, -1, 0, 5]

def test_duplicates():
    assert quick_sort([3, 1, 3, 2, 2, 1]) == [1, 1, 2, 2, 3, 3]

def test_large_input():
    arr = list(range(1000, 0, -1))
    sorted_arr = list(range(1, 1001))
    assert quick_sort(arr) == sorted_arr