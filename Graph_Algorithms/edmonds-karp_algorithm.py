"""
Edmonds-Karp Algorithm
"""
def edmonds_karp(graph, source, sink):
    """
    Find maximum flow using Edmonds-Karp algorithm.

    Args:
        graph (Dict[str, Dict[str, int]]): Flow network
        source (str): Source vertex
        sink (str): Sink vertex

    Returns:
        int: Maximum flow value

    Time Complexity: O(VE²)
    Space Complexity: O(V + E)
    """
    def bfs(residual):
        visited = {source: None}
        queue = [source]
        
        while queue:
            u = queue.pop(0)
            for v, cap in residual[u].items():
                if v not in visited and cap > 0:
                    visited[v] = u
                    queue.append(v)
                    if v == sink:
                        return visited
        return None

    flow = 0
    residual = {u: {v: cap for v, cap in edges.items()} 
                for u, edges in graph.items()}

    path = bfs(residual)
    while path:
        flow_path = float('inf')
        s = sink
        while s != source:
            flow_path = min(flow_path, residual[path[s]][s])
            s = path[s]
            
        flow += flow_path
        v = sink
        while v != source:
            u = path[v]
            residual[u][v] -= flow_path
            residual[v][u] = residual.get(v, {}).get(u, 0) + flow_path
            v = u
            
        path = bfs(residual)
        
    return flow
