import pytest
from best_time_to_buy_and_sell import Solution
from typing import List


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "prices, expected",
        [
            ([7, 1, 5, 3, 6, 4], 5),
            ([7, 6, 4, 3, 1], 0),
        ],
    )
    def test_max_profit(self, prices: List[int], expected: int) -> None:
        result = self.solution.max_profit(prices)

        assert result == expected
