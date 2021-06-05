from typing import Union, List


class StringCalculator:
    def add(self, input_str: str) -> int:
        if input_str == '':
            return 0
        vals = input_str.split(',')
        return self._sum_vals(vals)

    @staticmethod
    def _string_to_number(value: str) -> int:
        return int(value)

    @staticmethod
    def _sum_vals(vals: List[str]) -> int:
        s = 0
        for v in vals:
            s += StringCalculator._string_to_number(v)
        return s

    @staticmethod
    def _split_str(s: str) -> List[str]:
        return s.split(',')
