# Normally we'll prefer lazy evaluation
# In this case we can choose the order


def deco(func):
    def wrap(*args, **kwargs):
        print(f'decorator before calling - running {func.__name__}')
        ret = func(*args, **kwargs)
        print(f'decorator after calling - running {func.__name__}')
        return ret

    return wrap


@deco
def decorated_function_1():
    print('starting decorated_function_1')
    return None


@deco
def decorated_function_2():
    print('starting decorated_function_2')
    return None


decorated_function_1()
decorated_function_2()
