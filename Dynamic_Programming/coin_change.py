from typing import List, Tuple, Dict, Optional, NamedTuple
import time
from collections import defaultdict


class CoinChangeResult(NamedTuple):
    """Result of coin change optimization containing minimum coins and solution.
    
    Attributes:
        min_coins (int): Minimum number of coins needed (-1 if impossible).
        coins_used (List[int]): List of coin denominations used in optimal solution.
        coin_counts (Dict[int, int]): Count of each coin denomination used.
    """
    min_coins: int
    coins_used: List[int]
    coin_counts: Dict[int, int]


def coin_change_recursive(coins: List[int], amount: int) -> int:
    """Find minimum coins needed using naive recursion.
    
    This is the most straightforward but inefficient approach with exponential time complexity.
    For each amount, we try every coin and take the minimum.
    
    Args:
        coins (List[int]): Available coin denominations.
        amount (int): Target amount to make change for.
        
    Returns:
        int: Minimum number of coins needed, or -1 if impossible.
        
    Raises:
        ValueError: If amount is negative or coins list is invalid.
        
    Time Complexity: O(amount^coins) exponential
    Space Complexity: O(amount) due to recursion stack
    """
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    if not coins or any(coin <= 0 for coin in coins):
        raise ValueError("Invalid coin denominations")
    
    # Base cases
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    
    min_coins = float('inf')
    
    # Try each coin
    for coin in coins:
        if coin <= amount:
            sub_result = coin_change_recursive(coins, amount - coin)
            if sub_result != -1:
                min_coins = min(min_coins, sub_result + 1)
    
    return min_coins if min_coins != float('inf') else -1


def coin_change_memoization(
    coins: List[int], 
    amount: int, 
    memo: Dict[int, int] = None
) -> int:
    """Find minimum coins needed using memoization (top-down DP).
    
    This approach caches subproblem results to avoid redundant calculations.
    
    Args:
        coins (List[int]): Available coin denominations.
        amount (int): Target amount to make change for.
        memo (Dict[int, int]): Memoization cache. Defaults to None.
        
    Returns:
        int: Minimum number of coins needed, or -1 if impossible.
        
    Raises:
        ValueError: If amount is negative or coins list is invalid.
        
    Time Complexity: O(amount * len(coins))
    Space Complexity: O(amount) for memoization table + recursion stack
    """
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    if not coins or any(coin <= 0 for coin in coins):
        raise ValueError("Invalid coin denominations")
    
    if memo is None:
        memo = {}
    
    # Base cases
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    
    # Check if already computed
    if amount in memo:
        return memo[amount]
    
    min_coins = float('inf')
    
    # Try each coin
    for coin in coins:
        if coin <= amount:
            sub_result = coin_change_memoization(coins, amount - coin, memo)
            if sub_result != -1:
                min_coins = min(min_coins, sub_result + 1)
    
    memo[amount] = min_coins if min_coins != float('inf') else -1
    return memo[amount]


def coin_change_tabulation(coins: List[int], amount: int) -> int:
    """Find minimum coins needed using tabulation (bottom-up DP).
    
    This approach builds up the solution iteratively using a 1D DP array.
    dp[i] represents minimum coins needed to make amount i.
    
    Args:
        coins (List[int]): Available coin denominations.
        amount (int): Target amount to make change for.
        
    Returns:
        int: Minimum number of coins needed, or -1 if impossible.
        
    Raises:
        ValueError: If amount is negative or coins list is invalid.
        
    Time Complexity: O(amount * len(coins))
    Space Complexity: O(amount) for the DP array
    """
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    if not coins or any(coin <= 0 for coin in coins):
        raise ValueError("Invalid coin denominations")
    
    if amount == 0:
        return 0
    
    # Initialize DP array: dp[i] = min coins for amount i
    dp: List[int] = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed for amount 0
    
    # Fill DP array bottom-up
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1


def coin_change_with_solution(coins: List[int], amount: int) -> CoinChangeResult:
    """Find minimum coins and return the actual coins used.
    
    Uses tabulation approach and backtracks to find which coins were used.
    
    Args:
        coins (List[int]): Available coin denominations.
        amount (int): Target amount to make change for.
        
    Returns:
        CoinChangeResult: Contains min coins, coins used, and coin counts.
        
    Raises:
        ValueError: If amount is negative or coins list is invalid.
        
    Time Complexity: O(amount * len(coins))
    Space Complexity: O(amount) for DP array and parent tracking
    """
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    if not coins or any(coin <= 0 for coin in coins):
        raise ValueError("Invalid coin denominations")
    
    if amount == 0:
        return CoinChangeResult(0, [], {})
    
    # DP array and parent tracking for reconstruction
    dp: List[int] = [float('inf')] * (amount + 1)
    parent: List[int] = [-1] * (amount + 1)  # Track which coin was used
    dp[0] = 0
    
    # Fill DP array and track parents
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] != float('inf'):
                if dp[i - coin] + 1 < dp[i]:
                    dp[i] = dp[i - coin] + 1
                    parent[i] = coin
    
    if dp[amount] == float('inf'):
        return CoinChangeResult(-1, [], {})
    
    # Backtrack to find coins used
    coins_used: List[int] = []
    coin_counts: Dict[int, int] = defaultdict(int)
    current_amount = amount
    
    while current_amount > 0:
        coin_used = parent[current_amount]
        coins_used.append(coin_used)
        coin_counts[coin_used] += 1
        current_amount -= coin_used
    
    return CoinChangeResult(dp[amount], coins_used, dict(coin_counts))


