import pytest
from number_of_one_bits import Solution


class TestSolution:
    def setup_method(self) -> None:
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected",
        [
            (11, 3),
            (128, 1),
            (2147483645, 30),
        ],
    )
    def test_number_of_one_bits(
        self,
        nums: int,
        expected: int,
    ) -> None:
        result = self.solution.number_of_one_bits(nums)
        assert result == expected
