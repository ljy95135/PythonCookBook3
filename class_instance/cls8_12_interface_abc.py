from abc import ABCMeta, abstractmethod
import io
import collections


class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


# TypeError
# a = IStream()

class SocketStream(IStream):
    def read(self, maxbytes=-1):
        pass

    def write(self, data):
        pass


# check type
def serialize(obj, stream):
    if not isinstance(stream, IStream):
        raise TypeError('Expected an IStream')
    pass


# another way
# Register the built-in I/O classes as supporting our interface
# IStream.register(io.IOBase)  # IOBase is sub class of IStream
# f = open('foo.txt')
# isinstance(f, IStream)  # Returns True


# more decorators
# abstractmethod neat func name
class A(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @classmethod
    @abstractmethod
    def method1(cls):
        pass

    @staticmethod
    @abstractmethod
    def method2():
        pass


# ABC
print(isinstance([], collections.Sequence))
print(isinstance([], collections.Iterable))
print(isinstance([], collections.Sized))
print(isinstance([], collections.Mapping))
