# Insertion sort

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

- An efficient algorithm for sorting a small number of elements

- Conceptually similar to how people sort a hand of playing cards

## Algorithm

1. Iterate from `arr[1]` to `arr[n]` over the array

2. Compare the current element (key) to its predecessor

3. If the key is smaller, increase the array position of the predecessor by 1,

4. Decrease the pointer by 1 to compare with the next element, repeat [3] until key is greater

5. If the key is greater, insert the key into the position right after the current comparison

## Implementation

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        # comparison
        j = i - 1

        # move all elements > arr[i] one position up from their current
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # insert the key in the correct position
        arr[j + 1] = key
```

#### Complexity Analysis

- Time > $O(n^2)$; worst case would be to compare each element with every other element in the array

- Space > Inplace sorting $O(1)$
