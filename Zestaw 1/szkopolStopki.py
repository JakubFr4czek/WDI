x, k, a = input().split(' ')

x = int(x)
k = int(k)
a = int(a)

x = x%(k+a)
x = x-k

if x<0:
    print(1)
elif (x-a)< 0:
    print(0)