# named slice

record = '....................100 .......513.25 ..........'
cost1 = int(record[20:23]) * float(record[31:37])

SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost2 = int(record[SHARES]) * float(record[PRICE])

a = slice(5, 50, 2)
print(a.start, a.stop, a.step)

# slice.indices
s = 'HelloWorld'
print(a.indices(len(s)))  # change the end (5, 10, 2)
for i in range(*a.indices(len(s))):
    print(i, s[i])
