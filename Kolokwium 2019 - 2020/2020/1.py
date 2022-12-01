def jest(liczba):

    for a in range(2, int(liczba**(1/2)) + 1):    
        pot = 2

        while a**pot < liczba:

            pot+=1
        if a**pot == liczba: return True
    return False


T1 = [1,1,1,1,1,1,1,1,1,1,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
T2 = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,15,16,17,18,19,20,21,22,23,24,25]

N = len(T1)



for i in range(1, 24):

    # i - dl 1,
    # N - i - dl2

    for j in range(N):

        sum1 = 0

        if j + i <= N:

            for k in range(j, j + i):

                sum1 += T1[k] 

            for j1 in range(N):
                
                sum2 = 0

                if j1 + (24-i) <= N:

                    for k1 in range(j1, j1 + (24-i)):

                        sum2 += T2[k1]
                    if jest(sum1+sum2):
                        print("oko")
                        print(sum1 + sum2)
