from typing import List, Tuple, Optional, Dict, NamedTuple
import time
from enum import Enum


class LCSDirection(Enum):
    """Enum representing directions in LCS backtracking table."""
    DIAGONAL = "↖"  # Match/mismatch
    UP = "↑"        # Deletion from sequence 1
    LEFT = "←"      # Insertion to sequence 1


class LCSResult(NamedTuple):
    """Result of LCS computation containing length, subsequence, and alignment info.
    
    Attributes:
        length (int): Length of the longest common subsequence.
        subsequence (str): The actual LCS string.
        sequence1_indices (List[int]): Indices of LCS characters in sequence 1.
        sequence2_indices (List[int]): Indices of LCS characters in sequence 2.
    """
    length: int
    subsequence: str
    sequence1_indices: List[int]
    sequence2_indices: List[int]


def lcs_recursive(seq1: str, seq2: str, i: int = None, j: int = None) -> int:
    """Find length of LCS using naive recursion.
    
    This is the most straightforward but inefficient approach with exponential time complexity.
    For each position, we have three choices: match, skip from seq1, or skip from seq2.
    
    Args:
        seq1 (str): First sequence.
        seq2 (str): Second sequence.
        i (int, optional): Current index in seq1. Defaults to len(seq1)-1.
        j (int, optional): Current index in seq2. Defaults to len(seq2)-1.
        
    Returns:
        int: Length of the longest common subsequence.
        
    Time Complexity: O(2^(m+n)) where m, n are sequence lengths
    Space Complexity: O(m+n) due to recursion stack
    """
    if i is None:
        i = len(seq1) - 1
    if j is None:
        j = len(seq2) - 1
    
    # Base case: either sequence is exhausted
    if i < 0 or j < 0:
        return 0
    
    # If characters match, include in LCS
    if seq1[i] == seq2[j]:
        return 1 + lcs_recursive(seq1, seq2, i - 1, j - 1)
    
    # If characters don't match, try both possibilities
    return max(
        lcs_recursive(seq1, seq2, i - 1, j),  # Skip character from seq1
        lcs_recursive(seq1, seq2, i, j - 1)   # Skip character from seq2
    )


def lcs_memoization(
    seq1: str, 
    seq2: str, 
    i: int = None, 
    j: int = None, 
    memo: Dict[Tuple[int, int], int] = None
) -> int:
    """Find length of LCS using memoization (top-down DP).
    
    This approach caches subproblem results to avoid redundant calculations.
    
    Args:
        seq1 (str): First sequence.
        seq2 (str): Second sequence.
        i (int, optional): Current index in seq1. Defaults to len(seq1)-1.
        j (int, optional): Current index in seq2. Defaults to len(seq2)-1.
        memo (Dict[Tuple[int, int], int]): Memoization cache. Defaults to None.
        
    Returns:
        int: Length of the longest common subsequence.
        
    Time Complexity: O(m * n) where m, n are sequence lengths
    Space Complexity: O(m * n) for memoization table + O(m+n) for recursion stack
    """
    if i is None:
        i = len(seq1) - 1
    if j is None:
        j = len(seq2) - 1
    if memo is None:
        memo = {}
    
    # Base case: either sequence is exhausted
    if i < 0 or j < 0:
        return 0
    
    # Check if result already computed
    state = (i, j)
    if state in memo:
        return memo[state]
    
    # If characters match, include in LCS
    if seq1[i] == seq2[j]:
        result = 1 + lcs_memoization(seq1, seq2, i - 1, j - 1, memo)
    else:
        # If characters don't match, try both possibilities
        result = max(
            lcs_memoization(seq1, seq2, i - 1, j, memo),    # Skip from seq1
            lcs_memoization(seq1, seq2, i, j - 1, memo)     # Skip from seq2
        )
    
    memo[state] = result
    return result


def lcs_tabulation(seq1: str, seq2: str) -> int:
    """Find length of LCS using tabulation (bottom-up DP).
    
    This approach builds up the solution iteratively using a 2D DP table.
    dp[i][j] represents LCS length of seq1[0:i] and seq2[0:j].
    
    Args:
        seq1 (str): First sequence.
        seq2 (str): Second sequence.
        
    Returns:
        int: Length of the longest common subsequence.
        
    Time Complexity: O(m * n) where m, n are sequence lengths
    Space Complexity: O(m * n) for the DP table
    """
    m, n = len(seq1), len(seq2)
    
    # Create DP table: dp[i][j] = LCS length of seq1[0:i] and seq2[0:j]
    dp: List[List[int]] = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    # Fill the DP table bottom-up
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                # Characters match: add 1 to diagonal value
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # Characters don't match: take maximum from left or top
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]


