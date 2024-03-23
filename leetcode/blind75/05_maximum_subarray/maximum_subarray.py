from typing import List


class Solution:
    def maximum_subarray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0

        for n in nums:
            if curr_sum < 0:
                # reset the sliding window
                # set curr_sum to 0 and get rid of subarray before curr index
                curr_sum = 0
            curr_sum += n
            max_sum = max(max_sum, curr_sum)

        return max_sum
