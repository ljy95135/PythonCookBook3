from inspect import Signature, Parameter
import inspect

# example 1
parms = [Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
         Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=42),
         Parameter('z', Parameter.KEYWORD_ONLY, default=None)]
sig = Signature(parms)
print(sig)


def func(*args, **kwargs):
    bound_values = sig.bind(*args, **kwargs)
    for name, value in bound_values.arguments.items():
        print(name, value)


func(1, 2, z=3)


# example 2
def make_sig(*names):
    parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
             for name in names]
    return Signature(parms)


class Structure:
    __signature__ = make_sig()

    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)


class Stock(Structure):
    __signature__ = make_sig('name', 'shares', 'price')


class Point(Structure):
    __signature__ = make_sig('x', 'y')


print(inspect.signature(Stock))  # (name, shares, price)


# metaclass example

class StructureMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        clsdict['__signature__'] = make_sig(*clsdict.get('_fields', []))
        return super().__new__(cls, clsname, bases, clsdict)


class Structure(metaclass=StructureMeta):
    _fields = []

    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)  # used by signature
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)


class Stock(Structure):
    _fields = ['name', 'shares', 'price']


class Point(Structure):
    _fields = ['x', 'y']


print(inspect.signature(Stock))
