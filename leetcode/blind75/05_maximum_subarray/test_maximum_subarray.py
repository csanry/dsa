import pytest
from maximum_subarray import Solution
from typing import List


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
            ([1], 1),
            ([5, 4, -1, 7, 8], 23),
        ],
    )
    def test_maximum_subarray(self, nums: List[int], expected: int) -> None:
        result = self.solution.maximum_subarray(nums)
        assert result == expected
