def build_bad_char_table(pattern: str) -> dict:
    """
    Build the bad character table for Boyer-Moore algorithm.

    Args:
        pattern (str): Pattern to analyze

    Returns:
        dict: Table of rightmost occurrences of each character

    Time Complexity: O(m + k) where m is pattern length, k is alphabet size
    Space Complexity: O(k)
    """
    # Dictionary to store the last occurrence of each character
    # (like a character's favorite parking spot)
    table = {}
    
    for i in range(len(pattern)):
        table[pattern[i]] = i
        
    return table

def boyer_moore_search(text: str, pattern: str) -> list:
    """
    Perform Boyer-Moore pattern searching algorithm.

    Args:
        text (str): Text to search in
        pattern (str): Pattern to search for

    Returns:
        list: List of starting indices where pattern is found

    Time Complexity:
        - Best Case: O(n/m)
        - Average Case: O(n)
        - Worst Case: O(nm)
    Space Complexity: O(k) where k is alphabet size

    Example:
        >>> boyer_moore_search("WHICH-FINALLY-HALTS.--AT-THAT-POINT", "AT")
        [14, 23]
    """
    matches = []
    if not pattern or not text:
        return matches

    # Build the bad character table (our cheat sheet)
    bad_char = build_bad_char_table(pattern)
    
    m = len(pattern)
    n = len(text)
    i = m - 1  # Start at the end, because we're rebels

    while i < n:
        # Start matching from the end, like reading the last page first
        j = m - 1
        k = i
        
        while j >= 0 and text[k] == pattern[j]:
            j -= 1
            k -= 1
            
        if j < 0:
            # Found a match! Time to celebrate
            matches.append(k + 1)
            i += 1
        else:
            # Character mismatch, time to make a big jump
            char = text[k]
            skip = j - bad_char.get(char, -1)
            i += max(1, skip)

    return matches

if __name__ == "__main__":
    text = "WHICH-FINALLY-HALTS.--AT-THAT-POINT"
    pattern = "AT"
    
    result = boyer_moore_search(text, pattern)
    print(f"Pattern found at indices: {result}")
    
    # Edge cases (because we're responsible developers)
    print("\nTesting edge cases:")
    print("Empty text:", boyer_moore_search("", "ABC"))
    print("Empty pattern:", boyer_moore_search("ABC", ""))
    print("Single character:", boyer_moore_search("A", "A"))
    print("Pattern longer than text:", boyer_moore_search("ABC", "ABCD"))
