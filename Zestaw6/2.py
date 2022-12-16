import math

def sol(A, i, s1 = 0, s2 = 0, s3 = 0):

    if i + 1 == len(A):
        return s1 == s2 == s3

    #return sol(A, i + 1, s1 + A[i]....)
    # itd itp 





def prime_factors(n):

    liczba = n

    waga = 0

    a = 2


    while a <= math.sqrt(n):

        if liczba % a == 0:
            waga += 1

        while liczba % a == 0:
            liczba //= a

        a += 1

    if a != 2 and liczba > 1:
        waga += 1

    return waga


tab = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

for i in range(len(tab)):

    tab[i] = prime_factors(tab[i])
