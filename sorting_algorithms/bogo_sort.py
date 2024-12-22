import random

def is_sorted(values: list) -> bool:
    """
    Check if a list is sorted in ascending order.

    Args:
        values (list): List to check if sorted

    Returns:
        bool: True if sorted, False otherwise

    Time Complexity: O(n)
    Space Complexity: O(1)

    Example:
        >>> is_sorted([1, 2, 3, 4])
        True
        >>> is_sorted([1, 3, 2, 4])
        False
    """
    for index in range(len(values) - 1):
        if values[index] > values[index + 1]:
            return False
    return True

def bogo_sort(values: list) -> list:
    """
    Sort a list using the highly inefficient bogo sort algorithm.
    Randomly shuffles the list until it happens to be sorted.

    Args:
        values (list): List to be sorted

    Returns:
        list: Sorted list (eventually...)

    Time Complexity: O(n × n!) average case
    Space Complexity: O(1)

    Warning:
        This is an extremely inefficient sorting algorithm used only
        for educational purposes. Do not use in production code.

    Example:
        >>> bogo_sort([3, 1, 2])
        [1, 2, 3]
    """
    attempts = 0
    while not is_sorted(values):
        print(f"Attempt {attempts}")
        random.shuffle(values)
        attempts += 1
    return values

if __name__ == "__main__":
    # Test implementation
    test_list = [3, 1, 4, 1, 5]
    print("Original list:", test_list)
    sorted_list = bogo_sort(test_list.copy())
    print("Sorted list:", sorted_list)
