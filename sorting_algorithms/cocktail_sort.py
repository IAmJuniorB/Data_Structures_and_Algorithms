"""
Cocktail Sort
"""

def cocktail_sort(values: list) -> list:
    """
    Sort a list using the cocktail sort algorithm.

    Args:
        values (list): The list of numbers to be sorted

    Returns:
        list: The sorted list (modified in-place)

    Time Complexity: O(n²)
    Space Complexity: O(1)

    Example:
        >>> cocktail_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
    """
    n = len(values)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False

        # Forward pass 
        for i in range(start, end):
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]
                swapped = True

        if not swapped:
            break

        end -= 1
        swapped = False

        # Backward pass
        for i in range(end - 1, start - 1, -1):
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]
                swapped = True

        start += 1

    return values
