"""
Queue Implementation
A data structure that follows First-In-First-Out (FIFO) principle, 
like a line of people waiting for a bus where the first person to arrive is the first to board.
"""

class Queue:
    """
    Queue using a list for storage.
    Like a line of people where new people join at the back and leave from the front.

    Time Complexity:
        - Enqueue (Join line): O(1) amortized
        - Dequeue (Leave line): O(n)
        - Front (Check first person): O(1)
    Space Complexity: O(n) where n is number of items
    """
    def __init__(self):
        # Start with empty line
        self.items = []

    def enqueue(self, item):
        """
        Add item to end of queue.
        Like a person joining the back of the line.

        Time Complexity: O(1) amortized
        Space Complexity: O(1)
        """
        self.items.append(item)

    def dequeue(self):
        """
        Remove and return first item.
        Like the first person leaving the line.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def front(self):
        """
        See who's first in line without removing them.
        Like checking who's at the front of the line.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        """
        Check if queue is empty.
        Like checking if there's anyone in line.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return len(self.items) == 0

    def size(self):
        """
        Get number of items in queue.
        Like counting how many people are in line.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return len(self.items)

    def __str__(self):
        """Show contents of queue."""
        return f"Queue: {self.items}"

if __name__ == "__main__":
    # Test our queue
    queue = Queue()
    
    print("Testing Queue Operations:")
    print(f"Empty queue: {queue}")
    print(f"Is empty: {queue.is_empty()}")
    
    # Test adding items
    print("\nAdding people to line:")
    for person in ["Alice", "Bob", "Charlie"]:
        queue.enqueue(person)
        print(f"After {person} joins: {queue}")
    
    print(f"\nPeople in line: {queue.size()}")
    print(f"First person: {queue.front()}")
    
    # Test removing items
    print("\nPeople leaving line:")
    while not queue.is_empty():
        person = queue.dequeue()
        print(f"{person} left, Remaining line: {queue}")
    
    # Test edge cases
    print("\nTesting edge cases:")
    empty_queue = Queue()
    print(f"Empty queue dequeue: {empty_queue.dequeue()}")
    print(f"Empty queue front: {empty_queue.front()}")
