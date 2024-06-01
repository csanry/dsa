from typing import List


class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for idx, ele in enumerate(nums):
            if idx > 0 and ele == nums[idx - 1]:
                continue

            left, right = idx + 1, len(nums) - 1
            while left < right:
                three_sum = ele + nums[left] + nums[right]

                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    res.append([ele, nums[left], nums[right]])
                    left += 1

                    # we want to skip all duplicates on the left side
                    # the right side is handled by the above flow in subsequent iterations
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res
