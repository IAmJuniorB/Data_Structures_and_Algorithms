"""
Trie Data Structure
"""

from typing import Dict

class TrieNode:
    """
    Node in the Trie.

    Attributes:
        children (Dict[str, TrieNode]): Map of child nodes
        is_end (bool): True if the node represents the end of a word
    """
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    """
    Trie data structure for efficient string storage and retrieval.

    Time Complexity:
        - Insertion: O(m) where m is the length of the word
        - Search: O(m) where m is the length of the word
        - Prefix Search: O(m) where m is the length of the prefix

    Space Complexity: O(n*m) where n is number of words and m is average word length
    """

    def __init__(self):
        """Initialize an empty Trie."""
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Insert a word into the Trie.

        Args:
            word (str): Word to be inserted

        Example:
            >>> trie = Trie()
            >>> trie.insert("apple")
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True  # Mark the end of the word 

    def search(self, word: str) -> bool:
        """
        Search for a word in the Trie.

        Args:
            word (str): Word to search for

        Returns:
            bool: True if the word is in the Trie, False otherwise

        Example:
            >>> trie = Trie()
            >>> trie.insert("apple")
            >>> trie.search("apple")
            True
            >>> trie.search("app")
            False
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end  # Is it really the end? One way or another.

    def starts_with(self, prefix: str) -> bool:
        """
        Check if any word in the Trie starts with the given prefix.

        Args:
            prefix (str): Prefix to search for

        Returns:
            bool: True if any word starts with the prefix, False otherwise

        Example:
            >>> trie = Trie()
            >>> trie.insert("apple")
            >>> trie.starts_with("app")
            True
            >>> trie.starts_with("b")
            False
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True  # We made it! (It's like checkpoint city)

def verify_trie():
    """Verify if the Trie implementation works correctly."""
    trie = Trie()
    words = ["apple", "app", "apricot", "banana", "bat"]
    
    print("Inserting words:", words)
    for word in words:
        trie.insert(word)
    
    print("\nTesting search:")
    test_words = ["apple", "app", "apricot", "banana", "bat", "ball", "cat"]
    for word in test_words:
        print(f"Search '{word}': {trie.search(word)}")
    
    print("\nTesting starts_with:")
    prefixes = ["ap", "ba", "cat", "b", "banan"]
    for prefix in prefixes:
        print(f"Starts with '{prefix}': {trie.starts_with(prefix)}")

if __name__ == "__main__":
    verify_trie()
    
    print("\nTesting edge cases:")
    empty_trie = Trie()
    print("Empty Trie - Search 'a':", empty_trie.search("a"))
    print("Empty Trie - Starts with '':", empty_trie.starts_with(""))
    
    single_char_trie = Trie()
    single_char_trie.insert("a")
    print("Single char Trie - Search 'a':", single_char_trie.search("a"))
    print("Single char Trie - Search 'b':", single_char_trie.search("b"))
