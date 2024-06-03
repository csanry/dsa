class Solution:
    def number_of_one_bits(self, num: int) -> int:
        res = 0

        while num > 0:
            if num & 1:
                res += 1

            # bitwise right shift to reduce the number
            num >>= 1

        return res
