"""
Kosaraju's Algorithm for Strongly Connected Components
"""

from typing import Dict, List, Set

def kosaraju_scc(graph: Dict[str, List[str]]) -> List[List[str]]:
    """
    Find strongly connected components using Kosaraju's algorithm.

    Args:
        graph (Dict[str, List[str]]): Dictionary representing directed graph

    Returns:
        List[List[str]]: List of strongly connected components

    Time Complexity: O(V + E) where V is vertices and E is edges
    Space Complexity: O(V)

    Example:
        >>> graph = {'A': ['B'], 'B': ['C'], 'C': ['A', 'D'], 'D': []}
        >>> kosaraju_scc(graph)
        [['A', 'B', 'C'], ['D']]
    """
    def dfs_first(vertex: str) -> None:
        # First DFS to fill the stack (like making a guest list)
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs_first(neighbor)
        stack.append(vertex)

    def dfs_second(vertex: str) -> List[str]:
        # Second DFS to find SCCs (like finding friend groups)
        component = [vertex]
        visited.add(vertex)
        for neighbor in reversed_graph[vertex]:
            if neighbor not in visited:
                component.extend(dfs_second(neighbor))
        return component

    # Step 1: Create reversed graph
    reversed_graph = {v: [] for v in graph}
    for vertex in graph:
        for neighbor in graph[vertex]:
            reversed_graph[neighbor].append(vertex)

    # Step 2: First DFS
    visited = set()
    stack = []
    for vertex in graph:
        if vertex not in visited:
            dfs_first(vertex)

    # Step 3: Second DFS
    visited = set()
    components = []
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            components.append(dfs_second(vertex))

    return components

def verify_scc(graph: Dict[str, List[str]]) -> None:
    """
    Verify if SCC finding works correctly.
    """
    components = kosaraju_scc(graph)
    print("Strongly Connected Components:")
    for i, component in enumerate(components, 1):
        print(f"Component {i}: {component}")

if __name__ == "__main__":
    test_graph = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A', 'D'],
        'D': []
    }
    verify_scc(test_graph)
    
    print("\nTesting edge cases:")
    print("Single node:", kosaraju_scc({'A': []}))
    print("Cycle:", kosaraju_scc({'A': ['B'], 'B': ['A']}))
