from typing import List


class Solution:
    def container_with_most_water(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, area)

            # try and find other candidates
            # determine which of the heights is the "bottleneck"
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
