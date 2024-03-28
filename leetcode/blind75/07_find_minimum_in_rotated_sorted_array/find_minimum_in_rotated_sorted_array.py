from typing import List


class Solution:
    def find_minimum(self, nums: List[int]) -> int:
        res = nums[0]
        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            # pivot found
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            mid = (left + right) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        return res
