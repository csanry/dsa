# Selection sort

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

- Select the smallest element from an unsorted list in each iteration

- Places that element at the beginning of the unsorted list

- Useful when list is small, checking of all elements is compulsory, cost of writing to memory matters

## Algorithm

- Set the first element as minimum

- Compare minimum with the second element - if the second element is smaller, assign the second element to be minimum

- Compare minimum with the third element - if it is smaller, assign minimum to the 3rd element; otherwise, do nothing

- This process goes on until the last element

- Place the minimum reference in front of the unsorted list

- Restart the iteration with the next index until all elements are placed at their correct positions

```python
def selection_sort(array, size):

    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):

            # change > to < to sort in descending order
            # selects the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
        # once the min value is found, swap with min_idx
        array[step], array[min_idx] = array[min_idx], array[step]
```

#### Complexity Analysis

- Selection sort performs
    - 1st cycle $(n - 1)$ comparisons
    - 2nd cycle $(n - 2)$ comparisons ...
    - last 1 comparison

- Hence the number of comparisons is an arithmetic progression
    - $(n-1) + (n-2) + ... + 1 = n(n-1)/2$

- Which is $O(n^2)$ complexity

- Another way to think about it
    - Selection sort requires two loops (one nested) - hence complexity is $n * n = n^2$

- Time
    - The worst case is $O(n^2)$, when the array is in descending order
    - Best case is still $O(n^2)$ - array is already sorted
    - Average case is $O(n^2)$, when the array elements are jumbled up

- Space > $O(1)$ inplace sorting > variable to store step is used
