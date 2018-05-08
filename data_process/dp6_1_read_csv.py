# can use pandas not split csv line
import csv
import io
from collections import namedtuple

s = io.StringIO()
s.write('''Symbol,Price,Date,Time,Change,Volume
"AA", 39.48, "6/11/2007", "9:36am", -0.18, 181800
"AIG", 71.38, "6/11/2007", "9:36am", -0.15, 195500
"AXP", 62.58, "6/11/2007", "9:36am", -0.46, 935000
"BA", 98.31, "6/11/2007", "9:36am", +0.12, 104800
"C", 53.08, "6/11/2007", "9:36am", -0.25, 360900
"CAT", 78.29, "6/11/2007", "9:36am", -0.23, 225400''')
s.seek(0)
# print(s.getvalue())

f_csv = csv.reader(s)  # _csv.reader can change delimiter
headers = next(f_csv)  # ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
Row = namedtuple('Row', headers)
print(headers)
for row in f_csv:
    # all str, convert yourself
    print(row)  # ['AA', ' 39.48', ' "6/11/2007"', ' "9:36am"', ' -0.18', ' 181800']
    print(Row(*row))  # can use namedtuple

# use dict
s.seek(0)
f_csv = csv.DictReader(s)
for row in f_csv:
    print(row)  # OrderedDict
