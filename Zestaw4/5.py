T = [[1,2,2,2],
     [2,3,4,6],
     [1,3,5,6],
     [8,9,10,11]]

N = len(T)

T2 = [-1 for _ in range(N * N)]
it = 0

kolumna = [0 for _ in range(N)] #iterator dla kazdego wiersza


while True:

    #print(kolumna)

    min = 10**20
    ile = 0

    for i in range(N):

        if kolumna[i] < N and T[i][kolumna[i]] < min:
            min = T[i][kolumna[i]]
            ile = 1
        elif kolumna[i] < N and T[i][kolumna[i]] == min:
            ile += 1

    for i in range(N):

        if kolumna[i] < N and T[i][kolumna[i]] == min:

            if ile == 1:
                T2[it] = min
                it += 1
            #print(kolumna[i], N, min)
            while kolumna[i] < N and T[i][kolumna[i]] == min:
                kolumna[i] += 1
                

    cnt = 0

    for i in range(N):
        if kolumna[i] == N:
            cnt += 1

    if cnt == N: break

print(T2)
            
        

    




    

        




print(T2)
