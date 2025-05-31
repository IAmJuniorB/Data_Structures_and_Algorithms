from typing import List, Tuple, Optional, NamedTuple
import time
from enum import Enum


class SubarrayResult(NamedTuple):
    """Result of maximum subarray computation with detailed information.
    
    Attributes:
        max_sum (int): Maximum sum of the subarray.
        start_index (int): Starting index of the maximum subarray.
        end_index (int): Ending index of the maximum subarray.
        subarray (List[int]): The actual maximum subarray elements.
    """
    max_sum: int
    start_index: int
    end_index: int
    subarray: List[int]


class SubarrayVariant(Enum):
    """Enum representing different subarray problem variants."""
    STANDARD = "Standard (allow empty if all negative)"
    NO_EMPTY = "No empty subarray allowed"
    CIRCULAR = "Circular array (wraparound allowed)"


def max_subarray_brute_force(arr: List[int]) -> int:
    """Find maximum subarray sum using brute force approach.
    
    This is the naive O(n²) approach that checks every possible subarray.
    Included for educational comparison and verification purposes.
    
    Args:
        arr (List[int]): Input array of integers.
        
    Returns:
        int: Maximum sum of any contiguous subarray.
        
    Raises:
        ValueError: If array is empty.
        
    Time Complexity: O(n²) where n is array length
    Space Complexity: O(1)
    """
    if not arr:
        raise ValueError("Array cannot be empty")
    
    max_sum = float('-inf')
    n = len(arr)
    
    # Check every possible subarray
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            max_sum = max(max_sum, current_sum)
    
    return max_sum


def kadane_algorithm_basic(arr: List[int]) -> int:
    """Find maximum subarray sum using Kadane's algorithm (basic version).
    
    This is the classic implementation of Kadane's algorithm that efficiently
    finds the maximum sum of any contiguous subarray in linear time.
    
    The algorithm maintains two variables:
    - max_ending_here: Maximum sum ending at current position
    - max_so_far: Maximum sum seen so far
    
    Args:
        arr (List[int]): Input array of integers.
        
    Returns:
        int: Maximum sum of any contiguous subarray.
        
    Raises:
        ValueError: If array is empty.
        
    Time Complexity: O(n) where n is array length
    Space Complexity: O(1)
    
    Applications:
    - Stock trading: Maximum profit from buy/sell operations
    - Gaming: Maximum score in consecutive moves
    - Signal processing: Finding strongest signal segments
    - Financial analysis: Maximum consecutive profit periods
    """
    if not arr:
        raise ValueError("Array cannot be empty")
    
    max_ending_here = arr[0]  # Maximum sum ending at current position
    max_so_far = arr[0]       # Maximum sum seen so far
    
    # Iterate through array starting from second element
    for i in range(1, len(arr)):
        # Either extend previous subarray or start new one
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        # Update global maximum if current is better
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far


def kadane_algorithm_with_indices(arr: List[int]) -> SubarrayResult:
    """Find maximum subarray sum and return indices and actual subarray.
    
    Enhanced version of Kadane's algorithm that tracks the start and end
    indices of the maximum subarray, allowing reconstruction of the solution.
    
    Args:
        arr (List[int]): Input array of integers.
        
    Returns:
        SubarrayResult: Contains max sum, indices, and actual subarray.
        
    Raises:
        ValueError: If array is empty.
        
    Time Complexity: O(n) where n is array length
    Space Complexity: O(k) where k is length of max subarray for result storage
    """
    if not arr:
        raise ValueError("Array cannot be empty")
    
    max_ending_here = arr[0]
    max_so_far = arr[0]
    
    # Track indices for the maximum subarray
    start = 0          # Start of current subarray being considered
    end = 0            # End of maximum subarray found so far
    temp_start = 0     # Temporary start for current subarray
    
    for i in range(1, len(arr)):
        # If starting fresh gives better sum, update temp_start
        if arr[i] > max_ending_here + arr[i]:
            max_ending_here = arr[i]
            temp_start = i
        else:
            max_ending_here = max_ending_here + arr[i]
        
        # Update global maximum and indices if current is better
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = temp_start
            end = i
    
    # Extract the actual subarray
    subarray = arr[start:end + 1]
    
    return SubarrayResult(max_so_far, start, end, subarray)


