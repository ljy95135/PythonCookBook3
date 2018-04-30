import unicodedata

# one unicode has many representation
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

# \u0303n and \u00f1
print(s1)  # len 14
print(s2)  # len 15
print(s1 == s2)  # False

# NFC combined
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1)
print(t2)
print(t1 == t2)  # True

# NFD decomposed
t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print(t3 == t4)  # True

print(ascii(t1))
print(ascii(t3))

# NFKC NFKD
s = '\ufb01'
print(s)
print(unicodedata.normalize('NFD', s))
print(unicodedata.normalize('NFKD', s))  # two characters
print(unicodedata.normalize('NFKC', s))  # two characters

# erase accidental signs
# return combining class for accidental
t1 = unicodedata.normalize('NFD', s1)
print(''.join(c for c in t1 if not unicodedata.combining(c)))
