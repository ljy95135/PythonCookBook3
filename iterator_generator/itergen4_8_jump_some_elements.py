# dropwhile only drops the start
from itertools import dropwhile


def drop(file):
    with open(file) as f:
        for line in dropwhile(lambda a_line: a_line.statswith('#'), f):
            print(line, end='')
