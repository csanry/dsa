import pytest
from missing_number import Solution
from typing import List


class TestSolution:
    def setup_method(self) -> None:
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([3, 0, 1], 2),
            ([0, 1], 2),
            ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
        ],
    )
    def test_missing_number(
        self,
        nums: List[int],
        expected: int,
    ) -> None:
        result = self.solution.missing_number(nums)
        assert result == expected
