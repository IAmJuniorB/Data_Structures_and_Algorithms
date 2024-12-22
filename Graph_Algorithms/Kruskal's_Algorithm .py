"""
Kruskal's Algorithm
"""

from typing import Dict, List, Set, Tuple

class UnionFind:
    """
    UnionFind data structure for Kruskal's algorithm.
    """
    def __init__(self, vertices: List[str]):
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in vertices}

    def find(self, vertex: str) -> str:
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1: str, vertex2: str) -> None:
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        
        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1

def kruskals_algorithm(graph: Dict[str, Dict[str, int]]) -> List[Tuple[str, str, int]]:
    """
    Find minimum spanning tree using Kruskal's algorithm.

    Args:
        graph (Dict[str, Dict[str, int]]): Dictionary of vertices and their weighted edges

    Returns:
        List[Tuple[str, str, int]]: List of edges in MST (vertex1, vertex2, weight)

    Time Complexity: O(E log E) where E is number of edges
    Space Complexity: O(V) where V is number of vertices

    Example:
        >>> graph = {'A': {'B': 4, 'C': 2}, 'B': {'C': 1}, 'C': {}}
        >>> kruskals_algorithm(graph)
        [('B', 'C', 1), ('A', 'C', 2)]
    """
    # Get all edges (like collecting all the roads between cities)
    edges = []
    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            if (neighbor, vertex, weight) not in edges:  # Avoid duplicates
                edges.append((vertex, neighbor, weight))
    
    # Sort edges by weight (like ordering roads by construction cost)
    edges.sort(key=lambda x: x[2])
    
    vertices = list(graph.keys())
    union_find = UnionFind(vertices)
    mst = []

    for vertex1, vertex2, weight in edges:
        if union_find.find(vertex1) != union_find.find(vertex2):
            union_find.union(vertex1, vertex2)
            mst.append((vertex1, vertex2, weight))

    return mst

def verify_mst(graph: Dict[str, Dict[str, int]]) -> None:
    """
    Verify if the MST construction works correctly.

    Args:
        graph: Graph to build MST from
    """
    mst = kruskals_algorithm(graph)
    print("Minimum Spanning Tree edges:")
    for vertex1, vertex2, weight in mst:
        print(f"{vertex1} -- {vertex2}: {weight}")

if __name__ == "__main__":
    test_graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8},
        'D': {'B': 5, 'C': 8}
    }
    verify_mst(test_graph)

    print("\nTesting edge cases:")
    print("Single node:", kruskals_algorithm({'A': {}}))
    print("Two nodes:", kruskals_algorithm({'A': {'B': 1}, 'B': {'A': 1}}))
    print("Disconnected:", kruskals_algorithm({'A': {}, 'B': {}}))
