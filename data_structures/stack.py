"""
Stack Implementation
A data structure that follows Last-In-First-Out (LIFO) principle,
like a stack of plates where you can only add or remove from the top.
"""

class Stack:
    """
    Stack using a list for storage.
    Like a stack of plates where you can only interact with the top plate.

    Time Complexity:
        - Push (Add): O(1) amortized
        - Pop (Remove): O(1)
        - Peek (Look): O(1)
    Space Complexity: O(n) where n is number of items
    """
    def __init__(self):
        # Start with empty stack (no plates)
        self.items = []

    def push(self, item) -> None:
        """
        Add item to top of stack.
        Like placing a new plate on top.

        Time Complexity: O(1) amortized
        Space Complexity: O(1)
        """
        self.items.append(item)

    def pop(self):
        """
        Remove and return top item.
        Like taking the top plate off.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        """
        Look at top item without removing it.
        Like looking at the top plate without touching it.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self) -> bool:
        """
        Check if stack is empty.
        Like checking if we have any plates.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return len(self.items) == 0

    def size(self) -> int:
        """
        Get number of items in stack.
        Like counting how many plates we have.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return len(self.items)

    def __str__(self) -> str:
        """Show contents of stack."""
        return f"Stack: {self.items}"

if __name__ == "__main__":
    # Test our stack
    stack = Stack()
    
    # Test empty stack
    print(f"Empty stack: {stack}")
    print(f"Is empty: {stack.is_empty()}")
    
    # Test pushing elements
    print("\nPushing elements:")
    for item in [1, 2, 3]:
        stack.push(item)
        print(f"After pushing {item}: {stack}")
    
    print(f"\nStack size: {stack.size()}")
    print(f"Top element: {stack.peek()}")
    
    # Test popping elements
    print("\nPopping elements:")
    while not stack.is_empty():
        print(f"Popped: {stack.pop()}")
        print(f"Remaining stack: {stack}")
    
    # Test edge cases
    print("\nTesting edge cases:")
    empty_stack = Stack()
    print(f"Empty stack pop: {empty_stack.pop()}")
    print(f"Empty stack peek: {empty_stack.peek()}")