def kadane_all_negative_handling(arr: List[int], allow_empty: bool = True) -> int:
    """Kadane's algorithm with proper handling of all-negative arrays.
    
    Standard Kadane's algorithm handles the case where all elements are negative
    by either returning 0 (empty subarray) or the maximum element.
    
    Args:
        arr (List[int]): Input array of integers.
        allow_empty (bool): If True, return 0 for all-negative arrays.
                           If False, return the maximum element. Defaults to True.
        
    Returns:
        int: Maximum sum of any contiguous subarray.
        
    Raises:
        ValueError: If array is empty.
        
    Time Complexity: O(n) where n is array length
    Space Complexity: O(1)
    """
    if not arr:
        raise ValueError("Array cannot be empty")
    
    # Check if all elements are negative
    if all(x < 0 for x in arr):
        if allow_empty:
            return 0  # Empty subarray has sum 0
        else:
            return max(arr)  # Return least negative element
    
    # Standard Kadane's algorithm for mixed positive/negative
    max_ending_here = 0  # Can start with 0 since we allow empty subarray
    max_so_far = 0
    
    for num in arr:
        max_ending_here = max(0, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far


def max_subarray_circular(arr: List[int]) -> int:
    """Find maximum subarray sum in a circular array.
    
    In a circular array, elements wrap around, so we need to consider:
    1. Normal maximum subarray (non-circular)
    2. Maximum circular subarray = Total sum - Minimum subarray
    
    Args:
        arr (List[int]): Input array of integers.
        
    Returns:
        int: Maximum sum of any contiguous subarray (including circular).
        
    Raises:
        ValueError: If array is empty.
        
    Time Complexity: O(n) where n is array length
    Space Complexity: O(1)
    
    Applications:
    - Circular race tracks: Maximum consecutive lap scores
    - Time series: Patterns that wrap around (daily/weekly cycles)
    - Ring buffers: Maximum consecutive data segments
    """
    if not arr:
        raise ValueError("Array cannot be empty")
    
    def kadane_max(nums: List[int]) -> int:
        """Standard Kadane's for maximum subarray."""
        max_ending = nums[0]
        max_so_far = nums[0]
        for i in range(1, len(nums)):
            max_ending = max(nums[i], max_ending + nums[i])
            max_so_far = max(max_so_far, max_ending)
        return max_so_far
    
    def kadane_min(nums: List[int]) -> int:
        """Modified Kadane's for minimum subarray."""
        min_ending = nums[0]
        min_so_far = nums[0]
        for i in range(1, len(nums)):
            min_ending = min(nums[i], min_ending + nums[i])
            min_so_far = min(min_so_far, min_ending)
        return min_so_far
    
    # Case 1: Maximum subarray is non-circular
    max_kadane = kadane_max(arr)
    
    # Case 2: Maximum subarray is circular
    # Circular max = Total sum - Minimum subarray
    total_sum = sum(arr)
    min_kadane = kadane_min(arr)
    max_circular = total_sum - min_kadane
    
    # Handle edge case: if all elements are negative,
    # max_circular would be 0 (empty array), so return max_kadane
    if max_circular == 0:
        return max_kadane
    
    return max(max_kadane, max_circular)


def max_subarray_k_elements(arr: List[int], k: int) -> int:
    """Find maximum sum of exactly k consecutive elements.
    
    This is a variant where we must select exactly k elements.
    Uses sliding window technique for efficiency.
    
    Args:
        arr (List[int]): Input array of integers.
        k (int): Number of consecutive elements to select.
        
    Returns:
        int: Maximum sum of exactly k consecutive elements.
        
    Raises:
        ValueError: If array is empty or k is invalid.
        
    Time Complexity: O(n) where n is array length
    Space Complexity: O(1)
    """
    if not arr:
        raise ValueError("Array cannot be empty")
    if k <= 0 or k > len(arr):
        raise ValueError(f"k must be between 1 and {len(arr)}")
    
    # Calculate sum of first k elements
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window
    for i in range(k, len(arr)):
        # Remove leftmost element, add rightmost element
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum


def max_subarray_with_at_most_k_zeros(arr: List[int], k: int) -> SubarrayResult:
    """Find maximum subarray sum with at most k zeros allowed.
    
    This variant allows zeros in the subarray but limits their count.
    Uses sliding window with two pointers.
    
    Args:
        arr (List[int]): Input array of integers.
        k (int): Maximum number of zeros allowed in subarray.
        
    Returns:
        SubarrayResult: Contains max sum, indices, and actual subarray.
        
    Raises:
        ValueError: If array is empty or k is negative.
        
    Time Complexity: O(n) where n is array length
    Space Complexity: O(k) for result storage
    """
    if not arr:
        raise ValueError("Array cannot be empty")
    if k < 0:
        raise ValueError("k cannot be negative")
    
    left = 0
    zero_count = 0
    current_sum = 0
    max_sum = float('-inf')
    best_left, best_right = 0, 0
    
    for right in range(len(arr)):
        # Expand window
        current_sum += arr[right]
        if arr[right] == 0:
            zero_count += 1
        
        # Contract window if too many zeros
        while zero_count > k:
            if arr[left] == 0:
                zero_count -= 1
            current_sum -= arr[left]
            left += 1
        
        # Update maximum
        if current_sum > max_sum:
            max_sum = current_sum
            best_left, best_right = left, right
    
    subarray = arr[best_left:best_right + 1]
    return SubarrayResult(max_sum, best_left, best_right, subarray)


def stock_trading_max_profit(prices: List[int]) -> Tuple[int, int, int]:
    """Apply Kadane's algorithm to stock trading problem.
    
    Find the maximum profit from buying and selling a stock once.
    This is equivalent to finding maximum subarray in price differences.
    
    Args:
        prices (List[int]): Daily stock prices.
        
    Returns:
        Tuple[int, int, int]: (max_profit, buy_day, sell_day)
        
    Raises:
        ValueError: If prices list is empty or has less than 2 elements.
        
    Time Complexity: O(n) where n is number of days
    Space Complexity: O(1)
    
    Real-world Application:
    - Stock trading: When to buy and sell for maximum profit
    - Currency exchange: Optimal exchange timing
    - Resource planning: Buy low, sell high scenarios
    """
    if len(prices) < 2:
        raise ValueError("Need at least 2 prices for trading")
    
    # Convert to profit/loss array (daily changes)
    changes = [prices[i] - prices[i-1] for i in range(1, len(prices))]
    
    # Apply Kadane's algorithm to find maximum profit sequence
    max_ending_here = changes[0]
    max_so_far = changes[0]
    
    start = 0
    end = 0
    temp_start = 0
    
    for i in range(1, len(changes)):
        if changes[i] > max_ending_here + changes[i]:
            max_ending_here = changes[i]
            temp_start = i
        else:
            max_ending_here = max_ending_here + changes[i]
        
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = temp_start
            end = i
    
    # Convert back to original indices (buy day, sell day)
    buy_day = start  # Day before the start of profitable sequence
    sell_day = end + 1  # Last day of profitable sequence
    
    max_profit = max(0, max_so_far)  # Can't have negative profit (don't trade)
    
    return max_profit, buy_day, sell_day


def gaming_max_score(scores: List[int]) -> SubarrayResult:
    """Find maximum consecutive gaming score using Kadane's algorithm.
    
    In gaming, you want to find the sequence of moves that gives maximum score.
    Negative scores represent penalties or losses.
    
    Args:
        scores (List[int]): Scores for each move/level.
        
    Returns:
        SubarrayResult: Contains max score, move indices, and move sequence.
        
    Applications:
    - Video games: Best sequence of moves/levels
    - Sports: Best consecutive performance period
    - Academic: Best consecutive test scores
    """
    if not scores:
        return SubarrayResult(0, 0, 0, [])
    
    return kadane_algorithm_with_indices(scores)


def print_subarray_result(result: SubarrayResult, title: str = "Maximum Subarray") -> None:
    """Pretty print subarray result with detailed information.
    
    Args:
        result (SubarrayResult): Result from subarray computation.
        title (str): Title for the output. Defaults to "Maximum Subarray".
    """
    print(f"{title}")
    print("-" * len(title))
    print(f"Maximum Sum: {result.max_sum}")
    print(f"Start Index: {result.start_index}")
    print(f"End Index: {result.end_index}")
    print(f"Subarray: {result.subarray}")
    print(f"Length: {len(result.subarray)}")


def benchmark_subarray_methods(arr: List[int]) -> None:
    """Benchmark different maximum subarray solution methods.
    
    Args:
        arr (List[int]): Input array for benchmarking.
    """
    methods = [
        ("Kadane's Algorithm", kadane_algorithm_basic),
        ("All Negative Handling", lambda x: kadane_all_negative_handling(x, False)),
    ]
    
    # Only include brute force for small arrays
    if len(arr) <= 1000:
        methods.append(("Brute Force", max_subarray_brute_force))
    
    print(f"Benchmarking Maximum Subarray (Array Length: {len(arr)})")
    print("-" * 55)
    
    for method_name, method_func in methods:
        start_time = time.time()
        result = method_func(arr)
        end_time = time.time()
        
        print(f"{method_name:20}: Sum {result:6} | Time: {end_time - start_time:.6f}s")


# Example usage and testing
if __name__ == "__main__":
    print("Maximum Subarray Problem - Kadane's Algorithm")
    print("=" * 50)
    
    # Classic example from literature
    classic_array = [-2, -3, 4, -1, -2, 1, 5, -3]
    
    print("Example 1: Classic Maximum Subarray")
    print("-" * 35)
    print(f"Array: {classic_array}")
    result1 = kadane_algorithm_with_indices(classic_array)
    print_subarray_result(result1)
    
    # Compare with brute force
    brute_result = max_subarray_brute_force(classic_array)
    print(f"Brute Force Verification: {brute_result}")
    print(f"Results Match: {result1.max_sum == brute_result}")
    print()
    
    # Stock trading example
    stock_prices = [7, 1, 5, 3, 6, 4]
    
    print("Example 2: Stock Trading Application")
    print("-" * 35)
    print(f"Stock Prices: {stock_prices}")
    max_profit, buy_day, sell_day = stock_trading_max_profit(stock_prices)
    print(f"Maximum Profit: ${max_profit}")
    print(f"Buy on day {buy_day} (price: ${stock_prices[buy_day]})")
    print(f"Sell on day {sell_day} (price: ${stock_prices[sell_day]})")
    print()
    
    # Gaming score example
    game_scores = [3, -2, 5, -1, 2, -3, 4, -2]
    
    print("Example 3: Gaming Score Application")
    print("-" * 35)
    print(f"Level Scores: {game_scores}")
    game_result = gaming_max_score(game_scores)
    print_subarray_result(game_result, "Best Gaming Sequence")
    print()
    
    # Circular array example
    circular_array = [5, -3, 5]
    
    print("Example 4: Circular Array Maximum")
    print("-" * 35)
    print(f"Circular Array: {circular_array}")
    normal_max = kadane_algorithm_basic(circular_array)
    circular_max = max_subarray_circular(circular_array)
    print(f"Normal Maximum: {normal_max}")
    print(f"Circular Maximum: {circular_max}")
    print(f"Circular is better: {circular_max > normal_max}")
    print()
    
    # All negative array handling
    negative_array = [-5, -2, -8, -1]
    
    print("Example 5: All Negative Array Handling")
    print("-" * 40)
    print(f"All Negative Array: {negative_array}")
    empty_allowed = kadane_all_negative_handling(negative_array, allow_empty=True)
    no_empty = kadane_all_negative_handling(negative_array, allow_empty=False)
    print(f"Allow Empty Subarray: {empty_allowed}")
    print(f"No Empty Subarray: {no_empty}")
    print()
    
    # Fixed size subarray
    k_elements = 3
    k_array = [2, 1, -3, 4, -1, 2, 1, -5, 4]
    
    print(f"Example 6: Maximum Sum of Exactly {k_elements} Elements")
    print("-" * 45)
    print(f"Array: {k_array}")
    k_max = max_subarray_k_elements(k_array, k_elements)
    print(f"Maximum sum of {k_elements} consecutive elements: {k_max}")
    print()
    
    # Performance comparison
    print("Performance Comparison:")
    large_array = [i % 10 - 5 for i in range(100)]  # Mix of positive and negative
    benchmark_subarray_methods(large_array)
    
    print()
    print("Key Applications of Kadane's Algorithm:")
    print("=" * 45)
    print("• Stock Trading: Maximum profit from buy/sell operations")
    print("• Gaming: Best consecutive performance periods")
    print("• Signal Processing: Strongest consecutive signal segments")
    print("• Financial Analysis: Maximum consecutive profit periods")
    print("• Image Processing: Finding bright regions in scans")
    print("• Time Series: Detecting trending periods in data")
    print("• Resource Allocation: Optimal consecutive resource usage")
    print("• Bioinformatics: Finding significant gene sequences")
