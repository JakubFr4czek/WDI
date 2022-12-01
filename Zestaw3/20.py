from math import sqrt

def prime_factors(liczba):



    for i in range(2, int(sqrt(liczba)) + 1):
        
        if liczba % i == 0:
            liczba//=i
        if liczba % i == 0:
            return False


    return True


T = [2,23,33,35,7,4,6,7,5,11,13,22]
N = len(T)

suma = 1
cnt = 1
maks = 0
for i in range(N):

    suma *= T[i]
    if prime_factors(suma) == True:
        cnt += 1
    elif prime_factors(suma) == False:
        
        if cnt > maks:
            maks = cnt

        j = 0
        while j <= i and prime_factors(suma) is False:
            suma//=T[j]
            cnt -= 1


print(maks)
