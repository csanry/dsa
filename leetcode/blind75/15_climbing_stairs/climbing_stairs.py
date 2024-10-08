class Solution:
    def climbing_stairs(self, n: int) -> int:
        one, two = 1, 1

        for _ in range(n - 1):
            tmp = one
            one += two
            two = tmp

        return one
