import sys
import os

print(sys.getfilesystemencoding())  # 'utf-8'


def file():
    with open('jalape\xf1o.txt', 'w') as f:
        f.write('Spicy!')
    os.listdir('.')
    os.listdir(b'.')  # byte string  [b'jalapen\xcc\x83o.txt']
    with open(b'jalapen\xcc\x83o.txt') as f:
        print(f.read())
