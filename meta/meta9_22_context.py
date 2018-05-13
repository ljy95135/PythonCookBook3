# Plan A
# __enter__ __exit__

# Plan B
# @contextmanager

import time
from contextlib import contextmanager


@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield  # before is __enter__
        # after is __exit__
    finally:
        end = time.time()
        print('{}: {}'.format(label, end - start))


@contextmanager
def timethis2(label):
    start = time.time()
    yield
    end = time.time()
    print('{}: {}'.format(label, end - start))


# Example use
# slow than decorator with just countdown
with timethis('counting'):
    n = 10000000
    while n > 0:
        n -= 1

with timethis2('counting'):
    n = 10000000
    while n > 0:
        n -= 1


# example 2
@contextmanager
def list_transaction(orig_list):
    working = list(orig_list)
    yield working
    orig_list[:] = working


items = [1, 2, 3]

with list_transaction(items) as working:
    working.append(4)
    working.append(5)

print(items)
try:
    with list_transaction(items) as working:
        working.append(6)
        working.append(7)
        raise RuntimeError('oops')
except RuntimeError:
    pass

print(items)  # [1, 2, 3, 4, 5]


class timethis3:
    def __init__(self, label):
        self.label = label

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_ty, exc_val, exc_tb):
        end = time.time()
        print('{}: {}'.format(self.label, end - self.start))


# same speed
# so it is not the problem of contextmanager
with timethis3('counting'):
    n = 10000000
    while n > 0:
        n -= 1
