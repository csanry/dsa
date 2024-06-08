import math
from typing import List


class Solution:
    def coin_change(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)  # we need one extra space for 0
        dp[0] = 0  # base case of 0 coins to form 0

        for amt in range(1, amount + 1):
            for denom in coins:
                # this is a possible solution
                if amt - denom >= 0:
                    # this is the recurrence relation
                    # eg. dp[7] will look at $1 + dp[6], $3 + dp[4], $4 + dp[3] and $5 + dp[2]
                    # and take the minimum amount of coins from these possibilities
                    dp[amt] = min(dp[amt], 1 + dp[amt - denom])

        return dp[amount] if dp[amount] != math.inf else -1
