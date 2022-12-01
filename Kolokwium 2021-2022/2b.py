import math

def zamiana(liczba, sys):

    T = []

    while liczba > 0:

        T.append(liczba%sys)
        liczba//=sys

    return T


n = int(input())

N = int(math.log10(n)) + 1 #dlugosc liczby

def prime(liczba):

    if liczba < 2: return False

    if liczba == 2 or liczba == 3:
        return True

    if liczba % 2 == 0 or liczba % 3==0:
        return False

    a = 5

    while a < int(math.sqrt(liczba)) + 1:

        if liczba % a == 0:
            return False
        a+=2

        if liczba % a == 0:
            return False

        a+=4

    return True

def czy_iloczynowo_pierwsza(T):

    suma = 1

    for i in range(len(T)):
        suma*= T[i]
    print(suma)
    if prime(suma): return True
    return False

for i in range(2, 16 + 1):
    T = zamiana(n, i)

    if czy_iloczynowo_pierwsza(T):
        print("Pikoci: ", i)

for j in range(N - 1): #N - 1, bo rotuje N - 1 razy
    
    n = (n%10**(N - 1))*10 + n//10**(N-1)
    
    for i in range(2, 16):
        T = zamiana(n, i)
        if czy_iloczynowo_pierwsza(T):
            print("Mlekoczi: ", i)

    

