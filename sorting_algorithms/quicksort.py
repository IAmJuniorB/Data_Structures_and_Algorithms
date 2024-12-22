"""
Quicksort
"""

import sys

def quicksort(values: list) -> list:
    """
    Implement quicksort algorithm using a pivot-based partitioning approach.

    Args:
        values (list): The list of numbers to be sorted.

    Returns:
        list: A new sorted list containing all elements from the input list.

    Time Complexity: O(n log n) average case, O(n²) worst case
    Space Complexity: O(n) due to creating new lists

    Example:
        >>> quicksort([3, 1, 4, 1, 5, 9, 2, 6])
        [1, 1, 2, 3, 4, 5, 6, 9]
    """
    if len(values) <= 1:
        return values

    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]

    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)

    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

def verify_sort(values: list) -> None:
    """
    Verify if the sorting function works correctly by printing original and sorted lists.

    Args:
        values (list): List of numbers to be sorted.

    Example:
        >>> verify_sort([3, 1, 4, 1, 5])
        Original list: [3, 1, 4, 1, 5]
        Sorted list: [1, 1, 3, 4, 5]
    """
    print("Original list:", values)
    sorted_values = quicksort(values)
    print("Sorted list:", sorted_values)

# Test the implementation
if __name__ == "__main__":
    test_numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    verify_sort(test_numbers)
