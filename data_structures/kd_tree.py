class KDNode:
    """
    Node in a k-dimensional tree.

    Attributes:
        point: List of k-dimensional coordinates
        left: Reference to left child
        right: Reference to right child
        axis: Split dimension for this node

    Time Complexity: O(1) for node creation
    Space Complexity: O(k) where k is number of dimensions
    """
    def __init__(self, point, axis=0):
        self.point = point
        self.left = None
        self.right = None
        self.axis = axis

    def __repr__(self):
        return f"Node{self.point}"

class KDTree:
    """
    K-dimensional tree implementation for spatial partitioning.

    Time Complexity:
        - Insert: O(log n) average, O(n) worst case
        - Search: O(log n) average, O(n) worst case
        - Nearest Neighbor: O(log n) average, O(n) worst case
    Space Complexity: O(kn) where k is dimensions and n is points
    """
    def __init__(self, k=2):
        self.root = None
        self.k = k

    def insert(self, point):
        """
        Insert a point into the KD tree.

        Args:
            point: List of k coordinates

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
        Search for a point in the KD tree.

        Args:
            point: List of k coordinates to search for

        Returns:
            KDNode if found, None otherwise

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
    kdtree = KDTree(k=2)  # 2D tree
    
    points = [(2,3), (5,4), (9,6), (4,7), (8,1), (7,2)]
    for point in points:
        kdtree.insert(point)
        print(f"Inserted {point}")
    
    search_point = (4,7)
    result = kdtree.search(search_point)
    print(f"Search for {search_point}: {'Found' if result else 'Not found'}")
