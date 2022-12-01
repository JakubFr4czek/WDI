import math




k = int(input())
len_k = len(str(k))

def cyfry2(liczba):

    Z = [0 for _ in range(len_k)]

    for i in range(1, len_k + 1):
        Z[i - 1] = (liczba%(10**i))//(10**(i-1))
        
    for i in range(len_k):

        for j in range(len_k):

            if(i != j and Z[i] == Z[j]):
                print("duplikaaaT")

    print(Z)



'''
def cyfry(liczba):

    for i in range(1, len_k + 1):


            a = (liczba%10**i)//10**(i - 1)
            
            b = (liczba%10**(len_k - i + 1))//10**(len_k - i)


        print(a," ", b)
    '''
#cyfry2(k)

#it = 0

#T = [0 for _ in range(len_k**2)]

for M in range(len_k+1):
    for N in range(len_k+1):
        if N>=M: continue
        liczba = (k%(10**M))//10**N
        print(M," ",N," ",liczba)

