class Queue:
    """
    Queue implementation using a Python list with FIFO (First In, First Out) behavior.

    Attributes:
        items (list): Internal list to store queue elements

    Time Complexity:
        - Enqueue: O(1) amortized
        - Dequeue: O(n)
        - Front: O(1)
        - is_empty: O(1)
        - size: O(1)
    Space Complexity: O(n) where n is the number of elements in the queue
    """
    def __init__(self):
        """
        Initialize empty queue.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.items = []

    def enqueue(self, item) -> None:
        """
        Add an item to the end of the queue.

        Args:
            item: Element to be added to queue

        Time Complexity: O(1) amortized
        Space Complexity: O(1)

        Example:
            >>> q = Queue()
            >>> q.enqueue(5)
            >>> q.front()
            5
        """
        self.items.append(item)

    def dequeue(self):
        """
        Remove and return the first item in the queue.

        Returns:
            The first item if queue is not empty, None otherwise

        Time Complexity: O(n) - requires shifting all elements
        Space Complexity: O(1)

        Example:
            >>> q = Queue()
            >>> q.enqueue(5)
            >>> q.dequeue()
            5
        """
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def front(self):
        """
        Return the first item without removing it.

        Returns:
            The first item if queue is not empty, None otherwise

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self) -> bool:
        """
        Check if the queue is empty.

        Returns:
            bool: True if queue is empty, False otherwise

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return len(self.items) == 0

    def size(self) -> int:
        """
        Return the number of items in the queue.

        Returns:
            int: Number of items in queue

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return len(self.items)

    def __str__(self) -> str:
        """
        Return string representation of the queue.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        return f"Queue: {self.items}"

if __name__ == "__main__":
    queue = Queue()
    
    # Just a bunch of tests below to show the code is working.
    print(f"Empty queue: {queue}")
    print(f"Is empty: {queue.is_empty()}")
    
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(f"After enqueuing 1, 2, 3: {queue}")
    print(f"Size: {queue.size()}")
    
    print(f"Front element: {queue.front()}")
    
    print(f"Dequeue first element: {queue.dequeue()}")
    print(f"After dequeue: {queue}")
    
    queue.enqueue(4)
    print(f"After enqueuing 4: {queue}")
    print(f"Final size: {queue.size()}")
