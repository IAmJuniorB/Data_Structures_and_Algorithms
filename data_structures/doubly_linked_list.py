class Node:
    """
    A node in a doubly linked list.

    Attributes:
        data: The value stored in the node
        prev_node: Reference to the previous node
        next_node: Reference to the next node

    Time Complexity: O(1) for all operations
    Space Complexity: O(1)
    """
    def __init__(self, data, prev_node=None, next_node=None):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node

    def __repr__(self):
        return f"{self.data}"

class DoublyLinkedList:
    """
    Doubly linked list implementation where each node points to both 
    previous and next nodes.

    Attributes:
        head: First node of the list
        __count: Private counter for list size

    Example:
        >>> dll = DoublyLinkedList()
        >>> dll.add(1)
        >>> dll.add(2)
        >>> len(dll)
        2
    """
    def __init__(self):
        self.head = None
        self.__count = 0

    def is_empty(self) -> bool:
        """
        Check if list is empty.

        Time Complexity: O(1)
        Space Complexity: O(1)

        Returns:
            bool: True if list is empty, False otherwise
        """
        return self.head is None

    def __len__(self) -> int:
        """
        Get the number of nodes in the list.

        Time Complexity: O(1)
        Space Complexity: O(1)

        Returns:
            int: Number of nodes in the list
        """
        return self.__count

    def add(self, data) -> None:
        """
        Add a new node containing data at the head of the list.

        Args:
            data: Value to be stored in the new node

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        new_node = Node(data)
        self.__count += 1
        
        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head.prev_node = new_node
            self.head = new_node

    def remove(self, key) -> Node:
        """
        Remove and return the first node with data matching the key.

        Args:
            key: Value to search for and remove

        Returns:
            Node: Removed node or None if not found

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        current = self.head
        
        while current:
            if current.data == key:
                self.__count -= 1
                
                if current.prev_node:
                    current.prev_node.next_node = current.next_node
                else:
                    self.head = current.next_node
                    
                if current.next_node:
                    current.next_node.prev_node = current.prev_node
                    
                return current
                
            current = current.next_node
        return None

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
        return '<->'.join(nodes)

if __name__ == "__main__":
    dll = DoublyLinkedList()
    
    dll.add(1)
    dll.add(2)
    dll.add(3)
    print(f"Initial list: {dll}")
    print(f"Size: {len(dll)}")

    removed = dll.remove(2)
    print(f"After removing {removed}: {dll}")
    print(f"New size: {len(dll)}")

    print(f"Is empty: {dll.is_empty()}")
