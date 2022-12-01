
from math import sqrt

def NWD(a,b):

    while b > 0:
        a,b = b, a%b

    return a

def skroc(a, b):

    #podzielić przez Najwiekszy wspolny dzielnik (NWD)

    nwd = NWD(a, b)

    return a//nwd, b//nwd

def ile25(liczba):

    ile2 = 0
    ile5 = 0

    while(liczba%2==0):
        ile2 += 1
        liczba//=2

    while(liczba%5==0):
        ile5 += 1
        liczba//=5

    if liczba != 1:
        return 0

    return max(ile2, ile5)



a = int(input())
b = int(input())

a, b = skroc(a, b)

print(a//b, end = '')

if (a//b)*b == a:
    exit()

print(".",end = '')

for i in range(ile25(b)):

    a*=10

    print(a//b, end = '')

    a = a%b

if a != 0:

    print('(', end = '')

    print("reszta: ")
    reszta = a
    print(reszta)

    while True:
        a*=10
        print(a//b, end = '')
        a%=b

        if a == reszta:
            break

    print(")", end='')


    

    