import struct


class StructField:
    """
    Descriptor representing a simple structure field
    """

    def __init__(self, struct_format, offset):
        self.format = struct_format
        self.offset = offset

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            r = struct.unpack_from(self.format, instance._buffer, self.offset)
            return r[0] if len(r) == 1 else r


class Structure:
    def __init__(self, bytedata):
        self._buffer = memoryview(bytedata)


class PolyHeader(Structure):
    file_code = StructField('<i', 0)
    min_x = StructField('<d', 4)
    min_y = StructField('<d', 12)
    max_x = StructField('<d', 20)
    max_y = StructField('<d', 28)
    num_polys = StructField('<i', 36)


def poly(f):
    phead = PolyHeader(f.read(40))
    print(phead.file_code == 0x1234, phead.min_x)
