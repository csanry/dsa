from typing import List


class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for val in nums:
            if val in hashset:
                return True
            hashset.add(val)

        return False
