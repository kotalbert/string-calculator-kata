import pytest
from sc import StringCalculator


class TestSringCalculator:

    def test_empty(self, sc):
        assert sc.add('') == 0


@pytest.fixture()
def sc():
    return StringCalculator()
