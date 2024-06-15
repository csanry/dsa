"""
Problem Statement
Given the head of a singly linked list, write a method to check if the linked list is a palindrome or not.
Your algorithm should use constant space.
The input linked list should be in the original form once the algorithm is finished.

Example 1:
Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
Output: true

Example 2:
Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
Output: false
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def is_palindromic_linked_list(head):
    if head is None or head.next is None:
        return True

    slow, fast = head, head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    head_second_half = reverse(slow)
    copy_head_second_half = head_second_half

    # compare the first and second half
    while head is not None and head_second_half is not None:
        if head.value != head_second_half.value:
            break  # not a palindrome

        head = head.next
        head_second_half = head_second_half.next

    reverse(copy_head_second_half)  # revert the reversal operation of the second half

    if head is None or head_second_half is None:  # if both halves match
        return True

    return False


def reverse(head):
    prev = None

    while head is not None:
        next = head.next
        head.next = prev
        prev = head
        head = next

    return prev


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print(f"Is palindrome: {is_palindromic_linked_list(head)}")  # True

    head.next.next.next.next.next = Node(2)
    print(f"Is palindrome: {is_palindromic_linked_list(head)}")  # False


if __name__ == "__main__":
    main()

"""
Time Complexity
The above algorithm will have a time complexity of O(N) where `N` is the number of nodes in the linked list.

Space Complexity
The algorithm runs in constant space O(1).
"""
