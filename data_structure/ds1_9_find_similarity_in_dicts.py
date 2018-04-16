# find similarity in two dicts

a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}

# common keys
print(a.keys() & b.keys())  # { 'x', 'y' }
print(a.keys() - b.keys())  # { 'z' } not in b
print(a.items() & b.items())  # { ('y', 2) }

# new dict with certain keys removed
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(c)
