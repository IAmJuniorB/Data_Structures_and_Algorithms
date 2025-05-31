from typing import List, Tuple, Dict, Optional, NamedTuple
from enum import Enum
import time


class EditOperation(Enum):
    """Enum representing different edit operations."""
    INSERT = "INSERT"
    DELETE = "DELETE"
    SUBSTITUTE = "SUBSTITUTE"
    MATCH = "MATCH"


class EditStep(NamedTuple):
    """Represents a single edit operation step.
    
    Attributes:
        operation (EditOperation): Type of operation performed.
        char (str): Character involved in the operation.
        position (int): Position in the target string.
        cost (int): Cost of this operation.
    """
    operation: EditOperation
    char: str
    position: int
    cost: int


class EditDistanceResult(NamedTuple):
    """Result of edit distance computation with detailed transformation info.
    
    Attributes:
        distance (int): Minimum edit distance between strings.
        operations (List[EditStep]): Sequence of operations to transform string.
        alignment (Tuple[str, str]): Visual alignment of the two strings.
    """
    distance: int
    operations: List[EditStep]
    alignment: Tuple[str, str]


def edit_distance_recursive(str1: str, str2: str, i: int = None, j: int = None) -> int:
    """Calculate edit distance using naive recursion.
    
    This is the most straightforward but inefficient approach with exponential time complexity.
    For each position, we consider insert, delete, or substitute operations.
    
    Args:
        str1 (str): Source string to transform.
        str2 (str): Target string to transform into.
        i (int, optional): Current index in str1. Defaults to len(str1).
        j (int, optional): Current index in str2. Defaults to len(str2).
        
    Returns:
        int: Minimum edit distance between the strings.
        
    Time Complexity: O(3^(m+n)) where m, n are string lengths
    Space Complexity: O(m+n) due to recursion stack
    """
    if i is None:
        i = len(str1)
    if j is None:
        j = len(str2)
    
    # Base cases: one string is empty
    if i == 0:
        return j  # Insert all characters from str2
    if j == 0:
        return i  # Delete all characters from str1
    
    # If characters match, no operation needed
    if str1[i - 1] == str2[j - 1]:
        return edit_distance_recursive(str1, str2, i - 1, j - 1)
    
    # Try all three operations and take minimum
    insert_cost = 1 + edit_distance_recursive(str1, str2, i, j - 1)
    delete_cost = 1 + edit_distance_recursive(str1, str2, i - 1, j)
    substitute_cost = 1 + edit_distance_recursive(str1, str2, i - 1, j - 1)
    
    return min(insert_cost, delete_cost, substitute_cost)


def edit_distance_memoization(
    str1: str, 
    str2: str, 
    i: int = None, 
    j: int = None, 
    memo: Dict[Tuple[int, int], int] = None
) -> int:
    """Calculate edit distance using memoization (top-down DP).
    
    This approach caches subproblem results to avoid redundant calculations.
    
    Args:
        str1 (str): Source string to transform.
        str2 (str): Target string to transform into.
        i (int, optional): Current index in str1. Defaults to len(str1).
        j (int, optional): Current index in str2. Defaults to len(str2).
        memo (Dict[Tuple[int, int], int]): Memoization cache. Defaults to None.
        
    Returns:
        int: Minimum edit distance between the strings.
        
    Time Complexity: O(m * n) where m, n are string lengths
    Space Complexity: O(m * n) for memoization table + O(m+n) for recursion stack
    """
    if i is None:
        i = len(str1)
    if j is None:
        j = len(str2)
    if memo is None:
        memo = {}
    
    # Base cases
    if i == 0:
        return j
    if j == 0:
        return i
    
    # Check if already computed
    state = (i, j)
    if state in memo:
        return memo[state]
    
    # If characters match, no operation needed
    if str1[i - 1] == str2[j - 1]:
        result = edit_distance_memoization(str1, str2, i - 1, j - 1, memo)
    else:
        # Try all three operations and take minimum
        insert_cost = 1 + edit_distance_memoization(str1, str2, i, j - 1, memo)
        delete_cost = 1 + edit_distance_memoization(str1, str2, i - 1, j, memo)
        substitute_cost = 1 + edit_distance_memoization(str1, str2, i - 1, j - 1, memo)
        
        result = min(insert_cost, delete_cost, substitute_cost)
    
    memo[state] = result
    return result


