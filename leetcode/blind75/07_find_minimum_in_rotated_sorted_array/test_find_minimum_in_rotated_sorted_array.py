import pytest
from find_minimum_in_rotated_sorted_array import Solution
from typing import List


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([3, 4, 5, 1, 2], 1),
            ([4, 5, 6, 7, 0, 1, 2], 0),
            ([11, 13, 15, 17], 11),
        ],
    )
    def test_find_minimum(self, nums: List[int], expected: int) -> None:
        result = self.solution.find_minimum(nums)
        assert result == expected
