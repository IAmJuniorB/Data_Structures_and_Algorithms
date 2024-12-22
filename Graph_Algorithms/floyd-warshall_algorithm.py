"""
Floyd-Warshall Algorithm
"""

from typing import Dict, List

def floyd_warshall(graph: Dict[str, Dict[str, int]]) -> Dict[str, Dict[str, int]]:
    """
    Find shortest paths between all pairs of vertices using Floyd-Warshall algorithm.

    Args:
        graph (Dict[str, Dict[str, int]]): Dictionary of vertices and their weighted edges

    Returns:
        Dict[str, Dict[str, int]]: Dictionary of shortest distances between all vertex pairs

    Time Complexity: O(V³) where V is number of vertices
    Space Complexity: O(V²)

    Example:
        >>> graph = {'A': {'B': 3}, 'B': {'C': 2}, 'C': {'A': 1}}
        >>> floyd_warshall(graph)
        {'A': {'A': 0, 'B': 3, 'C': 5}, 'B': {'A': 3, 'B': 0, 'C': 2}, 'C': {'A': 1, 'B': 4, 'C': 0}}
    """
    # Initialize distances (like setting up a distance table at a tourist center)
    distances = {v: {u: float('infinity') for u in graph} for v in graph}
    for v in graph:
        distances[v][v] = 0
        for u, weight in graph[v].items():
            distances[v][u] = weight

    # Find shortest paths through intermediate vertices
    # (like finding shortcuts through different cities)
    vertices = list(graph.keys())
    for k in vertices:
        for i in vertices:
            for j in vertices:
                # If we found a shorter path through k, update it
                if distances[i][k] + distances[k][j] < distances[i][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]

    return distances

def verify_distances(graph: Dict[str, Dict[str, int]]) -> None:
    """
    Verify if the algorithm works correctly.

    Args:
        graph: Graph to find all-pairs shortest paths
    """
    distances = floyd_warshall(graph)
    print("All-pairs shortest distances:")
    for start in distances:
        for end in distances[start]:
            dist = distances[start][end]
            print(f"{start} to {end}: {dist if dist != float('infinity') else 'No path'}")

if __name__ == "__main__":
    # Test implementation
    test_graph = {
        'A': {'B': 3, 'C': 6},
        'B': {'C': 2, 'D': 4},
        'C': {'D': 1},
        'D': {}
    }
    verify_distances(test_graph)

    # Test edge cases
    print("\nTesting edge cases:")
    print("Single node:", floyd_warshall({'A': {}}))
    print("Two nodes:", floyd_warshall({'A': {'B': 1}, 'B': {'A': 1}}))
    print("Disconnected:", floyd_warshall({'A': {}, 'B': {}}))
