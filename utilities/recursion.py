"""
Recursion
"""

def sum(numbers: list) -> int:
    """
    Calculate the sum of a list of numbers using recursion.

    Args:
        numbers (list): List of numbers to sum.

    Returns:
        int: The sum of all numbers in the list.

    Time Complexity: O(n)
    Space Complexity: O(n) due to recursive call stack

    Example:
        >>> sum([1, 2, 3, 4])
        10
    """
    if not numbers:
        return 0
    
    remaining_sum = sum(numbers[1:])
    total = numbers[0] + remaining_sum
    
    print(f"Call to sum({numbers}) returning {numbers[0]} + {remaining_sum}")
    return total

if __name__ == "__main__":
    test_numbers = [1, 43, 56, 74, 1, 2, 12]
    print(f"Final sum: {sum(test_numbers)}")