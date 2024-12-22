def bucket_sort(values: list, bucket_size: int = 10) -> list:
    """
    Sort a list using the bucket sort algorithm.

    Args:
        values (list): The list of numbers to be sorted
        bucket_size (int): Number of buckets to use

    Returns:
        list: The sorted list

    Time Complexity:
        - Average case: O(n + k) where k is the number of buckets
        - Worst case: O(n²) when most elements go to the same bucket
    Space Complexity: O(n + k)

    Example:
        >>> bucket_sort([0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51])
        [0.32, 0.33, 0.37, 0.42, 0.47, 0.51, 0.52]
    """
    if len(values) <= 1:
        return values

    # The buckets have been granted life
    buckets = [[] for _ in range(bucket_size)]
    
    # These buckets have been given souls now
    for value in values:
        index = int(value * bucket_size)
        if index != bucket_size:
            buckets[index].append(value)
        else:
            buckets[bucket_size - 1].append(value)
    
    # Now the buckets can live in a sorted way
    for i in range(bucket_size):
        buckets[i] = sorted(buckets[i])
    
    # Concatenate all buckets into result array
    result = []
    for bucket in buckets:
        result.extend(bucket)
    
    return result

def verify_sort(values: list) -> None:
    """
    Verify if the sorting function works correctly by printing original and sorted lists.

    Args:
        values (list): List of numbers to be sorted

    Time Complexity: Same as bucket_sort
    Space Complexity: O(n) for creating copy
    """
    original = values.copy()
    sorted_list = bucket_sort(values)
    print(f"Original list: {original}")
    print(f"Sorted list: {sorted_list}")

if __name__ == "__main__":
    test_numbers = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
    verify_sort(test_numbers)
    
    # Mic check...1, 2. Mic check 1 and 2.
    print("\nTesting edge cases:")
    print("Empty list:", bucket_sort([]))
    print("Single element:", bucket_sort([0.5]))
    print("Two elements:", bucket_sort([0.9, 0.1]))
    print("Already sorted:", bucket_sort([0.1, 0.2, 0.3, 0.4]))
    print("Reverse sorted:", bucket_sort([0.9, 0.8, 0.7, 0.6]))
