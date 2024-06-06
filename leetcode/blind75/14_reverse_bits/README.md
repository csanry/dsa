# Reverse Bits

### Description

- Reverse bits of a given 32 bits unsigned integer.

### Summary

- Reverse each of 32 bits using bitwise operations

#### Example 1

```
Input: n = 0b00000010100101000001111010011100
Output: 964176192 (0b00111001011110000010100101000000)
Explanation: The input binary string 0b00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 0b00111001011110000010100101000000.
```

#### Example 2

```
Input: n = 0b11111111111111111111111111111101
Output: 3221225471 (0b10111111111111111111111111111111)
Explanation: The input binary string 0b11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 0b10111111111111111111111111111111.
```

### Constraints

- The input must be a binary representation of an integer of length 32

### Notes

- One approach is to traverse the binary representation bit by bit and perform a `x & 1` operation to determine if the bit was `0` or `1`

- This is done by looping through each bit - at iteration `i`

- Perform a right shift of `n` by `i` to compare the bit with `& 1`

- Insert the bit into the `res` using a logic or comparison `|`, left shifted by `31 - i` to insert the bit at the correct position

```python
class Solution:
    def reverse_bits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))

        return res
```

- Since we will only be comparing 32 bits, the solution runs in $O(1)$ time

- The solution also runs in $O(1)$ memory

### [Link to leetcode](https://leetcode.com/problems/reverse-bits/description/)
