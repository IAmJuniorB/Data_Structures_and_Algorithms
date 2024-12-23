"""
Priority Queue Implementation
A queue where each element has a priority, like a hospital emergency room where 
patients are seen based on urgency rather than arrival time.
"""

class PriorityQueue:
    """
    Priority Queue using a binary heap for efficient priority management.
    Like a hospital triage system that automatically organizes patients by urgency.

    Time Complexity:
        - Enqueue (Add): O(log n)
        - Dequeue (Remove): O(log n)
        - Peek: O(1)
    Space Complexity: O(n) where n is number of items
    """
    def __init__(self):
        self.heap = []
        self.size = 0

    def _parent(self, i):
        return (i - 1) // 2

    def _left_child(self, i):
        return 2 * i + 1

    def _right_child(self, i):
        return 2 * i + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def enqueue(self, item, priority):
        """
        Add item with given priority.
        Like adding a new patient to the emergency room.

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        self.heap.append((priority, item))
        self._sift_up(len(self.heap) - 1)
        self.size += 1

    def dequeue(self):
        """
        Remove and return highest priority item.
        Like calling the next patient based on urgency.

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        if not self.heap:
            return None

        if len(self.heap) == 1:
            self.size -= 1
            return self.heap.pop()[1]

        root = self.heap[0][1]
        self.heap[0] = self.heap.pop()
        self.size -= 1
        if self.heap:
            self._sift_down(0)
        return root

    def _sift_up(self, i):
        parent = self._parent(i)
        if i > 0 and self.heap[i][0] < self.heap[parent][0]:
            self._swap(i, parent)
            self._sift_up(parent)

    def _sift_down(self, i):
        min_index = i
        left = self._left_child(i)
        right = self._right_child(i)

        if left < len(self.heap) and self.heap[left][0] < self.heap[min_index][0]:
            min_index = left

        if right < len(self.heap) and self.heap[right][0] < self.heap[min_index][0]:
            min_index = right

        if i != min_index:
            self._swap(i, min_index)
            self._sift_down(min_index)

if __name__ == "__main__":
    # Test our priority queue
    pq = PriorityQueue()
    
    # Test insertions
    test_items = [
        ("Critical Patient", 1),
        ("Moderate Case", 3),
        ("Minor Injury", 5),
        ("Emergency Case", 2),
        ("Routine Checkup", 4)
    ]
    
    print("Adding items to queue:")
    for item, priority in test_items:
        print(f"Adding {item} with priority {priority}")
        pq.enqueue(item, priority)
    
    print("\nProcessing items (should be in priority order):")
    while pq.size > 0:
        item = pq.dequeue()
        print(f"Processing: {item}")
    
    # Test edge cases
    print("\nTesting edge cases:")
    empty_pq = PriorityQueue()
    print("Empty queue dequeue:", empty_pq.dequeue())
    
    single_pq = PriorityQueue()
    single_pq.enqueue("Single Item", 1)
    print("Single item dequeue:", single_pq.dequeue())
