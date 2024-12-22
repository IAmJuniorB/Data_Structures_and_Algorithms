class Node:
    """
    An object for storing a single node of a linked list.
    
    Attributes:
        data: The value stored in the node
        next_node: Reference to the next node

    Time Complexity: O(1) for all operations
    Space Complexity: O(1)
    """
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return f"{self.data}"

class LinkedList:
    """
    Singly linked list implementation.
    
    Attributes:
        head: First node of the linked list

    Example:
        >>> l = LinkedList()
        >>> l.add(1)
        >>> l.add(2)
        >>> print(l)
        [Head: 2]->[Tail: 1]
    """
    def __init__(self):
        self.head = None

    def is_empty(self) -> bool:
        """
        Check if list is empty.
        
        Time Complexity: O(1)
        """
        return self.head == None

    def size(self) -> int:
        """
        Returns number of nodes in the list.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count

    def add(self, data) -> None:
        """
        Add new Node containing data at head of list.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def node_at_index(self, index: int) -> Node:
        """
        Return node at specified index.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if index == 0:
            return self.head
        current = self.head
        position = 0
        while position < index:
            current = current.next_node
            position += 1
        return current

    def __repr__(self) -> str:
        """
        Return string representation of the list.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node is None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"[{current.data}]")
            current = current.next_node
        return '->'.join(nodes)

if __name__ == "__main__":
    # Test implementation
    l = LinkedList()
    l.add(1)
    l.add(2)
    l.add(3)
    print(f"List: {l}")
    print(f"Size: {l.size()}")
    print(f"Node at index 1: {l.node_at_index(1)}")