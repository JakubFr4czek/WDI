from math import sqrt

n = int(input())

a = 1
b = 1

while a <= sqrt(n):

    if n % a == 0:

        c = b
        d = a + b

        x = n//a

        while c <= n:

            if c == x:
                print(a, " ", c)
                exit()
            
            c,d = d, c + d
        
    a,b = b,a+b
print("Nie istnieje")