"""
Recursive Binary Search
Does not run in constant time like an iterative binary search.
Creates a new list for every loop where the function calls itself though it the list is decreased by half
The space complexity is considered O(log n)
Time complexity of O(log n)
"""

def recursive_binary_search(list: list, target: int):
    """
    Perform a binary search using recursion to determine if a target element exists in a sorted list.

    Args:
        list (list): A sorted list of elements to search through.
        target: The element to search for in the list.

    Returns:
        bool: True if the target element is found, False otherwise.

    Example:
        >>> recursive_binary_search([1, 2, 3, 4, 5], 3)
        True
        >>> recursive_binary_search([1, 2, 3, 4, 5], 6)
        False

    Note:
        - This implementation uses slicing to create new sublists, which can increase memory usage for large lists.
        - The input list must be sorted in ascending order for the search to work correctly.
        - The time complexity of this algorithm is O(log n), but due to slicing, the space complexity increases to O(n) for each recursive call.
    """
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list)) // 2
        
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint + 1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)

def verify(result: bool):
    """
    Print the result of the binary search operation.

    Args:
        result (bool): The result of the search operation (True if the target was found, False otherwise).

    Example:
        >>> verify(True)
        Target found: True
        >>> verify(False)
        Target found: False
    """
    print("Target found: ", result)
    
numbers = [1,2,3,4,5,6,7,8,9,10]

result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 6)
verify(result)