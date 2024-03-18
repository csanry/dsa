import pytest
from two_sum import Solution
from typing import List


class TestSolution:
    def setup_method(self) -> None:
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, target, expected",
        [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
        ],
    )
    def test_two_sum(
        self,
        nums: List[int],
        target: int,
        expected: List[int],
    ) -> None:
        result = self.solution.two_sum(nums, target)
        assert sorted(result) == expected
