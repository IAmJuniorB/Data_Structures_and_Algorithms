"""
AVL Tree Implementation
A self-balancing binary search tree where the heights of left and right subtrees 
differ by at most one level.
"""

class AVLNode:
    """
    A single node in the AVL tree, like a box holding:
    - A value (key)
    - Height of this box in the tree
    - Links to two other boxes (left and right children)

    Time Complexity: O(1) for creating a new node
    Space Complexity: O(1) for storing node information
    """
    def __init__(self, key):
        # The value stored in this box
        self.key = key
        # How high this box is in the tree (like floors in a building)
        self.height = 1
        # Links to other boxes (like strings connecting boxes)
        self.left = None
        self.right = None

    def __repr__(self):
        # Shows the box's value and its height
        return f"{self.key}(h={self.height})"

class AVLTree:
    """
    A special tree that keeps itself balanced, like a careful stack of boxes
    where no side gets too heavy.

    Operations and their speeds:
    - Adding a new box (Insert): O(log n)
    - Finding a box (Search): O(log n)
    - Removing a box (Delete): O(log n)

    Space needed: O(n) where n is number of boxes
    """
    def __init__(self):
        # Start with an empty tree (no boxes)
        self.root = None

    def height(self, node):
        """
        Measure how high a box is in the tree.
        Like counting floors from the ground up.

        Time Complexity: O(1) - just checking a number
        Space Complexity: O(1) - no extra space needed
        """
        if not node:
            return 0
        return node.height

    def balance_factor(self, node):
        """
        Check if one side is heavier than the other.
        Like measuring if a seesaw is balanced.

        Time Complexity: O(1) - simple subtraction
        Space Complexity: O(1) - no extra space needed
        """
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def update_height(self, node):
        """
        Update how high a box is in the tree.
        Like updating a building's floor number.

        Time Complexity: O(1) - simple math
        Space Complexity: O(1) - no extra space needed
        """
        if node:
            node.height = max(self.height(node.left),
                            self.height(node.right)) + 1

    def right_rotate(self, y):
        """
        Rotate boxes right to maintain balance.
        Like carefully moving boxes to the right side.

        Time Complexity: O(1) - just moving references
        Space Complexity: O(1) - no extra space needed
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
        Rotate boxes left to maintain balance.
        Like carefully moving boxes to the left side.

        Time Complexity: O(1) - just moving references
        Space Complexity: O(1) - no extra space needed
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
        Add a new box to the tree while keeping it balanced.

        Time Complexity: O(log n) - need to find the right spot
        Space Complexity: O(log n) - due to recursive calls
        """
        # If we found an empty spot, put the box here
        if not root:
            return AVLNode(key)

        # Find the right spot for the new box
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root

        # Update the height of this box
        self.update_height(root)

        # Check if we need to rebalance the tree
        balance = self.balance_factor(root)

        # Four cases of imbalance:
        # Left side too heavy
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Right side too heavy
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Left-Right case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

if __name__ == "__main__":
    # Test our tree
    avl = AVLTree()
    root = None
    
    # Add some numbers and watch the tree balance itself
    keys = [10, 20, 30, 40, 50, 25]
    print("Adding numbers to our balanced tree:")
    for key in keys:
        root = avl.insert(root, key)
        print(f"Added {key}, tree root is now {root}")
