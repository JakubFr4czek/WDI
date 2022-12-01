def maska(liczba,w):

    niezlasumka = 0

    while liczba > 0:

        niezlasumka*=10

        niezlasumka += liczba%w

        liczba//=w

    return niezlasumka


def f(T, S):
    cnt = 0
    for i in range(0, 3**len(T)):
        mask = maska(i,3)
        #print(mask)

        suma = 0

        for i in range(len(T)):

            if mask%10 == 0:
                suma += T[i]
            else:
                suma += S[i]

            mask//=10

        print(suma)
        cnt+=1
    print(cnt)

T = [1,2,3,3,4,2]
S = [3,2,1,2,3,4]

f(T,S)

