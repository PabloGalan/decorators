def decorator_function_1(func):
    print('function 1')
    return func


def decorator_function_2(func):
    print('function 2')
    return func


@decorator_function_1
@decorator_function_2
def decorated_function(name):
    print(f"Hello {name}")
    return 1


#  the decorators being executed in the order they are listed. In other words, @decorated_function calls
#  @decorator_function_1, which calls decorator_function_2(), or
#  decorated_function(decorator_function_1(decorator_function_2()))

decorated_function('Example')
