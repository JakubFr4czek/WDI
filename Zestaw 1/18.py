
s = int(input())

a = 1
b = (s/(a*a) + 2*a)/3

eps = 10e-7

while abs(a - b) > eps:
    a = b
    b = (s/(a*a) + 2*a)/3

print(b)