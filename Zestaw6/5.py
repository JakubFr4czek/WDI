import math

def is_print(n):

    if n < 2: return False

    if(n == 3 or n == 2): return True

    if(n %2 == 0 or n%3 == 0): return True

    a = 5

    while a <= math.sqrt(n):

        if n%a == 0:
            return False

        a += 2

        if n%a == 0:
            return False

        a += 4

    return True

def binToDec(A, p, k):

    a = 0
    res = 0
    for i in range(k, p - 1, -1):
        
        res += ((2**a)* A[i])
        a += 1
        #print(res)

    return res







T = [1,0,1,1,1,0,0,0,1,1,0,1,0,1]

print(binToDec(T, 0,1))