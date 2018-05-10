import math


# property
# use when we need logic works for some attr
# not saved in memory but compute when use

# noinspection PyAttributeOutsideInit
class Person:
    def __init__(self, first_name):
        self.first_name = first_name  # use setter method

    # Getter function
    @property
    def first_name(self):  # same name with  setter and deleter
        return self._first_name

    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")


a = Person('Guido')
print(a.first_name)
a.first_name = 'Guido2'


# another way to implement
# noinspection PyAttributeOutsideInit
class Person2:
    def __init__(self, first_name):
        self.set_first_name(first_name)

    # Getter function
    def get_first_name(self):
        return self._first_name

    # Setter function
    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Deleter function (optional)
    def del_first_name(self):
        raise AttributeError("Can't delete attribute")

    # Make a property from existing get/set methods
    name = property(get_first_name, set_first_name, del_first_name)


a = Person2('Guido')
print(a.name)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius


c = Circle(4.0)
print(c.diameter)
