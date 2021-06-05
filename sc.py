class StringCalculator:
    def add(self, s: str) -> int:
        if s == '':
            return 0
        return self.parse_number(s)

    @staticmethod
    def parse_number(number: str):
        return int(number)
