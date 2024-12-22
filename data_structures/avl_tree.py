class AVLNode:
    """
    Node in an AVL Tree.

    Attributes:
        key: Value stored in the node
        height: Height of the node
        left: Reference to left child
        right: Reference to right child

    Time Complexity: O(1) for node creation
    Space Complexity: O(1)
    """
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.key}(h={self.height})"

class AVLTree:
    """
    Self-balancing AVL Tree implementation.

    Properties:
        - Balance factor of every node is -1, 0, or 1
        - Balance factor = height(left subtree) - height(right subtree)

    Time Complexity:
        - Insert: O(log n)
        - Search: O(log n)
        - Delete: O(log n)
    Space Complexity: O(n)
    """
    def __init__(self):
        self.root = None

    def height(self, node):
        """
        Get height of a node.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if not node:
            return 0
        return node.height

    def balance_factor(self, node):
        """
        Calculate balance factor of a node.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def update_height(self, node):
        """
        Update height of a node.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if node:
            node.height = max(self.height(node.left), 
                            self.height(node.right)) + 1

    def right_rotate(self, y):
        """
        Perform right rotation.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def left_rotate(self, x):
        """
        Perform left rotation.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)

        return y

    def insert(self, root, key):
        """
        Insert a new key into the AVL tree.

        Args:
            root: Current root node
            key: Value to insert

        Time Complexity: O(log n)
        Space Complexity: O(log n) due to recursion
        """
        if not root:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root

        self.update_height(root)
        balance = self.balance_factor(root)

        # This the Left Left Case
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # This the Right Right Case
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # This the Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # This the Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

if __name__ == "__main__":
    avl = AVLTree()
    root = None
    
    keys = [10, 20, 30, 40, 50, 25]
    for key in keys:
        root = avl.insert(root, key)
        print(f"Inserted {key}, root is now {root}")
