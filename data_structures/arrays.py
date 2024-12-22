def array_examples():
    """
    Demonstrate Python array (list) operations and characteristics.

    Time Complexity:
        - Access: O(1)
        - Append: O(1) amortized
        - Insert: O(n)
        - Delete: O(n)
        - Search: O(n)
    Space Complexity: O(n)

    Example:
        >>> numbers = []
        >>> numbers.append(10)  # [10]
        >>> numbers.extend([20, 30])  # [10, 20, 30]
    """
    # Demonstrate array creation and heterogeneous data
    new_list = [1, 'Joe', 25, True, 15, 'Bri', [1, 2, 3]]
    print(f"Heterogeneous array: {new_list}")
    
    # Demonstrate array operations
    numbers = []
    print(f"Empty array length: {len(numbers)}")
    
    # Single element append
    numbers.append(10)
    print(f"After append(10): {numbers}")
    
    # Multiple element append
    numbers.append(50)
    numbers.append(60)
    print(f"After multiple appends: {numbers}")
    
    # Extend with multiple elements
    numbers.extend([15, 65, 78])
    print(f"After extend: {numbers}")
    print(f"Final array length: {len(numbers)}")

    # Demonstrate array indexing
    print(f"First element: {numbers[0]}")
    print(f"Last element: {numbers[-1]}")

if __name__ == "__main__":
    # Test implementation
    array_examples()
    
    # Additional array operations demonstration
    test_array = [1, 2, 3, 4, 5]
    print("\nArray operations:")
    print(f"Original array: {test_array}")
    test_array.insert(2, 10)  # Insert 10 at index 2
    print(f"After insert(2, 10): {test_array}")
    test_array.remove(3)  # Remove first occurrence of 3
    print(f"After remove(3): {test_array}")
