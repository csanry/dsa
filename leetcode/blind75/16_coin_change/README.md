# Coin Change

### Description

- You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

- Return the fewest number of coins that you need to make up that amount.

- If that amount of money cannot be made up by any combination of the coins, return `-1`.

- You can use any amount of each denomination of coin.

### Summary

- This is a classic unbounded knapsack problem involving an array of choices with a constraint to hit a target

- Two possible dynamic programming approaches: top-down uses a recursive DFS for the amount, branch for each coin, maintain a cache to store the previous `coin_count` for each amount

- Bottom-up: compute coins for `amount = 1`, up until `n`, using for each coin `(amount - coin)`, cache prev values


#### Example 1

```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
```

#### Example 2

```
Input: coins = [2], amount = 3
Output: -1
```

#### Example 3

```
Input: coins = [1], amount = 0
Output: 0
```

### Constraints

- $1 \le \text{coins.len()} \le 12$

- $1 \le \text{coins[i]} \le 2^{31} - 1$

- $0 \le \text{amount} \le 10^4$

### Notes

- Can we adopt a greedy approach by starting from `0`, and taking the biggest possible denomination without going over the target?

- Unfortunately, this does not guarantee the optimal solution, as shown in the example below

```
Amount = 7
[1, 3, 4, 5]

1st step: take 5, the largest without going over the limit
2nd step: take 1, total 6
3rd step: take 1, total 7, return 3

The optimal solution here is 2 using a combination of [3, 4]
```

- What about a DFS / backtracking approach? Each coin selection represents a possible branch option in a decision tree

```
Level 1
Branch #1: Take 1, remaining 6
Branch #2: Take 3, remaining 4
Branch #3: Take 4, remaining 3
Branch #4: Take 5, remaining 2

Level 2, continue searching down branch #4
Branch #4a: only 1 is a possible option as all the other options exceed the target sum
Searching down the [5, 1, 1] branch provides us with a possible result of 3 coins
The optimal solution is [3, 4] or [4, 3] with 2 coins
```

- This approach guarantees correctness, but is $O(n^m)$ where `n` is the number of coins and `m` is the amount

- We can gain efficiency by caching the results of visited branches already - using a top-down approach

1. Start from the end goal, take away a coin of each denominator and compute the minimum coins at each step

2. Memoize the minimium coins needed when visiting a new branch by storing them in a cache

    - When calling `dfs(target)`, if `target`, exists in `cache`, return `cache[target]`

3. Top down DFS approaches break on several base cases

    - If the `target <= 0`, this is not a valid solution, return `-1`

    - If the `target == 0`, return `0`

```python
class Solution:
    def coin_change(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(target):
            # base cases
            if target in cache:
                return cache[target]
            if target < 0:  # not a valid solution
                return -1
            if target == 0:  # possible solution found
                return 0

            min_coins = math.inf
            # Try possible combinations with backtracking, store min so far and subproblems in cache
            for denom in coins:
                res = dfs(target - denom)
                if res >= 0:
                    min_coins = min(min_coins, 1 + res)

            # store the result in the cache
            cache[target] = min_coins if min_coins != math.inf else -1
            return cache[target]

        res = dfs(amount)
        return res
```

- A bottom up dynamic programming approach to build the solution would compute the minimum number of coins to form an amount, starting from `0` and working up all the way to the `target`

```
DP[0] = 0
DP[1] = 1
DP[2] = 2 (Use $1 + DP[1])
DP[3] = 1 (minimum of use $1 + DP[2], use $3 + DP[0])
DP[4] = 1 (minimum of use $1 + DP[3], use $3 + DP[1], use $4 + DP[0])
DP[5] = 1 (minimum of use $1 + DP[4], use $3 + DP[2], use $4 + DP[1], use $5 + DP[0])
DP[6] = 2
DP[7]: either
  Use $1 + DP[6] --> 3 coins
  Use $3 + DP[4] --> 2 coins < These are optimal
  Use $4 + DP[3] --> 2 coins <
  Use $5 + DP[2] --> 3 coins
```

- Forming the recurrence relation: $\text{dp[amt]} = min(\text{dp[amt]}, 1 + \text{dp[amt - denom]})$ for each `denom` in `coins`

```python
import math

class Solution:
    def coin_change(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)
        dp[0] = 0  # base case

        for amt in range(1, amount + 1):
            for denom in coins:
                # this is a possible solution
                if amt - denom >= 0:
                    # this is the recurrence relation
                    # eg. dp[7] will look at $1 + dp[6], $3 + dp[4], $4 + dp[3] and $5 + dp[2]
                    # and take the minimum amount of coins from these possibilities
                    dp[amt] = min(dp[amt], 1 + dp[amt - denom])

        return dp[amount] if dp[amount] != math.inf else -1
```

- Time complexity is $O(n * m)$, where `n` is the target amount and `m` is the number of coins

    - At each step, we could potentially have all `m` denominations be potential coin candidates

- Space complexity is $O(n)$ to create an array to store `dp[i]` up to `i = n`

### [Link to leetcode](https://leetcode.com/problems/coin-change/description/)
