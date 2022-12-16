import math

mini = 10**20

def sol(A, k, w = 0, suma = 0,):

    if w == 8:
        global mini
        if suma < mini:
            mini = suma
        return

    #print(w, k)
    suma += A[w][k]

    if k - 1 > 0:
        sol(A, k - 1, w + 1, suma)
    if k + 1 < 8:
        sol(A, k + 1, w + 1, suma)

    sol(A, k, w + 1, suma)



A = [ [1,2,3,4,5,6,7,8],
     [1,2,3,4,5,6,7,8],
     [1,2,3,4,5,6,7,8],
     [1,2,3,4,5,6,7,8],
     [1,2,3,4,5,6,7,8],
     [1,2,3,4,5,6,7,8],
     [1,2,3,4,5,6,7,8],
     [1,2,3,4,5,6,7,8] ]
print(A)

sol(A, 4)

print(mini)