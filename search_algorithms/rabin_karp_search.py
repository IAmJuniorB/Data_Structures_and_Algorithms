def rabin_karp_search(text: str, pattern: str, d: int = 256, q: int = 101) -> list:
    """
    Perform Rabin-Karp pattern searching algorithm using rolling hash.

    Args:
        text (str): Text to search in
        pattern (str): Pattern to search for
        d (int): Number of characters in the alphabet
        q (int): A prime number for hash calculation

    Returns:
        list: List of starting indices where pattern is found

    Time Complexity:
        - Average and Best Case: O(n + m)
        - Worst Case: O(nm)
    Space Complexity: O(1)

    Example:
        >>> rabin_karp_search("AABAACAADAABAAABAA", "AABA")
        [0, 9, 13]
    """
    results = []
    M = len(pattern)
    N = len(text)
    
    if M > N or M == 0 or N == 0:
        return results

    # Calculate hash value for pattern and first window
    pattern_hash = 0
    text_hash = 0
    h = pow(d, M-1) % q  # The value of h would be pow(d, M-1) % q

    # Calculate initial hash values like a responsible adult
    for i in range(M):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % q
        text_hash = (d * text_hash + ord(text[i])) % q

    # Time to slide the pattern over text like butter on toast
    for i in range(N - M + 1):
        if pattern_hash == text_hash:
            # Hash match! But let's double-check (trust issues, you know?)
            if text[i:i+M] == pattern:
                results.append(i)

        if i < N - M:
            # Roll the hash forward, because that's how we roll
            text_hash = (d * (text_hash - ord(text[i]) * h) + 
                        ord(text[i + M])) % q
            if text_hash < 0:
                text_hash += q

    return results

if __name__ == "__main__":
    text = "AABAACAADAABAAABAA"
    pattern = "AABA"
    
    result = rabin_karp_search(text, pattern)
    print(f"Pattern found at indices: {result}")
    
    # Edge cases (because we're thorough like that)
    print("\nTesting edge cases:")
    print("Empty text:", rabin_karp_search("", "ABC"))
    print("Empty pattern:", rabin_karp_search("ABC", ""))
    print("Single character:", rabin_karp_search("A", "A"))
    print("Pattern longer than text:", rabin_karp_search("ABC", "ABCD"))
