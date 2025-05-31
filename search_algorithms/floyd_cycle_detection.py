from typing import Optional

class ListNode:
    def __init__(self, value: int, next: Optional['ListNode'] = None):
        """Initialize a node with a value and a pointer to the next node."""
        self.value = value
        self.next = next


def list_to_linked_list(lst: list[int]) -> Optional[ListNode]:
    """Convert a Python list to a singly linked list.

    Args:
        lst (list[int]): List of integers to convert.

    Returns:
        Optional[ListNode]: Head node of the linked list or None if list is empty.
    """
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def fast_slow(head: Optional[ListNode]) -> Optional[int]:
    """Find the middle element of a linked list using the fast and slow pointer technique.

    Args:
        head (Optional[ListNode]): The head node of the linked list.

    Returns:
        Optional[int]: The value of the middle node, or None if the list is empty.
    """
    if head is None:
        return None

    slow = head  # Slow pointer moves one step at a time
    fast = head  # Fast pointer moves two steps at a time

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.value

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
linked_list = list_to_linked_list(numbers)

middle_value = fast_slow(linked_list)
print(f"The middle value of the linked list is: {middle_value}")
