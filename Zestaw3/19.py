
T = [2,1,2,3,4,5,2,1,8,9,10,11,12,13,14,15] 
N = len(T)

maks = 0
sumaIndeksow = 0
sumaLiczb = 0
Licznik = 0

for i in range(N - 1):
    
    if T[i] < T[i + 1]:
        Licznik += 1
        sumaLiczb += T[i]
        sumaIndeksow += i
    else:
        sumaLiczb += T[i]
        sumaIndeksow += i

        if Licznik > maks:
            maks = Licznik

        Licznik = 1
if Licznik > maks:
    maks = Licznik
print(maks)