def edit_distance_tabulation(str1: str, str2: str) -> int:
    """Calculate edit distance using tabulation (bottom-up DP).
    
    This approach builds up the solution iteratively using a 2D DP table.
    dp[i][j] represents edit distance between str1[0:i] and str2[0:j].
    
    Args:
        str1 (str): Source string to transform.
        str2 (str): Target string to transform into.
        
    Returns:
        int: Minimum edit distance between the strings.
        
    Time Complexity: O(m * n) where m, n are string lengths
    Space Complexity: O(m * n) for the DP table
    """
    m, n = len(str1), len(str2)
    
    # Create DP table: dp[i][j] = edit distance of str1[0:i] and str2[0:j]
    dp: List[List[int]] = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i  # Delete all characters from str1
    for j in range(n + 1):
        dp[0][j] = j  # Insert all characters from str2
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                # Characters match: no operation needed
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Take minimum of insert, delete, substitute
                dp[i][j] = 1 + min(
                    dp[i][j - 1],      # Insert
                    dp[i - 1][j],      # Delete
                    dp[i - 1][j - 1]   # Substitute
                )
    
    return dp[m][n]


def edit_distance_space_optimized(str1: str, str2: str) -> int:
    """Calculate edit distance with space-optimized tabulation.
    
    Uses only two rows instead of full DP table since we only need the previous row.
    
    Args:
        str1 (str): Source string to transform.
        str2 (str): Target string to transform into.
        
    Returns:
        int: Minimum edit distance between the strings.
        
    Time Complexity: O(m * n) where m, n are string lengths
    Space Complexity: O(min(m, n)) - only two arrays
    """
    m, n = len(str1), len(str2)
    
    # Optimize by making the shorter string the column dimension
    if m > n:
        str1, str2 = str2, str1
        m, n = n, m
    
    # Use two arrays: previous row and current row
    prev: List[int] = list(range(m + 1))
    curr: List[int] = [0] * (m + 1)
    
    for j in range(1, n + 1):
        curr[0] = j  # Base case for current row
        
        for i in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                curr[i] = prev[i - 1]  # Characters match
            else:
                curr[i] = 1 + min(
                    curr[i - 1],     # Insert
                    prev[i],         # Delete
                    prev[i - 1]      # Substitute
                )
        
        # Swap arrays for next iteration
        prev, curr = curr, prev
    
    return prev[m]


def edit_distance_with_operations(str1: str, str2: str) -> EditDistanceResult:
    """Calculate edit distance and return the sequence of operations.
    
    Uses tabulation approach and backtracks to find the actual edit operations.
    
    Args:
        str1 (str): Source string to transform.
        str2 (str): Target string to transform into.
        
    Returns:
        EditDistanceResult: Contains distance, operations, and alignment.
        
    Time Complexity: O(m * n) where m, n are string lengths
    Space Complexity: O(m * n) for the DP table
    """
    m, n = len(str1), len(str2)
    
    # Create DP table
    dp: List[List[int]] = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i][j - 1],      # Insert
                    dp[i - 1][j],      # Delete
                    dp[i - 1][j - 1]   # Substitute
                )
    
    # Backtrack to find operations
    operations: List[EditStep] = []
    i, j = m, n
    
    while i > 0 or j > 0:
        if i > 0 and j > 0 and str1[i - 1] == str2[j - 1]:
            # Characters match
            operations.append(EditStep(EditOperation.MATCH, str1[i - 1], j - 1, 0))
            i -= 1
            j -= 1
        elif i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + 1:
            # Substitute
            operations.append(EditStep(EditOperation.SUBSTITUTE, str2[j - 1], j - 1, 1))
            i -= 1
            j -= 1
        elif j > 0 and dp[i][j] == dp[i][j - 1] + 1:
            # Insert
            operations.append(EditStep(EditOperation.INSERT, str2[j - 1], j - 1, 1))
            j -= 1
        elif i > 0 and dp[i][j] == dp[i - 1][j] + 1:
            # Delete
            operations.append(EditStep(EditOperation.DELETE, str1[i - 1], i - 1, 1))
            i -= 1
    
    operations.reverse()  # Reverse to get operations in correct order
    
    # Create alignment visualization
    alignment = create_alignment(str1, str2, operations)
    
    return EditDistanceResult(dp[m][n], operations, alignment)


