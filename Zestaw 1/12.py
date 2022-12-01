def nwd(a, b):

    while b != 0:
        c = b
        b = a % b
        a = c

    return a

a = int(input())
b = int(input())
c = int(input())

print(nwd(nwd(a,b),c))
       