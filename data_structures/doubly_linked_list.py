"""
Doubly Linked List Implementation
A list where each element points to both its previous and next neighbors,
like a chain where each link is connected to the ones before and after it.
"""

class Node:
    """
    A single element in the doubly linked list, like a box containing:
    - Some data (the value)
    - A link to the previous box
    - A link to the next box

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
    A list of connected nodes, each pointing to its neighbors.
    Like a train where each car is connected to the ones before and after it.

    Time Complexity:
        - Add: O(1)
        - Remove: O(n)
        - Search: O(n)
    Space Complexity: O(n) where n is number of nodes
    """
    def __init__(self):
        self.head = None
        self.__count = 0

    def is_empty(self) -> bool:
        """
        Check if the list is empty.
        Like checking if the train has any cars.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self.head is None

    def __len__(self) -> int:
        """
        Get the number of nodes in the list.
        Like counting the cars in a train.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self.__count

    def add(self, data) -> None:
        """
        Add a new node at the start of the list.
        Like adding a new car to the front of a train.

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
        Remove the first node with matching data.
        Like removing a specific car from the train.

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
        Create a string representation of the list.
        Like describing the train car by car.

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
    # Test our doubly linked list
    dll = DoublyLinkedList()
    
    # Add some numbers
    print("Adding numbers to list:")
    for num in [3, 1, 4, 1, 5]:
        dll.add(num)
        print(f"Added {num}, List: {dll}")
    
    print(f"\nList size: {len(dll)}")
    
    # Test removal
    remove_key = 1
    removed = dll.remove(remove_key)
    print(f"\nRemoved first {remove_key}: {dll}")
    print(f"New size: {len(dll)}")
    
    # Test empty check
    print(f"\nIs list empty? {dll.is_empty()}")
