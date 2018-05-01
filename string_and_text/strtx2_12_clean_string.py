#  str.translate()
import unicodedata
import sys

s = 'pýtĥöñ\fis\tawesome\r\n'
remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None  # Deleted
}
a = s.translate(remap)
print(a)  # pýtĥöñ is awesome\n

# noinspection PyTypeChecker
# fromkeys(seq[, value])
# all accidental signs
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', a)
print(b.translate(cmb_chrs))  # python is awesome\n

# change unicode num into ascii
digitmap = {c: ord('0') + unicodedata.digit(chr(c))
            for c in range(sys.maxunicode)
            if unicodedata.category(chr(c)) == 'Nd'}
print(len(digitmap))  # 580
x = '\u0661\u0662\u0663'
print(x.translate(digitmap))  # 123

# use encode decode
b = unicodedata.normalize('NFD', a)
# ignore replace strict: how to handle error
print(b.encode('ascii', 'ignore'))  # b'python is awesome\n'
print(b.encode('ascii', 'ignore').decode('ascii'))  # python is awesome\n

# multi replace can faster than translate
