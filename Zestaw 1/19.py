from re import A


def silnia(n):
    if n == 0: return 1
    return silnia(n - 1)*n

eps = 10e-700

sum = 1
a = 1/silnia(1)
count = 2
while abs(a - (1/silnia(count))) > eps:
    sum += a
    a = 1/silnia(count)
    count+=1

print(sum)
