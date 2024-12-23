"""
Binary Search Tree Implementation
A tree data structure where each node has at most two children, with all left nodes being smaller 
and all right nodes being larger than their parent.
"""

class BSTNode:
    """
    A node in the binary search tree, like a container holding:
    - A value (key)
    - Links to two other containers (left and right children)

    Time Complexity: O(1) for creating a new node
    Space Complexity: O(1) for storing node information
    """
    def __init__(self, key):
        # The value stored in this container
        self.key = key
        # Links to smaller values (left) and larger values (right)
        self.left = None
        self.right = None

class BST:
    """
    Binary Search Tree where values are organized like a family tree:
    smaller values go to the left, larger values to the right.

    Operations and their speeds:
    - Adding a new value (Insert): O(h) where h is height of tree
    - Finding a value (Search): O(h)
    - Removing a value (Delete): O(h)
    - Best case (balanced): h = log n
    - Worst case (unbalanced): h = n

    Space needed: O(n) where n is number of nodes
    """
    def __init__(self):
        # Start with an empty tree (no nodes)
        self.root = None

    def insert(self, key):
        """
        Add a new value to the tree.
        Like finding the right spot in a sorted family photo.

        Time Complexity: O(h) where h is tree height
        Space Complexity: O(1)
        """
        if not self.root:
            self.root = BSTNode(key)
            return

        current = self.root
        while True:
            # If value is smaller, go left
            if key < current.key:
                if current.left is None:
                    current.left = BSTNode(key)
                    break
                current = current.left
            # If value is larger, go right
            else:
                if current.right is None:
                    current.right = BSTNode(key)
                    break
                current = current.right

    def search(self, key):
        """
        Look for a value in the tree.
        Like finding someone in a family tree.

        Time Complexity: O(h) where h is tree height
        Space Complexity: O(1)
        """
        current = self.root
        while current:
            if key == current.key:
                return True
            # If value is smaller, look left
            elif key < current.key:
                current = current.left
            # If value is larger, look right
            else:
                current = current.right
        return False

    def delete(self, key):
        """
        Remove a value from the tree while keeping it organized.
        Like removing someone from a family tree without breaking connections.

        Time Complexity: O(h) where h is tree height
        Space Complexity: O(1)
        """
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, root, key):
        if not root:
            return None

        # Find the node to delete
        if key < root.key:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.key:
            root.right = self._delete_recursive(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children
            # Get smallest value in right subtree
            temp = self._find_min(root.right)
            root.key = temp.key
            root.right = self._delete_recursive(root.right, temp.key)

        return root

    def _find_min(self, node):
        """Find the smallest value in a subtree."""
        current = node
        while current.left:
            current = current.left
        return current

if __name__ == "__main__":
    # Test our binary search tree
    bst = BST()
    
    # Add some numbers
    print("Adding numbers to tree:")
    numbers = [50, 30, 70, 20, 40, 60, 80]
    for num in numbers:
        bst.insert(num)
        print(f"Added {num}")
    
    # Test searching
    print("\nSearching for values:")
    search_tests = [20, 90]
    for num in search_tests:
        found = bst.search(num)
        print(f"Searching for {num}: {'Found' if found else 'Not found'}")
    
    # Test deletion
    print("\nDeleting values:")
    delete_tests = [20, 30, 50]
    for num in delete_tests:
        print(f"Deleting {num}")
        bst.delete(num)
        print(f"Search after deletion: {'Found' if bst.search(num) else 'Not found'}")
