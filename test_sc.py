import pytest
from sc import StringCalculator


class TestStringCalculator:

    def test_empty_value(self, sc):
        """Empty string should produce 0"""
        assert sc.add('') == 0

    @pytest.mark.parametrize('test_input, expected', [('1', 1), ('2', 2)])
    def test_single_value(self, test_input, expected, sc):
        """Single digit should be converted to value"""
        assert sc.add(test_input) == expected


@pytest.fixture()
def sc():
    return StringCalculator()
