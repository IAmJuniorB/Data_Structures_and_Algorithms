def binary_search(list: list, target: int) -> int|None:
    """
    Perform a binary search to find the index of a target element in a sorted list.

    Args:
        list (list): A sorted list of elements to search through
        target (int): The element to search for in the list

    Returns:
        int|None: The index of the target element if found, None if not found

    Time Complexity: 
        - Best Case: O(1) - target is at midpoint
        - Average Case: O(log n)
        - Worst Case: O(log n)
    Space Complexity: O(1)

    Example:
        >>> binary_search([1, 2, 3, 4, 5], 3)
        2
        >>> binary_search([1, 2, 3, 4, 5], 6)
        None

    Note:
        This function assumes the input list is sorted in ascending order
    """
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2
        
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
            
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
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Testing
    result = binary_search(numbers, 6)
    verify(result)
    
    result = binary_search(numbers, 12)
    verify(result)
