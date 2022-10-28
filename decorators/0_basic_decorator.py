# A decorator is a callable that takes another function as an argument (the decorated function)

# Example of decorated function

def decorate(func):
    print('inside decoration function')
    return func


@decorate
def decorated_function():
    print('running decorated function')


decorated_function()


# Is the same as...

def non_decorated_function():
    print('running non decorated function')


decorate(non_decorated_function())
