import pytest
from contains_duplicate import Solution
from typing import List


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 3, 1], True),
            ([1, 2, 3, 4], False),
            ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ],
    )
    def test_contains_duplicate(self, nums: List[int], expected: bool) -> None:
        result = self.solution.contains_duplicate(nums)
        assert result == expected
