from typing import List, Tuple, Dict, NamedTuple
import time


class Item(NamedTuple):
    """Represents an item with weight, value, and optional name.
    
    Attributes:
        weight (int): The weight of the item.
        value (int): The value/profit of the item.
        name (str): Optional name for the item (defaults to empty string).
    """
    weight: int
    value: int
    name: str = ""


class KnapsackResult(NamedTuple):
    """Result of knapsack optimization containing value and selected items.
    
    Attributes:
        max_value (int): Maximum value that can be obtained.
        selected_items (List[Item]): List of items selected for optimal solution.
        total_weight (int): Total weight of selected items.
    """
    max_value: int
    selected_items: List[Item]
    total_weight: int


def knapsack_recursive(items: List[Item], capacity: int, index: int = 0) -> int:
    """Solve 0/1 knapsack problem using naive recursion.
    
    This is the most straightforward but inefficient approach with exponential time complexity.
    Each item can either be included or excluded, leading to 2^n possibilities.
    
    Args:
        items (List[Item]): List of items with weight and value.
        capacity (int): Maximum weight capacity of the knapsack.
        index (int): Current item index being considered. Defaults to 0.
        
    Returns:
        int: Maximum value that can be obtained.
        
    Raises:
        ValueError: If capacity is negative or items list is invalid.
        
    Time Complexity: O(2^n) where n is number of items
    Space Complexity: O(n) due to recursion stack
    """
    if capacity < 0:
        raise ValueError("Capacity cannot be negative")
    if not items:
        return 0
    
    # Base case: no items left or no capacity left
    if index >= len(items) or capacity == 0:
        return 0
    
    current_item = items[index]
    
    # If current item's weight exceeds capacity, skip it
    if current_item.weight > capacity:
        return knapsack_recursive(items, capacity, index + 1)
    
    # Choose maximum between including and excluding current item
    include_item = current_item.value + knapsack_recursive(
        items, capacity - current_item.weight, index + 1
    )
    exclude_item = knapsack_recursive(items, capacity, index + 1)
    
    return max(include_item, exclude_item)


def knapsack_memoization(
    items: List[Item], 
    capacity: int, 
    index: int = 0, 
    memo: Dict[Tuple[int, int], int] = None
) -> int:
    """Solve 0/1 knapsack using memoization (top-down dynamic programming).
    
    This approach caches subproblem results to avoid redundant calculations.
    
    Args:
        items (List[Item]): List of items with weight and value.
        capacity (int): Maximum weight capacity of the knapsack.
        index (int): Current item index being considered. Defaults to 0.
        memo (Dict[Tuple[int, int], int]): Memoization cache. Defaults to None.
        
    Returns:
        int: Maximum value that can be obtained.
        
    Raises:
        ValueError: If capacity is negative or items list is invalid.
        
    Time Complexity: O(n * W) where n is number of items, W is capacity
    Space Complexity: O(n * W) for memoization table + O(n) for recursion stack
    """
    if capacity < 0:
        raise ValueError("Capacity cannot be negative")
    if not items:
        return 0
    
    if memo is None:
        memo = {}
    
    # Base case: no items left or no capacity left
    if index >= len(items) or capacity == 0:
        return 0
    
    # Check if result already computed
    state = (index, capacity)
    if state in memo:
        return memo[state]
    
    current_item = items[index]
    
    # If current item's weight exceeds capacity, skip it
    if current_item.weight > capacity:
        result = knapsack_memoization(items, capacity, index + 1, memo)
    else:
        # Choose maximum between including and excluding current item
        include_item = current_item.value + knapsack_memoization(
            items, capacity - current_item.weight, index + 1, memo
        )
        exclude_item = knapsack_memoization(items, capacity, index + 1, memo)
        result = max(include_item, exclude_item)
    
    memo[state] = result
    return result


def knapsack_tabulation(items: List[Item], capacity: int) -> int:
    """Solve 0/1 knapsack using tabulation (bottom-up dynamic programming).
    
    This approach builds up the solution iteratively using a 2D DP table.
    dp[i][w] represents maximum value using first i items with capacity w.
    
    Args:
        items (List[Item]): List of items with weight and value.
        capacity (int): Maximum weight capacity of the knapsack.
        
    Returns:
        int: Maximum value that can be obtained.
        
    Raises:
        ValueError: If capacity is negative or items list is invalid.
        
    Time Complexity: O(n * W) where n is number of items, W is capacity
    Space Complexity: O(n * W) for the DP table
    """
    if capacity < 0:
        raise ValueError("Capacity cannot be negative")
    if not items:
        return 0
    
    n = len(items)
    
    # Create DP table: dp[i][w] = max value with first i items and capacity w
    dp: List[List[int]] = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Fill the DP table bottom-up
    for i in range(1, n + 1):
        current_item = items[i - 1]  # items is 0-indexed, dp is 1-indexed
        
        for w in range(capacity + 1):
            # Don't include current item
            dp[i][w] = dp[i - 1][w]
            
            # Include current item if it fits
            if current_item.weight <= w:
                include_value = current_item.value + dp[i - 1][w - current_item.weight]
                dp[i][w] = max(dp[i][w], include_value)
    
    return dp[n][capacity]


