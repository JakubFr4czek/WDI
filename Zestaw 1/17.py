eps = 10e-7
a = 1
b = 1

x = 0

while abs(b/a - x) > eps:
    x = b/a
    a, b = b, a+b
print(x)