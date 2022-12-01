
eps = 1e-10

a = 1
b = 10

x = (a+b)/2

while abs(x**x - 2022) > eps:

    x = (a+b)/2

    if(x**x - 2022 > 0):
        b = x
    else:
        a = x
print(x)