# Deques

> A deque, or Double Ended Queue, is a type of queue in which insertion and removal of elements can either be performed from the front or the rear

- Deques can additionally be modified to restrict operations in certain ends

- Input restricted deque: input is restricted at a certain end, but allows deletion at both ends

- Output restricted deque: output is restricted at a single end, but allows insertion at both ends

### Instantiating a deque

> Deques are commonly implemented as linear or circular arrays. If the array is full in a circular array, the front pointer gets repointed to the beginning. The deque starting state involves the following steps

1. Take an array of size `n`

2. Set two pointers, `FRONT = -1` and `REAR = 0` at index `0`

### Operations on a deque

- `insertFront`: Add an element at the front

- `insertRear`: Add an element at the rear

- `deleteFront`: Pops an element at the front

- `deleteRear`: Pops an element at the rear

- `isEmpty`: Check if the deque is empty (`front = -1`)

- `isFull`: Check if the deque is full (`front = 0` and `rear = n - 1` OR `front = rear + 1`)

### Workings of insertFront

- This operation adds an element to the front of the deque

- Check the index position of `FRONT` - if the index position is `0`, the deque is full in the linear implementation

- For circular implementations, repoint `FRONT` to `n-1` (the last index)

- Decrease `FRONT` by 1 and add the element `v` to `array[FRONT]`


### Workings of insertRear

- This operation adds an element to the rear of the deque

- Check if the array `isFull` - if not, increase `REAR` by 1 and add the element `v` to `array[REAR]`

### Workings of deleteFront

- Check if the deque is empty and terminate the operation if `true`

- If the deque has only one element (`FRONT = REAR`), pop out the element at `FRONT` index, and set `FRONT` and `REAR` to `-1`

- Pop out the element at `FRONT`, and increase the `FRONT` index by `1`

### Workings of deleteRear

- Check if the deque is empty and terminate the operation if `true`

- If the deque has only one element (`FRONT = REAR`), pop out the element at `FRONT` index, and set `FRONT` and `REAR` to `-1`

- Pop out the element at `REAR`, and decrease the `REAR` index by `1`

### [Python implementation](./deque.py)

### Applications of Deques

- In undo operations on software

- To store history in browsers

- For implementing both stacks and queues
