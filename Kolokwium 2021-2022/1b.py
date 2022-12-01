import math

def czy_piersza(liczba):

    if liczba < 2: 
        return False

    if liczba %2 == 0 or liczba %3 == 0:
        return False

    a = 5

    while a < int(math.sqrt(liczba)) + 1:

        if liczba%a == 0:
            return False
        a+=2

        if liczba%a == 0:
            return False
        a+=4

    return True

T = [8, 8, 17, 17, 289, 17, 49143]

N = len(T)

iloczyn = 1

maxiIndex = -1

for i in range(N):

    if czy_piersza(T[i]):
        iloczyn *= T[i]
    elif T[i] == iloczyn:
        maxiIndex = i

if maxiIndex != -1:
    print("Piks szczęśliwy :), pikoooo: ", maxiIndex)
else:
    print("Piko kurwaaaa: None")

