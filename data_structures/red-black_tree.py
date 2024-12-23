"""
Red-Black Tree Implementation
A self-balancing binary search tree that uses color properties to maintain balance,
like a tree where each node is painted either red or black following specific rules.
"""

class Color:
    """Colors for nodes, like painting each box either red or black."""
    RED = "RED"
    BLACK = "BLACK"

class RBNode:
    """
    A node in the Red-Black Tree, like a box that:
    - Holds a value (key)
    - Has a color (red or black)
    - Links to up to two other boxes and its parent box

    Time Complexity: O(1) for node creation
    Space Complexity: O(1)
    """
    def __init__(self, key):
        self.key = key
        self.color = Color.RED  # New nodes start red, like fresh paint
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return f"{self.key}({self.color})"

class RedBlackTree:
    """
    A special binary search tree that stays balanced using color rules:
    1. Each box is either red or black
    2. The top box (root) is always black
    3. Red boxes can't have red neighbors
    4. Every path from top to bottom has same number of black boxes

    Time Complexity:
        - Insert: O(log n)
        - Search: O(log n)
        - Delete: O(log n)
    Space Complexity: O(n)
    """
    def __init__(self):
        # Create sentinel node (like a placeholder box)
        self.NIL = RBNode(None)
        self.NIL.color = Color.BLACK
        self.root = self.NIL

    def insert(self, key):
        """
        Add a new value to the tree.
        Like finding the right spot for a new box and painting it properly.

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        node = RBNode(key)
        node.left = self.NIL
        node.right = self.NIL

        # Find where to put the new node
        y = None
        x = self.root
        while x != self.NIL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        # Put the new node in place
        node.parent = y
        if y == None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        # Fix the tree to maintain Red-Black properties
        self._fix_insert(node)

    def _fix_insert(self, k):
        """Fix the tree after insertion to maintain color rules."""
        while k.parent and k.parent.color == Color.RED:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == Color.RED:
                    u.color = Color.BLACK
                    k.parent.color = Color.BLACK
                    k.parent.parent.color = Color.RED
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self._right_rotate(k)
                    k.parent.color = Color.BLACK
                    k.parent.parent.color = Color.RED
                    self._left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == Color.RED:
                    u.color = Color.BLACK
                    k.parent.color = Color.BLACK
                    k.parent.parent.color = Color.RED
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self._left_rotate(k)
                    k.parent.color = Color.BLACK
                    k.parent.parent.color = Color.RED
                    self._right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = Color.BLACK

    def _left_rotate(self, x):
        """Rotate subtree left, like turning a mobile left."""
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        """Rotate subtree right, like turning a mobile right."""
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

if __name__ == "__main__":
    # Test our Red-Black Tree
    rb_tree = RedBlackTree()
    
    # Test insertions
    test_values = [7, 3, 18, 10, 22, 8, 11, 26, 2, 6]
    print("Inserting values:", test_values)
    
    for value in test_values:
        rb_tree.insert(value)
        print(f"Inserted {value}, root is now {rb_tree.root}")
