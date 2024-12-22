class Node:
    """Node class implementation as defined in linked_list.py"""
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return f"{self.data}"

class LinkedList:
    """LinkedList class implementation as defined in linked_list.py"""
    def __init__(self):
        self.head = None

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count

    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def node_at_index(self, index):
        if index == 0:
            return self.head
        current = self.head
        position = 0
        while position < index:
            current = current.next_node
            position += 1
        return current

    def __repr__(self):
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

def merge_sort(linked_list: LinkedList) -> LinkedList:
    """
    Sort a linked list in ascending order using merge sort.

    Args:
        linked_list: LinkedList to be sorted

    Returns:
        LinkedList: A new sorted linked list

    Time Complexity: O(kn log n) overall
    Space Complexity: O(n)

    Example:
        >>> l = LinkedList()
        >>> l.add(3)
        >>> l.add(1)
        >>> sorted_list = merge_sort(l)
        >>> print(sorted_list)
        [Head: 1]->[Tail: 3]
    """
    if linked_list.size() <= 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list: LinkedList) -> tuple:
    """
    Split the linked list at midpoint.

    Time Complexity: O(k log n)
    Space Complexity: O(n)
    """
    if linked_list is None or linked_list.head is None:
        return linked_list, None

    size = linked_list.size()
    mid = size // 2
    mid_node = linked_list.node_at_index(mid-1)

    left_half = linked_list
    right_half = LinkedList()
    right_half.head = mid_node.next_node
    mid_node.next_node = None

    return left_half, right_half

def merge(left: LinkedList, right: LinkedList) -> LinkedList:
    """
    Merge two sorted linked lists.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    merged = LinkedList()
    merged.add(0)
    current = merged.head
    left_head = left.head
    right_head = right.head

    while left_head or right_head:
        if left_head is None:
            current.next_node = right_head
            right_head = right_head.next_node
        elif right_head is None:
            current.next_node = left_head
            left_head = left_head.next_node
        else:
            if left_head.data < right_head.data:
                current.next_node = left_head
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                right_head = right_head.next_node
        current = current.next_node

    head = merged.head.next_node
    merged.head = head
    return merged

if __name__ == "__main__":
    # Test implementation
    test_list = LinkedList()
    test_data = [74, 32, 100, 45, 99, 1, 12]
    for num in test_data:
        test_list.add(num)

    print("Original list:", test_list)
    sorted_list = merge_sort(test_list)
    print("Sorted list:", sorted_list)
