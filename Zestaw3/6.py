from random import randint

def czy_odd_exists(liczba):

    while liczba > 0:
        if (liczba%10)%2 == 1:
            return True
        liczba//=10
    return False

n = int(input())

T = [randint(1, 1000) for _ in range(n)]
print(T)
for i in range(n):

    if czy_odd_exists(T[i]) == False:
        print("Piks smutny")
        exit()

print("Piks szczesliwy")