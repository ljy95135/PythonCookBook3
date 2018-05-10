# Descriptor attribute for an integer type-checked attribute
# can be used in type check


class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):  # in this example: Point obj and Point
        print(self, instance, cls)
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


# caught by Integer for x and y
class Point:
    x = Integer('x')  # class level
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(2, 3)
p2 = Point(3, 4)
print(p1.x, p2.x)
print(Point.x)  # instance is None


# example
# Descriptor for a type-checked attribute
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected ' + str(self.expected_type))
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


# Class decorator that applies it to selected attributes
def typeassert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
            # Attach a Typed descriptor to the class
            setattr(cls, name, Typed(name, expected_type))
        return cls

    return decorate


# Example use
@typeassert(name=str, shares=int, price=float)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
