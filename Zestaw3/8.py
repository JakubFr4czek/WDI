from random import randint
from math import sqrt


#T = [randint(1,100) for i in range(N)]
T = [85, 6,3,2,1,2,3,4,5,6,7,8,1,2,3,4,5,4]
N = len(T)
print(T)

liczba = T[0]
for i in range(2, int(sqrt(liczba)) + 1 ):
    print(i, N - 1, i == N - 1)
    if liczba %i == 0:
        if i == N - 1:
            print("Piks mega szczęśliwy!!!!")
        liczba//=i

if liczba != 1:
    if liczba == N-1:
        print("Piks jednak hepi")

print("Piks smutny! :(")
