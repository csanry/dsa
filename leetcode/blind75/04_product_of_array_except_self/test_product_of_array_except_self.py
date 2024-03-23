import pytest
from product_of_array_except_self import Solution
from typing import List


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 3, 4], [24, 12, 8, 6]),
            ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ],
    )
    def test_product_except_self(self, nums: List[int], expected: List[int]) -> None:
        result = self.solution.product_except_self(nums)
        assert result == expected
