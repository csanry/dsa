import pytest
from maximum_product_subarray import Solution
from typing import List


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([2, 3, -2, 4], 6),
            ([-2, 0, -1], 0),
        ],
    )
    def test_maximum_product_subarray(self, nums: List[int], expected: int) -> None:
        result = self.solution.maximum_product_subarray(nums)
        assert result == expected
