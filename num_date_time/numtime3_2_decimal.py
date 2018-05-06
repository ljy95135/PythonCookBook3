# Decimal
from decimal import Decimal, getcontext, localcontext
import math

a = 4.2
b = 2.1
print(a + b)
print(a + b == 6.3)  # False

a = Decimal('4.2')
b = Decimal('2.1')
print(a + b)
print((a + b) == Decimal('6.3'))  # True

# context
a = Decimal('1.3')
b = Decimal('1.7')
print(a / b)
print(getcontext())
with localcontext() as ctx:
    ctx.prec = 50
    print(a / b)

# deviation/error
nums = [1.23e+18, 1, -1.23e+18]
print(sum(nums))
print(math.fsum(nums))