def lcs_space_optimized(seq1: str, seq2: str) -> int:
    """Find length of LCS with space-optimized tabulation.
    
    Uses only two rows instead of full DP table since we only need the previous row.
    
    Args:
        seq1 (str): First sequence.
        seq2 (str): Second sequence.
        
    Returns:
        int: Length of the longest common subsequence.
        
    Time Complexity: O(m * n) where m, n are sequence lengths
    Space Complexity: O(min(m, n)) - only two arrays
    """
    m, n = len(seq1), len(seq2)
    
    # Optimize by making the shorter sequence the column dimension
    if m > n:
        seq1, seq2 = seq2, seq1
        m, n = n, m
    
    # Use two arrays: previous row and current row
    prev: List[int] = [0] * (m + 1)
    curr: List[int] = [0] * (m + 1)
    
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if seq1[i - 1] == seq2[j - 1]:
                curr[i] = prev[i - 1] + 1
            else:
                curr[i] = max(prev[i], curr[i - 1])
        
        # Swap arrays for next iteration
        prev, curr = curr, prev
    
    return prev[m]


def lcs_with_subsequence(seq1: str, seq2: str) -> LCSResult:
    """Find LCS and return both length and the actual subsequence with indices.
    
    Uses tabulation approach and backtracks to construct the actual LCS.
    
    Args:
        seq1 (str): First sequence.
        seq2 (str): Second sequence.
        
    Returns:
        LCSResult: Contains length, subsequence, and character indices.
        
    Time Complexity: O(m * n) where m, n are sequence lengths
    Space Complexity: O(m * n) for the DP table
    """
    m, n = len(seq1), len(seq2)
    
    # Create DP table
    dp: List[List[int]] = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Backtrack to construct the LCS
    lcs_chars: List[str] = []
    seq1_indices: List[int] = []
    seq2_indices: List[int] = []
    
    i, j = m, n
    while i > 0 and j > 0:
        if seq1[i - 1] == seq2[j - 1]:
            # Characters match: part of LCS
            lcs_chars.append(seq1[i - 1])
            seq1_indices.append(i - 1)
            seq2_indices.append(j - 1)
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            # Move up
            i -= 1
        else:
            # Move left
            j -= 1
    
    # Reverse to get correct order
    lcs_chars.reverse()
    seq1_indices.reverse()
    seq2_indices.reverse()
    
    return LCSResult(
        length=dp[m][n],
        subsequence=''.join(lcs_chars),
        sequence1_indices=seq1_indices,
        sequence2_indices=seq2_indices
    )


def lcs_all_subsequences(seq1: str, seq2: str) -> List[str]:
    """Find all possible longest common subsequences.
    
    Note: This can be exponential in the worst case, so use with caution.
    
    Args:
        seq1 (str): First sequence.
        seq2 (str): Second sequence.
        
    Returns:
        List[str]: All possible LCS strings.
        
    Time Complexity: O(m * n * 2^(m+n)) in worst case
    Space Complexity: O(m * n) for the DP table
    """
    m, n = len(seq1), len(seq2)
    
    # First, build the DP table
    dp: List[List[int]] = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Recursive function to generate all LCS
    def generate_all_lcs(i: int, j: int) -> List[str]:
        if i == 0 or j == 0:
            return [""]
        
        if seq1[i - 1] == seq2[j - 1]:
            # Characters match: extend all LCS from (i-1, j-1)
            prev_lcs = generate_all_lcs(i - 1, j - 1)
            return [lcs + seq1[i - 1] for lcs in prev_lcs]
        
        result = []
        
        # If moving up gives optimal solution
        if dp[i - 1][j] == dp[i][j]:
            result.extend(generate_all_lcs(i - 1, j))
        
        # If moving left gives optimal solution
        if dp[i][j - 1] == dp[i][j]:
            result.extend(generate_all_lcs(i, j - 1))
        
        return list(set(result))  # Remove duplicates
    
    return generate_all_lcs(m, n)


