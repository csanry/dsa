# Number of One Bits

### Description

- Write a function that takes the binary representation of a positive integer and returns the number of set bits it has ([Hamming weight](https://en.wikipedia.org/wiki/Hamming_weight))

### Summary

- Use bitshift operations instead of mod to get 1's place, use bitwise & 1;

#### Example 1

```
Input: n = 11
Output: 3
Explanation: The input binary string 1011 has a total of three set bits.
```

#### Example 2

```
Input: n = 128
Output: 1
Explanation: The input binary string 10000000 has a total of one set bit.
```

#### Example 3

```
Input: n = 2147483645
Output: 30
Explanation: The input binary string 1111111111111111111111111111101 has a total of thirty set bits.
```

### Constraints

- $1 \le \text{n} \le 2^{31} - 1$

### Notes

- It is more efficient to use bitwise calculations to tackle this problem

- Looking at the rightmost bit, we can check if it is 1 or 0 using a bitwise `x & 1` operation

- Both `num` and `1` are converted into binary, and then are compared bit by bit

- This results in two possibilities

```
Rightmost bit is 0
1 1 0 0
0 0 0 1
-------
0 0 0 0 --> returns 0

Rightmost bit is 1
1 1 0 1
0 0 0 1
-------
0 0 0 1 --> returns 1
```

- If the bitwise and operation evaluates to `1`, we can then increase our running count

- To look at the next bit, perform a bitwise right shift operation `>>= 1` to shift all the bits by 1

```python
class Solution:
    def number_of_one_bits(self, num: int) -> int:
        res = 0

        while num > 0:
            if num & 1:
                res += 1
            num >>= 1

        return res
```

- Based on the problem constraints, algorithm will run at most 32 times, which evaluates to $O(1)$ time

- Algorithm requires $O(1)$ space to store the result

### [Link to leetcode](https://leetcode.com/problems/number-of-1-bits/description/)
