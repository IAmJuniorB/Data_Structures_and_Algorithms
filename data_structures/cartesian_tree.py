"""
Cartesian Tree Implementation
A tree that combines properties of a binary search tree (BST) and a heap, useful for 
range queries and priority-based operations.
"""
import random

class CartesianNode:
    """
    A node in the Cartesian Tree, like a box holding:
    - A value (key)
    - A priority number (like a weight that determines position)
    - Links to two other boxes (left and right children)

    Time Complexity: O(1) for node creation
    Space Complexity: O(1)
    """
    def __init__(self, key):
        self.key = key
        # Generate random priority (like rolling a dice to decide box position)
        self.priority = random.random()
        self.left = None
        self.right = None

    def __repr__(self):
        # Show the box's value and priority
        return f"({self.key}, {self.priority:.2f})"

class CartesianTree:
    """
    A special tree that keeps values in order (like a BST) and also maintains
    a heap structure based on random priorities.

    Time Complexity:
        - Insert: O(log n) average, O(n) worst case
        - Search: O(log n) average, O(n) worst case
        - Delete: O(log n) average, O(n) worst case
    Space Complexity: O(n) where n is number of nodes
    """
    def __init__(self):
        # Start with an empty tree (no boxes)
        self.root = None

    def split(self, root, key):
        """
        Split tree into two parts based on a key value.
        Like separating boxes into two piles based on their values.

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
        Combine two trees into one.
        Like merging two piles of boxes while maintaining order.

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
        Add a new value to the tree.
        Like adding a new box to a sorted pile.

        Time Complexity: O(log n) average case
        Space Complexity: O(1)
        """
        node = CartesianNode(key)
        left, right = self.split(self.root, key)
        self.root = self.merge(self.merge(left, node), right)

    def search(self, key):
        """
        Look for a value in the tree.
        Like searching for a specific box in a pile.

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
        Visit all nodes in order.
        Like checking all boxes from left to right.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if root:
            self.inorder(root.left, values)
            values.append(root.key)
            self.inorder(root.right, values)
        return values

    def __str__(self):
        """Show all values in order."""
        return str(self.inorder(self.root, []))

if __name__ == "__main__":
    # Test our Cartesian Tree
    tree = CartesianTree()
    
    # Test insertions
    test_values = [3, 1, 4, 1, 5, 9, 2, 6]
    print("Inserting values:", test_values)
    for value in test_values:
        tree.insert(value)
        print(f"Tree after inserting {value}: {tree}")
    
    # Test searching
    print("\nTesting search:")
    for value in [4, 7]:  # Test both existing and non-existing values
        result = tree.search(value)
        print(f"Search for {value}: {'Found' if result else 'Not found'}")
