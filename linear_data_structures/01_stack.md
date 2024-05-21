# Stack

> A stack is a linear data structure that follows the principle of Last In First Out (LIFO).

- We can think of the stack data structure as a pile of plates on top of one another

- Operations that you can perform include:

1. Put one plate on top of the other (`push` operation)

2. Remove the top plate (`pop` operation)

- If you need to remove the plate on the bottom, you must first remove all the plates on top

### Basic stack operations

- `push`: Add an element to the top of a stack

- `pop`: Remove an element from the top of a stack

- `isEmpty`: Check if the stack is empty

- `isFull`: Check if the stack is full

- `peek`: Get the value of the top element without removing it

### Workings of a Stack Data Structure

The operations work as follows:

- A pointer called `TOP` is used to keep track of the top element in the stack

- When initializing the stack, we set its value to `-1` so that we can check if the stack is empty by comparing `TOP == -1`

- On pushing an element, increase the value of `TOP` and place the new element in the position pointed to by `TOP`

- On popping an element, we return the element pointed to by `TOP` and reduce its value

- Before pushing, check if the stack is already full and terminate the process if `true`

- Before popping, check if the stack is already empty and terminate the process if `true`

### Python implementation

```python
# Stack implementation
class Stack:

    def __init__(self):
        self.stack = []

    # Helper function to check if a stack is empty
    def _check_empty(self):
        return len(self.stack) == 0

    # Adding an item into the stack: O(1) time
    def push(self, item):
        self.stack.append(item)
        print(f'Pushed item {item}')

    # Removing an element from the stack: O(1) time
    def pop(self):
        if self._check_empty():
            print('No item to pop; Stack is empty')
            return None
        pop = self.stack.pop()
        print(f'Popped item: {pop}')
        return pop
```

### Applications of Stack Data Structure

> Although stacks are simple data structures to implement, they are very powerful.

- To reverse a word - Put all the letters in a stack and pop them out. Because of the LIFO order of stack, you will get the letters in reverse order

- In compilers - Compilers use the stack to calculate the value of expressions like `2 + 4 / 5 * (7 - 9)` by converting the expression to prefix or postfix form

- In browsers - The back button in a browser saves all the URLs you have visited previously in a stack. Each time you visit a new page, it is added on top of the stack. When you press the back button, the current URL is removed from the stack, and the previous URL is accessed
