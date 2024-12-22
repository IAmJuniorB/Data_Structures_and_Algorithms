import random

class Node:
    """
    Node in a skip list.

    Attributes:
        data: Value stored in the node
        next_nodes: List of references to next nodes at each level

    Time Complexity: O(1) for node creation
    Space Complexity: O(level) for storing next node references
    """
    def __init__(self, data, level):
        self.data = data
        self.next_nodes = [None] * (level + 1)

    def __repr__(self):
        return f"{self.data}"

class SkipList:
    """
    Skip list implementation with probabilistic balancing.

    Attributes:
        max_level (int): Maximum allowed level in the skip list
        p (float): Probability factor for level generation
        header: Head node of the skip list
        current_level (int): Current maximum level in use

    Time Complexity:
        - Search: O(log n) average, O(n) worst case
        - Insert: O(log n) average, O(n) worst case
        - Delete: O(log n) average, O(n) worst case
    Space Complexity: O(n) where n is number of elements
    """
    def __init__(self, max_level=4, p=0.5):
        self.max_level = max_level
        self.p = p
        self.header = Node(None, max_level)
        self.current_level = 0

    def random_level(self) -> int:
        """
        Generate random level for a new node.

        Returns:
            int: Random level between 0 and max_level
        """
        level = 0
        while random.random() < self.p and level < self.max_level:
            level += 1
        return level

    def insert(self, data) -> None:
        """
        Insert a new element into the skip list.

        Args:
            data: Value to insert

        Time Complexity: O(log n) average case
        """
        update = [None] * (self.max_level + 1)
        current = self.header

        for i in range(self.current_level, -1, -1):
            while current.next_nodes[i] and current.next_nodes[i].data < data:
                current = current.next_nodes[i]
            update[i] = current

        level = self.random_level()
        if level > self.current_level:
            for i in range(self.current_level + 1, level + 1):
                update[i] = self.header
            self.current_level = level

        new_node = Node(data, level)
        for i in range(level + 1):
            new_node.next_nodes[i] = update[i].next_nodes[i]
            update[i].next_nodes[i] = new_node

    def search(self, data):
        """
        Search for an element in the skip list.

        Args:
            data: Value to search for

        Returns:
            Node if found, None otherwise

        Time Complexity: O(log n) average case
        """
        current = self.header
        for i in range(self.current_level, -1, -1):
            while current.next_nodes[i] and current.next_nodes[i].data < data:
                current = current.next_nodes[i]
        current = current.next_nodes[0]
        if current and current.data == data:
            return current
        return None

    def __str__(self) -> str:
        """
        Return string representation of skip list.

        Time Complexity: O(n*level) where n is number of nodes
        """
        result = []
        for level in range(self.current_level + 1):
            current = self.header.next_nodes[level]
            level_str = f"Level {level}: "
            while current:
                level_str += f"{current.data} -> "
                current = current.next_nodes[level]
            level_str += "None"
            result.append(level_str)
        return "\n".join(result)

if __name__ == "__main__":
    skip_list = SkipList(max_level=3)
    
    # Testing
    test_data = [3, 6, 7, 9, 12, 19, 17, 26, 21, 25]
    for num in test_data:
        skip_list.insert(num)
    print("Skip List after insertions:")
    print(skip_list)
    
    print("\nSearch Tests:")
    print(f"Search for 19: {skip_list.search(19)}")
    print(f"Search for 20: {skip_list.search(20)}")