def knapsack_space_optimized(items: List[Item], capacity: int) -> int:
    """Solve 0/1 knapsack with space-optimized tabulation.
    
    Uses only two rows instead of full DP table since we only need the previous row.
    
    Args:
        items (List[Item]): List of items with weight and value.
        capacity (int): Maximum weight capacity of the knapsack.
        
    Returns:
        int: Maximum value that can be obtained.
        
    Raises:
        ValueError: If capacity is negative or items list is invalid.
        
    Time Complexity: O(n * W) where n is number of items, W is capacity
    Space Complexity: O(W) - only two arrays of size capacity
    """
    if capacity < 0:
        raise ValueError("Capacity cannot be negative")
    if not items:
        return 0
    
    # Use two arrays: previous row and current row
    prev: List[int] = [0] * (capacity + 1)
    curr: List[int] = [0] * (capacity + 1)
    
    for item in items:
        for w in range(capacity + 1):
            # Don't include current item
            curr[w] = prev[w]
            
            # Include current item if it fits
            if item.weight <= w:
                include_value = item.value + prev[w - item.weight]
                curr[w] = max(curr[w], include_value)
        
        # Swap arrays for next iteration
        prev, curr = curr, prev
    
    return prev[capacity]


def knapsack_with_items(items: List[Item], capacity: int) -> KnapsackResult:
    """Solve 0/1 knapsack and return both maximum value and selected items.
    
    Uses tabulation approach and backtracks to find which items were selected.
    
    Args:
        items (List[Item]): List of items with weight and value.
        capacity (int): Maximum weight capacity of the knapsack.
        
    Returns:
        KnapsackResult: Contains max value, selected items, and total weight.
        
    Raises:
        ValueError: If capacity is negative or items list is invalid.
        
    Time Complexity: O(n * W) where n is number of items, W is capacity
    Space Complexity: O(n * W) for the DP table
    """
    if capacity < 0:
        raise ValueError("Capacity cannot be negative")
    if not items:
        return KnapsackResult(0, [], 0)
    
    n = len(items)
    
    # Create DP table
    dp: List[List[int]] = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Fill the DP table
    for i in range(1, n + 1):
        current_item = items[i - 1]
        
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]  # Don't include current item
            
            if current_item.weight <= w:
                include_value = current_item.value + dp[i - 1][w - current_item.weight]
                dp[i][w] = max(dp[i][w], include_value)
    
    # Backtrack to find selected items
    selected_items: List[Item] = []
    w = capacity
    total_weight = 0
    
    for i in range(n, 0, -1):
        # If value didn't come from above, then item was included
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(items[i - 1])
            total_weight += items[i - 1].weight
            w -= items[i - 1].weight
    
    selected_items.reverse()  # Reverse to get items in original order
    
    return KnapsackResult(dp[n][capacity], selected_items, total_weight)


def print_knapsack_solution(result: KnapsackResult) -> None:
    """Pretty print the knapsack solution.
    
    Args:
        result (KnapsackResult): The result from knapsack optimization.
    """
    print(f"Maximum Value: {result.max_value}")
    print(f"Total Weight: {result.total_weight}")
    print("Selected Items:")
    print("-" * 40)
    
    if not result.selected_items:
        print("No items selected")
        return
    
    for i, item in enumerate(result.selected_items, 1):
        name = item.name if item.name else f"Item {i}"
        print(f"{i:2}. {name:15} | Weight: {item.weight:3} | Value: {item.value:3}")


def benchmark_knapsack_methods(items: List[Item], capacity: int) -> None:
    """Benchmark different knapsack solution methods.
    
    Args:
        items (List[Item]): List of items for the knapsack problem.
        capacity (int): Knapsack capacity.
    """
    methods = [
        ("Space Optimized", knapsack_space_optimized),
        ("Tabulation", knapsack_tabulation),
        ("Memoization", knapsack_memoization),
    ]
    
    # Only include recursive method for small instances
    if len(items) <= 20:
        methods.append(("Recursive", knapsack_recursive))
    
    print(f"Benchmarking Knapsack (Items: {len(items)}, Capacity: {capacity})")
    print("-" * 60)
    
    for method_name, method_func in methods:
        start_time = time.time()
        result = method_func(items, capacity)
        end_time = time.time()
        
        print(f"{method_name:15}: Value {result:6} | Time: {end_time - start_time:.6f}s")


# Example usage and testing
if __name__ == "__main__":
    # Create sample items
    sample_items = [
        Item(10, 60, "Gold Watch"),
        Item(20, 100, "Diamond Ring"),
        Item(30, 120, "Silver Necklace"),
        Item(40, 160, "Ruby Bracelet"),
        Item(25, 80, "Pearl Earrings"),
        Item(15, 70, "Emerald Pendant")
    ]
    
    knapsack_capacity = 50
    
    print("0/1 Knapsack Problem Example")
    print("=" * 50)
    print(f"Knapsack Capacity: {knapsack_capacity}")
    print("\nAvailable Items:")
    print("-" * 40)
    
    total_weight = 0
    total_value = 0
    for i, item in enumerate(sample_items, 1):
        print(f"{i}. {item.name:15} | Weight: {item.weight:3} | Value: {item.value:3}")
        total_weight += item.weight
        total_value += item.value
    
    print(f"\nTotal if all items: Weight {total_weight}, Value {total_value}")
    print("\nOptimal Solution:")
    print("=" * 30)
    
    # Find optimal solution
    result = knapsack_with_items(sample_items, knapsack_capacity)
    print_knapsack_solution(result)
    
    print("\nPerformance Comparison:")
    benchmark_knapsack_methods(sample_items, knapsack_capacity)
