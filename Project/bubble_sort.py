
# Project/bubble_sort.py
"""
Bubble Sort Algorithm
Written by: Conan
"""

def bubble_sort(arr):
    if arr is None:
        raise ValueError("Input cannot be None")

    result = arr[:]
    n = len(result)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True

        if not swapped:
            break  # Stop if already sorted

    return result
