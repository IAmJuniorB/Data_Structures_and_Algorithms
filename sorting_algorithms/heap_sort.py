def heapify(arr: list, n: int, i: int) -> None:
    """
    Heapify subtree rooted at index i.

    Args:
        arr (list): The array to heapify
        n (int): Size of the heap
        i (int): Root index of the subtree

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(values: list) -> list:
    """
    Sort a list using the heap sort algorithm.

    Args:
        values (list): The list of numbers to be sorted

    Returns:
        list: The sorted list (modified in-place)

    Time Complexity: O(n log n) for all cases
    Space Complexity: O(1) as it sorts in-place

    Example:
        >>> heap_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
    """
    n = len(values)

    # Lets heapify to the max
    for i in range(n // 2 - 1, -1, -1):
        heapify(values, n, i)

    # Extraction...one...by...one...
    for i in range(n - 1, 0, -1):
        values[0], values[i] = values[i], values[0]
        heapify(values, i, 0)

    return values

def verify_sort(values: list) -> None:
    """
    Verify if the sorting function works correctly by printing original and sorted lists.

    Args:
        values (list): List of numbers to be sorted

    Time Complexity: O(n log n) - same as heap_sort
    Space Complexity: O(n) for creating copy
    """
    original = values.copy()
    sorted_list = heap_sort(values)
    print(f"Original list: {original}")
    print(f"Sorted list: {sorted_list}")

if __name__ == "__main__":
    test_numbers = [64, 34, 25, 12, 22, 11, 90]
    verify_sort(test_numbers)
    
    print("\nTesting edge cases:")
    print("Empty list:", heap_sort([]))
    print("Single element:", heap_sort([1]))
    print("Two elements:", heap_sort([2, 1]))
    print("Already sorted:", heap_sort([1, 2, 3, 4, 5]))
    print("Reverse sorted:", heap_sort([5, 4, 3, 2, 1]))
    print("Duplicate elements:", heap_sort([3, 3, 3, 1, 2, 2]))
