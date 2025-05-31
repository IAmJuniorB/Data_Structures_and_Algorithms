from typing import Dict, List, Tuple
from functools import lru_cache
import time


def fibonacci_naive(n: int) -> int:
    """Calculate the nth Fibonacci number using naive recursion.
    
    This is the most straightforward but inefficient approach with O(2^n) time complexity.
    Included for educational comparison purposes.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed).
        
    Returns:
        int: The nth Fibonacci number.
        
    Raises:
        ValueError: If n is negative.
        
    Time Complexity: O(2^n)
    Space Complexity: O(n) due to recursion stack
    """
    if n < 0:
        raise ValueError("Fibonacci sequence is not defined for negative numbers")
    
    if n <= 1:
        return n
    
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


def fibonacci_memoization(n: int, memo: Dict[int, int] = None) -> int:
    """Calculate the nth Fibonacci number using memoization (top-down DP).
    
    This approach stores previously calculated values to avoid redundant calculations.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed).
        memo (Dict[int, int], optional): Memoization dictionary. Defaults to None.
        
    Returns:
        int: The nth Fibonacci number.
        
    Raises:
        ValueError: If n is negative.
        
    Time Complexity: O(n)
    Space Complexity: O(n) for memo dictionary and recursion stack
    """
    if n < 0:
        raise ValueError("Fibonacci sequence is not defined for negative numbers")
    
    if memo is None:
        memo = {}
    
    # Base cases
    if n <= 1:
        return n
    
    # Check if already computed
    if n in memo:
        return memo[n]
    
    # Compute and store result
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]


@lru_cache(maxsize=None)
def fibonacci_lru_cache(n: int) -> int:
    """Calculate the nth Fibonacci number using Python's built-in LRU cache.
    
    This demonstrates Python's decorator approach to memoization.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed).
        
    Returns:
        int: The nth Fibonacci number.
        
    Raises:
        ValueError: If n is negative.
        
    Time Complexity: O(n)
    Space Complexity: O(n) for cache and recursion stack
    """
    if n < 0:
        raise ValueError("Fibonacci sequence is not defined for negative numbers")
    
    if n <= 1:
        return n
    
    return fibonacci_lru_cache(n - 1) + fibonacci_lru_cache(n - 2)


def fibonacci_tabulation(n: int) -> int:
    """Calculate the nth Fibonacci number using tabulation (bottom-up DP).
    
    This approach builds up the solution iteratively from the base cases.
    Most efficient approach for single calculations.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed).
        
    Returns:
        int: The nth Fibonacci number.
        
    Raises:
        ValueError: If n is negative.
        
    Time Complexity: O(n)
    Space Complexity: O(n) for the DP table
    """
    if n < 0:
        raise ValueError("Fibonacci sequence is not defined for negative numbers")
    
    if n <= 1:
        return n
    
    # Create DP table
    dp: List[int] = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    
    # Fill the table bottom-up
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


def fibonacci_space_optimized(n: int) -> int:
    """Calculate the nth Fibonacci number with optimized space complexity.
    
    This approach only keeps track of the last two values, reducing space complexity to O(1).
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed).
        
    Returns:
        int: The nth Fibonacci number.
        
    Raises:
        ValueError: If n is negative.
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if n < 0:
        raise ValueError("Fibonacci sequence is not defined for negative numbers")
    
    if n <= 1:
        return n
    
    # Only keep track of the last two values
    prev_prev: int = 0  # fib(0)
    prev: int = 1       # fib(1)
    
    for i in range(2, n + 1):
        current: int = prev + prev_prev
        prev_prev = prev
        prev = current
    
    return prev


def fibonacci_sequence_list(n: int) -> List[int]:
    """Generate the first n+1 Fibonacci numbers as a list.
    
    Useful when you need multiple Fibonacci numbers.
    
    Args:
        n (int): Generate Fibonacci numbers from 0 to n (inclusive).
        
    Returns:
        List[int]: List containing Fibonacci numbers from fib(0) to fib(n).
        
    Raises:
        ValueError: If n is negative.
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if n < 0:
        raise ValueError("Fibonacci sequence is not defined for negative numbers")
    
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    
    # Initialize the sequence
    fib_sequence: List[int] = [0, 1]
    
    # Generate remaining numbers
    for i in range(2, n + 1):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    
    return fib_sequence


def benchmark_fibonacci_methods(n: int) -> None:
    """Benchmark different Fibonacci calculation methods.
    
    Compares the performance of different approaches for educational purposes.
    
    Args:
        n (int): The Fibonacci number to calculate.
    """
    methods = [
        ("Space Optimized", fibonacci_space_optimized),
        ("Tabulation", fibonacci_tabulation),
        ("Memoization", fibonacci_memoization),
        ("LRU Cache", fibonacci_lru_cache),
    ]
    
    # Only include naive method for small values to avoid long computation
    if n <= 35:
        methods.append(("Naive Recursion", fibonacci_naive))
    
    print(f"Benchmarking Fibonacci calculation for n = {n}")
    print("-" * 50)
    
    for method_name, method_func in methods:
        start_time = time.time()
        result = method_func(n)
        end_time = time.time()
        
        print(f"{method_name:15}: {result:12} | Time: {end_time - start_time:.6f}s")


# Example usage and testing
if __name__ == "__main__":
    # Test basic functionality
    test_cases: List[int] = [0, 1, 5, 10, 20]
    
    print("Fibonacci Sequence Examples:")
    print("=" * 40)
    
    for n in test_cases:
        result = fibonacci_space_optimized(n)
        print(f"fib({n}) = {result}")
    
    print("\nFirst 15 Fibonacci numbers:")
    sequence = fibonacci_sequence_list(14)
    print(sequence)
    
    print("\nPerformance Comparison:")
    benchmark_fibonacci_methods(30)