def create_alignment(str1: str, str2: str, operations: List[EditStep]) -> Tuple[str, str]:
    """Create visual alignment strings showing the transformation.
    
    Args:
        str1 (str): Source string.
        str2 (str): Target string.
        operations (List[EditStep]): List of edit operations.
        
    Returns:
        Tuple[str, str]: Aligned strings showing transformation.
    """
    align1: List[str] = []
    align2: List[str] = []
    
    i, j = 0, 0
    
    for op in operations:
        if op.operation == EditOperation.MATCH:
            align1.append(str1[i])
            align2.append(str2[j])
            i += 1
            j += 1
        elif op.operation == EditOperation.SUBSTITUTE:
            align1.append(str1[i])
            align2.append(str2[j])
            i += 1
            j += 1
        elif op.operation == EditOperation.INSERT:
            align1.append('-')
            align2.append(str2[j])
            j += 1
        elif op.operation == EditOperation.DELETE:
            align1.append(str1[i])
            align2.append('-')
            i += 1
    
    return ''.join(align1), ''.join(align2)


def edit_distance_weighted(
    str1: str, 
    str2: str, 
    insert_cost: int = 1, 
    delete_cost: int = 1, 
    substitute_cost: int = 1
) -> int:
    """Calculate edit distance with custom operation costs.
    
    Args:
        str1 (str): Source string to transform.
        str2 (str): Target string to transform into.
        insert_cost (int): Cost of insert operation. Defaults to 1.
        delete_cost (int): Cost of delete operation. Defaults to 1.
        substitute_cost (int): Cost of substitute operation. Defaults to 1.
        
    Returns:
        int: Minimum weighted edit distance.
        
    Time Complexity: O(m * n) where m, n are string lengths
    Space Complexity: O(m * n) for the DP table
    """
    m, n = len(str1), len(str2)
    
    # Create DP table
    dp: List[List[int]] = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    # Initialize base cases with custom costs
    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] + delete_cost
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] + insert_cost
    
    # Fill the DP table with weighted costs
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No cost for match
            else:
                dp[i][j] = min(
                    dp[i][j - 1] + insert_cost,         # Insert
                    dp[i - 1][j] + delete_cost,         # Delete
                    dp[i - 1][j - 1] + substitute_cost  # Substitute
                )
    
    return dp[m][n]


def similarity_ratio(str1: str, str2: str) -> float:
    """Calculate similarity ratio between two strings based on edit distance.
    
    Args:
        str1 (str): First string.
        str2 (str): Second string.
        
    Returns:
        float: Similarity ratio between 0 and 1.
    """
    if not str1 and not str2:
        return 1.0
    
    max_len = max(len(str1), len(str2))
    if max_len == 0:
        return 1.0
    
    distance = edit_distance_tabulation(str1, str2)
    return 1.0 - (distance / max_len)


def spell_check_suggestions(
    word: str, 
    dictionary: List[str], 
    max_distance: int = 2
) -> List[Tuple[str, int]]:
    """Find spell check suggestions using edit distance.
    
    Args:
        word (str): Misspelled word.
        dictionary (List[str]): List of correct words.
        max_distance (int): Maximum edit distance for suggestions. Defaults to 2.
        
    Returns:
        List[Tuple[str, int]]: List of (suggested_word, distance) sorted by distance.
    """
    suggestions: List[Tuple[str, int]] = []
    
    for dict_word in dictionary:
        distance = edit_distance_tabulation(word, dict_word)
        if distance <= max_distance:
            suggestions.append((dict_word, distance))
    
    # Sort by distance, then alphabetically
    suggestions.sort(key=lambda x: (x[1], x[0]))
    return suggestions


