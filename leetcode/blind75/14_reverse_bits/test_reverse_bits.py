import pytest
from reverse_bits import Solution


class TestSolution:
    def setup_method(self) -> None:
        self.solution = Solution()

    @pytest.mark.parametrize(
        "n, expected",
        [
            (0b00000010100101000001111010011100, 964176192),
            (0b11111111111111111111111111111101, 3221225471),
        ],
    )
    def test_reverse_bits(self, n: int, expected: int) -> None:
        result = self.solution.reverse_bits(n)
        assert result == expected
