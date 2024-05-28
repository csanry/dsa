# Two Pointers

- In problems where we deal with sorted arrays (or linked lists) and need to find a set of elements that fulfill certain constraints, the Two Pointers approach becomes quite useful.

- The set of elements could be a pair, a triplet or even a subarray. For example, take a look at the following problem:

    > Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

- To solve this problem, we can consider each element one by one (pointed out by the first pointer) and iterate through the remaining elements (pointed out by the second pointer) to find a pair with the given sum

- The time complexity of this algorithm will be `O(n^2)` where `n` is the number of elements in the input array.

- Given that the input array is sorted, an efficient way would be to start with one pointer in the beginning and another pointer at the end

- At every step, we will see if the numbers pointed by the two pointers add up to the target sum. If they do not, we will do one of two things:

    1. If the sum of the two numbers pointed by the two pointers is greater than the target sum, this means that we need a pair with a smaller sum. So, to try more pairs, we can decrement the end-pointer.

    2. If the sum of the two numbers pointed by the two pointers is smaller than the target sum, this means that we need a pair with a larger sum. So, to try more pairs, we can increment the start-pointer.


## Ways to identify

1. Finding values in a linear data structure, such as an array or linked list

2. Having a target that needs to be a combination of two or more elements

## Problems

### [Two Sum](./02_two_sum.py)

> Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
>
> Write a function to return the indices of two numbers (the pair) such that they add up to a target.

#### Brute force solution

- A basic brute force would be to iterate through the array, taking one number at a time, and search for the second number through binary search

- The time complexity for this will be $O(n \log n)$ as we iterate through all elements in the array and perform a binary search $O(\log n)$

#### Two pointers

1. Start with one pointer at the beginning of the array, and another pointing at the end.

2. At every step, check if the numbers at pointer positions add up to the target sum. If they do, we have found our pair;

3. If the sum of the two numbers pointed by the two pointers is greater than the target sum, we need a pair with a smaller sum. So, to try more pairs, we decrement the end-pointer.

4. If the sum of the two numbers pointed by the two pointers is smaller than the target sum, we need a pair with a larger sum. So, to try more pairs, we increment the start-pointer.

```python
def pair_with_target_sum(arr, target_sum):
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return [left, right]

        if target_sum > current_sum:
            left += 1
        else:
            right -= 1

    return [-1, -1]
```

- The time complexity of the above algorithm wil be $O(n)$ where `n` is the total number of elements in the given array (worse case of the pair of numbers in the middle).

- The algorithm runs in constant space $O(1)$

### [Remove Duplicates](./03_remove_duplicates.py)

> Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the length of the subarray that has no duplicate in it.

1. In this problem, we need to remove the duplicates in-place such that the resultant length of the array remains sorted.

2. As the input array is sorted, therefore, one way to do this is to shift the elements left whenever we encounter duplicates.

3. In other words, we will keep one pointer for iterating the array and one pointer for placing the next non-duplicate number.

4. So our algorithm will be to iterate the array and whenever we see a non-duplicate number we move it next to the last non-duplicate number we’ve seen.

```python
def remove_duplicates(arr):
    left, right = 1, 1

    while right < len(arr):
        if arr[left - 1] != arr[right]:
            arr[left] = arr[right]
            left += 1
        right += 1

    return left
```

- The time complexity of the above algorithm will be `O(n)`, where `n` is the total number of elements in the given array.

- The algorithm runs in constant space `O(1)`

### [Remove Element](./04_remove_element.py)

> Given an unsorted array of numbers and a target `key`, remove all instances of `key` in-place and return the new length of the array.

1. In this problem, let the left pointer keep track of the next index to replace. Shift this down by one after every new replacement.

2. The right pointer traverses the array to compare the numbers and see if it matches the target `key`. If the value is not `key` it should push that number to the front by swapping the position to the left pointer

3. After reaching the end of the array, the result is our left pointer.

