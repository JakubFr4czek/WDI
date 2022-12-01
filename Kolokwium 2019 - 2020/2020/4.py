from math import sqrt

def czy_pierwsza(liczba):

    if liczba < 2:
        return False

    if liczba == 2 or liczba ==3:
        return True

    if liczba %2 == 0 or liczba %2 == 0:
        return False

    a = 5

    while a <= int(sqrt(liczba) + 1):

        if liczba % a == 0:
            return False
        a+=2

        if liczba % a ==0:
            return False
        a+=2

    return True

def prime_factors(liczba):

    count = 0

    a = 2

    while liczba > 1:

        while liczba % a == 0:
            count +=1
            liczba//=a
        a+=1

    if liczba > 1:
        count +=1
        
    return count

t1 = [1,2,3,4,5,6,7,8,9,10]
t2 = [1,2,3,4,5,6,7,8,9,10]

N = len(t1)

for i in range(1, N + 1): #dlugosc kawalka

    for j in range(N):

        if j + i <= N:

            suma1 = 0

            for k in range(j,j + i):
                suma1 += t1[k]

            for j1 in range(N):

                if j1 + i <= N:

                    suma2 = 0

                    for k1 in range(j1, j1 + i):
                        suma2 += t2[k1]

                    if prime_factors(suma1*suma2) == 2:
                        print("Istnieje!", j," ", j + i, " | ", j1, " ", j1 + i," || ", suma1*suma2)
                    
                    

                    

                