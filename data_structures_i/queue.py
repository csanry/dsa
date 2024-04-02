# Queue implementation
class Queue:
    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued item: {item}")

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        pop = self.queue.pop(0)
        print(f"Dequeued item: {pop}")
        return pop

    # Display the queue
    def display(self):
        print(self.queue)

    # return the size of the queue
    def size(self):
        return len(self.queue)


"""
The complexity of enqueue and dequeue operations in a queue using an array is O(1).
If you use pop(N) in python code,
then the complexity might be O(n) depending on the position of the item to be popped.
"""
