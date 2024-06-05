from typing import List


class Solution:
    def missing_number(self, nums: List[int]) -> int:
        # res = len(nums)

        # for i in range(len(nums)):
        #     res += i - nums[i]

        # return res
        n = len(nums)
        expected = n * (n + 1) // 2
        actual = sum(nums)
        return expected - actual


# if __name__ == "__main__":
#   solution = Solution()
#   solution.missing_number([3, 0, 1, 4])
