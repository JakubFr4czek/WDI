def sprawdz(a, b):

    t1 = [False for _ in range(10)] #0 - 9
    t2 = [False for _ in range(10)] #0 - 9

    while a > 0:
        t1[a%10]=True
        a//=10

    while b > 0:
        t2[b%10]=True
        b//=10

    for i in range(10):
        if t1[i] != t2[i]:
            return False

    return True








T = [[1112,2,3,4,15],
     [1,21,3,4,5],
     [1,2,33,4,5],
     [1,2,3,43,5],
     [1,2,344444,4,1115],]

N = len(T)

for i in range(N):
    for j in range(N):
        for k in range(N):
            for l in range(N):

                if k != i or l != j:

                    if sprawdz(T[i][j], T[k][l]):
                        

                        print(T[i][j], T[k][l]) 
            


 
