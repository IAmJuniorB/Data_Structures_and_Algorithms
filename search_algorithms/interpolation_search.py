def interpolation_search(arr: list, target: int) -> int:
    """
    Perform interpolation search to find the index of a target element.

    Args:
        arr (list): Sorted list to search through
        target (int): Element to find

    Returns:
        int: Index of target if found, -1 if not found

    Time Complexity: 
        - Average case: O(log(log n))
        - Worst case: O(n)
    Space Complexity: O(1)

    Example:
        >>> interpolation_search([1, 2, 4, 6, 8, 10, 12, 14, 16, 18], 10)
        5
    """
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1

        pos = low + ((high - low) * (target - arr[low]) // 
                    (arr[high] - arr[low]))

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1

def verify_search(arr: list, target: int) -> None:
    """
    Verify if the search function works correctly.

    Args:
        arr (list): List to search through
        target (int): Element to find

    Time Complexity: Same as interpolation_search
    Space Complexity: O(1)
    """
    index = interpolation_search(arr, target)
    if index != -1:
        print(f"Element {target} found at index: {index}")
    else:
        print(f"Element {target} not found in list")

if __name__ == "__main__":
    test_list = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    
    verify_search(test_list, 10)
    verify_search(test_list, 14)
    
    verify_search([], 5) 
    verify_search([1], 1) 
    verify_search(test_list, 5)
