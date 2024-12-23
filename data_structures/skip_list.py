"""
Skip List Implementation
A probabilistic data structure that allows for faster search by maintaining multiple 
sorted linked lists at different levels, like an express elevator that can skip floors.
"""

import random

class Node:
    """
    A node in the skip list, like a building floor that:
    - Holds a value (data)
    - Has multiple express routes to other floors
    
    Time Complexity: O(1) for node creation
    Space Complexity: O(level) for storing express routes
    """
    def __init__(self, data, level):
        self.data = data
        # Express routes to other nodes (like elevator buttons)
        self.next_nodes = [None] * (level + 1)

    def __repr__(self):
        return f"{self.data}"

class SkipList:
    """
    A layered linked list with express lanes for faster searching.
    Like a building with express elevators that can skip floors.

    Time Complexity:
        - Search: O(log n) average, O(n) worst case
        - Insert: O(log n) average, O(n) worst case
        - Delete: O(log n) average, O(n) worst case
    Space Complexity: O(n) where n is number of elements
    """
    def __init__(self, max_level=4, p=0.5):
        # Maximum number of express routes
        self.max_level = max_level
        # Probability of creating express routes
        self.p = p
        # Entry point to our building
        self.header = Node(None, max_level)
        # Current highest express route
        self.current_level = 0

    def random_level(self):
        """
        Decide how many express routes to create.
        Like randomly choosing which elevator buttons to install.

        Time Complexity: O(max_level)
        Space Complexity: O(1)
        """
        level = 0
        while random.random() < self.p and level < self.max_level:
            level += 1
        return level

    def insert(self, data):
        """
        Add a new value to the skip list.
        Like adding a new floor with the right elevator connections.

        Time Complexity: O(log n) average case
        Space Complexity: O(max_level)
        """
        update = [None] * (self.max_level + 1)
        current = self.header

        # Find where to insert at each level
        for i in range(self.current_level, -1, -1):
            while current.next_nodes[i] and current.next_nodes[i].data < data:
                current = current.next_nodes[i]
            update[i] = current

        # Create new node with random number of express routes
        level = self.random_level()
        if level > self.current_level:
            for i in range(self.current_level + 1, level + 1):
                update[i] = self.header
            self.current_level = level

        new_node = Node(data, level)
        
        # Connect all routes
        for i in range(level + 1):
            new_node.next_nodes[i] = update[i].next_nodes[i]
            update[i].next_nodes[i] = new_node

    def search(self, data):
        """
        Look for a value in the skip list.
        Like using express elevators to quickly find the right floor.

        Time Complexity: O(log n) average case
        Space Complexity: O(1)
        """
        current = self.header
        
        # Start from highest level and work down
        for i in range(self.current_level, -1, -1):
            while current.next_nodes[i] and current.next_nodes[i].data < data:
                current = current.next_nodes[i]

        current = current.next_nodes[0]
        
        if current and current.data == data:
            return current
        return None

    def __str__(self):
        """
        Show the skip list structure.
        Like drawing a building's elevator diagram.

        Time Complexity: O(n * level)
        Space Complexity: O(n * level)
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
    # Test our skip list
    skip_list = SkipList(max_level=3)
    
    # Test insertions
    test_data = [3, 6, 7, 9, 12, 19, 17, 26, 21, 25]
    print("Inserting values:", test_data)
    for num in test_data:
        skip_list.insert(num)
    
    print("\nSkip List structure:")
    print(skip_list)
    
    # Test searching
    print("\nSearch Tests:")
    for num in [19, 20]:  # Test both existing and non-existing values
        result = skip_list.search(num)
        print(f"Search for {num}: {'Found' if result else 'Not found'}")
