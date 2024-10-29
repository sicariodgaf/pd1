class InvalidArgumentError(Exception):
    pass


class UnknownOperationError(Exception):
    pass


class InvalidOperandError(Exception):
    pass


class Calculator:
    def __init__(self):
        self.operations = {}

    def add_operation(self, operator: str, function):
        if not isinstance(operator, str) or not callable(function):
            raise InvalidArgumentError('INVALID_ARGUMENT')
        self.operations[operator] = function

    def _parse_expression(self, expression: str):
        parts = expression.split()
        if len(parts) != 3:
            raise InvalidOperandError('INVALID_OPERAND')

        a, operator, b = parts
        return self._convert_operands(a, b), operator

    def _convert_operands(self, a: str, b: str):
        try:
            return float(a), float(b)
        except ValueError:
            raise InvalidOperandError('INVALID_OPERAND')

    def calculate(self, expression: str):
        if not isinstance(expression, str):
            raise InvalidArgumentError('INVALID_ARGUMENT')

        (a, b), operator = self._parse_expression(expression)

        if operator not in self.operations:
            raise UnknownOperationError('UNKNOWN_OPERATION')

        return self.operations[operator](a, b)


if __name__ == "__main__":
    calc = Calculator()
    calc.add_operation('+', lambda a, b: a + b)
    calc.add_operation('-', lambda a, b: a - b)
    calc.add_operation('*', lambda a, b: a * b)
    calc.add_operation('/', lambda a, b: a / b)

    test_cases = [
        "10 + 1",
        "10 - 1",
        "10 * 3",
        "10 / 0",
        "a - 10",
        "2 ** 3",
        10 + 1
    ]

    for case in test_cases:
        try:
            result = calc.calculate(case)
            print(f"{case} = {result}")
        except (InvalidArgumentError, UnknownOperationError, InvalidOperandError, ZeroDivisionError) as e:
            print(f"Error: {e}")
