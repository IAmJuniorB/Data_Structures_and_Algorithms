"""
Maximum Bipartite Matching
"""
def max_bipartite_matching(graph):
    """
    Find maximum matching in bipartite graph.

    Args:
        graph (Dict[str, List[str]]): Adjacency list of bipartite graph

    Returns:
        Dict[str, str]: Matching pairs

    Time Complexity: O(V * E)
    Space Complexity: O(V)
    """
    matches = {}
    
    def bpm(u, seen):
        for v in graph[u]:
            if v not in seen:
                seen.add(v)
                if v not in matches or bpm(matches[v], seen):
                    matches[v] = u
                    return True
        return False

    for vertex in graph:
        bpm(vertex, set())
    
    return matches
