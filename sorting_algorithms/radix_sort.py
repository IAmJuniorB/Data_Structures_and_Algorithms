def counting_sort_for_radix(arr: list, exp: int) -> None:
    """
    Helper function for radix sort that sorts digits at a specific place value.

    Args:
        arr (list): The list to be sorted
        exp (int): Place value (1, 10, 100, etc.)

    Time Complexity: O(n + k) where k is range of digits (10)
    Space Complexity: O(n)
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # How many times did this ish occur
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    # Gotta build an entire output array, but what do they do?
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(values: list) -> list:
    """
    Sort a list using the radix sort algorithm.

    Args:
        values (list): The list of numbers to be sorted

    Returns:
        list: The sorted list (modified in-place)

    Time Complexity: O(d * (n + k)) where:
        - n is the number of elements
        - k is the range of each digit (10 for decimal)
        - d is the number of digits in maximum element
    Space Complexity: O(n + k)

    Example:
        >>> radix_sort([170, 45, 75, 90, 802, 24, 2, 66])
        [2, 24, 45, 66, 75, 90, 170, 802]
    """
    if not values:
        return values

    max_num = max(values)

    # Gotta do a counting sort for every digit...Ikr
    exp = 1
    while max_num // exp > 0:
        counting_sort_for_radix(values, exp)
        exp *= 10

    return values

def verify_sort(values: list) -> None:
    """
    Verify if the sorting function works correctly.

    Args:
        values (list): List of numbers to be sorted

    Time Complexity: Same as radix_sort
    Space Complexity: O(n) for creating copy
    """
    original = values.copy()
    sorted_list = radix_sort(values)
    print(f"Original list: {original}")
    print(f"Sorted list: {sorted_list}")

if __name__ == "__main__":
    test_numbers = [170, 45, 75, 90, 802, 24, 2, 66]
    verify_sort(test_numbers)
    
    # These tests are rad dude
    print("\nTesting edge cases:")
    print("Empty list:", radix_sort([]))
    print("Single element:", radix_sort([1]))
    print("Two elements:", radix_sort([2, 1]))
    print("Already sorted:", radix_sort([1, 2, 3, 4, 5]))
    print("Reverse sorted:", radix_sort([5, 4, 3, 2, 1]))
    print("Duplicate elements:", radix_sort([3, 3, 3, 1, 2, 2]))
