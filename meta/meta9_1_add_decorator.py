import time
from functools import wraps


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
def countdown(n):
    pass


# equals to
# def countdown(n):
#     pass
# countdown = timethis(countdown)

class A:
    @classmethod
    def method(cls):
        pass


class B:
    # Equivalent definition of a class method
    def method(cls):
        pass

    method = classmethod(method)
