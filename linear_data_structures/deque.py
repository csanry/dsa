# Deque implementation
class Deque:
    def __init__(self):
        self.deque = []

    def is_empty(self):
        return self.deque == []

    # Add an element from the rear
    def add_rear(self, item):
        self.deque.append(item)

    def add_front(self, item):
        self.deque.insert(0, item)

    # Remove an element from the rear
    def remove_rear(self):
        return self.deque.pop()

    # Remove an element from the front
    def remove_front(self):
        return self.deque.pop(0)

    # Display the queue
    def display(self):
        return self.deque

    # return the size of the queue
    def size(self):
        return len(self.items)


"""
In deques, insertion and removal can be performed from the front or the rear.
Thus, deques do not adhere to the FIFO rule (First In First Out).
"""

"""
The time complexity of all the above operations is constant i.e. O(1).
"""
