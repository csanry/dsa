"""
Problem Statement
Given the head of a singly linked list and a number `k`, reverse every `k` sized sublist starting from the head.

If, in the end, you are left with a sublist with less than `k` elements, reverse it too.
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


# implementation
def reverse_every_k_elements(head, k):
    # base cases
    if k <= 1 or head is None:
        return head

    current, previous = head, None
    while True:
        last_node_of_previous_part = previous
        # after reversing the linked list, curretn will become the last node of the sublist
        last_node_of_sublist = current
        next = None  # used to temporarily store the next node
        i = 0

        while current is not None and i < k:  # reverse k nodes
            next = current.next
            current.next = previous
            previous = current
            current = next
            i += 1

        # connect with the previous part
        if last_node_of_previous_part is not None:
            last_node_of_previous_part.next = previous
        else:
            head = previous

        # connect with the next part
        last_node_of_sublist.next = current

        if current is None:
            break
        previous = last_node_of_sublist

    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original linked list are: ", end="")
    head.print_list()
    result = reverse_every_k_elements(head, 3)
    print("Nodes of reversed linked list are: ", end="")
    result.print_list()


if __name__ == "__main__":
    main()

"""
Time complexity
The time complexity of our algorithm will be O(N) where 'N' is the total number of nodes in the linked list.

Space complexity
We only used constant space, therefore, the space complexity of our algorithm is O(1).
"""
