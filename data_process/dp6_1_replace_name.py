# with invalid name
# Street Address,Num-Premises,Latitude,Longitude 5412 N CLARK,10,41.980262,-87.668452
import csv
import re
from collections import namedtuple


def replace(f):
    f_csv = csv.reader(f)
    headers = [re.sub('[^a-zA-Z_]', '-', h) for h in next(f_csv)]
    Row = namedtuple('Row', headers)
    # convert myself
    col_types = [str, float, str, str, float, int]
    for r in f_csv:
        _ = Row(*r)
        _ = tuple(convert(value) for convert, value in zip(col_types, r))
    # for dict
    field_types = [('Price', float),
                   ('Change', float),
                   ('Volume', int)]
    for row in csv.DictReader(f):
        row.update((key, conversion(row[key])) for key, conversion in field_types)
