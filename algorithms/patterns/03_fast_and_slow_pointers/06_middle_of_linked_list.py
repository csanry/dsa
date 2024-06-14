"""
Problem Statement
Given the head of a singly linked list, write a method to return the middle node of the linked list.

If the total number of nodes in the linked list is even, return the second middle node.

Example 1:
Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
Output: 3

Example 2:
Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
Output: 4

Example 3:
Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> null
Output: 4
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_middle_of_linked_list(head):
    slow, fast = head, head

    # When fast finishes, slow would have traversed half of the array
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    return slow


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print(f"Middle Node: {find_middle_of_linked_list(head).value}")  # 3

    head.next.next.next.next.next = Node(6)
    print(f"Middle Node: {find_middle_of_linked_list(head).value}")  # 4

    head.next.next.next.next.next.next = Node(7)
    print(f"Middle Node: {find_middle_of_linked_list(head).value}")  # 4


if __name__ == "__main__":
    main()

"""
Time Complexity
The above algorithm will have a time complexity of O(N) where `N` is the number of nodes in the linked list.

Space Complexity
The algorithm runs in constant space O(1).
"""
