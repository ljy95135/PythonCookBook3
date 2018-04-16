# sort dicts list by one keyword
# use operator.itemgetter to generate a callable for key param

import operator

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

rows_by_fname = sorted(rows, key=operator.itemgetter('fname'))  # also can be index
rows_by_uid = sorted(rows, key=operator.itemgetter('uid'))
print(rows_by_uid)
rows_by_lfname = sorted(rows, key=operator.itemgetter('lname', 'fname'))  # return tuple (l[lname], l[fname])
# equals to
# lambda: r: r[0] or r: (r[0], r[1])
