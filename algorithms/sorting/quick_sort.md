# Quick sort

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

- Defining characteristic of quick sort is selecting a pivot through the partition helper function

- Utilizes a recursive approach to sort the array - the array is broken down into subarrays

## Algorithm

#### Partition concept

1. Goal of partition: given an array and an element x of array

2. Have a final output where x is in the correct position in the array

3. All smaller elements will be to the left of x

4. All larger elements will be to the right of x

#### Partition logic

1. A pointer is fixed at the pivot (right most element) then compare the elements beginning from the first index

2. If the element is greater than the pivot, set a second pointer for that element

3. Pivot is compared with the other elements. If an element smaller than the pivot element is reached, the smaller element is swapped with the greater element found earlier

4. Process is repeated - find an element greater, an element smaller, and swap the elements

5. When the second last element is reached, swap the pivot element with the second pointer; typically the partition function returns the index

6. Repeat the partition call on the left and the right of the pivot

7. When each subarray is a single element, the array is sorted

## Implementation

```python
# function to find the partition position
def partition(array, low, high):
    # choose the rightmost element as pivot
    pivot = array[high]

    # set the i pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # if smaller element found
            # swap with the greater element found by i
            i += 1
            # swapping element at i with element at j
            array[i], array[j] = array[j], array[i]

    # at the second last element
    # swap the pivot element with the element at current position i
    array[i + 1], array[high] = array[high], array[i + 1]

    # return the position from where partition is done
    return i + 1

# function to perform quicksort
def quick_sort(array, low, high):

    # if low == high, array is size 1 and no need to sort
    if low < high:
        # find pivot element position
        # smaller elements on the left, greater on the right
        p = partition(array, low, high)

        # call quick_sort on the left and right of pivot
        quick_sort(array, low, p - 1)
        quick_sort(array, p + 1, high)

```

#### Complexity Analysis

- Time
    - The worst case occurs when the partition process always picks greatest or smallest element as the pivot > O(n^2)
    - The best case occurs when the partition process always picks the median as pivot > O(n log n)
    - Quick sort has an average case of O(n log n)

- Space -> Inplace sorting O(1)
