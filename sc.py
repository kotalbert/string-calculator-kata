from typing import Union, List


class StringCalculator:
    def add(self, input_str: str) -> int:
        if input_str == '':
            return 0
        s = 0
        for number_str in input_str.split(','):
            s += self._string_to_number(number_str)
        return s

    @staticmethod
    def _string_to_number(value: str) -> int:
        return int(value)
