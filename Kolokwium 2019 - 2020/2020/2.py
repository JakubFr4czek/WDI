def to_binary(liczba):

    jedynki = 0

    while liczba > 0:

        if liczba%2 == 1:
            jedynki += 1
        liczba//=2
    if jedynki %2 == 0: return False
    return True

T = [[1,2,3,4], [1,2,3,4], [1,2,3,4], [1,2,3,4]]

N = len(T)

for i in range(N):

    for j in range(N):

        T[i][j] = to_binary(T[i][j])

print(T)

for i in range(N): #ktory wiersz usuwam

    for j in range(N): #ktora kolumne usuwam

        for k in range(N): #ktora druga kolumne usuwam

            if k !=j:
                start = 0
                end = 0
                for q in range(N):

                    for w in range(N):
                        start +=1
                        if q != i and w != k and w != j:
                            
                            if T[q][w] == False:
                                print("CHUUUUJOOOOWOOOOO\n")
                                end +=1
                if end ==0:print("aaqaaa")
        
if start != end:
    print(start, end, "ok")
