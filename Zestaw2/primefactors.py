from math import sqrt

def prime_factors(n):

    liczba = n
    a = 2

    while a <= sqrt(n):

        while liczba%a == 0:
            print(a)
            liczba//=a
        
        a+=1

    if a != 2 and liczba != n:
        print(liczba)

n = int(input())

prime_factors(n)