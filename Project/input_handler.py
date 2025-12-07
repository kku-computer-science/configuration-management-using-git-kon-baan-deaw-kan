# Project/input_handler.py
"""
Input Parser
Written by: Tharanon_3873
"""

def parse_numbers(raw_input):
    """
    Parse user input (space or comma separated)
    Example:
        "1 2 3"
        "1,2,3"
        "1, 2, 3"
    """
    if not raw_input:
        return []

    raw_input = raw_input.replace(",", " ")
    tokens = raw_input.split()

    try:
        return [int(t) for t in tokens]
    except ValueError:
        raise ValueError("Invalid input: numbers only.")