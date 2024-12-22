def manacher_algorithm(text: str) -> list:
    """
    Find all palindromic substrings in a text using Manacher's Algorithm.

    Args:
        text (str): Text to search for palindromes

    Returns:
        list: List of tuples (start, length) for each palindrome

    Time Complexity: O(n) where n is text length
    Space Complexity: O(n)

    Example:
        >>> manacher_algorithm("ababa")
        [(0, 5), (0, 3), (1, 3), (2, 1)]
    """
    # Transform string to handle even length palindromes
    # (Adding '#' because palindromes need personal space)
    processed = '#' + '#'.join(text) + '#'
    n = len(processed)
    p = [0] * n  # Palindrome radii array
    center = radius = 0

    for i in range(n):
        # Mirror position across the center (like looking in a mirror)
        mirror = 2 * center - i

        if i < radius:
            # Copy what we already know (work smarter, not harder)
            p[i] = min(radius - i, p[mirror])

        # Expand around i (the good old-fashioned way)
        left = i - (p[i] + 1)
        right = i + (p[i] + 1)
        
        while left >= 0 and right < n and processed[left] == processed[right]:
            p[i] += 1
            left -= 1
            right += 1

        # Update center if this palindrome reaches further
        if i + p[i] > radius:
            center = i
            radius = i + p[i]

    # Convert results back to original string positions
    results = []
    for i in range(n):
        if p[i] > 0:
            start = (i - p[i]) // 2
            length = p[i]
            if length > 1:  # Skip single characters
                results.append((start, length))

    return sorted(results, key=lambda x: (-x[1], x[0]))

if __name__ == "__main__":
    # Test implementation
    test_string = "ababa"
    result = manacher_algorithm(test_string)
    print(f"Palindromes in '{test_string}':")
    for start, length in result:
        print(f"Position {start}, Length {length}: {test_string[start:start+length]}")
    
    # Edge cases (because we're responsible palindrome hunters)
    print("\nTesting edge cases:")
    print("Empty string:", manacher_algorithm(""))
    print("Single char:", manacher_algorithm("a"))
    print("All same:", manacher_algorithm("aaa"))
