# Fast and Slow Pointers

- The **Fast and Slow Pointers** approach uses two pointers which move through the array (or sequence / linked list) at different speeds.

- This is also known as the **Hare and Tortoise** algorithm.

- By moving at different speeds (say, in a cyclic linked list), the algorithm proves that the two pointers are bound to meet.

- The fast pointer should catch the slow pointer once both the pointers are in a cyclic loop.

- One of the famous problems solved using this technique was **Finding a cycle in a LinkedList**.

## Ways to identify

1. Dealing with data structures such as cyclic linked lists or arrays

2. Detect cycles, palindromes, or patterns

## Problems

### [Linked List Cycle](./02_linked_list_cycle.py)

> Given the head of a **Singly LinkedList** (one pointer to the next node), write a function to determine if the LinkedList has a cycle in it or not.

- Imagine two racers running in a circular racing track. If one racer is faster than the other, the faster racer is bound to catch up and lap the slower racer.

- We can use this fact to devise an algorithm, known as the Floyd's tortoise and hare algorithm, to determine if a linked list has a cycle in it or not.

- Imagine we have a slow and a fast pointer to traverse the linked list. In each iteration, the slow pointer moves one step and the fast pointer moves two steps.

This gives us two conclusions:

1. If the linked list doesn't have a cycle in it, the fast pointer will reach
   the end of the linked list before the slow pointer to reveal that there is no
   cycle in the linked list.

2. The slow pointer will never catch up to the fast pointer (if there is no
   cycle).

- If the linked list has a cycle, the fast pointer enters the cycle first,
followed by the slow pointer.

- After this, both pointers will keep moving in the cycle infinitely.

- If at any stage both of these pointers meet, we can conclude that the linked list has a cycle in it.

- Let's analyze if it is possible for the two pointers to meet.

When the fast pointer is approaching the slow pointer from behind we have two possibilities:

1. The fast pointer is one step behind the slow pointer.

2. The fast pointer is two steps behind the slow pointer.

All other distances between the fast and slow pointers will reduce to one of these two possibilities. Let's analyze these scenarios, considering the fast pointer always moves first:

1. If the fast pointer is one step behind the slow pointer: The fast pointer moves two steps and the slow pointer moves one step, and they both meet.

2. If the fast pointer is two steps behind the slow pointer: The fast pointer moves two steps and the slow pointer moves one step. This results in the fast pointer ending up one step behind the slow pointer,
   which reduces this scenario to the first scenario. This means that the two pointers will meet in the next iteration.

Therefore, the two pointers will definitely meet if the linked list has a cycle.

```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    slow, fast = head, head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return True

    return False
```

- Once the slow pointer enters the cycle, the fast pointer will meet the slow pointer in the same loop.

- Therefore, the time complexity of our algorithm will be $O(n)$ where `n` is the total number of nodes in the linked list.

- The algorithm runs in constant space $O(1)$, since it doesn't require
  additional memory.

### [Linked List Cycle Length](./03_linked_list_cycle_length.py)

> Given the head of a linked list with a cycle, find the length of the cycle.

- Once the fast and slow pointers meet, we can stop the slow pointer

- Next, we can create another pointer to traverse the whole cycle with another pointer

- We will find the length of the cycle when we see the slow pointer again

```python
def find_cycle_length(head):
    slow, fast = head, head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            return calculate_cycle_length(slow)

    return 0


def calculate_cycle_length(slow):
    current = slow
    cycle_length = 0

    while True:
        current = current.next
        cycle_length += 1

        if current == slow:
            break

    return cycle_length
```

- The above algorithm runs in $O(n)$ time complexity and $O(1)$ space complexity.

### [Start of Linked List Cycle](./04_start_linked_list_cycle.py)

> Given the head of a **singly linked list** that contains a cycle, write a function to find the **starting node of the cycle**.

If we know the length of the linked list cycle, we can find the start of the
cycle through the following steps:

1. Take two pointers. Let's call them `pointer1` and `pointer2`.

2. Initialize both pointers to point to the start of the linked list.

3. We can find the length of the linked list cycle using the approach discussed in **Linked List Cycle Length**.

4. Assuming the length of the cycle is `K` nodes, move `pointer2` ahead by `K` nodes.

5. Now, keep incrementing `pointer1` and `pointer2` until they both meet.

6. As `pointer2` is `K` nodes ahead of `pointer1`, which means, `pointer2` must have completed one loop in the cycle when both pointers meet. Their meeting point will be the start of the cycle.

- Find the cycle in a linked list with `n` nodes and also finding the length of the cycle requires $O(n)$

- We will need $O(n)$ to find the start of the cycle. Therefore, the overall time complexity of our algorithm will be $O(n)$.

- The algorithm runs in constant space $O(1)$.

### [Happy Number](./05_happy_number.py)

> Any number will be called a happy number if, after repeatedly replacing it with a number equal to the **sum of the square of all of its digits, leads us to number `1`**. All other (not-happy) numbers will never reach `1`. Instead, they will be stuck in a cycle of numbers which does not include `1`

- The process to find out if a number is a happy number or not always ends in a cycle

- If the number is a happy number, the process is stuck in a cycle on `1`

- If the number is not a happy number, the process will be stuck in a cycle with a set of numbers

- For eg. 12 will eventually get stuck in the following loop

```text
89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89
```

- Given that this is essentially a linked list with a cycle, we can use the **Fast and Slow Pointers** to find a cycle in the set of numbers

- Once the cycle is found, we can see if the cycle is stuck on number `1` to find out if the numbers is happy or not

```python
def find_happy_number(num):
    slow, fast = num, num

    while True:
        fast = square(square(fast))
        slow = square(slow)

        if slow == fast:
            break

    return slow == 1


def square(num):
    square_num = 0

    while num > 0:
        square_num += (num % 10) ** 2
        num //= 10

    return square_num
```

- Running through sequence examples, the algorithm has a time complexity of $O(\log n)$

- The algorithm runs in constant space $O(1)$
