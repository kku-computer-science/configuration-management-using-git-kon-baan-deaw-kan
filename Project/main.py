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
    while True:
        print("\nSelect an option:")
        print("  1) Sort with Quick Sort")
        print("  2) Sort with Bubble Sort")
        print("  3) Exit")

        choice = input("Choice (1/2/3): ").strip()

        if choice == "3":
            print("Bye!")
            break
        elif choice not in {"1", "2"}:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        raw = input("Enter numbers (space/comma separated): ")
        try:
            arr = parse_numbers(raw)
        except ValueError as e:
            print("Error:", e)
            continue

        algo = "quick" if choice == "1" else "bubble"

        try:
            result = choose_algorithm(arr, algo)
        except ValueError as e:
            print("Error:", e)
            continue

        print("\n------------------------")
        print("Algorithm:", "Quick Sort" if algo == "quick" else "Bubble Sort")
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