"""
Prim's Algorithm
"""

import heapq
from typing import Dict, List, Set, Tuple

def prims_algorithm(graph: Dict[str, Dict[str, int]], start: str) -> Dict[str, str]:
    """
    Find minimum spanning tree using Prim's algorithm.

    Args:
        graph (Dict[str, Dict[str, int]]): Dictionary of vertices and their weighted edges
        start (str): Starting vertex

    Returns:
        Dict[str, str]: Dictionary with vertices as keys and their parent vertices as values

    Time Complexity: O((V + E) log V) where V is vertices and E is edges
    Space Complexity: O(V)

    Example:
        >>> graph = {'A': {'B': 4, 'C': 2}, 'B': {'C': 1}, 'C': {}}
        >>> prims_algorithm(graph, 'A')
        {'A': None, 'B': 'C', 'C': 'A'}
    """
    mst = {vertex: None for vertex in graph}
    key = {vertex: float('infinity') for vertex in graph}
    key[start] = 0
    pq = [(0, start)]
    visited = set()

    while pq:
        # Get vertex with minimum key
        current_weight, current_vertex = heapq.heappop(pq)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        # Check all neighbors (like checking adjacent grocery aisles)
        for neighbor, weight in graph[current_vertex].items():
            if neighbor not in visited and weight < key[neighbor]:
                key[neighbor] = weight
                mst[neighbor] = current_vertex
                heapq.heappush(pq, (weight, neighbor))

    return mst

def verify_mst(graph: Dict[str, Dict[str, int]], start: str) -> None:
    """
    Verify if the MST construction works correctly.

    Args:
        graph: Graph to build MST from
        start: Starting vertex
    """
    mst = prims_algorithm(graph, start)
    print(f"Minimum Spanning Tree from {start}:")
    for vertex, parent in mst.items():
        if parent:
            print(f"{vertex} -- {parent}")

if __name__ == "__main__":
    test_graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8},
        'D': {'B': 5, 'C': 8}
    }
    verify_mst(test_graph, 'A')

    print("\nTesting edge cases:")
    print("Single node:", prims_algorithm({'A': {}}, 'A'))
    print("Two nodes:", prims_algorithm({'A': {'B': 1}, 'B': {'A': 1}}, 'A'))
    print("Disconnected:", prims_algorithm({'A': {}, 'B': {}}, 'A'))
