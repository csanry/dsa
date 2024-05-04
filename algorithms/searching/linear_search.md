# Linear search

## Objective

Given a sequence of n numbers

```
arr
[a1, a2, ..., an]
```

Return the index of a target element `k` if it exists; return `-1` otherwise
```
i such that arr[i] == k
```

## Characteristics

- A sequential sorting algorithm which starts from one end and check every element of the list until the desired element is found

- A simple algorithm that assumes nothing about the list of elements

## Algorithm

- Start from the first element, compare `k` with each element `x`

- If `x == k`, return the index

- If we hit the end of the array and did not find `k`, return `not found`

```python
def linear_search(k: int, arr: list[int]) -> int:
    for idx, x in enumerate(arr):
        if x == k:
            return idx

    # Element not found case
    return -1
```

#### Complexity Analysis

- Time complexity $O(n)$
    - The best case is when the target element is located in the first index $O(1)$ since there is only one comparison operation
    - The average case is $O(n)$
    - The worst case is when the target element is the last element of the array or is absent
    - It costs $O(n)$ time to traverse the entire array and perform $n$ comparisons

- Space complexity $O(1)$
    - The algorithm requires constant amount of additional space regardless of the size of the array
