T = [[1,2,3,4,5],
     [1,2,3,4,5],
     [1,2,3,4,5],
     [1,2,3,4,5],
     [1,2,3,4,5],]

N = len(T)

for i in range(N * N):

    x1 = i//N
    y1 = i%N

    for j in range(N * N):

        x2 = j//N
        y2 = j%N

    if x1 