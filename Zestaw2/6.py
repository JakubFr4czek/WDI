from math import sqrt
liczba = int(input())

if int(sqrt(liczba))**2 == liczba:
    print(sqrt(liczba), " ", sqrt(liczba))
    exit()

c = d =-1
min = liczba

for i in range(1, int(sqrt(liczba) + 1)):

    
    if liczba % i == 0:
        a = liczba //i
        
        if abs(a - i) < min:
            min = abs(a - i)
            c, d = a, i

print(c," ", d)
        
