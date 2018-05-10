# Basic use
class A1:
    def __init__(self):
        self.x = 0

    def spam(self):
        print('A.spam')


class B1(A1):
    def __init__(self):
        super().__init__()
        self.y = 1

    def spam(self):
        print('B.spam')
        super().spam()  # Call parent spam()


b = B1()
print(b.x)


# example
class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):  # when default fails
        return getattr(self._obj, name)  # _obj.name

    # Delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)  # Call original __setattr__
        else:
            setattr(self._obj, name, value)


# sometimes
class Base2:
    def __init__(self):
        print('Base.__init__')


class A2(Base2):
    def __init__(self):
        Base2.__init__(self)
        print('A.__init__')


# but for multi inherit
class Base3:
    def __init__(self):
        print('Base.__init__')


class A3(Base3):
    def __init__(self):
        Base3.__init__(self)
        print('A3.__init__')


class B3(Base3):
    def __init__(self):
        Base3.__init__(self)
        print('B3.__init__')


class C3(A3, B3):
    def __init__(self):
        A3.__init__(self)
        B3.__init__(self)
        print('C3.__init__')


c = C3()  # Base-A-Base-B-C


# use super
class Base4:
    def __init__(self):
        print('Base4.__init__')


class A4(Base4):
    def __init__(self):
        super().__init__()
        print('A4.__init__')


class B4(Base4):
    def __init__(self):
        super().__init__()
        print('B4.__init__')


class C4(A4, B4):
    def __init__(self):
        super().__init__()  # Only one call to super() here
        print('C4.__init__')


c = C4()  # Base-B-A-C

# method resolution order mro
# first check sub than base
# check base in order
# choose the first valid base
print(C4.__mro__)  # C A B Base object


# example
class A5:
    def spam(self):
        print('A.spam')
        super().spam()


# a = A5()
# a.spam()  # error


class B5:
    # noinspection PyMethodMayBeStatic
    def spam(self):
        print('B.spam')


class C5(A5, B5):
    pass


c = C5()
c.spam()  # A.spam B.spam
# C5.__mro__ C A B obj
# use A's spam and super is B
