# Bubble sort

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

- Compares two adjacent elements and swaps them

- Sorted elements will move to the end in each iteration

- Very simple and easy to implement

## Algorithm

- Start from the first index, compare the 1st and 2nd elements

- If the 1st element is greater, swap the elements

- Move down and compared 2nd and 3rd elements - repeat the swap if 2nd > 3rd

- Once the last element is hit, we are finished with one iteration and the far most element is sorted

- Restart from the 1st element and compare again up to the last unsorted element


```python
def bubble_sort(array):

    # loop to access each array element
    for i in range(len(array)):

        # loop to compare array elements
        for j in range(0, len(array) - i - 1):
            # compare two adjacent elements
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
```

#### Complexity Analysis

- Bubble sort compares adjacent elements
    - 1st cycle (n - 1) comparisons
    - 2nd cycle (n - 2) comparisons ...
    - last 1 comparison

- Hence the number of comparisons is an arithmetic progression
    - (n-1) + (n-2) + ... + 1 = n(n-1)/2

- Which is O(n^2) complexity

- Another way to think about it
    - Bubble sort requires two loops - hence complexity is n * n = n^2

- Time
    - The worst case is O(n^2), when the array is in descending order
    - Best case is O(n) - array is already sorted
    - Average case is O(n^2), when the array elements are jumbled up

- Space -> O(1) inplace sorting
