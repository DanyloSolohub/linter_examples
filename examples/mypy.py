"""
Mypy:

    def example_function(first_parameter: list, second_parameter: set, third_parameter: int):
        first_parameter = first_parameter + second_parameter + third_parameter
        return first_parameter
Result:

    examples/mypy.py:1: error: Function is missing a return type annotation
    examples/mypy.py:2: error: Unsupported operand types for + ("List[Any]" and "Set[Any]")
    examples/mypy.py:2: error: Unsupported operand types for + ("List[Any]" and "int")
"""
