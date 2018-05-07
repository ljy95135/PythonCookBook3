from itertools import permutations, combinations, combinations_with_replacement

items = ['a', 'b', 'c']
for p in permutations(items):
    print(p)  # ABC tuple

for p in permutations(items, 2):
    print(p)  # AB tuple

for c in combinations(items, 3):
    print(c)

for c in combinations(items, 1):
    print(c)

for c in combinations_with_replacement(items, 3):
    print(c)
