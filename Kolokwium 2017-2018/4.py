def czy_palindrom(a,b, T):

    for k in range((b-a)//2):

        if T[a + k] != T[b - k - 1] or T[a + k] %2 ==0:
            return False

        if (b - a)%2 == 1:
            if T[a + (b - a)//2]%2==0:return False

    return True


T = [1,1,1,2,2,2,3,7,7,9,7,7,3,8]

N = len(T)

for i in range(1, N): #dlugosc

    for j in range(N):

        if j + i <= N:

            if(czy_palindrom(j, j + i, T)):

               print(T[j:j+i])

            

                    

            

