import re
from calendar import month_abbr

# str.replace(old, new[, count])
text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))  # return a copy of string

# re.sub
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
# \1 \2 is group number (start from 1)
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
newtext, n = datepat.subn(r'\3-\1-\2', text)
print(n)  # 2


# use a func
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))


print(datepat.sub(change_date, text))  # Today is 27 Nov 2012. PyCon starts 13 Mar 2013.
