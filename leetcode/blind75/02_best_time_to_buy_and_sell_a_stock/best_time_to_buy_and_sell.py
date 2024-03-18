from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        max_profit = 0
        left, right = 0, 1

        while right < len(prices):
            # check if profit candidate
            if prices[left] < prices[right]:
                curr_profit = prices[right] - prices[left]
                max_profit = max(max_profit, curr_profit)
            # otherwise assign left to right
            else:
                left = right
            right += 1

        return max_profit
