# Container with most water

### Description

- You are given an integer array `height` of length `n`. There are `n` vertical lines with heights, such that the height of line `i` is `height[i]`.

- Find two lines that together with the x-axis form a container, such that the container contains the most water.

- Return the maximum amount of water a container can store.

- You may not slant the container (the top must be parallel to the x-axis).

### Summary

- Shrinking window, left and right pointers initially at endpoints, shift the pointer with min height inwards to find other candidates

#### Example 1

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water the container can contain is 49, from line 8 to line 7 (leading to a max height of 7 and length of 7)
```

#### Example 2

```
Input: height = [1,1]
Output: 1
```

### Constraints

- $n = \text{height.len()}$

- $2 \le n \le 10^5$

- $0 \le \text{height[i]} <= 10^4$

### Notes

- A brute force solution is to iterate through all combinations of containers, which would take $O(n^2)$

```python
class Solution:
    def max_area(self, height: List[int]) -> int:
        # brute force
        max_area = 0

        for left in range(len(height)):
            for right in range(left + 1, len(height)):
                area = (right - left) * min(height[left], height[right])
                max_area = max(max_area, area)

        return max_area
```

- Key to note that the minimum height of the container is the bottleneck, and that longer container widths are generally better

- A more optimal solution would be to start the left and right pointers at the ends of the array (to try and maximise width)

- We then they to update the pointer with the lesser height by shifting it inwards

- This is to try and increase the bottleneck that is the minimum height of the container

```
array
1 8 6 2 5 4 8 3 7
^ <<shift-l     ^
L               R

1 8 6 2 5 4 8 3 7
  ^  shift-r>>  ^
L               R
```

- The algorithm stops when the pointers meet

- Since we traverse the array only once, the entire algorithm takes $O(n)$ time

- The solution requires $O(n)$ space to store two pointers and the max area found

```python
class Solution:
    def container_with_most_water(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
```

### [Link to leetcode](https://leetcode.com/problems/container-with-most-water/description/)
