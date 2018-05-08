def read():
    with open('somefile.txt', 'rt') as f:
        _ = f.read()

    # encoding
    with open('somefile.txt', 'rt', encoding='latin-1') as _:
        pass


def write():
    with open('somefile.txt', 'rt') as f:
        for _ in f:
            pass

# wt: truncate
# print(line2, file=f)
# f.close without with
# newline to handle \n \r\n
# errors to handle error
