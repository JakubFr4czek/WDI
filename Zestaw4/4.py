T = [[1,2,3,4,0],
     [1,2,3,4,0],
     [1,2,3,4,1],
     [1,2,3,4,0],
     [1,2,3,4,0],]

N = len(T)

sumyKolumn = [0 for _ in range(N)]
sumyWierszy = [0 for _ in range(N)]

for i in range(N):
    for j in range(N):

        sumyKolumn[i] += T[i][j]
        sumyWierszy[j] += T[i][j]

maks = 0
x = -1
y = -1

print(sumyKolumn)
print(sumyWierszy)

for i in range(N):
    for j in range(N):

        if sumyKolumn[i] / sumyWierszy[j] > maks:
            maks = sumyKolumn[i] / sumyWierszy[j]
            x = i
            y = j

print(x, " ", y)