import math

n = int(input())

a = 2

while(a < math.sqrt(n)):
    if n % a == 0:
        print(a, n//a)
    a+=1

if a * a == n:
    print(a)

print(n)
