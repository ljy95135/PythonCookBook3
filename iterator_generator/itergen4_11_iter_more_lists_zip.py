# zip length is the shortest one
from itertools import zip_longest

xpts = [1, 5, 4, 2]
ypts = [101, 78, 37, 15, 62, 99]
for x, y in zip(xpts, ypts):
    print(x, y)

for x, y in zip_longest(xpts, ypts, fillvalue=None):
    print(x, y)
