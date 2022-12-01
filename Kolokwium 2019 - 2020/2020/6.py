
def next(x,y,suma,N):
    if x == N - 1:
        return suma == 0

    for i in range(N):

        if abs(y - i) > 1:
            if next(x + 1, i,suma + T[x + 1][i], N):return True

    return False







T = [[1,2,3,4],
     [1,2,-1,4],
     [1,2,3,4],
     [1,2,-1,4]]

N = len(T)

for i in range(N):

    if next(0, i, T[0][i], N):
        print("OK")
    else:
        print("NOT OK")





