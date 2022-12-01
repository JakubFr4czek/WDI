
def sumy(T):

    N = len(T)

    kolumna = [0 for _ in range(N)]
    wiersz = [0 for _ in range(N)]

    for i in range(N):

        for j in range(N):

            kolumna[i] += T[i][j]
            wiersz[j] += T[i][j] 

    return kolumna, wiersz


def chess(T):

    N = len(T)

    sumyKolumny, sumyWiersz = sumy(T)

    maks = 0
    suma = 0

    for i in range(N):

        for j in range(N):

            for k in range(N):

                for l in range(N):
                    
                    suma = 0

                    if i != k or j != l: 

                        tow1 = (i,j)
                        tow2 = (k,l)

                        suma += sumyKolumny[i] + sumyWiersz[j] + sumyKolumny[k] + sumyWiersz[l] - 2*T[i][j] - 2*T[k][l] - T[i][l] - T[k][j]

                        if i == k:
                            suma -= sumyKolumny[i] + T[i][l] + T[k][j]
                        if j == l:
                            suma -= sumyWiersz[j] + T[i][l] + T[k][j]

                        if suma > maks:
                            maks = suma

                        print("i: ",i," j: ",j," k: ",k, " l: ",l, "suma: ", suma)
    return maks









T = [[1,1,2,3],[-1,3,-1,4], [4,1,5,4], [5,0,3,6]]

print(chess(T))