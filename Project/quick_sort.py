
"""
Quick Sort Algorithm 
Written by: Thongchai_595-6
"""

def quick_sort(arr): 
    
    if arr is None:
        raise ValueError("Input array cannot be None")
    
    # Base case
    if len(arr) <= 1:
        return arr[:]
    
    pivot_index = len(arr) // 2
    pivot = arr[pivot_index]

    left = []
    mid = []
    right = []

    # Partitioning 
    for value in arr:
        if value < pivot:
            left.append(value)
        elif value > pivot:
            right.append(value)
        else:
            mid.append(value)

    # Recursively sort 
    return quick_sort(left) + mid + quick_sort(right)