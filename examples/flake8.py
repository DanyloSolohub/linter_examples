"""
flake8-functions

    def some_long_function(first_parameter: int, second_parameter: int, third_parameter: int):
        first_parameter = first_parameter + second_parameter + third_parameter

        first_parameter = first_parameter + second_parameter + third_parameter

        first_parameter = first_parameter + second_parameter + third_parameter

        return first_parameter

Result:

    examples/flake8.py:1:1: CFQ001 Function some_long_function has length 6 that exceeds max allowed length 5




flake8-variables-names:

    a = 1
    foo = 2
    result = a + foo

Result:

    examples/flake8.py:29:1: VNE001 single letter variable names like 'a' are not allowed
    examples/flake8.py:30:1: VNE002 variable name 'foo' should be clarified




flake8-expression-complexity:

    first = 11
    second = 12
    if (first and second) and first > second and (second + 1 != first or first + 2 != second) and second < first:
        pass
Result:

    examples/flake8.py:29:4: ECE001 Expression is too complex (4 > 3)





flake8-cognitive-complexity:

    def f(a, b):
        if a:
            for i in range(b):
                if b:
                    return 1
Result:

    examples/flake8.py:39:1: CCR001 Cognitive complexity is too high (6 > 3)
"""