def coin_change_ways_count(coins: List[int], amount: int) -> int:
    """Count the number of ways to make change for given amount.
    
    This is a different variant: instead of minimum coins, count all possible ways.
    
    Args:
        coins (List[int]): Available coin denominations.
        amount (int): Target amount to make change for.
        
    Returns:
        int: Number of different ways to make the amount.
        
    Raises:
        ValueError: If amount is negative or coins list is invalid.
        
    Time Complexity: O(amount * len(coins))
    Space Complexity: O(amount) for the DP array
    """
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    if not coins or any(coin <= 0 for coin in coins):
        raise ValueError("Invalid coin denominations")
    
    # dp[i] = number of ways to make amount i
    dp: List[int] = [0] * (amount + 1)
    dp[0] = 1  # One way to make amount 0: use no coins
    
    # For each coin, update all amounts that can be made
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    
    return dp[amount]


def coin_change_ways_count_with_order(coins: List[int], amount: int) -> int:
    """Count ways to make change considering order of coins (permutations).
    
    This variant treats [1,2] and [2,1] as different ways.
    
    Args:
        coins (List[int]): Available coin denominations.
        amount (int): Target amount to make change for.
        
    Returns:
        int: Number of different ordered ways to make the amount.
        
    Time Complexity: O(amount * len(coins))
    Space Complexity: O(amount) for the DP array
    """
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    if not coins or any(coin <= 0 for coin in coins):
        raise ValueError("Invalid coin denominations")
    
    # dp[i] = number of ordered ways to make amount i
    dp: List[int] = [0] * (amount + 1)
    dp[0] = 1  # One way to make amount 0
    
    # For each amount, try all coins
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] += dp[i - coin]
    
    return dp[i]


