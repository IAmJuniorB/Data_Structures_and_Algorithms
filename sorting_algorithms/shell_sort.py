def shell_sort(values: list) -> list:
    """
    Sort a list using the Shell sort algorithm with gap sequence n/2.

    Args:
        values (list): The list of numbers to be sorted

    Returns:
        list: The sorted list (modified in-place)

    Time Complexity: 
        - Best case: O(n log n)
        - Average case: O(n log n)
        - Worst case: O(n²)
    Space Complexity: O(1) as it sorts in-place

    Example:
        >>> shell_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
    """
    n = len(values)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = values[i]
            j = i

            while j >= gap and values[j - gap] > temp:
                values[j] = values[j - gap]
                j -= gap

            values[j] = temp
        gap //= 2

    return values

def verify_sort(values: list) -> None:
    """
    Verify if the sorting function works correctly by printing original and sorted lists.

    Args:
        values (list): List of numbers to be sorted

    Time Complexity: Same as shell_sort
    Space Complexity: O(n) for creating copy
    """
    original = values.copy()
    sorted_list = shell_sort(values)
    print(f"Original list: {original}")
    print(f"Sorted list: {sorted_list}")

if __name__ == "__main__":
    test_numbers = [64, 34, 25, 12, 22, 11, 90]
    verify_sort(test_numbers)
    
    # Testing...COMMENCE
    print("\nTesting edge cases:")
    print("Empty list:", shell_sort([]))
    print("Single element:", shell_sort([1]))
    print("Two elements:", shell_sort([2, 1]))
    print("Already sorted:", shell_sort([1, 2, 3, 4, 5]))
    print("Reverse sorted:", shell_sort([5, 4, 3, 2, 1]))
    print("Duplicate elements:", shell_sort([3, 3, 3, 1, 2, 2]))
