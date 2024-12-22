def merge_sort(list: list) -> list:
    """
    Sort a list in ascending order using the merge sort algorithm.

    Args:
        list (list): The list to be sorted

    Returns:
        list: A new sorted list

    Time Complexity: O(n log n)
    Space Complexity: O(n)

    Example:
        >>> merge_sort([98, 17, 2, 45])
        [2, 17, 45, 98]

    Process:
        1. Divide: Find the midpoint of the list and divide into sublists
        2. Conquer: Recursively sort the sublists created in previous step
        3. Combine: Merge the sorted sublists created in previous step
    """
    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list: list) -> tuple:
    """
    Divide the unsorted list at midpoint into sublists.

    Args:
        list (list): List to be divided

    Returns:
        tuple: Two sublists - left and right

    Time Complexity: O(log n)
    Space Complexity: O(n)

    Example:
        >>> split([1, 2, 3, 4])
        ([1, 2], [3, 4])
    """
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]
    return left, right

def merge(left: list, right: list) -> list:
    """
    Merge two lists, sorting them in the process.

    Args:
        left (list): First sorted list
        right (list): Second sorted list

    Returns:
        list: A new merged sorted list

    Time Complexity: O(n)
    Space Complexity: O(n)

    Example:
        >>> merge([1, 3], [2, 4])
        [1, 2, 3, 4]
    """
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged

def verify_sorted(list: list) -> bool:
    """
    Verify if a list is sorted in ascending order.

    Args:
        list (list): List to verify

    Returns:
        bool: True if sorted, False otherwise

    Time Complexity: O(n)
    Space Complexity: O(n) due to recursion

    Example:
        >>> verify_sorted([1, 2, 3, 4])
        True
    """
    n = len(list)
    if n == 0 or n == 1:
        return True
    return list[0] <= list[1] and verify_sorted(list[1:])

if __name__ == "__main__":
    # Test cases
    test_list = [1, 98, 17, 2, 45, 100, 74, 66, 145, 98, 0, 14, 57]
    print("Original list:", test_list)
    
    sorted_list = merge_sort(test_list)
    print("Sorted list:", sorted_list)
    print("Is sorted:", verify_sorted(sorted_list))

    # Edge cases
    print("\nTesting edge cases:")
    print("Empty list:", merge_sort([]))
    print("Single element:", merge_sort([1]))
    print("Two elements:", merge_sort([2, 1]))
    print("Duplicate elements:", merge_sort([3, 3, 3]))
