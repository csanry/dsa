# Missing Number

### Description

- Given an array nums containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

### Summary

- Compute expected sum - real sum; xor n with each index and value


#### Example 1

```
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
```

#### Example 2

```
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
```

#### Example 3

```
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
```

### Constraints

- $n == \text{nums.len()}$

- $1 \le \text{n} \le 10^4$

- $0 \le \text{nums[i]} \le n$

- All numbers in `nums` are unique

### Notes

- `XOR` function: a number xor with itself will return `0`

```
5 ^ 5
-----
1 0 1
1 0 1
-----
0 0 0
```

- A number xor with `0` will return the number

```
3 ^ 0
-----
0 1 1
0 0 0
-----
0 1 1
```

- This solution takes advantage of the properties of `XOR` by performing element wise comparisons on the lists

- The first is the expected value using the `range` function, while the second list is the input array

```python
class Solution:
    def missing_number(self, nums: List[int]) -> int:
        xor = 0

        for i in range(len(nums) + 1):
            xor ^= i
        for val in nums:
            xor ^= val

        return xor
```

- This solution uses $O(1)$ space and $O(n)$ space (iterating through 2 arrays)

- Another approach is to compute the expected sum and the actual sum and take the difference to find out the missing number

- This can be done through looping or using [Gauss's method](https://nrich.maths.org/2478#:~:text=One%20way%20of%20presenting%20Gauss,times%20(n%2B1).)

```python
class Solution:
    def missing_number(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]

        return res
```

```python
class Solution:
    def missing_number(self, nums: List[int]) -> int:
        n = len(nums)
        expected = n * (n + 1) // 2
        actual = sum(nums)
        return expected - actual
```

- This solution takes $O(n)$ time (to sum the actual array); the method with Gauss's formula takes $O(1)$ time to compute the expected sum

- Both methods use $O(1)$ memory

### [Link to leetcode](https://leetcode.com/problems/missing-number/description/)
