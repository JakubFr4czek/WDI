def znajdz(liczba):

    a = 1
    b = 1

    suma = 0

    while suma < liczba:
        suma += a
        a,b = b, a+b

    if suma == liczba: return True

    a = b = 1

    while suma > liczba:
        suma -= a
        a,b = b, a+b

    if suma == liczba: return True
    return False


n = int(input())

while znajdz(n) == False:
    n += 1
print(n)