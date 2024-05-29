"""
Problem Statement
Given the head of a singly linked list, write a function to determine if the linked list has a cycle in it or not.

Example 1:
Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

Example 2:
Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# implementation
def has_cycle(head):
    # initialise a hare and tortoise pointer
    slow, fast = head, head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

        # This happens if at any point both pointers enter a cycle
        if slow == fast:
            return True

    # The while loop breaks if we hit the end of a the linked list
    return False


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print(f"Linked list has cycle: {has_cycle(head)}")  # False

    head.next.next.next.next.next.next = head.next.next
    print(f"Linked list has cycle: {has_cycle(head)}")  # True

    head.next.next.next.next.next.next = head.next.next.next
    print(f"Linked list has cycle: {has_cycle(head)}")  # True


if __name__ == "__main__":
    main()


"""
Time Complexity
Once the slow pointer enters the cycle, the fast pointer will meet the slow pointer in the same loop.
The time complexity is therefore O(N) where 'N' is the number of nodes in the linked list.

Space Complexity
The algorithm runs in constant space O(1).
"""
