import pytest
from counting_bits import Solution
from typing import List


class TestSolution:
    def setup_method(self) -> None:
        self.solution = Solution()

    @pytest.mark.parametrize(
        "num, expected",
        [
            (2, [0, 1, 1]),
            (5, [0, 1, 1, 2, 1, 2]),
        ],
    )
    def test_counting_bits(
        self,
        num: int,
        expected: List[int],
    ) -> None:
        result = self.solution.counting_bits(num)
        assert result == expected
