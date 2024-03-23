# Maximum Subarray

### Description

- Given an array of integers `nums`, find the subarray with the largest sum, and return its sum

#### Example 1

```
Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: The subarray [4, -1, 2, 1] has the largest sum 6
```

#### Example 2

```
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1
```

#### Example 3

```
Input: nums = [5, 4, -1, 7, 8]
Output: 23
Explanation: The subarray [5, 4, -1, 7, 8] has the largest sum 23
```

### Constraints

- $1 \le \text{nums.len()} \le 10^5$

- $-10^4 \le \text{nums[i]} \le 10^4$

### Notes

- A brute force solution would be to compute all the possible subarrays and maintain a running count of the best result

```python
from math import inf

class Solution:
    def maximum_subarray(self, nums: List[int]) -> int:
        res = -inf
        n = len(nums)

        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += nums[j]
                res = max(curr_sum, res)

        return res
```

- This requires $O(n^2)$ time and $O(1)$ space

- What is opimisation from here? Do we have to compute every subarray starting at every single value? Certain negatives values will not contribute to the total value

```
-2 1 -3 4 ...
 ^ <<< pointless to include -2 here and compute all of its subarrays

-2 1 -3 4 ...
      ^ <<< extending the logic, (1 + (-3)) = -2, it is also pointless to include this into the subarray
```

- This logic can be implemented using a two pointers design pattern: sliding window - the left pointer keeps track of the prefixes

- When there are negative prefixes, shift the left pointer

- The right pointer traverses down the array to try and extend the sliding window

- This solution takes $O(n)$ time and is also known as [Kadane's algorithm](https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm)


### [Link to leetcode](https://leetcode.com/problems/maximum-subarray/description/)
