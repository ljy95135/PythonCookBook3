import math

a = float('inf')
x = float('inf')
b = float('-inf')
c = float('nan')

print(math.isinf(b))  # True
print(math.isnan(c))  # True

print(a > b)  # True
print(a == (a + 1))  # True
print(c == c)  # False
print(c != c)  # True

#  fpectl float point exception control
