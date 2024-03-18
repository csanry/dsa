# Contains Duplicate

### Description

- Given an array of integers `nums`, return `True` if any value appears at least twice in the array; return `False` otherwise

#### Example 1

```
Input: nums = [1, 2, 3, 1]
Output: True
```

#### Example 2

```
Input: nums = [1, 2, 3, 4]
Output: False
```

#### Example 3

```
Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Output: True
```

### Constraints

- $1 \le \text{nums.len()} \le 10^5$

- $-10^9 \le \text{nums[i]} \le 10^9$

### Notes

- A brute force solution would be to traverse the entire array and perform comparisons on every pairwise set of elements

- Such a solution would take $O(n^2)$ time and $O(1)$ space

```python
class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True

        return False
```

- A slightly more efficient method would be to first sort the array, and then compare each pair of neighbours

- Due to the characteristic of a sorted array (duplicates, if any, will be adjacent elements), we will only need to iterate through the entire array once after sorting

- This takes $O(n \log n)$ time from sorting

```python
class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)

        for left_val, right_val in zip(nums, nums[1:]):
            if left_val == right_val:
                return True

        return False
```

- The more efficient approach uses a hash set to store encountered elements

- While traversing through the array, we check if the new element already exists in the set and returns `True` if so; otherwise, add the element to the hash set

- This solution has a time complexity of $O(n)$ where $n$ is the length of the array to check

- We have to create a hash set which will require $O(n)$ space

```python
class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for val in nums:
            if val in hashset:
                return True
            hashset.add(val)

        return False
```

### [Link to leetcode](https://leetcode.com/problems/contains-duplicate/description/)
