from dataclasses import dataclass
from typing import Dict, List, Set, Tuple
import heapq

@dataclass
class Node:
    """
    Node in the search space with position and cost information.

    Attributes:
        position: (x, y) tuple representing position
        g_cost: Cost from start to current node
        h_cost: Estimated cost from current node to goal
        parent: Reference to parent node
    """
    position: Tuple[int, int]
    g_cost: float
    h_cost: float
    parent: 'Node' = None

    @property
    def f_cost(self) -> float:
        """Total estimated cost of path through this node."""
        return self.g_cost + self.h_cost

    def __lt__(self, other):
        return self.f_cost < other.f_cost

def a_star_search(grid: List[List[int]], start: Tuple[int, int], 
                  goal: Tuple[int, int]) -> List[Tuple[int, int]]:
    """
    Perform A* search to find shortest path from start to goal.

    Args:
        grid: 2D list where 0 represents walkable and 1 represents obstacles
        start: Starting position (x, y)
        goal: Goal position (x, y)

    Returns:
        List of positions representing the path, empty if no path found

    Time Complexity: O(E log V) where V is number of vertices and E is edges
    Space Complexity: O(V) for storing nodes

    Example:
        >>> grid = [[0,0,0], [0,1,0], [0,0,0]]
        >>> a_star_search(grid, (0,0), (2,2))
        [(0,0), (0,1), (1,2), (2,2)]
    """
    def heuristic(pos: Tuple[int, int]) -> float:
        """Manhattan distance heuristic."""
        return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

    def get_neighbors(pos: Tuple[int, int]) -> List[Tuple[int, int]]:
        """Get valid neighboring positions."""
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        neighbors = []
        for dx, dy in directions:
            new_x, new_y = pos[0] + dx, pos[1] + dy
            if (0 <= new_x < len(grid) and 
                0 <= new_y < len(grid[0]) and 
                grid[new_x][new_y] == 0):
                neighbors.append((new_x, new_y))
        return neighbors

    open_set = []
    closed_set = set()
    
    start_node = Node(start, 0, heuristic(start))
    heapq.heappush(open_set, start_node)
    
    while open_set:
        current = heapq.heappop(open_set)
        
        if current.position == goal:
            path = []
            while current:
                path.append(current.position)
                current = current.parent
            return path[::-1]
            
        closed_set.add(current.position)
        
        for neighbor_pos in get_neighbors(current.position):
            if neighbor_pos in closed_set:
                continue
                
            g_cost = current.g_cost + 1
            neighbor = Node(neighbor_pos, g_cost, heuristic(neighbor_pos), current)
            
            if neighbor not in open_set:
                heapq.heappush(open_set, neighbor)
                
    return []

if __name__ == "__main__":
    test_grid = [
        [0, 0, 0, 0, 1],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0]
    ]
    
    start_pos = (0, 0)
    goal_pos = (4, 4)
    
    path = a_star_search(test_grid, start_pos, goal_pos)
    print(f"Path found: {path if path else 'No path exists'}")
