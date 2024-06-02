import pytest
from container_with_most_water import Solution
from typing import List


class TestSolution:
    def setup_method(self) -> None:
        self.solution = Solution()

    @pytest.mark.parametrize(
        "height, expected",
        [
            ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
            ([1, 1], 1),
        ],
    )
    def test_container_with_most_water(
        self,
        height: List[int],
        expected: List[int],
    ) -> None:
        result = self.solution.container_with_most_water(height)
        assert result == expected
