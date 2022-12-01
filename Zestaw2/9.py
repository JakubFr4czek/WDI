def func(x):
    return 1/x

k = int(input())

eps = 1e-7
poczatek = 1

sum = 0

while poczatek + eps <= k:
    b = func(poczatek)
    a = poczatek + eps
    sum += a*b
    poczatek += eps
print(sum)

