def calculate_z_array(string: str) -> list:
    """
    Calculate Z array for pattern matching.

    Args:
        string (str): String to analyze

    Returns:
        list: Z array where Z[i] is length of longest substring starting from i
             that is also a prefix of string

    Time Complexity: O(n) where n is string length
    Space Complexity: O(n)
    """
    n = len(string)
    z = [0] * n
    # First element is the whole string (duh!)
    left = right = 0

    for i in range(1, n):
        if i > right:
            # Time to do it the old-fashioned way (brute force)
            left = right = i
            while right < n and string[right] == string[right - left]:
                right += 1
            z[i] = right - left
            right -= 1
        else:
            # Being clever and reusing previous work (work smarter, not harder)
            k = i - left
            if z[k] < right - i + 1:
                z[i] = z[k]
            else:
                # Can't be lazy here, gotta do some work
                left = i
                while right < n and string[right] == string[right - left]:
                    right += 1
                z[i] = right - left
                right -= 1

    return z

def z_algorithm_search(text: str, pattern: str) -> list:
    """
    Find all occurrences of pattern in text using Z algorithm.

    Args:
        text (str): Text to search in
        pattern (str): Pattern to search for

    Returns:
        list: List of starting indices where pattern is found

    Time Complexity: O(n + m) where n is text length, m is pattern length
    Space Complexity: O(n + m)

    Example:
        >>> z_algorithm_search("AABAACAADAABAAABAA", "AABA")
        [0, 9, 13]
    """
    if not pattern or not text:
        return []

    # Concatenate pattern and text with a character that won't appear in either
    concat = pattern + "$" + text
    z_array = calculate_z_array(concat)
    results = []

    # Find pattern matches (the moment of truth)
    pattern_length = len(pattern)
    for i in range(len(concat)):
        if z_array[i] == pattern_length:
            results.append(i - pattern_length - 1)

    return [x for x in results if x >= 0]

if __name__ == "__main__":
    # Test implementation
    text = "AABAACAADAABAAABAA"
    pattern = "AABA"
    
    result = z_algorithm_search(text, pattern)
    print(f"Pattern found at indices: {result}")
    
    # Edge cases (because we're professionals... mostly)
    print("\nTesting edge cases:")
    print("Empty text:", z_algorithm_search("", "ABC"))
    print("Empty pattern:", z_algorithm_search("ABC", ""))
    print("Single character:", z_algorithm_search("A", "A"))
    print("Pattern longer than text:", z_algorithm_search("ABC", "ABCD"))
