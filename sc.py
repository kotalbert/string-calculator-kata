import re
from typing import Union, List, Tuple


class StringCalculator:
    def add(self, input_str: str) -> int:
        if input_str == '':
            return 0
        str_vals = self._split_str(input_str)
        int_vals = self._convert_vals_to_ints(str_vals)
        self._validate(int_vals)
        return self._sum_vals(int_vals)

    @staticmethod
    def _string_to_number(value: str) -> int:
        return int(value)

    @staticmethod
    def _sum_vals(vals: List[int]) -> int:
        return sum(filter(lambda x: x <= 1000, vals))

    @staticmethod
    def _split_str(s: str) -> List[str]:
        separator, s_rest = StringCalculator.find_separator(s)
        return re.split(separator, s_rest)

    @staticmethod
    def _convert_vals_to_ints(vals: List[str]) -> List[int]:
        return [StringCalculator._string_to_number(v) for v in vals]

    @staticmethod
    def _validate(vals: List[int]) -> None:
        negs = list(filter(lambda x: x < 0, vals))
        if len(negs) > 0:
            negs_str = map(str, negs)
            raise ValueError('negatives not allowed ' + ','.join(negs_str))

    @staticmethod
    def find_separator(s: str) -> Tuple[str, str]:
        match = re.search(r'^//(.*)\n(.*)', s)
        default_separator = r'[\n,]'
        if match:
            return match.group(1), match.group(2)
        return default_separator, s
