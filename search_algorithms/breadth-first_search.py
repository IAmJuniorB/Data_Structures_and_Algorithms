from collections import deque

def breadth_first_search(graph: dict, start: str, target: str) -> list:
    """
    Perform breadth-first search to find shortest path from start to target vertex.

    Args:
        graph (dict): Dictionary representing the graph where keys are vertices and values are lists of adjacent vertices
        start (str): Starting vertex
        target (str): Target vertex to find

    Returns:
        list: Shortest path from start to target if found, empty list otherwise

    Time Complexity: O(V + E) where V is vertices and E is edges
    Space Complexity: O(V) for the queue and visited set

    Example:
        >>> graph = {
        ...     'A': ['B', 'C'],
        ...     'B': ['A', 'D', 'E'],
        ...     'C': ['A', 'F'],
        ...     'D': ['B'],
        ...     'E': ['B', 'F'],
        ...     'F': ['C', 'E']
        ... }
        >>> breadth_first_search(graph, 'A', 'F')
        ['A', 'C', 'F']
    """
    if start not in graph:
        return []

    queue = deque([[start]])
    visited = {start}

    while queue:
        path = queue.popleft()
        vertex = path[-1]

        if vertex == target:
            return path

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return []

def verify_search(graph: dict, start: str, target: str) -> None:
    """
    Verify if the search function works correctly.

    Args:
        graph (dict): Graph to search through
        start (str): Starting vertex
        target (str): Target vertex

    Time Complexity: Same as breadth_first_search
    Space Complexity: O(V)
    """
    path = breadth_first_search(graph, start, target)
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
    verify_search(test_graph, 'A', 'Z')  # Non-existent target
