def insertion_sort(values: list) -> list:
    """
    Sort a list using the insertion sort algorithm.

    Args:
        values (list): The list of numbers to be sorted

    Returns:
        list: The sorted list (modified in-place)

    Time Complexity: O(n²) worst and average case, O(n) best case
    Space Complexity: O(1) as it sorts in-place

    Example:
        >>> insertion_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
    """
    for i in range(1, len(values)):
        key = values[i]
        j = i - 1
        while j >= 0 and values[j] > key:
            values[j + 1] = values[j]
            j -= 1
        values[j + 1] = key
    return values

def verify_sort(values: list) -> None:
    """
    Verify if the sorting function works correctly by printing original and sorted lists.

    Args:
        values (list): List of numbers to be sorted

    Time Complexity: O(n²) - same as insertion_sort
    Space Complexity: O(n) for creating copy
    """
    original = values.copy()
    sorted_list = insertion_sort(values)
    print(f"Original list: {original}")
    print(f"Sorted list: {sorted_list}")

if __name__ == "__main__":
    test_numbers = [64, 34, 25, 12, 22, 11, 90]
    verify_sort(test_numbers)
    
    print("\nTesting edge cases:")
    print("Empty list:", insertion_sort([]))
    print("Single element:", insertion_sort([1]))
    print("Two elements:", insertion_sort([2, 1]))
    print("Already sorted:", insertion_sort([1, 2, 3, 4, 5]))
    print("Reverse sorted:", insertion_sort([5, 4, 3, 2, 1]))
    print("Duplicate elements:", insertion_sort([3, 3, 3, 1, 2, 2]))
