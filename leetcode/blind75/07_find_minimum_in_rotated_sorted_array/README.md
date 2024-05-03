# Find Minimum in Rotated Sorted Array

### Description

- Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times

- For example, the array `nums = [0, 1, 2, 4, 5, 6, 7]` might become:

    * `[4, 5, 6, 7, 0, 1, 2]` if it was rotated 4 times

    * `[0, 1, 2, 4, 5, 6, 7]` if it was rotated 7 times

- Notice that rotating an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`

- Given the sorted rotated array `nums` of unique elements, return the minimum element of this array using an algorithm that runs in $O(\log n)$

#### Example 1

```
Input: nums = [3, 4, 5, 1, 2]
Output: 1
Explanation: The original array was [1, 2, 3, 4, 5] rotated 3 times
```

#### Example 2

```
Input: nums = [4, 5, 6, 7, 0, 1, 2]
Output: 0
Explanation: The original array was [0, 1, 2, 4, 5, 6, 7] and it was rotated 4 times
```

#### Example 3

```
Input: nums = [11, 13, 15, 17]
Output: 11
Explanation: The original array was [11, 13, 15, 17] and it was rotated 4 times
```

### Constraints

- $n = \text{nums.len()}$

- $1 \le n \le 5000$

- $-5000 \le \text{nums[i]} \le 5000$

- All the integers of `nums` are unique

- `nums` is sorted and rotated between `1` and `n` times

### Notes

- A trivial solution would involve traversing the array while keeping a running count of the minimum value, which would require $O(n)$ time

- We can take advantage of the fact that the array is sorted to find the minimum sum using binary search

- Cases: when the left point value is lesser than the right point value

    * We have found a subarray in which the elements are monotonically increasing -> there is no point continuing the binary search and we can break out of the loop

```
eg.
1 2 3 4 5
3 4 5
12 13 14 15
```

- Next case: when the midpoint value is greater than / equal to the left point value

```
We would want to search the right half of the array
3 4 5 6 7 1 2
L     M     R

An edge case would be
3 4
L R
M
```

- Remaining case: when the midpoint value is lesser than the left point value

```
We would want to search the left half of the array
6 7 1 2 3 4 5
L     M     R
```

### [Link to leetcode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/)
