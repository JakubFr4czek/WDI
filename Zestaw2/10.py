def ciag(n):

    if n == 1: return 2
    else: return 3*ciag(n - 1) + 1

n = int(input())

i = 1
while(ciag(i) <= n):
    if n % ciag(i) == 0:
        print("tak")
        exit()

    i+=1
print("nie :(")
