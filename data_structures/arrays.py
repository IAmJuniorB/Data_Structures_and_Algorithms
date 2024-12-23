"""
Raw Array Implementation
"""

import ctypes

class Array:
    """
    Pure array implementation using memory blocks.
    No built-in Python functions or data structures used.

    Time Complexity:
        - Access: O(1)
        - Append: O(1) amortized
        - Insert: O(n)
        - Delete: O(n)
    Space Complexity: O(n)
    """
    def __init__(self, capacity=1):
        self.capacity = capacity
        # Simulate raw memory allocation with a block of memory
        self._data = self._allocate_memory(capacity)
        self._size = 0
    
    def _allocate_memory(self, size):
        # Simulate memory allocation at the lowest level
        return (size * ctypes.py_object)()
    
    def __len__(self):
        return self._size
    
    def __getitem__(self, index):
        if not self._is_valid_index(index):
            raise IndexError("Array index out of range")
        return self._data[index]
    
    def __setitem__(self, index, value):
        if not self._is_valid_index(index):
            raise IndexError("Array index out of range")
        self._data[index] = value
    
    def _is_valid_index(self, index):
        return 0 <= index < self._size
    
    def append(self, value):
        if self._size == self.capacity:
            # Double capacity and allocate new memory block
            new_capacity = self.capacity * 2
            new_data = self._allocate_memory(new_capacity)
            
            # Manual memory copy
            for i in range(self._size):
                new_data[i] = self._data[i]
                
            self._data = new_data
            self.capacity = new_capacity
            
        self._data[self._size] = value
        self._size += 1
    
    def insert(self, index, value):
        if not 0 <= index <= self._size:
            raise IndexError("Insert index out of range")
            
        if self._size == self.capacity:
            new_capacity = self.capacity * 2
            new_data = self._allocate_memory(new_capacity)
            
            # Manual copy up to index
            for i in range(index):
                new_data[i] = self._data[i]
                
            # Insert new element
            new_data[index] = value
            
            # Copy remaining elements
            for i in range(index, self._size):
                new_data[i + 1] = self._data[i]
                
            self._data = new_data
            self.capacity = new_capacity
        else:
            # Shift elements manually
            for i in range(self._size - 1, index - 1, -1):
                self._data[i + 1] = self._data[i]
            self._data[index] = value
            
        self._size += 1
        
    def remove(self, index):
        """
        Remove element at given index.

        Args:
            index: Index of element to remove

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not self._is_valid_index(index):
            raise IndexError("Remove index out of range")

        # Shift elements left to fill the gap (like sliding books on a shelf)
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        
        self._data[self._size - 1] = None
        self._size -= 1

if __name__ == "__main__":
    arr = Array(5)
    print("Empty array:", arr._data)

    # Test insertions func
    print("\nTesting insertions:")
    for i in range(7):  # Going beyond initial capacity to test resizing
        arr.append(i * 10)
        print(f"After appending {i * 10}:", [arr[j] for j in range(arr._size)])

    # Testing insertion at pt func
    print("\nTesting insert at index:")
    print("Before insert:", [arr[i] for i in range(arr._size)])
    arr.insert(2, 25)
    print("After insert at index 2:", [arr[i] for i in range(arr._size)])

    # Testing delete function
    print("\nTesting deletion:")
    print("Before deletion:", [arr[i] for i in range(arr._size)])
    arr.remove(2)
    print("After removing index 2:", [arr[i] for i in range(arr._size)])

    # Testing is critical folks
    print("\nTesting edge cases:")
    try:
        arr[arr._size + 1]
    except IndexError as e:
        print("Access out of bounds:", str(e))

    try:
        arr.insert(arr._size + 2, 100)
    except IndexError as e:
        print("Insert out of bounds:", str(e))

    try:
        arr.remove(arr._size + 1)
    except IndexError as e:
        print("Remove out of bounds:", str(e))
