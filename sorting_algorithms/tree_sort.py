class TreeNode:
    """
    Node in a Binary Search Tree used for Tree Sort.

    Attributes:
        data: Value stored in the node
        left: Reference to left child
        right: Reference to right child

    Time Complexity: O(1) for node creation
    Space Complexity: O(1)
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    """
    Insert a new value into the BST.

    Args:
        root: Current root node
        data: Value to insert

    Time Complexity: O(log n) average, O(n) worst case
    Space Complexity: O(log n) due to recursion
    """
    if root is None:
        return TreeNode(data)
    
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    
    return root

def inorder(root, result):
    """
    Perform inorder traversal to get sorted values.

    Args:
        root: Current root node
        result: List to store sorted values

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if root:
        inorder(root.left, result)
        result.append(root.data)
        inorder(root.right, result)

def tree_sort(values: list) -> list:
    """
    Sort a list using Tree Sort algorithm, which is an application of Binary Search Tree operations.

    Note:
        This is not a standalone sorting algorithm, but rather an application of two BST operations:
        1. BST insertion: Creates a BST by inserting each element (O(log n) per insertion)
        2. Inorder traversal: Retrieves elements in sorted order (O(n))

    Args:
        values (list): List to be sorted

    Returns:
        list: Sorted list

    Time Complexity: 
        - Average case: O(n log n)
        - Worst case: O(n²) for unbalanced tree
    Space Complexity: O(n)

    Example:
        >>> tree_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
    """
    
    if not values:
        return []
        
    root = None
    for value in values:
        root = insert(root, value)
    
    result = []
    inorder(root, result)
    return result

if __name__ == "__main__":
    test_numbers = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", test_numbers)
    sorted_list = tree_sort(test_numbers)
    print("Sorted list:", sorted_list)
    
    # They shall be tested
    print("\nTesting edge cases:")
    print("Empty list:", tree_sort([]))
    print("Single element:", tree_sort([1]))
    print("Two elements:", tree_sort([2, 1]))
    print("Already sorted:", tree_sort([1, 2, 3, 4, 5]))
    print("Reverse sorted:", tree_sort([5, 4, 3, 2, 1]))
    print("Duplicate elements:", tree_sort([3, 3, 3, 1, 2, 2]))
