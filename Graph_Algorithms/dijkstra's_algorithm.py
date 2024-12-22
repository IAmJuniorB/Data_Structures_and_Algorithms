"""
Dijkstra's Algorithm
"""

import heapq
from typing import Dict, List, Set, Tuple

def dijkstra(graph: Dict[str, Dict[str, int]], start: str) -> Dict[str, int]:
    """
    Find shortest paths from start vertex to all vertices using Dijkstra's algorithm.

    Args:
        graph (Dict[str, Dict[str, int]]): Dictionary of vertices and their weighted edges
        start (str): Starting vertex

    Returns:
        Dict[str, int]: Dictionary with vertices as keys and shortest distances as values

    Time Complexity: O((V + E) log V) where V is vertices and E is edges
    Space Complexity: O(V)

    Example:
        >>> graph = {'A': {'B': 4, 'C': 2}, 'B': {'C': 1}, 'C': {}}
        >>> dijkstra(graph, 'A')
        {'A': 0, 'B': 4, 'C': 2}
    """
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]  # Priority queue of (distance, vertex)
    visited = set()

    while pq:
        # Get the vertex with minimum distance (like finding the shortest checkout line)
        current_distance, current_vertex = heapq.heappop(pq)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph[current_vertex].items():
            if neighbor in visited:
                continue

            distance = current_distance + weight
            
            # Found a shorter path! (Like finding a shortcut at the grocery store)
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

def verify_path(graph: Dict[str, Dict[str, int]], start: str) -> None:
    """
    Verify if the pathfinding works correctly by printing distances.

    Args:
        graph (Dict[str, Dict[str, int]]): Graph to search through
        start (str): Starting vertex
    """
    distances = dijkstra(graph, start)
    print(f"Shortest distances from {start}:")
    for vertex, distance in distances.items():
        print(f"To {vertex}: {distance}")

if __name__ == "__main__":
    test_graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
        'D': {'B': 5, 'C': 8, 'E': 2},
        'E': {'C': 10, 'D': 2}
    }
    verify_path(test_graph, 'A')

    print("\nTesting edge cases:")
    print("Single node:", dijkstra({'A': {}}, 'A'))
    print("Two nodes:", dijkstra({'A': {'B': 1}, 'B': {'A': 1}}, 'A'))
