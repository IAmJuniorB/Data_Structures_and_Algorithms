def fibonacci_search(arr: list, target: int) -> int:
    """
    Perform fibonacci search to find the index of a target element.

    Args:
        arr (list): Sorted list to search through
        target (int): Element to find

    Returns:
        int: Index of target if found, -1 if not found

    Time Complexity: O(log n)
    Space Complexity: O(1)

    Example:
        >>> fibonacci_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 6)
        5
    """
    if not arr:
        return -1

    fib2 = 0  
    fib1 = 1  
    fib = fib1 + fib2 

    # smallest Fibonacci number greater than or equal to len(arr)
    while fib < len(arr):
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2

    offset = -1

    while fib > 1:
        # Check if fib2 is a valid location or an imaginary place
        i = min(offset + fib2, len(arr) - 1)

        if arr[i] < target:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif arr[i] > target:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return i

    if fib1 and offset < len(arr) - 1 and arr[offset + 1] == target:
        return offset + 1

    return -1

def verify_search(arr: list, target: int) -> None:
    """
    Verify if the search function works correctly.

    Args:
        arr (list): List to search through
        target (int): Element to find

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    index = fibonacci_search(arr, target)
    if index != -1:
        print(f"Element {target} found at index: {index}")
    else:
        print(f"Element {target} not found in list")

if __name__ == "__main__":
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    
    verify_search(test_list, 6)
    verify_search(test_list, 11)
    
    verify_search([], 5) 
    verify_search([1], 1) 
    verify_search(test_list, 12)  
    verify_search(test_list, 1) 
    verify_search(test_list, 11) 
