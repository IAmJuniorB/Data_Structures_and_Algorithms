def bubble_sort(values: list) -> list:
    """
    Sort a list using the bubble sort algorithm.

    Args:
        values (list): The list of numbers to be sorted

    Returns:
        list: The sorted list (modified in-place)

    Time Complexity: O(n²) for all cases
    Space Complexity: O(1) as it sorts in-place

    Example:
        >>> bubble_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
    """
    n = len(values)
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                swapped = True
        
        if not swapped:
            break
    
    return values

def verify_sort(values: list) -> None:
    """
    Verify if the sorting function works correctly by printing original and sorted lists.

    Args:
        values (list): List of numbers to be sorted

    Time Complexity: O(n²) - same as bubble_sort
    Space Complexity: O(n) for creating copy
    """
    original = values.copy()
    sorted_list = bubble_sort(values)
    print(f"Original list: {original}")
    print(f"Sorted list: {sorted_list}")

if __name__ == "__main__":
    test_numbers = [64, 34, 25, 12, 22, 11, 90]
    verify_sort(test_numbers)
    
    # Gotta test the work
    print("\nTesting edge cases:")
    print("Empty list:", bubble_sort([]))
    print("Single element:", bubble_sort([1]))
    print("Two elements:", bubble_sort([2, 1]))
    print("Already sorted:", bubble_sort([1, 2, 3, 4, 5]))
    print("Reverse sorted:", bubble_sort([5, 4, 3, 2, 1]))
    print("Duplicate elements:", bubble_sort([3, 3, 3, 1, 2, 2]))
