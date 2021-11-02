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

