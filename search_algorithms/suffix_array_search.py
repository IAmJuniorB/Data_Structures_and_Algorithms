def build_suffix_array(text: str) -> list:
    """
    Build suffix array for a given text.

    Args:
        text (str): Text to build suffix array from

    Returns:
        list: Sorted list of suffix indices

    Time Complexity: O(n log n) where n is text length
    Space Complexity: O(n)
    """
    # Create list of all suffixes and their starting indices
    # (like collecting all possible endings of a story)
    suffixes = [(text[i:], i) for i in range(len(text))]
    
    # Sort suffixes lexicographically (alphabetically, but fancier word)
    suffixes.sort()
    
    # Return just the indices (because that's all we really need)
    return [index for _, index in suffixes]

def suffix_array_search(text: str, pattern: str) -> list:
    """
    Find all occurrences of pattern in text using suffix array.

    Args:
        text (str): Text to search in
        pattern (str): Pattern to search for

    Returns:
        list: List of starting indices where pattern is found

    Time Complexity: O(m log n) where n is text length, m is pattern length
    Space Complexity: O(n)

    Example:
        >>> suffix_array_search("banana", "ana")
        [1, 3]
    """
    if not pattern or not text:
        return []

    # Build suffix array (our trusty search companion)
    suffix_array = build_suffix_array(text)
    
    # Binary search to find pattern (divide and conquer, like a boss)
    left = 0
    right = len(text) - 1
    results = []

    while left <= right:
        mid = (left + right) // 2
        suffix = text[suffix_array[mid]:]
        
        if suffix.startswith(pattern):
            # Found one! Now let's find any siblings
            results.append(suffix_array[mid])
            
            # Check neighbors (cause they be nosey)
            i = mid - 1
            while i >= 0 and text[suffix_array[i]:].startswith(pattern):
                results.append(suffix_array[i])
                i -= 1
                
            i = mid + 1
            while i < len(suffix_array) and text[suffix_array[i]:].startswith(pattern):
                results.append(suffix_array[i])
                i += 1
                
            break
            
        elif pattern < suffix[:len(pattern)]:
            right = mid - 1
        else:
            left = mid + 1

    return sorted(results)

if __name__ == "__main__":
    text = "banana"
    pattern = "ana"
    
    result = suffix_array_search(text, pattern)
    print(f"Pattern '{pattern}' found at indices: {result}")
    
    # Edge cases (because we're thorough like that)
    print("\nTesting edge cases:")
    print("Empty text:", suffix_array_search("", "abc"))
    print("Empty pattern:", suffix_array_search("abc", ""))
    print("Single character:", suffix_array_search("a", "a"))
    print("Pattern longer than text:", suffix_array_search("abc", "abcd"))
