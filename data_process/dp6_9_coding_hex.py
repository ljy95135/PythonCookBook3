import binascii
import base64

# bin<-->hex
# only accept bytes or ascii unicode

s = b'hello'
h = binascii.b2a_hex(s)  # hexlify
print(h)
print(binascii.a2b_hex(h))  # unhexlify

h = base64.b16encode(s)  # only upper case
print(h)
print(base64.b16decode(h))
