class Stack:
    """
    Stack implementation using a Python list with LIFO (Last In, First Out) behavior.

    Attributes:
        items (list): Internal list to store stack elements

    Time Complexity:
        - Push: O(1) amortized
        - Pop: O(1)
        - Peek: O(1)
        - is_empty: O(1)
        - size: O(1)
    Space Complexity: O(n) where n is the number of elements in the stack
    """
    def __init__(self):
        """
        Initialize empty stack.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.items = []

    def push(self, item) -> None:
        """
        Add an item to the top of the stack.

        Args:
            item: Element to be pushed onto stack

        Time Complexity: O(1) amortized
        Space Complexity: O(1)

        Example:
            >>> s = Stack()
            >>> s.push(5)
            >>> s.peek()
            5
        """
        self.items.append(item)

    def pop(self):
        """
        Remove and return the top item from the stack.

        Returns:
            The top item if stack is not empty, None otherwise

        Time Complexity: O(1)
        Space Complexity: O(1)

        Example:
            >>> s = Stack()
            >>> s.push(5)
            >>> s.pop()
            5
        """
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        """
        Return the top item without removing it.

        Returns:
            The top item if stack is not empty, None otherwise

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self) -> bool:
        """
        Check if the stack is empty.

        Returns:
            bool: True if stack is empty, False otherwise

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return len(self.items) == 0

    def size(self) -> int:
        """
        Return the number of items in the stack.

        Returns:
            int: Number of items in stack

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return len(self.items)

    def __str__(self) -> str:
        """
        Return string representation of the stack.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        return f"Stack: {self.items}"

if __name__ == "__main__":
    # Test implementation
    stack = Stack()
    
    # Test empty stack
    print(f"Empty stack: {stack}")
    print(f"Is empty: {stack.is_empty()}")
    
    # Test pushing elements
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"After pushing 1, 2, 3: {stack}")
    print(f"Size: {stack.size()}")
    
    # Test peek
    print(f"Peek at top element: {stack.peek()}")
    
    # Test pop
    print(f"Pop top element: {stack.pop()}")
    print(f"After pop: {stack}")
    
    # Test multiple operations
    stack.push(4)
    print(f"After pushing 4: {stack}")
    print(f"Final size: {stack.size()}")
