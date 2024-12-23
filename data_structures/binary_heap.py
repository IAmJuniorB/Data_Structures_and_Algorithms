"""
Binary Heap Implementation
A complete binary tree that satisfies the heap property - parent is always smaller 
(min heap) or larger (max heap) than its children.
"""

class BinaryHeap:
    """
    Binary Heap implementation supporting both min and max heaps.

    Time Complexity:
        - Insert: O(log n)
        - Extract min/max: O(log n)
        - Get min/max: O(1)
        - Heapify: O(log n)
    Space Complexity: O(n) where n is number of elements
    """
    def __init__(self, max_heap=False):
        # Store heap elements in a list (like a pyramid of numbers)
        self.heap = []
        # True for max heap (largest on top), False for min heap (smallest on top)
        self.max_heap = max_heap

    def parent(self, i):
        """Find parent's position, like finding a parent in a family tree."""
        return (i - 1) // 2

    def left_child(self, i):
        """Find left child's position, like finding left branch in a tree."""
        return 2 * i + 1

    def right_child(self, i):
        """Find right child's position, like finding right branch in a tree."""
        return 2 * i + 2

    def _compare(self, a, b):
        """Compare two values based on heap type."""
        if self.max_heap:
            return a > b  # For max heap, larger is better
        return a < b  # For min heap, smaller is better

    def _swap(self, i, j):
        """Swap two elements, like trading baseball cards."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_up(self, index):
        """
        Move a value up the heap until it's in the right spot.
        Like a bubble floating up in water.

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        parent = self.parent(index)
        if index > 0 and self._compare(self.heap[index], self.heap[parent]):
            self._swap(index, parent)
            self._heapify_up(parent)

    def _heapify_down(self, index):
        """
        Move a value down the heap until it's in the right spot.
        Like a heavy stone sinking in water.

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self._compare(self.heap[left], self.heap[smallest]):
            smallest = left

        if right < len(self.heap) and self._compare(self.heap[right], self.heap[smallest]):
            smallest = right

        if smallest != index:
            self._swap(index, smallest)
            self._heapify_down(smallest)

    def insert(self, key):
        """
        Add new value to heap.
        Like adding a new block to a pyramid.

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def extract(self):
        """
        Remove and return the top element.
        Like taking the top block off a pyramid.

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        if not self.heap:
            return None

        root = self.heap[0]
        last_element = self.heap.pop()
        
        if self.heap:
            self.heap[0] = last_element
            self._heapify_down(0)

        return root

if __name__ == "__main__":
    # Test Min Heap
    print("Testing Min Heap:")
    min_heap = BinaryHeap()
    test_values = [3, 7, 1, 5, 2, 4, 6]
    
    print("Inserting values:", test_values)
    for value in test_values:
        min_heap.insert(value)
        print(f"Heap after inserting {value}:", min_heap.heap)

    print("\nExtracting values (should be in ascending order):")
    while min_heap.heap:
        print(f"Extracted: {min_heap.extract()}, Remaining heap: {min_heap.heap}")

    # Test Max Heap
    print("\nTesting Max Heap:")
    max_heap = BinaryHeap(max_heap=True)
    print("Inserting same values:", test_values)
    for value in test_values:
        max_heap.insert(value)
        print(f"Heap after inserting {value}:", max_heap.heap)

    print("\nExtracting values (should be in descending order):")
    while max_heap.heap:
        print(f"Extracted: {max_heap.extract()}, Remaining heap: {max_heap.heap}")

    # Test edge cases
    print("\nTesting edge cases:")
    empty_heap = BinaryHeap()
    print("Empty heap extract:", empty_heap.extract())
    
    single_element = BinaryHeap()
    single_element.insert(1)
    print("Single element extract:", single_element.extract())
