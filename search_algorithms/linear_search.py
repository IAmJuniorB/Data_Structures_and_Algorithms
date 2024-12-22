def linear_search(list: list, target: int) -> int|None:
    """
    Perform a linear search to find the index of a target element in a list.

    Args:
        list (list): A list of elements to search through
        target (int): The element to search for in the list

    Returns:
        int|None: The index of the target element if found, None if not found

    Time Complexity: O(n) - must check each element in worst case
    Space Complexity: O(1) - only uses a single variable for iteration

    Example:
        >>> linear_search([1, 2, 3, 4, 5], 3)
        2
        >>> linear_search([1, 2, 3, 4, 5], 6)
        None

    Note:
        - Does not require the input list to be sorted
        - Searches elements sequentially until target is found
    """
    for i in range(len(list)):
        if list[i] == target:
            return i
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
    # Test implementation
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Test case 1: Finding an existing number
    result = linear_search(numbers, 8)
    verify(result)
    
    # Test case 2: Finding a non-existent number
    result = linear_search(numbers, 12)
    verify(result)
