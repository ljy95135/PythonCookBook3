# create a slice from generator
# islice
import itertools


def count(n):
    while True:
        yield n
        n += 1


c = count(0)
for x in itertools.islice(c, 10, 20):  # use None like 10:
    print(x)  # 10-19
