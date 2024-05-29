"""
Problem Statement
Given the head of a linked list with a cycle, find the length of the cycle.
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# implementation
def find_cycle_length(head):
    slow, fast = head, head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

        # cycle found
        if slow == fast:
            return calculate_cycle_length(slow)

    return 0


def calculate_cycle_length(slow):

    # pause the slow pointer
    current = slow
    cycle_length = 0

    # traverse the cycle until meeting the slow pointer again
    while True:
        current = current.next
        cycle_length += 1

        if current == slow:
            break

    return cycle_length


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = head.next.next

    print(f"Linked list cycle length: {find_cycle_length(head)}")  # 4

    head.next.next.next.next.next.next = head.next.next.next
    print(f"Linked list cycle length: {find_cycle_length(head)}")  # 3


if __name__ == "__main__":
    main()


"""
Time Complexity
Finding the cycle takes O(N) time.
After finding the cycle, calculating the cycle length also takes O(N) time.
The overall algorithm takes O(N) time.

Space Complexity
The algorithm runs in constant space O(1).
"""
