import math

n = int(input())

a = 1
b = 1

while a <= math.sqrt(n):
    if a * b == n:
        print(a, " ", b)
        break
    b = a + b
    a = b - a