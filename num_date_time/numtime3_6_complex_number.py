import cmath

# complex(real, imag)
a = complex(2, 4)
b = 3 - 5j
print(a, a.real, a.imag)
print(a + b)
print(a * b)
print(abs(a))

print(cmath.sin(a))
# error
# math.sqrt(-1)
print(cmath.sqrt(-1))
