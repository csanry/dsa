# Merge sort

## Objective

Given a sequence of n numbers

```
[a1, a2, ..., an]
```

Output a permutation (reordering) of the input sequence
```
[a'1, a'2, ..., a'n] -> such that
a'1 <= a'2 <= ... <= a'n
```

## Characteristics

- An efficient algorithm for larger arrays

- Utilizes the divide and conquer approach to sort the array - breaks down the array and builds it back up, doing comparisons along the way

- Does not typically sort in place

## Algorithm

1. Find the midpoint of the array

2. Split the array into subarrays

3. Recursively split until smallest array of size 1, this is done by calling merge_sort on the left half, then on the right_half

4. Merge the two sorted halves into a single sorted array through element comparisons

## Implementation

```python
def split(arr):
    """
    Divide step for the merge sort algorithm
    Returns two sublists: left and right

    O(log(n)) time
    """
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    return left, right

def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list
    i: keeps track of the indexes in the left list
    j: keeps track of the indexes in the right list

    O(n) time
    """
    lst = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lst.append(left[i])
            i += 1
        else:
            lst.append(right[j])
            j += 1
    # edge case where either list is shorter than the other
    # add remaining elements to the return list
    while i < len(left):
        lst.append(left[i])
        i += 1
    while j < len(right):
        lst.append(right[j])
        j += 1
    return lst

def merge_sort(arr):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step

    O(n log(n)) time
    """
    if len(arr) <= 1:
        return arr
    left_half, right_half = split(arr)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge(left, right)
```

#### Complexity Analysis

- Time -> O(n log n);

- Space -> O(n)
