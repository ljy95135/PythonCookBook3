# fnmatch: unix filename match
from fnmatch import fnmatch, fnmatchcase

# filename pattern
print(fnmatch('foo.txt', '*.txt'),
      fnmatch('foo.txt', '?oo.txt'),
      fnmatch('Dat45.csv', 'Dat[0-9]*'))  # True True True
# fnmatch case_sensitive or not is based on os Windows not sensitive
# fnmatchcase sensitive
print(fnmatchcase('foo.txt', '*.TXT'))  # False

# power is between str func and re
addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]
# ['5412 N CLARK ST', '1060 W ADDISON ST', '2122 N CLARK ST']
print([addr for addr in addresses if fnmatchcase(addr, '* ST')])
# ['5412 N CLARK ST']
print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])
