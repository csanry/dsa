# Best Time to Buy and Sell Stock

### Description

- Given an array of `prices`, where `prices[i]` is the price of a given stock on day `i`

- You want to maximise the profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock

- Return the maximum profit you can achieve from this transaction

- If you cannot achieve any profit, return `0`


#### Example 1

```
Input: prices = [7, 1, 5, 3, 6, 4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell
```

#### Example 2

```
Input: prices = [7, 6, 4, 3, 1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0
```

### Constraints

- $1 \le \text{prices.len()} \le 10^5$

- $0 \le \text{prices[i]} \le 10^4$

### Notes

- This leetcode can be solved using the two pointers design pattern

- We instantiate two pointers, left and right, which traverse the array in the same pass, and maintain a running count of the best profit

- The left pointer shifts whenever a lower price than its current position is found by the right pointer (the buy point)

- While the right pointer traverses through the array to identify profitable candidate days in the future (the sell point)

```
7 1 5 3 6 4
L R <<< right pointer finds a low candidate, left pointer is assigned to this candidate and right pointer moves to the next day

7 1 5 3 6 4
  L R <<< right pointer finds a profit candidate, the profit is calculated and compared against the current best
Since this profit of 5 - 1 = 4 is better than 0, we assign 4 to the current best profit

7 1 5 3 6 4
  L   R <<< right pointer shifts right once more
Since this profit of 3 - 1 = 2 is not better than 4, we move to 6

7 1 5 3 6 4
  L     R
6 - 1 = 5 is better than 4, so we assign 5 as the current best

7 1 5 3 6 4
  L       R
After the right pointer reaches the end, we break the algorithm and return the current best profit
```

- We will traverse the entire array once, leading to $O(n)$ time

- We don't incur any extra memory beyond storing the position of two pointers and the current best profit value, so the algorithm requires $O(1)$ space

```python
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
```

### [Link to leetcode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)
