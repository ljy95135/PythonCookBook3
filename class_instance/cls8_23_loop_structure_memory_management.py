# delete can work fine now
import gc
import weakref


# Class just to illustrate when deletion occurs
class Data:
    def __del__(self):
        print('Data.__del__')


# Node class involving a cycle
class Node:
    def __init__(self):
        self.data = Data()
        self.parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self


a = Data()
del a  # Immediately deleted
a = Node()
del a  # Immediately deleted
a = Node()
a.add_child(Node())
del a  # Not deleted (no message)
gc.collect()  # Force collection


# worse case
# Node class involving a cycle
class Node2:
    def __init__(self):
        self.data = Data()
        self.parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    # NEVER DEFINE LIKE THIS.
    # Only here to illustrate pathological behavior
    def __del__(self):
        del self.data
        del self.parent
        del self.children


print('worse case')
a = Node2()
a.add_child(Node2())
del a  # No message (not collected)
gc.collect()  # No message (not collected)

print('weakref')
a = Node()
a_ref = weakref.ref(a)
print(a_ref)
print(a_ref())
del a
print(a_ref())  # None
