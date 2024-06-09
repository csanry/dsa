"""
Problem Statement
Given the head of a singly linked list and two positions, `p` and `q`,
write a function to reverse the linked list from `p` to `q`.
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
def reverse_sublist(head, p, q):
    # base case where p = q
    if p == q:
        return head

    current, previous = head, None
    i = 0

    # skip `p-1` nodes, current will point to the `p`th node
    while current is not None and i < p - 1:
        previous = current
        current = current.next
        i += 1

    # we are interested in 3 parts of the LL
    # the section before `p`, the section between `p`-`q`, and the section after `q`
    last_node_of_first_part = previous
    # after reversing the LL, `current` will become the last node of the sublist
    last_node_of_sublist = current
    next = None  # used to temporarily store the next node

    i = 0
    # this reverses the sublist
    while current is not None and i < q - p + 1:
        next = current.next
        current.next = previous
        previous = current
        current = next
        i += 1

    # connect with the first part
    if last_node_of_first_part is not None:
        # previous is now the first node of the sublist
        last_node_of_first_part.next = previous
    else:  # `p` is at the position of head of the old LL
        head = previous

    # connect with the last part
    last_node_of_sublist.next = current
    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original linked list are: ", end="")
    head.print_list()
    result = reverse_sublist(head, 2, 4)
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
