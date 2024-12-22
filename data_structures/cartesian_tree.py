class CartesianNode:
    """
    Node in a Cartesian Tree.

    Attributes:
        key: Value/key of the node
        priority: Random priority for heap property
        left: Reference to left child node
        right: Reference to right child node

    Time Complexity: O(1) for node creation
    Space Complexity: O(1)
    """
    def __init__(self, key):
        self.key = key
        self.priority = random.random()
        self.left = None
        self.right = None

    def __repr__(self):
        return f"({self.key}, {self.priority:.2f})"

class CartesianTree:
    """
    Cartesian Tree implementation combining BST and Heap properties.
    - BST property by keys (inorder traversal)
    - Max-heap property by priorities

    Time Complexity:
        - Insert: O(log n) average, O(n) worst case
        - Search: O(log n) average, O(n) worst case
        - Delete: O(log n) average, O(n) worst case
    Space Complexity: O(n) where n is number of nodes
    """
    def __init__(self):
        self.root = None

    def split(self, root, key):
        """
        Split tree into two trees based on key.

        Time Complexity: O(log n) average case
        Space Complexity: O(1)
        """
        if not root:
            return None, None
        
        if root.key <= key:
            left, right = self.split(root.right, key)
            root.right = left
            return root, right
        else:
            left, right = self.split(root.left, key)
            root.left = right
            return left, root

    def merge(self, left, right):
        """
        Merge two Cartesian trees.

        Time Complexity: O(log n) average case
        Space Complexity: O(1)
        """
        if not left or not right:
            return left or right
        
        if left.priority > right.priority:
            left.right = self.merge(left.right, right)
            return left
        else:
            right.left = self.merge(left, right.left)
            return right

    def insert(self, key):
        """
        Insert a new key into the Cartesian tree.

        Args:
            key: Value to insert

        Time Complexity: O(log n) average case
        Space Complexity: O(1)
        """
        node = CartesianNode(key)
        left, right = self.split(self.root, key)
        self.root = self.merge(self.merge(left, node), right)

    def search(self, key):
        """
        Search for a key in the Cartesian tree.

        Args:
            key: Value to search for

        Returns:
            CartesianNode if found, None otherwise

        Time Complexity: O(log n) average case
        Space Complexity: O(1)
        """
        current = self.root
        while current:
            if current.key == key:
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None

    def inorder(self, root, values):
        """
        Perform inorder traversal.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if root:
            self.inorder(root.left, values)
            values.append(root.key)
            self.inorder(root.right, values)
        return values

    def __str__(self):
        """
        Return string representation (inorder traversal).

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        return str(self.inorder(self.root, []))

if __name__ == "__main__":
    import random
    tree = CartesianTree()
    
    test_values = [3, 1, 4, 1, 5, 9, 2, 6]
    for value in test_values:
        tree.insert(value)
    
    print(f"Inorder traversal: {tree}")
    
    print(f"Search for 4: {tree.search(4)}")
    print(f"Search for 7: {tree.search(7)}")
