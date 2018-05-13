import types
from functools import wraps


class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        print(self, instance, cls)
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


@Profiled
def add(x, y):
    return x + y


class Spam:
    @Profiled
    def bar(self, x):  # when we visit Profiled, trigger get
        print(self, x)


print(add.ncalls)
add(2, 3)
print(add.ncalls)

s = Spam()


def grok(self, x):
    pass


print(grok.__get__(s, Spam))
