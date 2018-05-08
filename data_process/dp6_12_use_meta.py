import struct


# noinspection PyMissingConstructor,PyMethodParameters,PyUnusedLocal
class StructureMeta(type):
    """
    Metaclass that automatically creates StructField descriptors
    """

    def __init__(self, clsname, bases, clsdict):
        fields = getattr(self, '_fields_', [])
        byte_order = ''
        offset = 0
        for struct_format, fieldname in fields:
            if struct_format.startswith(('<', '>', '!', '@')):
                byte_order = struct_format[0]
                struct_format = struct_format[1:]
            struct_format = byte_order + struct_format
            setattr(self, fieldname, StructField(struct_format, offset))
            offset += struct.calcsize(struct_format)
        setattr(self, 'struct_size', offset)


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


# noinspection PyUnresolvedReferences
class Structure(metaclass=StructureMeta):
    def __init__(self, bytedata):
        self._buffer = bytedata

    @classmethod
    def from_file(cls, f):
        return cls(f.read(cls.struct_size))


class PolyHeader(Structure):
    _fields_ = [
        ('<i', 'file_code'),
        ('d', 'min_x'),
        ('d', 'min_y'),
        ('d', 'max_x'),
        ('d', 'max_y'),
        ('i', 'num_polys')
    ]
