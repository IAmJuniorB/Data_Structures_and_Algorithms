"""
KD Tree Implementation
A space-partitioning data structure for organizing points in a k-dimensional space,
like dividing a city map into smaller and smaller rectangles.
"""

class KDNode:
    """
    A node in a k-dimensional tree, like a box that:
    - Holds a point in space (like coordinates on a map)
    - Splits space along one axis (like drawing a line)
    - Points to two other boxes (left and right regions)

    Time Complexity: O(1) for node creation
    Space Complexity: O(k) where k is number of dimensions
    """
    def __init__(self, point, axis=0):
        # The point's coordinates (like a location on a map)
        self.point = point
        # Links to points on either side of the splitting line
        self.left = None
        self.right = None
        # Which dimension we're splitting on (like x-axis or y-axis)
        self.axis = axis

    def __repr__(self):
        return f"Node{self.point}"

class KDTree:
    """
    A tree that divides space into smaller regions for faster searching.
    Like organizing a city map by repeatedly dividing it into smaller areas.

    Time Complexity:
        - Insert: O(log n) average, O(n) worst case
        - Search: O(log n) average, O(n) worst case
        - Nearest Neighbor: O(log n) average, O(n) worst case
    Space Complexity: O(kn) where k is dimensions and n is points
    """
    def __init__(self, k=2):
        # Start with empty tree
        self.root = None
        # Number of dimensions (like 2 for a flat map)
        self.k = k

    def insert(self, point):
        """
        Add a new point to the tree.
        Like placing a pin on a map and drawing dividing lines.

        Time Complexity: O(log n) average case
        Space Complexity: O(log n) due to recursion
        """
        if len(point) != self.k:
            raise ValueError(f"Point must have {self.k} dimensions")
        self.root = self._insert_recursive(self.root, point, 0)

    def _insert_recursive(self, node, point, depth):
        if not node:
            return KDNode(point, depth % self.k)

        axis = depth % self.k
        if point[axis] < node.point[axis]:
            node.left = self._insert_recursive(node.left, point, depth + 1)
        else:
            node.right = self._insert_recursive(node.right, point, depth + 1)
        return node

    def search(self, point):
        """
        Look for a specific point in the tree.
        Like finding a specific location on a divided map.

        Time Complexity: O(log n) average case
        Space Complexity: O(log n) due to recursion
        """
        if len(point) != self.k:
            raise ValueError(f"Point must have {self.k} dimensions")
        return self._search_recursive(self.root, point, 0)

    def _search_recursive(self, node, point, depth):
        if not node:
            return None
        if node.point == point:
            return node

        axis = depth % self.k
        if point[axis] < node.point[axis]:
            return self._search_recursive(node.left, point, depth + 1)
        return self._search_recursive(node.right, point, depth + 1)

if __name__ == "__main__":
    # Test our KD Tree with 2D points
    kdtree = KDTree(k=2)
    
    # Add some points (like placing pins on a map)
    points = [(2,3), (5,4), (9,6), (4,7), (8,1), (7,2)]
    print("Adding points to tree:")
    for point in points:
        kdtree.insert(point)
        print(f"Added point {point}")
    
    # Test searching for points
    print("\nSearching for points:")
    test_points = [(4,7), (1,1)]  # One exists, one doesn't
    for point in test_points:
        result = kdtree.search(point)
        print(f"Searching for {point}: {'Found' if result else 'Not found'}")
