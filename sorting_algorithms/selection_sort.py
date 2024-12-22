"""
Selection Sort
"""

import sys

def selection_sort(values: list) -> list:
    """
    Sort a list using the selection sort algorithm.

    Args:
        values (list): The list of numbers to be sorted.

    Returns:
        list: A new sorted list containing all elements from the input list.

    Time Complexity: O(n²)
    Space Complexity: O(n)

    Example:
        >>> selection_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
    """
    sorted_list = []
    
    for _ in range(len(values)):
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop(index_to_move))
    
    return sorted_list

def index_of_min(values: list) -> int:
    """
    Find the index of the minimum value in the list.

    Args:
        values (list): List to search through.

    Returns:
        int: Index of the minimum value in the list.

    Example:
        >>> index_of_min([64, 34, 25, 12, 22])
        3
    """
    min_index = 0
    for i in range(1, len(values)):
        if values[i] < values[min_index]:
            min_index = i
    return min_index

def verify_sort(values: list) -> None:
    """
    Verify if the sorting function works correctly by printing original and sorted lists.

    Args:
        values (list): List of numbers to be sorted.
    """
    original = values.copy()
    sorted_list = selection_sort(values)
    print(f"Original list: {original}")
    print(f"Sorted list: {sorted_list}")

if __name__ == "__main__":
    test_numbers = [64, 34, 25, 12, 22, 11, 90]
    verify_sort(test_numbers)
