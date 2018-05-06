# format of number
x = 1234.56789
print(format(x, '0.2f'))
print(format(x, '>10.1f'))
print(format(x, '^10.1f'))

# group operator/thousands separator
print(format(x, ','))
print(format(x, '0_.1f'))

# exponential
print(format(x, 'e'))
print(format(x, '0.2E'))
