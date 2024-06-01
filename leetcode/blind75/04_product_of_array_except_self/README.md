# Product of Array Except Self

### Description

- Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`

- The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer

- You must write an algorithm that runs in $O(n)$ time and without using the division operation

### Summary

- Make two passes, first in order, second in reverse, to compute the products

#### Example 1

```
Input: nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]
```

#### Example 2

```
Input: nums = [-1, 1, 0, -3, 3]
Output: [0, 0, 9, 0, 0]
```

### Constraints

- $2 \le \text{nums.len()} \le 10^5$

- $-30 \le \text{nums[i]} \le 30$

- The product of any prefix or suffix of `nums` is guaranteed to fit in a 32 bit integer

### Notes

- Every `answer[i]` should contain the product of all elements before `i`, multiplied by the product of all elements after `i`

- We can calculate the products of all prefixes in the first loop, then the products of all suffixes in the second loop, to have a time complexity of $O(n)$

- The results can be stored in their respective indexes in the `answer` array to have a memory efficient $O(1)$ space complexity (not accounting for the result array)

```
Initialise result to be 1 1 1 1 and prefix to be 1

At i = 0
1 2 3 4
^ <<< curr val
Assign result[0] to be prefix (1), then multiply prefix with val (1)
1 1 1 1 <<< prefix 1

i = 1
1 2 3 4
  ^ <<< curr val
Assign result[1] to be prefix (1), then multiply prefix with val (2)
1 1 1 1 <<< prefix 2

i = 2
1 2 3 4
    ^ <<< curr val
1 1 2 1 <<< prefix 6

i = 3
1 2 3 4
      ^ <<< curr val
1 1 2 6 <<< prefix 24
```

```
Next, pass through the input array from the end -> beginning
Multiply the postfix with the value in the position

At i = 3
1 2 3 4
      ^ <<< curr val
Multiply with postfix, then multiply postfix with val
1 1 2 6 <<< postfix 4

i = 2
1 2 3 4
    ^ <<< curr val
1 1 8 6 <<< postfix (4 * 3) = 12

i = 1
1 2 3 4
  ^ <<< curr val
1 12 8 6 <<< postfix (12 * 2) = 24

i =
1 2 3 4
^ <<< curr val
24 12 8 6 <<< postfix (24 * 1) = 24

The final array is the answer
```

### [Link to leetcode](https://leetcode.com/problems/product-of-array-except-self/description/)
