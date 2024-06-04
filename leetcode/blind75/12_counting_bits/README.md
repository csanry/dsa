# Counting Bits

### Description

- Given an integer `n`, return an array of length `n + 1` such that for each `i` (`0 <= i <= n`), `ans[i]` is the number of `1` in the binary representation of `i`

### Summary

- Write out result for num=16 to figure out pattern; `res[i] = res[i - offset]`, where `offset` is the biggest power of 2 $\le \text{I}$

#### Example 1

```
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
```

#### Example 2

```
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
```

### Constraints

- $0 \le \text{nums} \le 10^5$

### Notes

- The brute force solution $O(n \log n)$ simply iterates through each number `i` in the range up to `n` and calculates the number of set bits for each `i`

```python
class Solution:
    def counting_bits(self, num: int) -> List[int]:
        res = []

        for i in range(num + 1):
            cnt = 0
            while i:
                if i & 1:
                    cnt += 1
                i >>= 1
            res.append(cnt)

        return res
```

- Note in the binary representation below that the last two bits for 4 is the same as the last two bits for 0, same as `5` and `1`, `6` and `2`...

- The pattern is based on the offset, which is determined by the most significant bit (power of 2)

- When we hit the next offset is determined exponentially, as shown in the pattern below (1, 2, 4, 8, 16...)

```
 n     bits    1s
 0 --> 0000 -- 0
 1 --> 0001 -- 1 + dp[n-1]
 2 --> 0010 -- 1 + dp[n-2]
 3 --> 0011 -- 1 + dp[n-2]
 4 --> 0100 -- 1 + dp[n-4]
 5 --> 0101 -- 1 + dp[n-4]
 6 --> 0110 -- 1 + dp[n-4]
 7 --> 0111 -- 1 + dp[n-4]
 8 --> 1000 -- 1 + dp[n-8]
 9 --> 1001 -- 1 + dp[n-8]
10 --> 1010 -- 1 + dp[n-8]
11 --> 1011 -- 1 + dp[n-8]
12 --> 1100 -- 1 + dp[n-8]
13 --> 1101 -- 1 + dp[n-8]
14 --> 1110 -- 1 + dp[n-8]
15 --> 1111 -- 1 + dp[n-8]
16 --> 10000 -- 1 + dp[n-16]
...
```

```python
class Solution:
    def counting_bits(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        offset = 1

        for i in range(1, num + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]

        return dp
```

- This cuts down the processing needed for each number to $n * O(1) \rarr O(n)$

- We will store `n` elements in the result array, therefore the solution requires $O(n)$ space

### [Link to leetcode](https://leetcode.com/problems/counting-bits/description/)
