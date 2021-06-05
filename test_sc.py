import pytest
from sc import StringCalculator


class TestStringCalculator:

    def test_empty(self, sc):
        """Empty string should produce 0"""
        assert sc.add('') == 0


@pytest.fixture()
def sc():
    return StringCalculator()
