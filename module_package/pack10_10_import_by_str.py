import importlib

math = importlib.import_module('math')
print(math.sin(2))
mod = importlib.import_module('urllib.request')
u = mod.urlopen('http://www.python.org')
print(u)

# Same as 'from . import b'
# b = importlib.import_module('.b', __package__)
