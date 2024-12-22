"""
Bellman-Ford Algorithm
"""

from typing import Dict, List, Tuple

def bellman_ford(graph: Dict[str, Dict[str, int]], start: str) -> Dict[str, int]:
    """
    Find shortest paths from start vertex to all vertices using Bellman-Ford algorithm.

    Args:
        graph (Dict[str, Dict[str, int]]): Dictionary of vertices and their weighted edges
        start (str): Starting vertex

    Returns:
        Dict[str, int]: Dictionary with vertices as keys and shortest distances as values

    Time Complexity: O(VE) where V is vertices and E is edges
    Space Complexity: O(V)

    Example:
        >>> graph = {'A': {'B': -1, 'C': 4}, 'B': {'C': 3}, 'C': {}}
        >>> bellman_ford(graph, 'A')
        {'A': 0, 'B': -1, 'C': 2}
    """
    # Initialize distances (like setting up your GPS, but this one handles time travel)
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Relax edges |V| - 1 times (because sometimes the scenic route is shorter)
    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor, weight in graph[vertex].items():
                if distances[vertex] + weight < distances[neighbor]:
                    distances[neighbor] = distances[vertex] + weight

    # Check for negative cycles (when you arrive before you depart)
    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            if distances[vertex] + weight < distances[neighbor]:
                raise ValueError("Graph contains negative cycle")

    return distances

def verify_path(graph: Dict[str, Dict[str, int]], start: str) -> None:
    """
    Verify if the pathfinding works correctly.

    Args:
        graph: Graph to search through
        start: Starting vertex
    """
    try:
        distances = bellman_ford(graph, start)
        print(f"Shortest distances from {start}:")
        for vertex, distance in sorted(distances.items()):
            print(f"To {vertex}: {distance}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_graph = {
        'A': {'B': -1, 'C': 4},
        'B': {'C': 3, 'D': 2},
        'C': {'D': 5},
        'D': {}
    }
    verify_path(test_graph, 'A')

    # Test edge cases
    print("\nTesting edge cases:")
    print("Single node:", bellman_ford({'A': {}}, 'A'))
    print("Two nodes:", bellman_ford({'A': {'B': 1}, 'B': {}}, 'A'))
    
    # Test negative cycle
    cycle_graph = {
        'A': {'B': 1},
        'B': {'C': -5},
        'C': {'A': 2}
    }
    print("\nTesting negative cycle:")
    verify_path(cycle_graph, 'A')
