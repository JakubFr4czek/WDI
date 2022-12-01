pierwiastek = int(input())

a = 1
n = 1
suma = 1

while suma <= pierwiastek:
    n+=1
    a+=2
    suma += a
    

print(n - 1)