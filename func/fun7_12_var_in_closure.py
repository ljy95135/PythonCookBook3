import sys
from timeit import timeit


def sample():
    n = 0

    # Closure function
    def func():
        print('n=', n)

    # Accessor methods for n
    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    # Attach as function attributes
    func.get_n = get_n
    func.set_n = set_n
    return func


f = sample()
f()
f.set_n(10)
print(f.get_n())


# closure class
class ClosureInstance:
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals
        # Update instance dictionary with callables
        self.__dict__.update((key, value) for key, value in locals.items()
                             if callable(value))

    # Redirect special methods
    def __len__(self):
        return self.__dict__['__len__']()


def Stack():
    items = []

    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()


s = Stack()
print(s)
s.push(10)
s.push(20)
s.push('Hello')
print(s.pop(), s.pop(), s.pop())


class Stack2:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)


s = Stack()  # faster!
print(timeit('s.push(1);s.pop()', 'from __main__ import s'))
s = Stack2()
print(timeit('s.push(1);s.pop()', 'from __main__ import s'))
