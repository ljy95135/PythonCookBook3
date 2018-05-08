import sys

# can't write bytes to file
# sys.stdout.write(b'Hello\n')
sys.stdout.buffer.write(b'Hello\n')
print(b'Hello\n')