# Cyclic Sort

- Cyclic sort patterns take advantage of the fact that the input array contains numbers in the range of `1` to `n`

- The algorithm roughly follows the following steps:

    1. Place each number in its correct place (`1` at index `0`, `2` at `1`, and so on)

    2. Iterate through the array to find the indices that are missing the correct numbers

    3. These are our required numbers


## Ways to identify

1. Dealing with problems involving arrays with numbers in a given range

2. Sorting type problems of linear data structures

## Problems

### [Cyclic Sort](./02_cyclic_sort.py)

> Given an array containing `n` objects.
>
> Each object, when created, was assigned a unique number from `1` to `n` based on their creation sequence.
> This means that the object with sequence number `3` was created just before the object with sequence number `4`
>
> Write a function to sort the objects inplace on their creation sequence number in `O(n)`, without using extra space.

- We are given an input array containing numbers in the range of `1` to `n`

- Since all numbers are unique, we can try placing each number at its correct place (`1` at index `0`, `2` at index `1`...)

- This can be done efficiently by iterating through the array one number at a time

- If the current number we are iterating is not at the correct index, swap it with the number at the correct index

```python
def cyclic_sort(nums):
    i = 0

    while i < len(nums):
        j = nums[i] - 1

        if nums[i] == nums[j]:
            i += 1
        else:
            nums[i], nums[j] = nums[j], nums[i]

    return nums
```

- The time complexity of the above algorithm is $O(n)$; we don't increment the index when swapping the numbers, but the worst case is that the while loop
  swaps a total of `n - 1` numbers

- Once a number is at its correct index, we can move on

- Overall, our algorithm will take $O(n) + O(n-1)$, which is asymptotically equivalent to $O(n)$

- The algorithm runs in constant space $O(1)$


### [Find the Missing Number](./03_find_the_missing_number.py)

> We are given an array containing 'n' distinct numbers taken from the range 0 to 'n'.
Since the array has only 'n' numbers out of the total 'n+1' numbers, find the missing number.

- This problem follows the **Cyclic Sort** pattern

- Since the input array contains unique numbers from the range `0` to `n`, we can use a similar strategy as discussed in **Cyclic Sort** to place the numbers on their correct index

- Once we have every number in their correct place, we can iterate the array to find the index which does not have the correct number, which is our missing number

There are a few main differences with **Cyclic Sort**

1. The numbers are ranged from `0` to `n`, compared to `1` to `n`, therefore, each number should be equal to its index

2. Since the array will have `n` numbers, which means array indices will range from `0` to `n-1` - therefore we will ignore the number `n` as we can't place it in the array

3. If we swap the number at index `i` to place it in the correct index, we can still have the wrong number at index `i`; this is an issue as we have one extra number due to the larger range

    - This was not an issue in **Cyclic Sort**, as we made sure to place one number at its correct place in each step

    - We will not move to the next number at the after the swap until we have a correct number at index `i`

```python
def find_missing_number(nums):
    i, n = 0, len(nums)

    while i < n:
        j = nums[i]

        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i:
            return i

    return n
```

- The time complexity is still $O(n)$ as we are performing a cyclic sort

- The space complexity is $O(1)$ (inplace sorting)


### [Find all Missing Numbers](./04_find_all_missing_numbers.py)

> We are given an unsorted array containing numbers taken from the range `1 to 'n'`. The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.

- This problem is similar to **Find the Missing Number**, but there can be many duplicates unlike **Find the Missing Number**, and the range was greater than the length of the array

- We can follow a similar approach to place the numbers on their correct indices

- Once we are done with the cyclic sort, we will iterate through the array to find all indices that are missing the correct numbers

```python
def find_missing_numbers(nums):
    i = 0

    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    missing_numbers = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            missing_numbers.append(i + 1)

    return missing_numbers
```

- The time complexity of the above algorithm is $O(n)$

- Ignoring the space required for the output array, the algorithm runs in constant space $O(1)$


### [Find the Duplicate Number](./05_find_the_duplicate_number.py)

> We are given an unsorted array containing 'n+1' numbers taken from the range 1 to 'n'. The array has only one duplicate but it can be repeated multiple times. Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.

- We can use a similar approach to **Find the Missing Number**

- Since there is only one duplicate, if while swapping the number with its index both the numbers being swapped are the same, we have found our duplicate

```python
def find_duplicate(nums):
    i = 0

    while i < len(nums):
        if nums[i] != i + 1:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                return nums[i]
        else:
            i += 1

    return -1
```

- The time complexity of the above algorithm is O(n).

- The algorithm runs in constant space O(1) but modifies the input array

### [Find all Duplicate Numbers](./06_find_all_duplicate_numbers.py)

> We are given an unsorted array containing 'n' numbers taken from the range 1 to 'n'
> The array has some duplicates, find all the duplicate numbers without using any extra space.

- This problem shares similarities with **Find the Duplicate Number**

- We can use cyclic sort and then iterate through the array to find all numbers that are not at the correct indices (these numbers are duplicates)

```python
def find_all_duplicates(nums):
    i = 0

    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    duplicate_numbers = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            duplicate_numbers.append(nums[i])

    return duplicate_numbers
```

- The time complexity of the above algorithm is $O(n)$

- Ignoring the space required for storing the duplicates, the algorithm runs in constant space $O(1)$
