import math


def compute_roots(nums):
    result = []
    for n in nums:
        result.append(math.sqrt(n))
    return result


def compute_roots(nums):
    result = []
    result_append = result.append
    for n in nums:
        result_append(sqrt(n))
    return result


def compute_roots(nums):
    sqrt = math.sqrt
    result = []
    result_append = result.append
    for n in nums:
        result_append(sqrt(n))
    return result


# use func
# somescript.py
import sys
import csv

with open(sys.argv[1]) as f:
    for row in csv.reader(f):
        # Some kind of processing
        pass

# somescript.py
import sys
import csv


def main(filename):
    with open(filename) as f:
        for row in csv.reader(f):
            # Some kind of processing
            pass


main(sys.argv[1])
