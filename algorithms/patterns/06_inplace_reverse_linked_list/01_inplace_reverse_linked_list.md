# In-place Reversal of a Linked List

In a lot of problems, we are asked to reverse the links between a set of nodes of a linked list. Often, the constraint is that we need to do this in-place, ie. using the existing node objects and without using extra memory.

The **Inplace Reversal of a Linkedlist** pattern describes an efficient way to solve the above problem.

## Ways to identify

1. Dealing with a linked list

## Problems

### [Reverse a Linked List](./02_reverse_a_linkedlist.py)

> Given the head of a Singly Linkedlist, reverse the Linkedlist. Write a function to return the new head of the reverse Linkedlist.

- To reverse a linked list, we need to reverse one node at a time. We will start with a variable `current` which will initially point to the head of the linked list and a variable `previous` which will point to the previous node that we have processed; initially `previous` will point to `null`

- In a stepwise manner, we will reverse the `current` node by pointing it to the `previous` before moving on to the next node.

- Also, we will update the `previous` to always point to the previous node that we have processed.

- The order of assignment is `N.PC` (where `.` represents the repointing of `current.next`)

    1. If `current` is not `None`

    2. `next = current.next`

    3. `current.next = previous`

    4. `previous = current`

    5. `current = next`

- The time complexity of our algorithm will be $O(n)$ where `n` is the total number of nodes in the linked list.

- We only used constant space (storage for two pointers), therefore the space complexity is `O(1)`.

### [Reverse a Sub-list](./03_reverse_a_sublist.py)

> Given the head of a linked list and two positions `p` and `q`, reverse the linked list from position `p` to `q`.

- The problem follows the **Inplace Reversal of a linked list** pattern. We can use a similar approach as discussed in **Reverse a linked list**.

1. Skip the first `p-1` nodes, to reach the node at position `p`.
2. Remember the node at position `p-1` to be used later to connect with the reversed sublist.
3. Next, reverse the nodes from `p` to `q` using the same approach discussed in **Reverse a LinkedList**.
4. Connect the `p-1` and `q+1` nodes to the reversed sub-list.

- Time complexity of our algorithm will be $O(n)$ where `n` is the total number of nodes in the linked list.

- Space complexity of our algorithm is $O(1)$.

### [Reverse every K-element sublist](./04_reverse_every_k_element_sublist.py)

> Given the head of a linked list and a number `k`, reverse every `k` sized sublist, starting from the head.
>
> If, in the end, you are left with a sublist with less than `k` elements, reverse it too.

- The problem follows the **Inplace Reversal of a linked list** pattern and is quite similar to **Reverse a sublist**

- The main difference is that we have to reverse all sublists

- We can adopt the same approach, starting with the first sublist (ie. `p=1, q=k`) and keep reversing all the sublists of size `k`


- The time complexity of our algorithm will be $O(n)$ where `n` is the total number of nodes in the linked list

- The space complexity of the algorithm is $O(1)$ as the reversal is done inplace
