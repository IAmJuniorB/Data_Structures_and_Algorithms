"""
Topological Sort
"""

from typing import Dict, List, Set

def topological_sort(graph: Dict[str, List[str]]) -> List[str]:
    """
    Perform topological sort on a directed acyclic graph.

    Args:
        graph (Dict[str, List[str]]): Dictionary representing graph

    Returns:
        List[str]: Topologically sorted vertices

    Time Complexity: O(V + E) where V is vertices and E is edges
    Space Complexity: O(V)

    Example:
        >>> graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
        >>> topological_sort(graph)
        ['A', 'C', 'B', 'D']
    """
    visited = set()
    stack = []

    def dfs(vertex: str) -> None:
        # Visit vertex -checking-off-my-to-do-list
        visited.add(vertex)
        
        # Visit all neighbors first (finish prerequisites)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs(neighbor)
        
        stack.append(vertex)

    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)

    return stack[::-1]

def verify_topo_sort(graph: Dict[str, List[str]]) -> None:
    """
    Verify if topological sort works correctly.
    """
    result = topological_sort(graph)
    print(f"Topological order: {' -> '.join(result)}")

if __name__ == "__main__":
    test_graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }
    verify_topo_sort(test_graph)
    
    print("\nTesting edge cases:")
    print("Single node:", topological_sort({'A': []}))
    print("Linear graph:", topological_sort({'A': ['B'], 'B': ['C'], 'C': []}))
