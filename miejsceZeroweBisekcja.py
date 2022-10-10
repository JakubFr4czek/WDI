# f(x) = x^X - 2022

eps = 1e-10

a = 1
b = 10

x = (a+b)/2

while abs(x**x - 2022) >= eps:
    if x**x - 2022 > 0:
        b = x
    else:
        a = x
    x = (a+b)/2
print(x)