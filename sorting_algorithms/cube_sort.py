def cube_sort(values: list) -> list:
    """
    Sort a list using the cube sort algorithm.

    Args:
        values (list): The list of numbers to be sorted

    Returns:
        list: The sorted list

    Time Complexity: 
        - Best case: O(n)
        - Average case: O(n log n)
        - Worst case: O(n log n)
    Space Complexity: O(n)

    Example:
        >>> cube_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
    """
    if len(values) <= 1:
        return values

    # Sub cube time
    n = len(values)
    cube_size = int(pow(n, 1/3)) + 1
    cubes = [[] for _ in range(cube_size)]

    for i in range(n):
        cube_index = i % cube_size
        cubes[cube_index].append(values[i])

    for cube in cubes:
        cube.sort()

    result = []
    while any(cubes):
        min_val = float('inf')
        min_cube_index = 0
        
        # Finding the small guy
        for i, cube in enumerate(cubes):
            if cube and cube[0] < min_val:
                min_val = cube[0]
                min_cube_index = i
        
        result.append(cubes[min_cube_index].pop(0))
        
    return result

def verify_sort(values: list) -> None:
    """
    Verify if the sorting function works correctly.

    Args:
        values (list): List of numbers to be sorted

    Time Complexity: Same as cube_sort
    Space Complexity: O(n) for creating copy
    """
    original = values.copy()
    sorted_list = cube_sort(values)
    print(f"Original list: {original}")
    print(f"Sorted list: {sorted_list}")

if __name__ == "__main__":
    test_numbers = [64, 34, 25, 12, 22, 11, 90]
    verify_sort(test_numbers)
    
    # You want tests? We've got em.
    print("\nTesting edge cases:")
    print("Empty list:", cube_sort([]))
    print("Single element:", cube_sort([1]))
    print("Two elements:", cube_sort([2, 1]))
    print("Already sorted:", cube_sort([1, 2, 3, 4, 5]))
    print("Reverse sorted:", cube_sort([5, 4, 3, 2, 1]))
    print("Duplicate elements:", cube_sort([3, 3, 3, 1, 2, 2]))
