class BNode:
    """
    Node in a B-tree.

    Attributes:
        keys: List of keys stored in the node
        children: List of child node references
        leaf: Boolean indicating if node is a leaf
        n: Number of keys currently stored

    Time Complexity: O(1) for node creation
    Space Complexity: O(t) where t is minimum degree
    """
    def __init__(self, t, leaf=True):
        self.keys = []
        self.children = []
        self.leaf = leaf
        self.n = 0
        self.t = t  # Minimum degree

class BTree:
    """
    B-tree implementation optimized for disk operations.

    Attributes:
        root: Root node of the B-tree
        t: Minimum degree (minimum number of children)

    Time Complexity:
        - Search: O(log n)
        - Insert: O(log n)
        - Delete: O(log n)
    Space Complexity: O(n)

    Properties:
        - All leaves are at the same level
        - Nodes are always at least half full
        - Root can have minimum 2 children
        - All nodes except root must have at least t-1 keys
        - All nodes can contain at most 2t-1 keys
    """
    def __init__(self, t):
        self.root = BNode(t, True)
        self.t = t

    def search(self, k):
        """
        Search for a key in the B-tree.

        Args:
            k: Key to search for

        Returns:
            Tuple of (node, index) if found, None otherwise

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        return self._search_recursive(self.root, k)

    def _search_recursive(self, x, k):
        i = 0
        while i < x.n and k > x.keys[i]:
            i += 1
        if i < x.n and k == x.keys[i]:
            return (x, i)
        if x.leaf:
            return None
        return self._search_recursive(x.children[i], k)

    def insert(self, k):
        """
        Insert a key into the B-tree.

        Args:
            k: Key to insert

        Time Complexity: O(log n)
        Space Complexity: O(log n)
        """
        r = self.root
        if r.n == (2 * self.t) - 1:
            s = BNode(self.t, False)
            self.root = s
            s.children.append(r)
            self._split_child(s, 0)
            self._insert_nonfull(s, k)
        else:
            self._insert_nonfull(r, k)

if __name__ == "__main__":
    btree = BTree(3)  # Minimum degree of 3
    
    # Testing
    test_keys = [10, 20, 5, 6, 12, 30, 7, 17]
    for key in test_keys:
        btree.insert(key)
        print(f"Inserted {key}")
    
    search_key = 6
    result = btree.search(search_key)
    print(f"Search for {search_key}: {'Found' if result else 'Not found'}")
