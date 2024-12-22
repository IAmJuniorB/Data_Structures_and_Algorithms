def insertion_sort(arr: list, left: int, right: int) -> None:
    """
    Sort a small portion of the array using insertion sort.

    Args:
        arr (list): Array to be sorted
        left (int): Left boundary of subarray
        right (int): Right boundary of subarray

    Time Complexity: O(n²) worst case, O(n) for nearly sorted arrays
    Space Complexity: O(1)
    """
    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = i - 1
        while j >= left and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item

def merge(arr: list, l: int, m: int, r: int) -> None:
    """
    Merge two sorted subarrays.

    Args:
        arr (list): Array containing subarrays to merge
        l (int): Start of first subarray
        m (int): End of first subarray
        r (int): End of second subarray

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    left = arr[l:m + 1]
    right = arr[m + 1:r + 1]
    i = j = 0
    k = l

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1

    while j < len(right):
        arr[k] = right[j]
        k += 1
        j += 1

def timsort(arr: list) -> list:
    """
    Sort array using TimSort algorithm.

    Args:
        arr (list): Array to be sorted

    Returns:
        list: Sorted array

    Time Complexity:
        - Best case: O(n) for already sorted arrays
        - Average/Worst case: O(n log n)
    Space Complexity: O(n)

    Example:
        >>> timsort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
    """
    min_run = 32
    n = len(arr)

    # Create runs of minimum length
    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i + min_run - 1), n - 1))

    # Merge runs
    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))
            if midpoint < end:
                merge(arr, start, midpoint, end)
        size *= 2

    return arr

if __name__ == "__main__":
    test_numbers = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", test_numbers)
    sorted_array = timsort(test_numbers.copy())
    print("Sorted array:", sorted_array)

    print("\nTesting edge cases:")
    print("Empty list:", timsort([]))
    print("Single element:", timsort([1]))
    print("Two elements:", timsort([2, 1]))
    print("Already sorted:", timsort([1, 2, 3, 4, 5]))
    print("Reverse sorted:", timsort([5, 4, 3, 2, 1]))
    print("Duplicate elements:", timsort([3, 3, 3, 1, 2, 2]))
