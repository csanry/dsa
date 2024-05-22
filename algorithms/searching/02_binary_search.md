# Binary search

## Objective

Given a sequence of `n` numbers

```
arr
[a1, a2, ..., an]
```

Return the index of a target element element `k` if it exists; return `-1` otherwise
```
i such that arr[i] == k
```

## Characteristics

- A more efficient searching algorithm for sorted arrays

- If the elements are not already sorted, we need to sort them first (which incurs extra time complexity)

- Commonly implemented recursively using a divide and conquer approach

## Algorithm

1. Set two points, `low` and `high`, at the lowest and highest positions respectively

2. Find the middle element, pointer `mid` ie. `mid = (low + high) / 2`

3. If `k == arr[mid]`, then break the algorithm and return the element

4. Else, if `k <= arr[mid]`, shrink the search space to the left side, ie `high = mid - 1`

5. Else, `k > arr[mid]`, shrink the search space to the right side, ie `low = mid + 1`

6. Repeat steps 2 - 5 until `low` meets `high`

```python
# iterative method
def binary_search(arr, k):
    low, high = 0, len(arr) - 1

    while low <= high:
        # to prevent integer overflow
        mid = low + (high - low) // 2

        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            low = mid + 1
        else:
            high = mid - 1

    return -1
```

```python
# recursive method
def binary_search(arr, k, low, high):
    if low <= high:

        mid = low + (high - low) // 2

        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            return binary_search(arr, k, mid + 1, high)
        else:
            return binary_search(arr, k, low, mid - 1)

    return -1
```

## Complexity Analysis

- Time
    - Best case is when the element is at the midpoint - $O(1)$ time
    - The worst case is $O(log n)$, if the element is not in the array, we will
    - Average case is $O(log n)$, as the search space is reduced by half at each step

- Mathematical intuition for $O(log n)$ time complextiy

- At step `k`, we need to search through an array of size at most $n / 2^k$

- The smallest such `k` which we have no subarray to search through:

- $n / 2^k \lt 1 \rarr k = \lfloor\log_{2}(n)\rfloor + 1$

- For eg. an array of 1000 elements will terminate in about 10 steps ($2^{10} = 1024$) using binary search

- Space $\rarr O(1)$
