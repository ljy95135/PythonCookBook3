# __prepare__ creates class name space (a map)
# __new__ __init__
# keyword metaclass not pollute class name space
# class var only can see in new and init


class MyMeta(type):
    # Optional
    @classmethod
    def __prepare__(cls, name, bases, *, debug=False, synchronize=False):
        # Custom processing
        print("pre", cls, name, bases)  # cls: <class '__main__.MyMeta'>
        return super().__prepare__(name, bases)  # type create class

    # Required
    def __new__(cls, name, bases, ns, *, debug=False, synchronize=False):
        print(cls, name, bases, ns)
        return super().__new__(cls, name, bases, ns)

    # Required
    def __init__(self, name, bases, ns, *, debug=False, synchronize=False):
        print(self, name, bases, ns)
        super().__init__(name, bases, ns)


class Spam(metaclass=MyMeta, debug=True, synchronize=True):
    pass
