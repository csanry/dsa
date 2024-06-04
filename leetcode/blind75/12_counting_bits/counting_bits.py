from typing import List


class Solution:
    def counting_bits(self, num: int) -> List[int]:

        dp = [0] * (num + 1)
        offset = 1

        # we don't need to calculate for zero, which is the base case
        for i in range(1, num + 1):
            # when 4 * 2 == 8, offset = 8
            # when 8 * 2 == 16, offset = 16..
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]

        return dp
