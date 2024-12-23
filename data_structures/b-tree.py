"""
B-tree Implementation
A self-balancing tree structure that maintains sorted data and is optimized for disk operations 
(like a file system or database index).
"""

class BNode:
    """
    A node in a B-tree, like a container that can hold multiple values.
    Think of it as a drawer that can store several items in order.

    Time Complexity: O(1) for node creation
    Space Complexity: O(t) where t is minimum degree
    """
    def __init__(self, t, leaf=True):
        # List of values stored in the node (like items in a drawer)
        self.keys = []
        # List of children (like sub-drawers)
        self.children = []
        # Is this a bottom-level node? (like a drawer that can't have sub-drawers)
        self.leaf = leaf
        # How many values are currently stored
        self.n = 0
        # Minimum number of values required (like minimum drawer capacity)
        self.t = t

class BTree:
    """
    B-tree data structure optimized for systems that read/write large blocks of data.
    Like a filing cabinet where each drawer (node) can hold multiple items.

    Time Complexity:
        - Search: O(log n)
        - Insert: O(log n)
        - Delete: O(log n)
    Space Complexity: O(n)

    Properties:
        - All leaves are at same level (like a balanced filing system)
        - Nodes are always at least half full (efficient space usage)
        - Root can have minimum 2 children
        - All other nodes must have at least t-1 keys
        - All nodes can have at most 2t-1 keys
    """
    def __init__(self, t):
        # Create empty root node (like setting up first drawer)
        self.root = BNode(t, True)
        # Minimum degree (minimum capacity of each drawer)
        self.t = t

    def search(self, k):
        """
        Look for a value in the B-tree.
        Like searching for a file in a filing system.

        Args:
            k: Value to search for

        Returns:
            Tuple of (node, position) if found, None if not found

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        return self._search_recursive(self.root, k)

    def _search_recursive(self, x, k):
        # Find the right position in current node
        i = 0
        while i < x.n and k > x.keys[i]:
            i += 1

        # Found the key?
        if i < x.n and k == x.keys[i]:
            return (x, i)

        # If we're at a leaf and haven't found it, it's not in the tree
        if x.leaf:
            return None

        # Otherwise, search the appropriate child
        return self._search_recursive(x.children[i], k)

    def insert(self, k):
        """
        Add a new value to the B-tree.
        Like filing a new document in the correct drawer.

        Args:
            k: Value to insert

        Time Complexity: O(log n)
        Space Complexity: O(log n)
        """
        r = self.root
        # If root is full, split it
        if r.n == (2 * self.t) - 1:
            s = BNode(self.t, False)
            self.root = s
            s.children.append(r)
            self._split_child(s, 0)
            self._insert_nonfull(s, k)
        else:
            self._insert_nonfull(r, k)
            
    def _split_child(self, x, i):
        """
        Split a full child node.
        Like splitting an overfull drawer into two drawers.

        Time Complexity: O(t) where t is minimum degree
        Space Complexity: O(t)
        """
        t = self.t
        y = x.children[i]
        z = BNode(t, y.leaf)
        
        # Move the middle key up to the parent
        middle_key = y.keys[t-1]
        
        # Split the keys
        z.keys = y.keys[t:]  # Right half
        y.keys = y.keys[:t-1]  # Left half
        
        # If not leaf, split the children
        if not y.leaf:
            z.children = y.children[t:]  # Right half
            y.children = y.children[:t]  # Left half
        
        # Update counts
        z.n = len(z.keys)
        y.n = len(y.keys)
        
        # Insert new child into parent
        x.children.insert(i + 1, z)
        x.keys.insert(i, middle_key)
        x.n = len(x.keys)

    def _insert_nonfull(self, x, k):
        """
        Insert a key into a non-full node.
        Like adding a file to a drawer that has space.

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        i = x.n - 1
        
        if x.leaf:
            # Find location to insert and move all greater keys ahead
            while i >= 0 and k < x.keys[i]:
                i -= 1
            x.keys.insert(i+1, k)
            x.n += 1
        else:
            # Find child which is going to have the new key
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            
            # If child is full, split it
            if len(x.children[i].keys) == (2 * self.t) - 1:
                self._split_child(x, i)
                if k > x.keys[i]:
                    i += 1
                    
            self._insert_nonfull(x.children[i], k)

if __name__ == "__main__":
    # Test our B-tree
    btree = BTree(3)  # Each node can have between 2 and 5 keys
    
    # Test insertions
    test_keys = [10, 20, 5, 6, 12, 30, 7, 17]
    print("Inserting values:", test_keys)
    for key in test_keys:
        btree.insert(key)
        print(f"Inserted {key}")
    
    # Test searching
    search_tests = [6, 15]
    for key in search_tests:
        result = btree.search(key)
        print(f"Searching for {key}: {'Found' if result else 'Not found'}")
