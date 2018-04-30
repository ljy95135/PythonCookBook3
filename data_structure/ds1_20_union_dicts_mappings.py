# use ChainMap
# find in the order of params
from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)
print(c['x'])  # Outputs 1 (from a)
print(c['y'])  # Outputs 2 (from b)
print(c['z'])  # Outputs 3 (from a)

print(len(c))  # 3
list(c.keys())  # ['x', 'y', 'z']
list(c.values())  # [1, 2, 3]
# show first found values
# always change the first dict
c['z'] = 10
c['w'] = 40
del c['x']
print(a)  # {'w': 40, 'z': 10}
# you cant del c['y'] which is in b KeyError

values = ChainMap()
values['x'] = 1
# Add a new mapping
values = values.new_child()
values['x'] = 2
# Add a new mapping
values = values.new_child()
values['x'] = 3
print(values)  # ChainMap({'x': 3}, {'x': 2}, {'x': 1})
print(values['x'])  # 3 newest the first

# ChainMap({'x': 2}, {'x': 1})
# discard last mapping
values = values.parents
print(values)

# or use update
# but this is  a new dict
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
merged.update(a)
print(merged)  # {'y': 2, 'z': 3, 'x': 1}
