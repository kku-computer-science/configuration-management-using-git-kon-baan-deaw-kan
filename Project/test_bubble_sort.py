
# Project/test_bubble_sort.py
"""
Unit tests for Bubble Sort
Written by: Conan
"""

from bubble_sort import bubble_sort

def test_empty():
    assert bubble_sort([]) == []

def test_single():
    assert bubble_sort([9]) == [9]

def test_sorted():
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]

def test_reverse():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_negative():
    assert bubble_sort([0, -2, 5, -2]) == [-2, -2, 0, 5]

def test_duplicates():
    assert bubble_sort([3, 3, 1, 1]) == [1, 1, 3, 3]

def test_large_input():
    arr = list(range(300, 0, -1))
    sorted_arr = list(range(1, 301))
    assert bubble_sort(arr) == sorted_arr
