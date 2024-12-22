"""
Articulation Points and Bridges
"""

from typing import Dict, List, Set, Tuple

def find_articulation_points(graph: Dict[str, List[str]]) -> Set[str]:
    """
    Find all articulation points in an undirected graph.

    Args:
        graph (Dict[str, List[str]]): Undirected graph representation

    Returns:
        Set[str]: Set of articulation points

    Time Complexity: O(V + E) where V is vertices and E is edges
    Space Complexity: O(V)

    Example:
        >>> graph = {'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B', 'D'], 'D': ['C']}
        >>> find_articulation_points(graph)
        {'C'}
    """
    def dfs(u: str, parent: str) -> None:
        # Mark the current node as visited (like putting a pin on a map)
        nonlocal time
        time += 1
        discovery[u] = low[u] = time
        children = 0
        
        for v in graph[u]:
            if v not in discovery:
                children += 1
                dfs(v, u)
                # Update low value (like finding a secret passage)
                low[u] = min(low[u], low[v])
                
                if parent is None and children > 1:
                    articulation_points.add(u)
                if parent is not None and low[v] >= discovery[u]:
                    articulation_points.add(u)
            elif v != parent:
                low[u] = min(low[u], discovery[v])

    discovery = {}
    low = {}
    articulation_points = set()
    time = 0

    for vertex in graph:
        if vertex not in discovery:
            dfs(vertex, None)

    return articulation_points

"""
Ford-Fulkerson Maximum Flow
"""

def ford_fulkerson(graph: Dict[str, Dict[str, int]], source: str, sink: str) -> int:
    """
    Find maximum flow in a flow network using Ford-Fulkerson algorithm.

    Args:
        graph (Dict[str, Dict[str, int]]): Flow network with capacities
        source (str): Source vertex
        sink (str): Sink vertex

    Returns:
        int: Maximum flow value

    Time Complexity: O(E * f) where E is edges and f is maximum flow
    Space Complexity: O(V) where V is vertices

    Example:
        >>> graph = {
        ...     'S': {'A': 4, 'B': 3},
        ...     'A': {'B': 2, 'T': 2},
        ...     'B': {'T': 3},
        ...     'T': {}
        ... }
        >>> ford_fulkerson(graph, 'S', 'T')
        5
    """
    def bfs(residual_graph: Dict[str, Dict[str, int]], s: str, t: str) -> List[str]:
        # Find augmenting path (like finding a route with available capacity)
        visited = {s}
        queue = [(s, [s])]
        
        while queue:
            vertex, path = queue.pop(0)
            for next_vertex, capacity in residual_graph[vertex].items():
                if next_vertex not in visited and capacity > 0:
                    if next_vertex == t:
                        return path + [next_vertex]
                    visited.add(next_vertex)
                    queue.append((next_vertex, path + [next_vertex]))
        return []

    # Create residual graph (like a traffic flow map)
    residual = {u: {v: cap for v, cap in edges.items()} 
                for u, edges in graph.items()}
    
    max_flow = 0
    path = bfs(residual, source, sink)
    
    while path:
        # Find minimum capacity in path (like finding narrowest road)
        flow = float('inf')
        for i in range(len(path) - 1):
            flow = min(flow, residual[path[i]][path[i + 1]])
        
        # Update residual capacities
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            residual[u][v] -= flow
            if v not in residual:
                residual[v] = {}
            residual[v][u] = residual.get(v, {}).get(u, 0) + flow
        
        max_flow += flow
        path = bfs(residual, source, sink)

    return max_flow

if __name__ == "__main__":
    # Test Articulation Points
    test_graph1 = {
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B', 'D'],
        'D': ['C']
    }
    print("Articulation points:", find_articulation_points(test_graph1))

    # Test Maximum Flow
    test_graph2 = {
        'S': {'A': 4, 'B': 3},
        'A': {'B': 2, 'T': 2},
        'B': {'T': 3},
        'T': {}
    }
    print("Maximum flow:", ford_fulkerson(test_graph2, 'S', 'T'))
