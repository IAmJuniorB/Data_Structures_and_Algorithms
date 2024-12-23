"""
Trie Implementation
A tree-like data structure for storing and retrieving strings efficiently,
like a word dictionary where each letter leads to more letters.
"""

class TrieNode:
    """
    A node in the Trie, like a box that:
    - Holds letters (children)
    - Remembers if it's the end of a word
    
    Time Complexity: O(1) for node creation
    Space Complexity: O(1)
    """
    def __init__(self):
        # Map of letters to child nodes (like a branching path)
        self.children = {}
        # Is this the end of a word?
        self.is_end = False

class Trie:
    """
    A tree for storing strings, where each path from root to leaf spells a word.
    Like a family tree of letters that form words.

    Time Complexity:
        - Insert: O(m) where m is word length
        - Search: O(m) where m is word length
        - Prefix Search: O(m) where m is prefix length
    Space Complexity: O(n*m) where n is number of words, m is average length
    """
    def __init__(self):
        # Start with empty root node
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Add a word to the Trie.
        Like creating a path of letters one by one.

        Time Complexity: O(m) where m is word length
        Space Complexity: O(m)
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        """
        Look for a complete word in the Trie.
        Like following a path of letters to find a word.

        Time Complexity: O(m) where m is word length
        Space Complexity: O(1)
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def starts_with(self, prefix: str) -> bool:
        """
        Check if any word starts with given prefix.
        Like checking if a path of letters exists.

        Time Complexity: O(m) where m is prefix length
        Space Complexity: O(1)
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

if __name__ == "__main__":
    # Test our Trie
    trie = Trie()
    
    # Test insertions
    words = ["apple", "app", "apricot", "banana", "bat"]
    print("Inserting words:", words)
    for word in words:
        trie.insert(word)
    
    # Test word search
    print("\nTesting complete words:")
    test_words = ["apple", "app", "apt", "banana", "bat", "cat"]
    for word in test_words:
        print(f"Search '{word}': {trie.search(word)}")
    
    # Test prefix search
    print("\nTesting prefixes:")
    prefixes = ["ap", "ba", "cat", "b", "banan"]
    for prefix in prefixes:
        print(f"Prefix '{prefix}': {trie.starts_with(prefix)}")
    
    # Test edge cases
    print("\nTesting edge cases:")
    empty_trie = Trie()
    print("Empty Trie - Search 'a':", empty_trie.search("a"))
    print("Empty Trie - Prefix '':", empty_trie.starts_with(""))
