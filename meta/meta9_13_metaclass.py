import weakref


class NoInstances(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly")


class Spam(metaclass=NoInstances):
    @staticmethod
    def grok(x):
        print('Spam.grok')


# s = Spam()

class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


# Example
class Spam(metaclass=Singleton):
    def __init__(self):
        print('Creating Spam')


a = Spam()
b = Spam()
print(a is b)


class Cached(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(self, *args):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
        return obj


# Example
class Spam(metaclass=Cached):
    def __init__(self, name):
        print('Creating Spam({!r})'.format(name))
        self.name = name


a = Spam('Guido')
b = Spam('Diana')
c = Spam('Guido')  # Cached
print(a is b, a is c)
