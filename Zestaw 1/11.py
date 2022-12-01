from math import sqrt

def suma(liczba):

    a = 2
    suma = 0

    while a < sqrt(liczba):
        if liczba % a == 0:
            suma += a + liczba//a
        a+=1

    if a**a == liczba:
        suma += a
    suma += 1
    
    return suma

for i in range(1000000):
    
    a = suma(i)
    if(suma(a) == i and a != i): 
        print(a, " ", i)