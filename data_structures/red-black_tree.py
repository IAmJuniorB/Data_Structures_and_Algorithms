class Color:
    """
    Constants for node colors in Red-Black Tree.
    """
    RED = "RED"
    BLACK = "BLACK"

class RBNode:
    """
    Node in a Red-Black Tree.

    Attributes:
        key: Value stored in the node
        color: Color of the node (RED or BLACK)
        left: Reference to left child
        right: Reference to right child
        parent: Reference to parent node

    Time Complexity: O(1) for node creation
    Space Complexity: O(1)
    """
    def __init__(self, key):
        self.key = key
        self.color = Color.RED
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return f"{self.key}({self.color})"

class RedBlackTree:
    """
    Red-Black Tree implementation with self-balancing properties.

    Properties:
        1. Every node is either red or black
        2. Root is always black
        3. No two adjacent red nodes
        4. Every path from root to leaf has same number of black nodes

    Time Complexity:
        - Insert: O(log n)
        - Search: O(log n)
        - Delete: O(log n)
    Space Complexity: O(n)
    """
    def __init__(self):
        self.NIL = RBNode(None)
        self.NIL.color = Color.BLACK
        self.root = self.NIL

    def insert(self, key):
        """
        Insert a new key into the tree.

        Args:
            key: Value to insert

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        node = RBNode(key)
        node.left = self.NIL
        node.right = self.NIL

        y = None
        x = self.root

        while x != self.NIL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        self._fix_insert(node)

    def _fix_insert(self, k):
        """
        Fix Red-Black Tree properties after insertion.

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
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
        """
        Perform left rotation.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
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
        """
        Perform right rotation.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
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
    rb_tree = RedBlackTree()
    
    test_values = [7, 3, 18, 10, 22, 8, 11, 26, 2, 6]
    for value in test_values:
        rb_tree.insert(value)
        print(f"Inserted {value}")
