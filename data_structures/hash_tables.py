"""
Hash Table Implementation
A data structure that stores key-value pairs using a special function (hash) to determine 
where to store each item, like a filing cabinet where each drawer's number is calculated 
from the file name.
"""

class HashTable:
    """
    Hash table using open addressing with linear probing.
    Like a filing cabinet where we try the next drawer if one is full.

    Time Complexity:
        - Insert: O(1) average, O(n) worst case
        - Search: O(1) average, O(n) worst case
        - Delete: O(1) average, O(n) worst case
    Space Complexity: O(n) where n is table size
    """
    def __init__(self, size=100):
        # Create empty drawers (slots) in our filing cabinet
        self.size = size
        self.table = [None] * size
        self.count = 0

    def _hash(self, key: str) -> int:
        """
        Calculate which drawer to use for a given key.
        Like using a formula to decide which drawer to check.

        Time Complexity: O(k) where k is key length
        Space Complexity: O(1)
        """
        hash_value = 0
        for char in str(key):
            hash_value += ord(char)
        return hash_value % self.size

    def insert(self, key: str, value) -> None:
        """
        Store a key-value pair in the table.
        Like filing a document in the right drawer.

        Time Complexity: O(1) average case
        Space Complexity: O(1)
        """
        if self.count >= self.size:
            raise OverflowError("Filing cabinet is full!")

        index = self._hash(key)
        while self.table[index] is not None:
            # If key exists, update its value
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            # Try next drawer (linear probing)
            index = (index + 1) % self.size

        self.table[index] = (key, value)
        self.count += 1

    def get(self, key: str):
        """
        Retrieve value for a given key.
        Like finding a file in the cabinet.

        Time Complexity: O(1) average case
        Space Complexity: O(1)
        """
        index = self._hash(key)
        original_index = index

        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == original_index:
                break
        return None

    def remove(self, key: str) -> bool:
        """
        Remove a key-value pair from the table.
        Like taking a file out of the cabinet.

        Time Complexity: O(1) average case
        Space Complexity: O(1)
        """
        index = self._hash(key)
        original_index = index

        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                self.count -= 1
                return True
            index = (index + 1) % self.size
            if index == original_index:
                break
        return False

if __name__ == "__main__":
    # Test our hash table
    hash_table = HashTable(10)
    
    # Test insertions
    print("Adding items to hash table:")
    test_data = [
        ("name", "Joe"),
        ("age", 34),
        ("city", "Augusta"),
        ("hobby", "coding")
    ]
    
    for key, value in test_data:
        hash_table.insert(key, value)
        print(f"Added {key}: {value}")
    
    # Test retrievals
    print("\nRetrieving values:")
    for key, _ in test_data:
        print(f"{key}: {hash_table.get(key)}")
    
    # Test removal
    key_to_remove = "age"
    print(f"\nRemoving '{key_to_remove}'")
    hash_table.remove(key_to_remove)
    print(f"After removal, '{key_to_remove}' exists: {hash_table.get(key_to_remove) is not None}")
