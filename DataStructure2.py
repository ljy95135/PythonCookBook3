from collections import defaultdict, OrderedDict
import json

#################################################
# 1.6  multidict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)

d = {}  # A regular dictionary
d.setdefault('a', []).append(1)  # similar to get
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
print(d)

#################################################
# 1.7  sort dict
# OrderedDict
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
    print(key, d[key])
# used for json
print(json.dumps(d))
# double size than default dict

#################################################
# 1.8 computation on dict
# use zip
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
min_price = min(zip(prices.values(), prices.keys()))
# min_price is (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys()))
# max_price is (612.78, 'AAPL')

prices_sorted = sorted(zip(prices.values(), prices.keys()))
# prices_sorted is [(10.75, 'FB'), (37.2, 'HPQ'),
# (45.23, 'ACME'), (205.55, 'IBM'),
# (612.78, 'AAPL')]

# prices_and_names=zip(prices.values(), prices.keys())
# # zip can only use once!
# print(min(prices_and_names)) # OK
# print(max(prices_and_names)) # ValueError: max() arg is an empty sequence

# cant solve for same smallest ot biggest

#################################################
