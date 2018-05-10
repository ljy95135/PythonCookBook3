# singleton
import logging
import weakref

# example
a = logging.getLogger('foo')
b = logging.getLogger('bar')
c = logging.getLogger('foo')
print(a is c, a is b)


# The class in question
class Spam:
    def __init__(self, name):
        self.name = name


# Caching support
_spam_cache = weakref.WeakValueDictionary()


def get_spam(name):
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s
    else:
        s = _spam_cache[name]
    return s


a = get_spam('foo')
b = get_spam('bar')
c = get_spam('foo')
print(a is c, a is b)


# example not works
class Spam:
    _spam_cache = weakref.WeakValueDictionary()

    def __new__(cls, name):
        if name in cls._spam_cache:
            return cls._spam_cache[name]
        else:
            self = super().__new__(cls)
            cls._spam_cache[name] = self
            return self

    def __init__(self, name):
        print('Initializing Spam')
        self.name = name


s = Spam('Dave')
t = Spam('Dave')  # still init
print(s is t)  # True

print('weak ref')
a = get_spam('foo')
b = get_spam('bar')
c = get_spam('foo')
print(list(_spam_cache))  # ['foo', 'bar']
del a
print(list(_spam_cache))  # ['foo', 'bar']
del c
print(list(_spam_cache))  # ['bar']
del b
print(list(_spam_cache))  # []
