import math

def czy_pierwsza(liczba):

    if liczba < 2:
        return False

    if liczba % 2 == 0 or liczba % 3 == 0:
        return False

    a = 5

    while(a <= math.sqrt(liczba)):

        if(liczba % a == 0):
            return False 
        a+=2

        if(liczba % a == 0):
            return False
        a+=4
    return True

for i in range(100):
    if czy_pierwsza(i):
        print(i)

    