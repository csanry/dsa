from typing import List


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
