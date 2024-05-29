import pytest
from search_in_rotated_sorted_array import Solution
from typing import List


class TestSolution:
    def setup_method(self) -> None:
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, target, expected",
        [
            ([4, 5, 6, 7, 0, 1, 2], 0, 4),
            ([4, 5, 6, 7, 0, 1, 2], 3, -1),
            ([1], 0, -1),
        ],
    )
    def test_search_in_rotated_sorted_array(
        self,
        nums: List[int],
        target: int,
        expected: int,
    ) -> None:
        result = self.solution.search_in_rotated_sorted_array(nums, target)
        assert result == expected
