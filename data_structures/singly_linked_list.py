"""
Singly Linked List Implementation
A chain of connected nodes where each node points to the next one,
like a treasure hunt where each clue points to the location of the next clue.
"""

class Node:
    """
    A single node in the linked list, like a box that:
    - Holds some data (the treasure)
    - Has an arrow pointing to the next box

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
    A chain of nodes where each points to the next one.
    Like a scavenger hunt where each location has directions to the next spot.

    Time Complexity:
        - Add to front: O(1)
        - Find node: O(n)
        - Get size: O(n)
    Space Complexity: O(n) where n is number of nodes
    """
    def __init__(self):
        # Start with empty list (no boxes yet)
        self.head = None

    def is_empty(self) -> bool:
        """
        Check if list is empty.
        Like checking if we have any boxes at all.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self.head == None

    def size(self) -> int:
        """
        Count number of nodes in list.
        Like counting boxes by following the arrows.

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
        Add new node at start of list.
        Like adding a new box at the beginning of our treasure hunt.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def node_at_index(self, index: int) -> Node:
        """
        Find node at given position.
        Like following the arrows count times to find a specific box.

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
        Create string showing all nodes.
        Like drawing a map of our treasure hunt.

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
    # Test our linked list
    l = LinkedList()
    
    # Test adding elements
    print("Adding elements 3, 2, 1:")
    l.add(1)
    l.add(2)
    l.add(3)
    print(f"List: {l}")
    
    # Test size and node finding
    print(f"Size: {l.size()}")
    print(f"Node at index 1: {l.node_at_index(1)}")
    
    # Test empty list
    empty_list = LinkedList()
    print(f"\nEmpty list is empty: {empty_list.is_empty()}")
    print(f"Empty list size: {empty_list.size()}")
