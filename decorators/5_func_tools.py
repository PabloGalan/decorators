import functools
import time

"""
This decorator works by storing the time just before the function starts running (at the line marked # 1) and 
just after the function finishes (at # 2). The time the function takes is then the difference between the two (at # 3)
"""


def timer(func):
    # We can use functools.wraps to decorate using the function

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        print(f'Starting {func.__name__!r}')
        start_time = time.perf_counter()  # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()  # 2
        run_time = end_time - start_time  # 3
        print(f'Finished {func.__name__!r} in {run_time:.6f} secs')
        return value

    return wrapper_timer


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i ** 2 for i in range(10000)])


waste_some_time(5)
