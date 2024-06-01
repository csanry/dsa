# Maximum Product Subarray

### Description

- Given an integer array `nums`, find a subarray that has the largest product and return the product

- The answer will fit into a 32-bit integer

### Summary

- Dynamic programming, compute the max and max-abs-val for each prefix subarray

#### Example 1

```
Input: nums = [2, 3, -2, 4]
Output: 6
Explanation: [2, 3] has the largest product 6
```

#### Example 2

```
Input: nums = [-2, 0, -1]
Output: 0
Explanation: The result cannot be 2, because [-2, -1] is not a subarray
```

### Constraints

- $1 \le \text{nums.len()} \le 2 * 10^4$

- $-10 \le \text{nums[i]} \le 10$

### Notes

- A brute force solution would involve iterating through all subarrays and calculating the product - this would require $O(n^2)$ time

```python
class Solution:
    def maximum_product_subarray(self, nums: List[int]) -> int:
        max_prod = -inf
        n = len(nums)

        for i in range(n):
            curr_prod = 1
            for v in range(i, n):
                curr_prod *= nums[v]
                max_prod = max(max_prod, curr_prod)

        return max_prod
```

- The key insight to this problem is that all positive numbers would always lead to a monotonically increasing product - ie the max product would be the product of all the elements in the array

- If there were negative elements in the array, we would need an even number of negative elements to form a larger product

- This problem can be solved using dynamic programming to build

```
-1 -2 -3
| 2 | is the maximum value that can be formed from this subarray (-1 * -2)
|-2 | is the minimum value that can be formed from this subarray (-2)

we can then extend this step to account for the min and max inclusive of -3
-1 -2 -3
|  6  | is the maximum value that can be formed from this subarray (-2 * -3)
| -6  | is the minimum value that can be formed from this subarray (-1 * -2 * -3)

Since the max and min values can switch at any point, we need to maintain both values throughout the computation
```

- 0 is an edge case that will result in both the min and max being reset to 0

- We can essentially skip over 0s by resetting our max and min values to 1 whenever we encounter a 0

- The DP solution will have a time complexity of $O(n)$ and space complexity of $O(1)$

```python
class Solution:
    def maximum_product_subarray(self, nums: List[int]) -> int:
        res = max(nums)
        curr_min, curr_max = 1, 1

        for val in nums:
            if val == 0:
                curr_min, curr_max = 1, 1

            # store a temp so that curr_max is not lost when calculating the new curr_max
            tmp = curr_max * val
            curr_max = max(curr_max * val, curr_min * val, val)
            curr_min = min(tmp, curr_min * val, val)
            res = max(res, curr_max)

        return res
```

### [Link to leetcode](https://leetcode.com/problems/maximum-product-subarray/description/)
