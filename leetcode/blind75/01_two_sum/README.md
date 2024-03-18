# Two Sum

### Description

- Given an array of integers nums and an integer target, return indices of the
  two numbers such that they add up to target

- You may assume that each input would have exactly one solution, and you may
  not use the same element twice

- You can return the answer in any order

#### Example 1

```
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

#### Example 2

```
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
```

#### Example 3

```
Input: nums = [3, 3], target = 6
Output: [0, 1]
```

### Constraints

- $2 \le \text{nums.len()} \le 10^4$

- $-10^9 \le \text{nums[i]} \le 10^9$

- $-10^9 \le \text{target} \le 10^9$

- We are guaranteed that one valid answer exists

### Notes

- Note that we have to use two elements with distinct indexes, but they can have the same value

- A brute force solution would be to find all combinations of numbers in the
  array

```
2 1 5 3
^
start with 2 and compute its sum with all numbers after: 2 + 1, 2 + 5, 2 + 3

2 1 5 3
  ^
move to 1 and compute its sum with 5 and 3; we don't need to calculate 1 + 2 as that has been checked already
```

- For such a solution, we need to loop through the entire array once, and for
  each element check it against worst case `n` times, leading $n \times n \rarr O(n^2)$
  time complexity

- The space required does not depend on the size of the input, so this solution
  requires $O(1)$ space

```python
class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        for i, val in enumerate(nums):
            for j, comp in enumerate(nums[i + 1 :], start=i + 1):
                if comp == target - val:
                    return [i, j]
        return
```

- We can reduce the lookup time from $O(n) \rarr O(1)$ by trading space for speed

- A more efficient solution would involve iterating through the elements, performing a lookup to see if its complement exists in the hashmap, and inserting it in if it doesn't

```
hashmap = {}
2 1 5 3
^
start with 2 and compute its complement (5 - 2 = 3); since the complement doesn't exist insert the element and its index into the hashtable as the key and value

hashmap = {2: 0}
2 1 5 3
  ^
move to 1 and compute its complement (5 - 1 = 4); lookup the table and insert 1 as the complement does not exist

hashmap = {2: 0, 1: 1, 5: 2}
2 1 5 3
      ^
move to 5 and then 3; the complement of 3 (2) exists in the hash table, so return the index of 2 and 3 [0, 3]
```

- If the complement exists, we have found a solution and can return the indices

- Since we traverse the array only once, and each lookup costs $O(1)$ time, the entire algorithm takes $n \times O(1) \rarr O(n)$ time

- We will store at most `n` elements in the hashmap, therefore the solution requires $O(n)$ space

```python
class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, val in enumerate(nums):
            diff = target - val
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[val] = i

        return
```

### [Link to leetcode](https://leetcode.com/problems/two-sum/description/)
