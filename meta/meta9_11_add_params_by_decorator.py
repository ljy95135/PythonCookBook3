from functools import wraps
import inspect


def optional_debug(func):
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*args, **kwargs)

    return wrapper


@optional_debug
def spam(a, b, c):
    print(a, b, c)


# def a(x, debug=False):
#     if debug:
#         print('Calling a')
# def b(x, y, z, debug=False):
#     if debug:
#         print('Calling b')
# def c(x, y, debug=False):
#     if debug:
#         print('Calling c')


def optional_debug(func):
    if 'debug' in inspect.getargspec(func).args:
        raise TypeError('debug argument already defined')

    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*args, **kwargs)

    return wrapper


@optional_debug
def a(x):
    pass


print(inspect.signature(a))  # only x


def optional_debug2(func):
    if 'debug' in inspect.getargspec(func).args:
        raise TypeError('debug argument already defined')

    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*args, **kwargs)

    sig = inspect.signature(func)
    parms = list(sig.parameters.values())
    parms.append(inspect.Parameter('debug',
                                   inspect.Parameter.KEYWORD_ONLY,
                                   default=False))
    wrapper.__signature__ = sig.replace(parameters=parms)
    return wrapper


@optional_debug2
def b(x, y, z):
    pass


print(inspect.signature(b))


@optional_debug
def c(x, y):
    pass


spam(1, 2, 3)
spam(1, 2, 3, debug=True)
