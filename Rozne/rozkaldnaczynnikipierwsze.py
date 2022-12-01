from math import sqrt

n = int(input())
b = 2
while b <= sqrt(n):
    if n%b==0:
        print(b)
        n=n//b
    else:
        b+=1

if n > 1:
    print(n)