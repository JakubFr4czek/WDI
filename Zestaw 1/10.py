import math

n = int(input())

a = 2
suma = 0

while a < math.sqrt(n):

    if n % a == 0:
        suma += a + n//a
    a += 1

if a*a == n:
    suma += a
suma +=1     

print(suma)