def coin_change_unlimited_vs_limited(
    coins: List[int], 
    amounts: List[int], 
    amount: int
) -> Tuple[int, List[int]]:
    """Solve coin change with limited quantities of each coin.
    
    Args:
        coins (List[int]): Available coin denominations.
        amounts (List[int]): Available quantity for each coin denomination.
        amount (int): Target amount to make change for.
        
    Returns:
        Tuple[int, List[int]]: (min_coins, coins_used) or (-1, []) if impossible.
        
    Time Complexity: O(amount * sum(amounts))
    Space Complexity: O(amount)
    """
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    if len(coins) != len(amounts):
        raise ValueError("Coins and amounts lists must have same length")
    
    if amount == 0:
        return 0, []
    
    # DP with state: dp[i] = min coins to make amount i
    dp: List[int] = [float('inf')] * (amount + 1)
    parent: List[Tuple[int, int]] = [(-1, -1)] * (amount + 1)  # (coin_value, count_used)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin_idx, coin in enumerate(coins):
            max_count = min(amounts[coin_idx], i // coin)
            
            for count in range(1, max_count + 1):
                cost = coin * count
                if cost <= i and dp[i - cost] != float('inf'):
                    if dp[i - cost] + count < dp[i]:
                        dp[i] = dp[i - cost] + count
                        parent[i] = (coin, count)
    
    if dp[amount] == float('inf'):
        return -1, []
    
    # Reconstruct solution
    coins_used: List[int] = []
    current = amount
    
    while current > 0:
        coin_val, count = parent[current]
        coins_used.extend([coin_val] * count)
        current -= coin_val * count
    
    return dp[amount], coins_used


def print_coin_change_solution(result: CoinChangeResult, amount: int) -> None:
    """Pretty print the coin change solution.
    
    Args:
        result (CoinChangeResult): The result from coin change optimization.
        amount (int): The target amount.
    """
    if result.min_coins == -1:
        print(f"No solution possible for amount {amount}")
        return
    
    print(f"Amount: ${amount}")
    print(f"Minimum coins needed: {result.min_coins}")
    print(f"Coins used: {sorted(result.coins_used, reverse=True)}")
    print("Coin breakdown:")
    
    for coin, count in sorted(result.coin_counts.items(), reverse=True):
        total_value = coin * count
        print(f"  ${coin} × {count} = ${total_value}")


def make_change_greedy(coins: List[int], amount: int) -> Tuple[int, List[int]]:
    """Make change using greedy algorithm (may not be optimal).
    
    For comparison with DP solution. Only optimal for certain coin systems.
    
    Args:
        coins (List[int]): Available coin denominations (should be sorted desc).
        amount (int): Target amount to make change for.
        
    Returns:
        Tuple[int, List[int]]: (num_coins, coins_used) or (-1, []) if impossible.
    """
    if amount < 0:
        return -1, []
    if amount == 0:
        return 0, []
    
    coins_sorted = sorted(coins, reverse=True)
    coins_used: List[int] = []
    remaining = amount
    
    for coin in coins_sorted:
        while remaining >= coin:
            coins_used.append(coin)
            remaining -= coin
    
    if remaining == 0:
        return len(coins_used), coins_used
    else:
        return -1, []


def benchmark_coin_change_methods(coins: List[int], amount: int) -> None:
    """Benchmark different coin change solution methods.
    
    Args:
        coins (List[int]): Available coin denominations.
        amount (int): Target amount.
    """
    methods = [
        ("Tabulation", coin_change_tabulation),
        ("Memoization", coin_change_memoization),
    ]
    
    # Only include recursive method for small amounts
    if amount <= 50:
        methods.append(("Recursive", coin_change_recursive))
    
    print(f"Benchmarking Coin Change (Amount: {amount}, Coins: {coins})")
    print("-" * 60)
    
    for method_name, method_func in methods:
        start_time = time.time()
        result = method_func(coins, amount)
        end_time = time.time()
        
        print(f"{method_name:12}: {result:3} coins | Time: {end_time - start_time:.6f}s")
    
    # Compare with greedy
    start_time = time.time()
    greedy_result, _ = make_change_greedy(coins, amount)
    end_time = time.time()
    print(f"{'Greedy':12}: {greedy_result:3} coins | Time: {end_time - start_time:.6f}s")


# Example usage and testing
if __name__ == "__main__":
    print("Coin Change Problem Examples")
    print("=" * 50)
    
    # US currency example
    us_coins = [1, 5, 10, 25]  # penny, nickel, dime, quarter
    amount1 = 67
    
    print("Example 1: US Currency")
    print("-" * 30)
    result1 = coin_change_with_solution(us_coins, amount1)
    print_coin_change_solution(result1, amount1)
    
    # Compare with greedy
    greedy_coins, greedy_used = make_change_greedy(us_coins, amount1)
    print(f"\nGreedy algorithm: {greedy_coins} coins")
    print(f"Greedy coins used: {sorted(greedy_used, reverse=True)}")
    print()
    
    # Non-standard currency where greedy fails
    weird_coins = [1, 3, 4]
    amount2 = 6
    
    print("Example 2: Non-standard Currency (Greedy vs DP)")
    print("-" * 45)
    result2 = coin_change_with_solution(weird_coins, amount2)
    print_coin_change_solution(result2, amount2)
    
    greedy_coins2, greedy_used2 = make_change_greedy(weird_coins, amount2)
    print(f"\nGreedy algorithm: {greedy_coins2} coins")
    print(f"Greedy coins used: {sorted(greedy_used2, reverse=True) if greedy_used2 else 'No solution'}")
    print("Note: DP finds optimal solution, greedy doesn't!")
    print()
    
    # Count ways example
    print("Example 3: Count Number of Ways")
    print("-" * 30)
    coins3 = [1, 2, 5]
    amount3 = 5
    
    ways_unordered = coin_change_ways_count(coins3, amount3)
    ways_ordered = coin_change_ways_count_with_order(coins3, amount3)
    
    print(f"Amount: {amount3}, Coins: {coins3}")
    print(f"Ways (combinations): {ways_unordered}")
    print(f"Ways (permutations): {ways_ordered}")
    print()
    
    # Limited quantities example
    print("Example 4: Limited Coin Quantities")
    print("-" * 35)
    limited_coins = [1, 5, 10, 25]
    limited_amounts = [3, 2, 1, 1]  # 3 pennies, 2 nickels, 1 dime, 1 quarter
    amount4 = 40
    
    min_coins, coins_used = coin_change_unlimited_vs_limited(
        limited_coins, limited_amounts, amount4
    )
    
    print(f"Available: {dict(zip(limited_coins, limited_amounts))}")
    print(f"Amount: {amount4}")
    if min_coins != -1:
        print(f"Solution: {min_coins} coins")
        print(f"Coins used: {sorted(coins_used, reverse=True)}")
    else:
        print("No solution possible with limited quantities")
    print()
    
    print("Performance Comparison:")
    benchmark_coin_change_methods(us_coins, 100)