def print_edit_operations(result: EditDistanceResult) -> None:
    """Pretty print the edit operations and alignment.
    
    Args:
        result (EditDistanceResult): Result from edit distance computation.
    """
    print(f"Edit Distance: {result.distance}")
    print(f"Number of Operations: {len([op for op in result.operations if op.cost > 0])}")
    print()
    
    print("Operations:")
    print("-" * 40)
    operation_counts = {op.value: 0 for op in EditOperation}
    
    for i, op in enumerate(result.operations, 1):
        if op.operation != EditOperation.MATCH:
            print(f"{i:2}. {op.operation.value:10} '{op.char}' at position {op.position}")
        operation_counts[op.operation.value] += 1
    
    print(f"\nOperation Summary:")
    print(f"Matches: {operation_counts['MATCH']}")
    print(f"Substitutions: {operation_counts['SUBSTITUTE']}")
    print(f"Insertions: {operation_counts['INSERT']}")
    print(f"Deletions: {operation_counts['DELETE']}")
    
    print(f"\nAlignment:")
    print(f"Source: {result.alignment[0]}")
    print(f"Target: {result.alignment[1]}")


def benchmark_edit_distance_methods(str1: str, str2: str) -> None:
    """Benchmark different edit distance solution methods.
    
    Args:
        str1 (str): First string.
        str2 (str): Second string.
    """
    methods = [
        ("Space Optimized", edit_distance_space_optimized),
        ("Tabulation", edit_distance_tabulation),
        ("Memoization", edit_distance_memoization),
    ]
    
    # Only include recursive method for very short strings
    if len(str1) <= 8 and len(str2) <= 8:
        methods.append(("Recursive", edit_distance_recursive))
    
    print(f"Benchmarking Edit Distance (Lengths: {len(str1)}, {len(str2)})")
    print("-" * 55)
    
    for method_name, method_func in methods:
        start_time = time.time()
        result = method_func(str1, str2)
        end_time = time.time()
        
        print(f"{method_name:15}: Distance {result:2} | Time: {end_time - start_time:.6f}s")


# Example usage and testing
if __name__ == "__main__":
    print("Edit Distance (Levenshtein Distance) Examples")
    print("=" * 50)
    
    # Classic example
    word1 = "kitten"
    word2 = "sitting"
    
    print("Example 1: Classic Transformation")
    print("-" * 35)
    print(f"Transform '{word1}' → '{word2}'")
    result1 = edit_distance_with_operations(word1, word2)
    print_edit_operations(result1)
    print(f"Similarity: {similarity_ratio(word1, word2):.2%}")
    print()
    
    # DNA sequence example
    dna1 = "AGCTGAC"
    dna2 = "AGTCGAC"
    
    print("Example 2: DNA Sequence Analysis")
    print("-" * 35)
    print(f"DNA1: {dna1}")
    print(f"DNA2: {dna2}")
    result2 = edit_distance_with_operations(dna1, dna2)
    print_edit_operations(result2)
    print(f"Genetic Similarity: {similarity_ratio(dna1, dna2):.2%}")
    print()
    
    # Spell check example
    print("Example 3: Spell Check Suggestions")
    print("-" * 35)
    misspelled = "recieve"
    dictionary = ["receive", "believe", "achieve", "relieve", "deceive", "retrieve", "perceive"]
    
    suggestions = spell_check_suggestions(misspelled, dictionary, max_distance=2)
    print(f"Misspelled word: '{misspelled}'")
    print("Suggestions:")
    for word, distance in suggestions:
        print(f"  {word} (distance: {distance})")
    print()
    
    # Weighted edit distance example
    print("Example 4: Weighted Edit Distance")
    print("-" * 35)
    text1 = "cat"
    text2 = "dog"
    
    normal_distance = edit_distance_tabulation(text1, text2)
    expensive_substitute = edit_distance_weighted(text1, text2, 1, 1, 3)
    expensive_insert = edit_distance_weighted(text1, text2, 3, 1, 1)
    
    print(f"'{text1}' → '{text2}'")
    print(f"Normal costs (1,1,1): {normal_distance}")
    print(f"Expensive substitute (1,1,3): {expensive_substitute}")
    print(f"Expensive insert (3,1,1): {expensive_insert}")
    print()
    
    print("Performance Comparison:")
    benchmark_edit_distance_methods("intention", "execution")
