import os
import mmap


# map file to memory without using seek read&write
# mmp with memoryview
def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)


def use_mmp():
    size = 1000000
    with open('data', 'wb') as f:
        f.seek(size - 1)
        f.write(b'\x00')

    m = memory_map('data')
    print(len(m))  # 1000000
    print(m[0:10])
    print(m[0])
    m[0:11] = b'Hello World'  # also change at f
    m.close()
    print(m.closed)  # True

    # cast
    m = memory_map('data')
    v = memoryview(m).cast('I')  # see array module
    v[0] = 7
    print(m[:4])  # b'\x07\x00\x00\x00'
