import math

def jump_search(arr: list, target: int) -> int:
    """
    Perform jump search to find the index of a target element.

    Args:
        arr (list): Sorted list to search through
        target (int): Element to find

    Returns:
        int: Index of target if found, -1 if not found

    Time Complexity: O(√n)
    Space Complexity: O(1)

    Example:
        >>> jump_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 6)
        5
    """
    n = len(arr)
    if n == 0:
        return -1

    step = int(math.sqrt(n))
    
    # Searching for the hot block
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Linear search in the block that's been ID'd...The block is hot.
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1

    if arr[prev] == target:
        return prev
    
    return -1

def verify_search(arr: list, target: int) -> None:
    """
    Verify if the search function works correctly.

    Args:
        arr (list): List to search through
        target (int): Element to find

    Time Complexity: O(√n)
    Space Complexity: O(1)
    """
    index = jump_search(arr, target)
    if index != -1:
        print(f"Element {target} found at index: {index}")
    else:
        print(f"Element {target} not found in list")

if __name__ == "__main__":
    test_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    
    verify_search(test_list, 55)
    verify_search(test_list, 89)
    
    verify_search([], 5) 
    verify_search([1], 1) 
    verify_search(test_list, 100)  
