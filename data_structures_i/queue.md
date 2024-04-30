# Queues

> A queue is a linear data structure that follows the First In First Out (FIFO) rule. It is similar to the ticket queue outside a cinema hall, where the first person entering the queue is the first person who gets the ticket. In queues, the elements that are added first are also removed first

```
Queue implementation
-----------------
--->  2  1  --->
-----------------
```

- Since `1` was added to the queue before `2`, it is the first to be removed from the queue as well (in accordance with the FIFO rule)

- Putting items in the queue is called `enqueue`, and removing items from the queue is called `dequeue`.

### Basic queue operations

> A queue is an object (an abstract data structure - ADT) that allows the following operations

- `enqueue`: Add an element to the end of the queue

- `dequeue`: Remove an element from the front of the queue

- `isEmpty`: Check if the queue is empty

- `isFull`: Check if the queue is full

- `peek`: Get the value of the front of the queue without removing it

- Queues are typically represented using `lists` in Python and `arrays` in C++

### Working of a Queue

> Queue operations work as follows:

- `FRONT`: a pointer that tracks the first element of the queue

- `REAR`: a pointer that tracks the last element of the queue

- On initialisation, set the values of `FRONT` and `REAR` to `-1`


### Enqueue Operation

- Check if the queue is full and terminate the operation if `true`

- If the queue is empty, set the value of the `FRONT` index to `0`

- Increase the value of the `REAR` index by `1`

- Add the new element in the position pointed to by `REAR`

- End state of the `enqueue` operation

```
V -> Front
v -> Rear
=========
ptr V  v
---------
idx 0  1
---------
ele 1  2
```

### Dequeue Operation

- Check if the queue is empty and terminate the operation if `true`

- Return the value pointed by `FRONT`

- Increase the `FRONT` index by `1`

- If dequeueing the last element, reset the values of `FRONT` and `REAR` to `-1`

### [Python implementation](./queue.py)

### Limitations of Queues

- After multiple rounds of enqueuing and dequeuing, the size of the queue will be reduced

```
V -> Front
v -> Rear
=================
ptr       V     v
-----------------
idx 0  1  2  3  4
-----------------
ele       3  4  5
```

- We can only utilise the 0 and 1 indexes after the queue is reset (all elements are dequeued)

- After `REAR` reaches the last index, if we can store extra elements in the empty indexes (0 and 1), we can circumvent this limitation of queues

- This is implemented by a modified queue called the circular queue

### Applications of Queues

- CPU scheduling, disk scheduling

- When data is transferred asynchronously between two processes, the queue is used for synchronization. For example: IO Buffers, pipes, file IO, etc

- Handling of interrupts in real-time systems.

- Call Center phone systems use Queues to hold people calling them in order.
