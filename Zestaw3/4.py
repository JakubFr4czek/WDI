

def licz(n):

    e = [0 for _ in range(n)]
    e[0] = 1
    silnia = [0 for _ in range(n)]
    silnia[0] = 1

    silnia = 1
    silnia_cnt = 1

    while True:
        it = 1

        

        silnia*=silnia_cnt
        a = 1
        
        b = silnia



        while it < n and a != 0:

            a*=10

            e[it] += a//b

            a%=b
            it += 1

        silnia_cnt += 1
    for i in range(n-1, 0, -1):

        if(e[i]//10 > 0):
            e[i - 1] += e[i]//10
            e[i] = e[i]%10
    return e


n = int(input())

print(licz(n))