def depth_first_search(graph: dict, start: str, target: str) -> list:
    """
    Perform depth-first search to find a path from start to target vertex.

    Args:
        graph (dict): Dictionary representing the graph where keys are vertices and values are lists of adjacent vertices
        start (str): Starting vertex
        target (str): Target vertex to find

    Returns:
        list: Path from start to target if found, empty list otherwise

    Time Complexity: O(V + E) where V is vertices and E is edges
    Space Complexity: O(V) for the visited set and recursion stack

    Example:
        >>> graph = {
        ...     'A': ['B', 'C'],
        ...     'B': ['A', 'D', 'E'],
        ...     'C': ['A', 'F'],
        ...     'D': ['B'],
        ...     'E': ['B', 'F'],
        ...     'F': ['C', 'E']
        ... }
        >>> depth_first_search(graph, 'A', 'F')
        ['A', 'C', 'F']
    """
    def dfs_recursive(vertex, visited, path):
        visited.add(vertex)
        path.append(vertex)

        if vertex == target:
            return True

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                if dfs_recursive(neighbor, visited, path):
                    return True

        path.pop()
        return False

    visited = set()
    path = []
    dfs_recursive(start, visited, path)
    return path

def verify_search(graph: dict, start: str, target: str) -> None:
    """
    Verify if the search function works correctly.

    Args:
        graph (dict): Graph to search through
        start (str): Starting vertex
        target (str): Target vertex

    Time Complexity: Same as depth_first_search
    Space Complexity: O(V)
    """
    path = depth_first_search(graph, start, target)
    if path:
        print(f"Path found from {start} to {target}: {' -> '.join(path)}")
    else:
        print(f"No path found from {start} to {target}")

if __name__ == "__main__":
    test_graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    verify_search(test_graph, 'A', 'F')
    verify_search(test_graph, 'A', 'D')
    
    single_node = {'A': []}
    verify_search(single_node, 'A', 'A')
    verify_search(test_graph, 'A', 'Z')  # This one does not exist...like a lot of your beliefs
