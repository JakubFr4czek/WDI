

def na4(liczba):

    T = [0 for _ in range(4)]

    while liczba > 0:
        
        T[liczba%4] += 1
        liczba//=4

    return T








a = int(input())
b = int(input())

A = na4(a)
B = na4(b)


print(A)
print(B)

for i in range(4):

    if A[i] == 0 and B[i] != 0 or A[i] == 0 and B[i] != 0:
        print("Piks smutny :(")
        exit()
print("Piks szczęśliwy :)")