```python
def remove_element(nums, val):
    left = 0

    for right in range(len(nums)):
        if nums[right] != val:
            nums[left] = nums[right]
            left += 1

    return left
```

- The time complexity of the above algorithm is `O(n)`, where `n` is the total number of elements in the given array. This is because we traverse the array once only.

- The algorithm runs in constant space `O(1)`. This is because the array is sorted in-place.

### [Squaring a Sorted Array](./05_squaring_a_sorted_array.py)

> Given an integer array `nums` sorted in **non-decreasing** order, return an array of the squares of each number, sorted in non-decreasing order.

1. The main trick is that we can have negative numbers in the input array

2. One approach would be to first find the first non-negative number in the array; afterwards, we can use two pointers to iterate through the array

3. One pointer moves forward to process the non-negative numbers, and the other pointer moves backward to iterate the negative numbers

4. Compare the result at each step; whichever squared result is greater gets added to the output array

5. Another approach is to start at both ends of the input array, since either number is a candidate for the larger square

```python
def square_sorted_array(arr):
    left, right = 0, len(arr) - 1
    res = [0] * len(arr)
    current_idx = len(arr) - 1

    while left <= right:
        if arr[left] ** 2 > arr[right] ** 2:
            res[current_idx] = arr[left] ** 2
            left += 1
        else:
            res[current_idx] = arr[right] ** 2
            right -= 1
        current_idx -= 1

    return res
```

- The time complexity of the above algorithm will be $O(n)$ as we are iterating through the input array only once.

- The space complexity of the above algorithm will also be $O(n)$; this space will be used for the output array.

### [Triplet Sum to Zero](./06_triplet_sum_to_zero.py)

> Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

- This problem is an advanced version of **Two Sum**

- The main differences are the unsorted input array, and that we need to find triplets with a target sum of zero

- One approach is to sort the array and iterate through each number

    - At number `X`, we need to find `Y` and `Z` such that `X + Y + Z == 0`

    - This can be translated as finding a pair of `Y` and `Z` whose sum is `-X`

- Since we need to find unique triplets, we can skip any duplicate number, which is easy to do on the sorted array

```python
def search_triplets(arr):
    arr.sort()
    triplets = []

    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        search_pair(arr, -arr[i], i + 1, triplets)

    return triplets

def search_pair(arr, target_sum, left, triplets):
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target_sum:
            triplets.append([-target_sum, arr[left], arr[right]])
            left += 1
            right -= 1

            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1
```

- Sorting the array will take $O(N * \log N)$

- The `search_pair()` function will take $O(N)$. As we are calling `search_pair()` for every number in the input array, this means that overall `search_triplets()` will take $O(N * \log N + N^2)$, which is asymptotically equivalent to $O(N^2)$

- Ignoring the space required for the output array, the space complexity of the above algorithm will be $O(N)$ which is required for sorting

### [Triplet Sum close to Target](./07_triplet_sum_close_to_target.py)

> Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet.
>
> If there are more than one such triplet, return the sum of the triplet with the smallest sum.

- We can follow a similar approach to **Triplet Sum to Zero** to iterate through the array

- At each number, we will save the difference between the triplet and the target number

- If we find a difference of 0, we can end the algorithm early; otherwise, we return the triplet sum with the closest sum to the target

```python
import math

def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    smallest_difference = math.inf

    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1

        while left < right:
            target_diff = target_sum - (arr[i] + arr[left] + arr[right])

            if target_diff == 0:
                return target_sum

            if abs(target_diff) < abs(smallest_difference) or (
                abs(target_diff) == abs(smallest_difference)
                and target_diff > smallest_difference
            ):
                smallest_difference = target_diff

            if target_diff > 0:
                left += 1
            else:
                right -= 1

    return target_sum - smallest_difference
```

- Sorting the array takes $O(n \log n)$

- Finding the differences for each element in the array takes $O(n^2)$

- Overall the function takes $O(n \log n + n^2)$, which is asymptotically equivalent to $O(n^2)$

- The algorithm's space complexity is $O(n)$, which is required for sorting
