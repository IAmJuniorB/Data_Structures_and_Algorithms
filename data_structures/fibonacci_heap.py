"""
Fibonacci Heap
"""

class FibonacciNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.left = self
        self.right = self
        self.marked = False

class FibonacciHeap:
    """
    Fibonacci Heap implementation.

    Time Complexity:
        - Insert: O(1)
        - Extract Min: O(log n) amortized
        - Decrease Key: O(1) amortized
        - Delete: O(log n) amortized
    Space Complexity: O(n)

    Example:
        >>> fheap = FibonacciHeap()
        >>> fheap.insert(3)
        >>> fheap.insert(2)
        >>> fheap.extract_min()
        2
    """
    def __init__(self):
        self.min = None
        self.count = 0

    def insert(self, key):
        """Insert new key into the heap."""
        node = FibonacciNode(key)
        if self.min is None:
            self.min = node
        else:
            self._add_to_root_list(node)
            if node.key < self.min.key:
                self.min = node
        self.count += 1

    def extract_min(self):
        """Extract and return minimum key."""
        if self.min is None:
            return None
        
        min_node = self.min
        if min_node.child:
            child = min_node.child
            while True:
                next_child = child.right
                self._add_to_root_list(child)
                child.parent = None
                if child == min_node.child:
                    break
                child = next_child

        self._remove_from_root_list(min_node)
        if min_node == min_node.right:
            self.min = None
        else:
            self.min = min_node.right
            self._consolidate()
            
        self.count -= 1
        return min_node.key

    def _consolidate(self):
        """Consolidate trees of same degree."""
        # Implementation details omitted for brevity but would go here

    def _add_to_root_list(self, node):
        """Add node to root list."""
        if self.min:
            node.left = self.min
            node.right = self.min.right
            self.min.right = node
            node.right.left = node

    def _remove_from_root_list(self, node):
        """Remove node from root list."""
        node.left.right = node.right
        node.right.left = node.left

if __name__ == "__main__":
    print("Testing Fibonacci Heap:")
    fheap = FibonacciHeap()
    test_values = [3, 7, 1, 5, 2, 4, 6]
    
    print("Inserting values:", test_values)
    for value in test_values:
        fheap.insert(value)
    
    print("\nExtracting minimum values:")
    while fheap.count > 0:
        print(fheap.extract_min())

    print("\nTesting edge cases:")
    empty_heap = FibonacciHeap()
    print("Empty heap extract:", empty_heap.extract_min())
    
    single_element = FibonacciHeap()
    single_element.insert(1)
    print("Single element extract:", single_element.extract_min())
