import pytest
from sc import StringCalculator


class TestStringCalculator:

    def test_empty_value(self, sc):
        """Empty string should produce 0"""
        assert sc.add('') == 0

    @pytest.mark.parametrize('test_input, expected', [('1', 1), ('2', 2)])
    def test_single_value(self, test_input, expected, sc):
        """Single number string should be converted to value."""
        assert sc.add(test_input) == expected

    @pytest.mark.parametrize('test_input, expected', [('1,2', 3), ('10,20', 30)])
    def test_coma_separated_values(self, test_input, expected, sc):
        """Coma separated numbers should be added."""
        assert sc.add(test_input) == expected

    @pytest.mark.parametrize('test_input, expected', [('1\n2', 3), ('10\n20', 30)])
    def test_nl_separated_values(self, test_input, expected, sc):
        """Newline separated values should be added."""
        assert sc.add(test_input) == expected

    def test_either_separated_values(self, sc):
        assert sc.add('1\n2,3\n4') == 10

    @pytest.mark.parametrize('test_input, expected', [('-1,2,-3', '-1,-3'), ('-1,2', '-1'), ('1,-2', '-2')])
    def test_negative_values_not_allowed(self, test_input, expected, sc):
        """Negatives in input should raise exception"""
        expected_err_msg = f'negatives not allowed {expected}'
        with pytest.raises(ValueError):
            sc.add(test_input)

        try:
            sc.add(test_input)
        except ValueError as e:
            assert str(e) == expected_err_msg

    @pytest.mark.parametrize('test_input, expected', [('999,1000', 1990), ('1,999,1000,1001', 2000)])
    def test_gt_1000_ignored(self, test_input, expected, sc):
        assert sc.add(test_input) == expected


@pytest.fixture()
def sc():
    return StringCalculator()
