from math import sqrt

def suma_cyfr(liczba):

    suma = 0

    while liczba > 0:

        suma += liczba%10
        liczba//=10

    return suma

def rozklad_i_suma(liczba):
    suma = 0

    temp = liczba
    a = 2

    while a <= sqrt(liczba):
        while temp % a == 0:
            suma += suma_cyfr(a) 
           #print(a," ", liczba//a)
            temp//=a
        else:
            a+=1

    return suma


for a in range(10**2):

    if suma_cyfr(a) == rozklad_i_suma(a):
        print(a)
