import functools


def cache(func):
    """Keep a cache of previous function calls"""

    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        print(f'Call wrapper with {args[0]}')
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]

    wrapper_cache.cache = dict()
    return wrapper_cache


@cache
def fibonacci(num):
    print(f'Call fibonacci with {num}')
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


print(f'fibonacci {fibonacci(15)}')
print('------------------------------------------')
print(f'fibonacci {fibonacci(17)}')
