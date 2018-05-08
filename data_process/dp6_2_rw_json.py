import json
from urllib.request import urlopen
from pprint import pprint
from collections import OrderedDict

# None(null), bool(true false), int, float, str. lists, tuples, dicts
# key for dict: str

# basic
data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}
json_str = json.dumps(data)
data = json.loads(json_str)
print(data)
# use dump and load for files

# pprint Data pretty printer
u = urlopen('http://search.twitter.com/search.json?q=python&rpp=5')
resp = json.loads(u.read().decode('utf-8'))
pprint(resp)

# get a OrderedDict
s = '{"name": "ACME", "shares": 50, "price": 490.1}'
data = json.loads(s, object_pairs_hook=OrderedDict)
print(data)


# JSONobj
class JSONObject:
    def __init__(self, d):
        self.__dict__ = d  # just use dict


data = json.loads(s, object_hook=JSONObject)
print(data.name)

# indent
data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}
print(json.dumps(data, indent=4))


# json an obj
# must be JSON serializable
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def serialize_instance(obj):
    d = {'__classname__': type(obj).__name__}
    d.update(vars(obj))
    return d


# Dictionary mapping names to known classes
classes = {
    'Point': Point
}


def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)  # Make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
        return obj
    else:
        return d


p = Point(2, 3)
s = json.dumps(p, default=serialize_instance)
print(s)
a = json.loads(s, object_hook=unserialize_object)
