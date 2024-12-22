def counting_sort(values: list) -> list:
    """
    Sort a list using the counting sort algorithm.

    Args:
        values (list): The list of numbers to be sorted

    Returns:
        list: A new sorted list containing all elements from the input list

    Time Complexity: O(n + k) where k is the range of input
    Space Complexity: O(k) where k is the range of input

    Example:
        >>> counting_sort([4, 2, 2, 8, 3, 3, 1])
        [1, 2, 2, 3, 3, 4, 8]
    """
    if not values:
        return []

    max_val = max(values)
    min_val = min(values)
    range_of_elements = max_val - min_val + 1

    count = [0] * range_of_elements
    output = [0] * len(values)

    # Store count of each object
    for i in range(len(values)):
        count[values[i] - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(values) - 1, -1, -1):
        output[count[values[i] - min_val] - 1] = values[i]
        count[values[i] - min_val] -= 1

    return output

def verify_sort(values: list) -> None:
    """
    Verify if the sorting function works correctly by printing original and sorted lists.

    Args:
        values (list): List of numbers to be sorted

    Time Complexity: O(n + k)
    Space Complexity: O(n)
    """
    original = values.copy()
    sorted_list = counting_sort(values)
    print(f"Original list: {original}")
    print(f"Sorted list: {sorted_list}")

if __name__ == "__main__":
    test_numbers = [4, 2, 2, 8, 3, 3, 1]
    verify_sort(test_numbers)
    
    # Do the f$%*&^g tests
    print("\nTesting edge cases:")
    print("Empty list:", counting_sort([]))
    print("Single element:", counting_sort([1]))
    print("Two elements:", counting_sort([2, 1]))
    print("Already sorted:", counting_sort([1, 2, 3, 4, 5]))
    print("Reverse sorted:", counting_sort([5, 4, 3, 2, 1]))
    print("Duplicate elements:", counting_sort([3, 3, 3, 1, 2, 2]))
