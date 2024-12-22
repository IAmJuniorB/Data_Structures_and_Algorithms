class HashTable:
    """
    Hash table implementation using open addressing with linear probing.

    Attributes:
        size (int): Size of the hash table
        table (list): Internal list to store key-value pairs
        count (int): Number of items in the hash table

    Time Complexity:
        - Insert: O(1) average, O(n) worst case
        - Search: O(1) average, O(n) worst case
        - Delete: O(1) average, O(n) worst case
    Space Complexity: O(n) where n is the size of the hash table
    """
    def __init__(self, size=100):
        """
        Initialize empty hash table.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        self.size = size
        self.table = [None] * size
        self.count = 0

    def _hash(self, key: str) -> int:
        """
        Generate hash value for a key.

        Args:
            key (str): Key to be hashed

        Returns:
            int: Hash value between 0 and table size - 1

        Time Complexity: O(k) where k is length of key
        Space Complexity: O(1)
        """
        hash_value = 0
        for char in str(key):
            hash_value += ord(char)
        return hash_value % self.size

    def insert(self, key: str, value) -> None:
        """
        Insert a key-value pair into the hash table.

        Args:
            key (str): Key for the value
            value: Value to be stored

        Time Complexity: O(1) average case
        Space Complexity: O(1)

        Example:
            >>> ht = HashTable()
            >>> ht.insert("name", "Joe")
            >>> ht.get("name")
            'Joe'
        """
        if self.count >= self.size:
            raise OverflowError("Hash table is full")

        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size

        self.table[index] = (key, value)
        self.count += 1

    def get(self, key: str):
        """
        Retrieve value associated with key.

        Args:
            key (str): Key to look up

        Returns:
            Value associated with key or None if not found

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
        Remove key-value pair from hash table.

        Args:
            key (str): Key to remove

        Returns:
            bool: True if removed, False if not found

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

    def __str__(self) -> str:
        """
        Return string representation of the hash table.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        return str([item for item in self.table if item is not None])

if __name__ == "__main__":
    hash_table = HashTable(10)
    
    # Testing again
    hash_table.insert("name", "Joe")
    hash_table.insert("age", 25)
    hash_table.insert("city", "Augusta")
    print(f"Hash table after insertions: {hash_table}")
    
    print(f"Get 'name': {hash_table.get('name')}")
    print(f"Get 'age': {hash_table.get('age')}")
    print(f"Get 'invalid': {hash_table.get('invalid')}")
    
    print(f"Remove 'age': {hash_table.remove('age')}")
    print(f"Hash table after removal: {hash_table}")
