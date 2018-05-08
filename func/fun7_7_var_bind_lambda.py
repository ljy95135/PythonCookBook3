x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y
print(a(10))  # 30
print(b(10))  # 30

# free variable, use value when call
# if want the value when define
x = 10
a = lambda y, x=x: x + y
x = 20
b = lambda y, x=x: x + y
print(a(10))  # 20
print(b(10))  # 30

funcs = [lambda xx, n=n: xx + n for n in range(5)]
for f in funcs:
    print(f(0))
