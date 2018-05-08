from functools import partial

RECORD_SIZE = 32


def read_chunk():
    with open('somefile.data', 'rb') as f:
        records = iter(partial(f.read, RECORD_SIZE), b'')
        for r in records:
            print(r)
