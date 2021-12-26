from deque import Deque

dq = Deque()

dq.add_rear(2)
dq.add_rear(3)
dq.add_front(1)
print(dq.display())

dq.remove_front()
dq.remove_front()
print(dq.display())