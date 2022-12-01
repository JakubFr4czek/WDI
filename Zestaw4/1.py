N = int(input())

T = [[0 for _ in range(N)] for _ in range(N)]

liczba = 1

x = 0
y = N - 1

while x <= y:

    for a in range(x, y + 1):
        T[x][a] = liczba
        liczba += 1
    for b in range(x + 1, y):
        T[b][y] = liczba
        liczba += 1
    for c in range(y, x, -1):
        T[y][c] = liczba
        liczba += 1
    for d in range(y, x ,-1):
        T[d][x] = liczba
        liczba += 1
    
    x+=1
    y-=1

for i in range(N):
    print(T[i])


