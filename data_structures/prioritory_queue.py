"""
Priority Queue
"""
class PriorityQueue:
    def __init__(self):
        """
        Initialize priority queue using binary heap.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.heap = BinaryHeap()

    def enqueue(self, item, priority):
        """
        Add item with priority.

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        self.heap.insert((priority, item))

    def dequeue(self):
        """
        Remove and return highest priority item.

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        return self.heap.extract()[1] if self.heap.heap else None

if __name__ == "__main__":
    pq = PriorityQueue()
    
    print("Testing Priority Queue:")
    test_items = [
        ("Task 1", 3),
        ("Task 2", 1),
        ("Task 3", 4),
        ("Task 4", 1),
        ("Task 5", 2)
    ]
    
    print("Enqueueing items:")
    for item, priority in test_items:
        print(f"Adding {item} with priority {priority}")
        pq.enqueue(item, priority)
    
    print("\nDequeueing items:")
    while True:
        item = pq.dequeue()
        if item is None:
            break
        print(f"Dequeued: {item}")
    
    print("\nTesting edge cases:")
    empty_pq = PriorityQueue()
    print("Empty queue dequeue:", empty_pq.dequeue())
    
    single_item_pq = PriorityQueue()
    single_item_pq.enqueue("Single Task", 1)
    print("Single item dequeue:", single_item_pq.dequeue())
