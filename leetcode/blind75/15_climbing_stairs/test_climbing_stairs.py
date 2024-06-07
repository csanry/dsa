import pytest
from climbing_stairs import Solution


class TestSolution:
    def setup_method(self) -> None:
        self.solution = Solution()

    @pytest.mark.parametrize(
        "n, expected",
        [(2, 2), (3, 3)],
    )
    def test_climbing_stairs(self, n: int, expected: int) -> None:
        result = self.solution.climbing_stairs(n)
        assert result == expected
