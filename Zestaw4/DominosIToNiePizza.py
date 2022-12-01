def nwd(a,b):

    while b > 0:
        a,b = b, a%b

    return a


T = [[1,2,3,4,5],
     [1,2,3,4,5],
     [1,2,3,4,5],
     [1,2,3,4,5],
     [1,2,3,4,5]]

N = len(T)

#ustawiam 1 domino - poziomo

for i in range(N * N):

    y1 = i//N       #zabrioniony wiersz
    x1_1 = i%(N - 1)  #zabrioniona kolumna1
    x1_2 = x1_1 + 1      #zabrioniona kolumna2
    print(x1_1, x1_2)

    for j in range((N *N) - N):

        y2_1 = j//N
        y2_2 = y2_1 + 1
        #print(y2_1, y2_2)
        x2 = j%N


        if y2_1 != y1 and y2_2 != y1 and x2 != x1_1 and x2 != x1_2:

            #print(T[y1][x1_1])
            #print(T[y1][x1_2])
            #print(T[y2_1][x2])
            #print(T[y2_2][x2])

            #if nwd(nwd(T[y1][x1_1], T[y1][x1_2]),nwd(T[y2_1][x2], T[y2_2][x2])) == 1:
             #   print("yelllo, ", T[y1][x1_1], T[y1][x1_2], T[y2_1][x2], T[y2_2][x2])

            a = T[y1][x1_1]
            b = T[y1][x1_2]
            c = T[y2_1][x2]
            d = T[y2_2][x2]

            T[y1][x1_1] = -1
            T[y1][x1_2] = -1
            T[y2_1][x2] = -1
            T[y2_2][x2] = -1

            for x in range(N):
                print(T[x])

            T[y1][x1_1] = a
            T[y1][x1_2] = b
            T[y2_1][x2] = c
            T[y2_2][x2] = d
            print()
        

            

        
