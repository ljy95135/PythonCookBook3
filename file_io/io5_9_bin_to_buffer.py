import os.path


# bytearray buffer
def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf


def write_back():
    with open('sample.bin', 'wb') as f:
        f.write(b'Hello World')
    buf = read_into_buffer('sample.bin')
    buf[0:5] = b'Hallo'
    with open('newsample.bin', 'wb') as f:
        f.write(buf)
    # memoryview
    m1 = memoryview(buf)
    m2 = m1[-5:]
    m2[:] = b'WORLD'  # just change buf
