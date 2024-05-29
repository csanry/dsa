"""
Problem Statement
Given the head of a linked list with a cycle, find the starting node of the cycle.
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# implementation
def find_cycle_start(head):
    slow, fast = head, head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

        # cycle found
        if slow == fast:
            cycle_length = calculate_cycle_length(slow)
            break

    return search_start(head, cycle_length)


def calculate_cycle_length(slow):

    # pause the slow pointer
    current = slow
    cycle_length = 0

    # traverse the cycle until meeting the slow pointer again
    while current is not None:
        current = current.next
        cycle_length += 1

        if current == slow:
            return cycle_length

    return 0


def search_start(head, length):

    slow, fast = head, head

    for _ in range(length):
        fast = fast.next

    while slow != fast:
        fast = fast.next
        slow = slow.next

    return slow


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print(f"Linked list cycle length: {find_cycle_start(head).value}")  # 3

    head.next.next.next.next.next.next = head.next.next.next
    print(f"Linked list cycle length: {find_cycle_start(head).value}")  # 4

    head.next.next.next.next.next.next = head
    print(f"Linked list cycle length: {find_cycle_start(head).value}")  # 1


if __name__ == "__main__":
    main()


"""
Time Complexity
Finding the cycle takes O(N) time.
After finding the cycle, calculating the cycle length also takes O(N) time.
Finding the start of the cycle takes O(N) time.
The overall algorithm takes O(N) time.

Space Complexity
The algorithm runs in constant space O(1).
"""
