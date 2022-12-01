T = [[1,2,3,4,5],
     [1,2,3,4,5],
     [1,2,3,4,5],
     [1,2,3,4,5],
     [1,2,3,4,5],]

N = len(T)

liczba = int(input())

for y in range(N):

    for x in range(N):

        if x + 1 < N and y - 2 >= 0:

            if T[y][x] * T[y - 2][x + 1] == liczba: print("ok")

        if x + 2 < N and y - 1 >= 0:
        
            if T[y][x] * T[y - 1][x + 2] == liczba: print("ok")

        if x - 1 >= 0 and y - 2 >= 0:

            if T[y][x] * T[y - 2][x - 1] == liczba: print("ok")
        
        if x - 2 >= 0 and y - 1 >= 0:

            if T[y][x] * T[y - 1][x - 2] == liczba: print("ok")
        
        if x - 2 >= 0 and y + 1 < N:

            if T[y][x] * T[y + 1][x - 2] == liczba: print("ok")
        
        if x - 1 >= 0 and y + 2 < N:
         
            if T[y][x] * T[y + 2][x - 1] == liczba: print("ok")

        if x +2 < N and y + 1 < N:
        
            if T[y][x] * T[y + 1][x + 2] == liczba: print("ok")
