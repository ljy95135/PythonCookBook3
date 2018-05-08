import array  # array of basic values


def read():
    with open('somefile.bin', 'rb') as f:
        data = f.read()
        _ = data.encode('utf-8')


def write():
    with open('somefile.bin', 'wb') as f:
        f.write(b'Hello World')
        # use array
        nums = array.array('i', [1, 2, 3, 4])
        f.write(nums)
    a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
    # os dependent
    with open('data.bin', 'rb') as f:
        f.readinto(a)
