import re

# str.find()
text = 'yeah, but no, but yeah, but no, but yeah'
print(text == 'yeah')  # False
print(text.find('no'))  # 10

# re
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
# Simple matching: \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')

# also can compile re pattern
# regex.findall
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.match(text))  # None from start to end
print(datepat.findall(text))

# capture group
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
print(m.group(0))  # 11/27/2012
print(m.group(1))  # 11
print(m.group(2))  # 27
print(m.group(3))  # 2012
print(m.groups())  # ('11', '27', '2012')
print(datepat.findall(text))  # [('11', '27', '2012'), ('3', '13', '2013')]

# match return in a list
# use regex.finditer to return a generator
for m in datepat.finditer(text):
    print(m.groups())

# make sure end of string $
# datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
