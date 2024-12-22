def load_numbers(file_name: str) -> list:
    """
    Load numbers from a file into a list.

    Args:
        file_name (str): Path to the file containing numbers

    Returns:
        list: List of integers read from the file

    Raises:
        FileNotFoundError: If the file doesn't exist
        ValueError: If file contains non-integer values

    Example:
        >>> numbers = load_numbers('numbers.txt')
        >>> print(numbers[:5])
        [1, 2, 3, 4, 5]
    """
    numbers = []
    with open(file_name) as f:
        for line in f:
            numbers.append(int(line))
    return numbers

def load_strings(file_name: str) -> list:
    """
    Load strings from a file into a list.

    Args:
        file_name (str): Path to the file containing strings

    Returns:
        list: List of strings with whitespace removed

    Raises:
        FileNotFoundError: If the file doesn't exist

    Example:
        >>> strings = load_strings('words.txt')
        >>> print(strings[:3])
        ['apple', 'banana', 'cherry']
    """
    strings = []
    with open(file_name) as f:
        for line in f:
            strings.append(line.rstrip())
    return strings

# Test implementation
if __name__ == "__main__":
    try:
        numbers = load_numbers("numbers.txt")
        print(f"First 5 numbers: {numbers[:5]}")
        
        strings = load_strings("strings.txt")
        print(f"First 5 strings: {strings[:5]}")
    except FileNotFoundError:
        print("Test files not found")
