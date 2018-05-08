import gzip
import bz2


def gzip_read():
    with gzip.open('somefile.gz', 'rt') as f:
        text = f.read()
    with gzip.open('somefile.gz', 'wt', compresslevel=9) as f:  # 9 max 1 min
        f.write(text)
    # can use as file
    f = open('somefile.gz', 'rb')
    with gzip.open(f, 'rt') as g:
        _ = g.read()


def bz2_read():
    with bz2.open('somefile.bz2', 'rt') as f:
        text = f.read()
    with bz2.open('somefile.bz2', 'wt') as f:
        f.write(text)
