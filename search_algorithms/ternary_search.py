def ternary_search(arr: list, target: int) -> int|None:
    """
    Perform a ternary search to find the index of a target element.

    Args:
        arr (list): Sorted list to search through
        target (int): Element to find

    Returns:
        int|None: Index of target if found, None if not found

    Time Complexity: O(log₃ n)
    Space Complexity: O(1)

    Example:
        >>> ternary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 6)
        5
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        # Find two mid points or, you know, try at least.
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2

        if target < arr[mid1]:
            right = mid1 - 1
        elif target > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1

    return None

def verify(index: int|None) -> None:
    """
    Print the result of a search operation.

    Args:
        index (int|None): The index where target was found, or None if not found

    Example:
        >>> verify(3)
        Target found at index: 3
        >>> verify(None)
        Target not found
    """
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found")

if __name__ == "__main__":
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # You know we be testing around here
    print("Testing regular cases:")
    verify(ternary_search(test_list, 6))
    verify(ternary_search(test_list, 1))
    verify(ternary_search(test_list, 10))
    
    print("\nTesting edge cases:")
    verify(ternary_search([], 5))  
    verify(ternary_search([1], 1)) 
    verify(ternary_search(test_list, 11))  