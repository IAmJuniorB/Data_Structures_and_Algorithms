"""
KMP
"""
def compute_lps(pattern: str) -> list:
    """
    Compute Longest Proper Prefix which is also Suffix array.
    
    Args:
        pattern (str): Pattern to analyze
    
    Returns:
        list: LPS array
        
    Time Complexity: O(m) where m is pattern length
    Space Complexity: O(m)
    """
    m = len(pattern)
    lps = [0] * m  # Like a pattern diary, but with numbers
    
    # The pattern's self-discovery journey begins here
    length = 0  # Length of previous longest prefix suffix
    i = 1
    
    while i < m:
        if pattern[i] == pattern[length]:
            # Hey, we found a match! Party time!
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                # Backtracking like we forgot something
                length = lps[length - 1]
            else:
                # Nothing matches, just like my socks
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text: str, pattern: str) -> list:
    """
    Perform KMP pattern searching algorithm.

    Args:
        text (str): Text to search in
        pattern (str): Pattern to search for

    Returns:
        list: List of starting indices where pattern is found

    Time Complexity: O(n + m) where n is text length, m is pattern length
    Space Complexity: O(m)

    Example:
        >>> kmp_search("AABAACAADAABAAABAA", "AABA")
        [0, 9, 13]
    """
    if not pattern or not text:
        return []

    # First, let's get that LPS array (it's like a cheat sheet)
    lps = compute_lps(pattern)
    matches = []
    
    # Time to play hide and seek with our pattern
    i = 0  # Text index (the hiding spot)
    j = 0  # Pattern index (the seeker)
    
    while i < len(text):
        if pattern[j] == text[i]:
            # They match! It's like finding matching socks
            i += 1
            j += 1
        
        if j == len(pattern):
            # Found the whole pattern! Achievement unlocked!
            matches.append(i - j)
            j = lps[j - 1]
        
        elif i < len(text) and pattern[j] != text[i]:
            # Mismatch! Back to the drawing board
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
                
    return matches

if __name__ == "__main__":
    # Test implementation (or as I like to call it, "The Moment of Truth")
    text = "AABAACAADAABAAABAA"
    pattern = "AABA"
    
    result = kmp_search(text, pattern)
    print(f"Pattern found at indices: {result}")
    
    # Edge cases (because we're responsible adults)
    print("\nTesting edge cases:")
    print("Empty text:", kmp_search("", "ABC"))
    print("Empty pattern:", kmp_search("ABC", ""))
    print("Single character:", kmp_search("A", "A"))
    print("Pattern longer than text:", kmp_search("ABC", "ABCD"))
