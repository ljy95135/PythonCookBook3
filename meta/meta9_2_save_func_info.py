import time
from functools import wraps
from inspect import signature


def timethis(func):
    """
    Decorator that reports the execution time.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


@timethis
def countdown(n: int):
    """
    Counts down
    """
    while n > 0:
        n -= 1


countdown(10000000)
print(countdown.__name__)
print(countdown.__doc__)
print(countdown.__annotations__)

# call wrapped func by __wrapped
countdown.__wrapped__(100000)  # original one
print(signature(countdown))
