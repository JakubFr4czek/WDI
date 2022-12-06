#quicksort

def qs(T,l,p): # qs(T, 0, N - 1)

    i = l
    j = p
    
    s = T[(i + j)//2]

    while i <= j:

        while T[i] < s: i += 1
        while T[j] > s: j -= 1

        if(i <= j):
            T[j], T[i] = T[i], T[j]
            i += 1
            j -= 1

        if(l < j): qs(T, l, j)
        if(i < p): qs(T, i, p) 