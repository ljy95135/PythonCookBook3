import math


class Structure1:
    # Class variable that specifies expected fields
    _fields = []

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


class Stock(Structure1):
    _fields = ['name', 'shares', 'price']


class Point(Structure1):
    _fields = ['x', 'y']


class Circle(Structure1):
    _fields = ['radius']

    def area(self):
        return math.pi * self.radius ** 2


s = Stock('ACME', 50, 91.1)
p = Point(2, 3)
c = Circle(4.5)


# keyword
class Structure2:
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        # Set all of the positional arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
        # Set the remaining keyword arguments
        for name in self._fields[len(args):]:
            setattr(self, name, kwargs.pop(name))
        # Check for any remaining unknown arguments
        if kwargs:
            raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))


# or add new attr
def __init__(self, *args, **kwargs):
    if len(args) != len(self._fields):
        raise TypeError('Expected {} arguments'.format(len(self._fields)))
    # Set the arguments
    for name, value in zip(self._fields, args):
        setattr(self, name, value)
    # Set the additional arguments (if any)
    extra_args = kwargs.keys() - self._fields
    for name in extra_args:
        setattr(self, name, kwargs.pop(name))
    if kwargs:
        raise TypeError('Duplicate values for {}'.format(','.join(kwargs)))
