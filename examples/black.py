"""
Before:

    def example_func(
            some_variable, another_variable):
        result  = some_variable + \
                  another_variable
        return                 result
After:

def example_func(some_variable, another_variable):
    result = some_variable + another_variable
    return result

"""
