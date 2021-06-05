class StringCalculator:
    def add(self, s: str) -> int:
        if s == '':
            return 0
        return self._string_to_number(s)

    @staticmethod
    def _string_to_number(number: str):
        return int(number)
