from struct import Struct
import numpy as np


def write_records(records, binformat, f):
    """
    Write a sequence of tuples to a binary file of structures.
    """
    record_struct = Struct(binformat)
    for r in records:
        f.write(record_struct.pack(*r))


def read_records(binformat, f):
    record_struct = Struct(binformat)
    chunks = iter(lambda: f.read(record_struct.size), b'')
    return (record_struct.unpack(chunk) for chunk in chunks)


def unpack_records(binformat, data):
    record_struct = Struct(binformat)
    return (record_struct.unpack_from(data, offset)
            for offset in range(0, len(data), record_struct.size))


def write(f):
    records = [(1, 2.3, 4.5),
               (6, 7.8, 9.0),
               (12, 13.4, 56.7)]
    write_records(records, '<idd', f)


def read(f):
    for rec in read_records('<idd', f):
        print(rec)


# use numpy
def numpyfile(f):
    records = np.fromfile(f, dtype='<i,<d,<d')  # array
    print(records)
