# mymodule.py


class A:
    def spam(self):
        print('A.spam')


class B(A):
    def bar(self):
        print('B.bar')


"""
mymodule/
    __init__.py
    a.py
    b.py
"""


# a.py
class A:
    def spam(self):
        print('A.spam')


# b.py
# from .a import A
class B(A):
    def bar(self):
        print('B.bar')

# __init__.py
# then can just use mymodule to get A and B
# from .a import A
# from .b import B

# import mymodule
# a = mymodule.A()
# a.spam()
# b = mymodule.B()
# b.bar()

# delay import
# __init__.py
# def A():
#     from .a import A
#     return A()
# def B():
#     from .b import B
#     return B()

# but check instance different
#  a = mymodule.A()
#  isinstance(x, mymodule.a.A)
