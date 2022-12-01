T = [2,9,3,1,7,11,9,6,7,7,1,3,9,12,15]
N = len(T)

maxi = -1

for i in range(N):
    for j in range(N-1, -1, -1):

        if T[i] == T[j]:

            current = 1
            k = 1

            while i + k < N and j - k >= 0 and T[i+k] == T[j-k]:
                k+=1
                current+=1
            
            if current > maxi:
                maxi = current

print(maxi)

#łał to kurwa z palca zadzialalo troche w szoku jestem ngl