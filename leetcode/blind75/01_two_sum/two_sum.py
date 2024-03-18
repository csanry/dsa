from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, val in enumerate(nums):
            diff = target - val
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[val] = i

        return
