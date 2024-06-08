import pytest
from coin_change import Solution
from typing import List


class TestSolution:
    def setup_method(self) -> None:
        self.solution = Solution()

    @pytest.mark.parametrize(
        "coins, target, expected",
        [
            ([1, 2, 5], 11, 3),
            ([2], 3, -1),
            ([1], 0, 0),
        ],
    )
    def test_coin_change(
        self,
        coins: List[int],
        target: int,
        expected: int,
    ) -> None:
        result = self.solution.coin_change(coins, target)
        assert result == expected
