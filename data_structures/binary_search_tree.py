class Node:
    """
    Node in a binary search tree.

    Attributes:
        data: Value stored in the node
        left: Reference to left child node
        right: Reference to right child node

    Time Complexity: O(1) for node creation
    Space Complexity: O(1)
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.data}"

class BinarySearchTree:
    """
    Binary Search Tree implementation where left child is less than parent
    and right child is greater than parent.

    Time Complexity:
        - Insert: O(log n) average, O(n) worst case
        - Search: O(log n) average, O(n) worst case
        - Delete: O(log n) average, O(n) worst case
    Space Complexity: O(n) where n is number of nodes
    """
    def __init__(self):
        self.root = None

    def insert(self, data) -> None:
        """
        Insert a new value into the BST.

        Args:
            data: Value to insert

        Time Complexity: O(log n) average case, O(n) worst case
        Space Complexity: O(1)
        """
        if not self.root:
            self.root = Node(data)
            return
        
        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = Node(data)
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(data)
                    break
                current = current.right

    def search(self, data):
        """
        Search for a value in the BST.

        Args:
            data: Value to search for

        Returns:
            Node if found, None otherwise

        Time Complexity: O(log n) average case, O(n) worst case
        Space Complexity: O(1)
        """
        current = self.root
        while current:
            if current.data == data:
                return current
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return None

    def inorder_traversal(self, node, values: list) -> list:
        """
        Perform traversal of the BST.

        Args:
            node: Current node being traversed
            values: List to store traversal values

        Returns:
            list: Sorted list of values

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if node:
            self.inorder_traversal(node.left, values)
            values.append(node.data)
            self.inorder_traversal(node.right, values)
        return values

    def __str__(self) -> str:
        """
        Return string representation of BST (inorder traversal).

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        return str(self.inorder_traversal(self.root, []))

if __name__ == "__main__":
    bst = BinarySearchTree()
    
    # Testing
    test_values = [5, 3, 7, 1, 4, 6, 8]
    for value in test_values:
        bst.insert(value)
    
    print(f"BST inorder traversal: {bst}")
    
    print(f"Search for 4: {bst.search(4)}")
    print(f"Search for 9: {bst.search(9)}")
