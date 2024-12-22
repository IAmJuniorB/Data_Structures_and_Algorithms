"""
Binary Heap (Min/Max)
"""
class BinaryHeap:
    def __init__(self, max_heap=False):
        """
        Initialize empty binary heap.

        Args:
            max_heap (bool): If True, creates max heap; if False, creates min heap

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.heap = []
        self.max_heap = max_heap

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def insert(self, key):
        """
        Insert new key into heap.

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def extract(self):
        """
        Extract root element.

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
    print("Testing Min Heap:")
    min_heap = BinaryHeap()
    test_values = [3, 7, 1, 5, 2, 4, 6]
    
    print("Inserting values:", test_values)
    for value in test_values:
        min_heap.insert(value)
    
    print("\nExtracting values:")
    while min_heap.heap:
        print(min_heap.extract())
        
    print("\nTesting Max Heap:")
    max_heap = BinaryHeap(max_heap=True)
    for value in test_values:
        max_heap.insert(value)
        
    print("Extracting values:")
    while max_heap.heap:
        print(max_heap.extract())
        
    print("\nTesting edge cases:")
    empty_heap = BinaryHeap()
    print("Empty heap extract:", empty_heap.extract())
    
    single_element = BinaryHeap()
    single_element.insert(1)
    print("Single element extract:", single_element.extract())
