T = [[1,2,-1,4,5],
     [1,2,-1,4,5],
     [1,2,-1,4,5],
     [1,2,-1,4,5],
     [1,2,-1,4,2],]


N = len(T)


maks = 0
maks2 = 0

for d in range(1, 11): #wybieram dlugosc podciagu

    for i in range(N):

        for j in range(N):

            suma = 0
            suma2 = 0

            if j + d <= N:

                for k in range(j, j + d):
                    suma += T[i][k]
                    suma2 += T[k][i]

            if suma > maks:
                maks = suma
            if suma2 > maks2:
                maks2 = suma2



print(maks)
print(maks2)




