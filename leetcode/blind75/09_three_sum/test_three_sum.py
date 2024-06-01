import pytest
from three_sum import Solution
from typing import List


class TestSolution:
    def setup_method(self) -> None:
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
            ([0, 1, 1], []),
            ([0, 0, 0], [[0, 0, 0]]),
        ],
    )
    def test_three_sum(
        self,
        nums: List[int],
        expected: List[List[int]],
    ) -> None:
        result = self.solution.three_sum(nums)
        assert result == expected
