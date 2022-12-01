from math import log10

def zamiana(l,b):
    
    a = 0

    while l > 0:

        a*=10
        a += l%b
        l//=b

    return a

def sprawdz(a, b):
    
    N1 = int(log10(a)) + 1
    N2 = int(log10(b)) + 1

    T1 = [-1 for _ in range(N1)]
    T2 = [-1 for _ in range(N2)]

    for i in range(N1):
        T1[i] = a%10
        a//=10

    for i in range(N2):
        T2[i] = b%10
        b//=10

    for i in range(N1):

        for j in range(N2):

            if T1[i] == T2[j]:
                return False

    return True




a = int(input())
b = int(input())


for i in range(2, 17):

    l1 = zamiana(a,i)
    l2 = zamiana(b,i)

    if sprawdz(l1,l2):
        print(l1,l2)
