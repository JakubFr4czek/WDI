from random import randrange



T = [1,1,1,2,3,4,3,2,1,1,4,5]
N=len(T)
print(T)


for i in range(N):

    for j in range(i+2, N):
        a = i
        b = j
        
        while a < b and T[a] == T[b]:
            a += 1
            b -= 1
        if a == b or a > b:
            print(j - i)

        

