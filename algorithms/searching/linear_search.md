# Linear search

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

-
## Algorithm

-
```python
def
```

#### Complexity Analysis

- Selection sort performs
    - 1st cycle (n - 1) comparisons
    - 2nd cycle (n - 2) comparisons ...
    - last 1 comparison

- Hence the number of comparisons is an arithmetic progression
    - (n-1) + (n-2) + ... + 1 = n(n-1)/2

- Which is O(n^2) complexity

- Another way to think about it
    - Selection sort requires two loops (one nested) - hence complexity is n * n = n^2

- Time
    - The worst case is O(n^2), when the array is in descending order
    - Best case is still O(n^2) - array is already sorted
    - Average case is O(n^2), when the array elements are jumbled up

- Space -> O(1) inplace sorting > variable to store step is used
