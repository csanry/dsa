from typing import List


class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        prefix, postfix = 1, 1

        for i, val in enumerate(nums):
            res[i] = prefix
            prefix *= val

        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
