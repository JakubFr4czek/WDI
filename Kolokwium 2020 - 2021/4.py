from math import sqrt,log10

def sito_eratestonesa(N):

    T = []

    S = [True for _ in range(N + 1)]

    if N > 1:
        S[0] = S[1] = False

    for i in range(2, int(sqrt(N + 1)) + 1):

        if S[i]:

            for j in range(i*i, N, i):
                S[j] = False   

    for i in range(N + 1):

        if S[i]:
            T.append(i)

    return T

def czy_pierwsza(liczba):

    if liczba < 2: return False

    if liczba == 2 or liczba == 3: return True

    if liczba % 2 == 0 or liczba %3 == 0: return False

    a = 5

    while a <= int(sqrt(liczba)) + 1:

        if liczba % a == 0: return False

        a += 2

        if liczba %a == 0: return False

        a+=4

    return True

liczba = int(input())

N = int(log10(liczba)) + 1 #dlugosc liczby

T = sito_eratestonesa(N)

def znajdz_nastepna(liczba, kawalki, length, N):

    i = 1

    while i <= N:
        print(liczba%(10**i))
        if czy_pierwsza((liczba%(10**i))):


            znajdz_nastepna(liczba//(10**i), kawalki+1, length+i, N)
            i += 1
        i += 1


    if length == N and czy_pierwsza(kawalki):
        print("Pikoci :)")
    

znajdz_nastepna(liczba, 0, 0, N)


print("Pikś smutny :(")

        

