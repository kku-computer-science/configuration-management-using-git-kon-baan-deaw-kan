# Project/main.py
"""
Main Program for Sorting Project
Written by: Tharanon_3873
"""

from quick_sort import quick_sort
from bubble_sort import bubble_sort
from input_handler import parse_numbers
import sys

def choose_algorithm(arr, algo):
    algo = algo.lower()

    if algo in ["quick", "quicksort", "q"]:
        return quick_sort(arr)

    elif algo in ["bubble", "bubblesort", "b"]:
        return bubble_sort(arr)

    else:
        raise ValueError("Invalid algorithm (choose quick/bubble).")

def interactive_mode():
    print("==== Sorting Program ====")

    raw = input("Enter numbers (space/comma separated): ")
    arr = parse_numbers(raw)

    algo = input("Algorithm (quick/bubble): ")

    try:
        result = choose_algorithm(arr, algo)
    except ValueError as e:
        print(e)
        return

    print("\n------------------------")
    print("Input :", arr)
    print("Sorted:", result)
    print("------------------------")

def cli_mode(args):
    # Example:
    # python main.py "1 5 3" quick
    try:
        arr = parse_numbers(args[0])
        algo = args[1]
        result = choose_algorithm(arr, algo)
        print(result)
    except Exception as e:
        print("Error:", e)

if _name_ == "_main_":
    if len(sys.argv) > 1:
        cli_mode(sys.argv[1:])
    else:
        interactive_mode()