def print_lcs_alignment(seq1: str, seq2: str, result: LCSResult) -> None:
    """Print a visual alignment showing the LCS in both sequences.
    
    Args:
        seq1 (str): First sequence.
        seq2 (str): Second sequence.
        result (LCSResult): LCS computation result.
    """
    print(f"Sequence 1: {seq1}")
    print(f"Sequence 2: {seq2}")
    print(f"LCS:        {result.subsequence} (length: {result.length})")
    print()
    
    # Create alignment visualization
    alignment1 = list(" " * len(seq1))
    alignment2 = list(" " * len(seq2))
    
    for i, (idx1, idx2) in enumerate(zip(result.sequence1_indices, result.sequence2_indices)):
        alignment1[idx1] = seq1[idx1]
        alignment2[idx2] = seq2[idx2]
    
    print("Alignment:")
    print(f"Seq1: {seq1}")
    print(f"      {''.join(alignment1)}")
    print(f"Seq2: {seq2}")
    print(f"      {''.join(alignment2)}")


def lcs_similarity_ratio(seq1: str, seq2: str) -> float:
    """Calculate similarity ratio between two sequences based on LCS.
    
    Args:
        seq1 (str): First sequence.
        seq2 (str): Second sequence.
        
    Returns:
        float: Similarity ratio between 0 and 1.
    """
    if not seq1 and not seq2:
        return 1.0
    
    lcs_length = lcs_tabulation(seq1, seq2)
    max_length = max(len(seq1), len(seq2))
    
    return lcs_length / max_length if max_length > 0 else 0.0


def benchmark_lcs_methods(seq1: str, seq2: str) -> None:
    """Benchmark different LCS solution methods.
    
    Args:
        seq1 (str): First sequence.
        seq2 (str): Second sequence.
    """
    methods = [
        ("Space Optimized", lcs_space_optimized),
        ("Tabulation", lcs_tabulation),
        ("Memoization", lcs_memoization),
    ]
    
    # Only include recursive method for very small sequences
    if len(seq1) <= 15 and len(seq2) <= 15:
        methods.append(("Recursive", lcs_recursive))
    
    print(f"Benchmarking LCS (Lengths: {len(seq1)}, {len(seq2)})")
    print("-" * 50)
    
    for method_name, method_func in methods:
        start_time = time.time()
        result = method_func(seq1, seq2)
        end_time = time.time()
        
        print(f"{method_name:15}: Length {result:3} | Time: {end_time - start_time:.6f}s")


# Example usage and testing
if __name__ == "__main__":
    # DNA sequence example
    dna1 = "AGGTAB"
    dna2 = "GXTXAYB"
    
    print("Longest Common Subsequence (LCS) Examples")
    print("=" * 50)
    
    print("Example 1: DNA Sequences")
    print("-" * 30)
    result1 = lcs_with_subsequence(dna1, dna2)
    print_lcs_alignment(dna1, dna2, result1)
    print(f"Similarity: {lcs_similarity_ratio(dna1, dna2):.2%}")
    print()
    
    # Text comparison example
    text1 = "ABCDGH"
    text2 = "AEDFHR"
    
    print("Example 2: Text Comparison")
    print("-" * 30)
    result2 = lcs_with_subsequence(text1, text2)
    print_lcs_alignment(text1, text2, result2)
    print(f"Similarity: {lcs_similarity_ratio(text1, text2):.2%}")
    print()
    
    # Version control example (simplified)
    old_code = "function hello() { return 'world'; }"
    new_code = "function hello() { return 'Hello World!'; }"
    
    print("Example 3: Code Diff Simulation")
    print("-" * 30)
    result3 = lcs_with_subsequence(old_code, new_code)
    print(f"Common characters: {result3.length}/{max(len(old_code), len(new_code))}")
    print(f"Similarity: {lcs_similarity_ratio(old_code, new_code):.2%}")
    print()
    
    # All possible LCS example
    short1 = "ABC"
    short2 = "BAC"
    print("Example 4: All Possible LCS")
    print("-" * 30)
    all_lcs = lcs_all_subsequences(short1, short2)
    print(f"Sequences: {short1}, {short2}")
    print(f"All LCS: {all_lcs}")
    print()
    
    print("Performance Comparison:")
    benchmark_lcs_methods(dna1, dna2)
