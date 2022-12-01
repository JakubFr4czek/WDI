import math

def czy_iloraz(n):


    a = b = 1

    while a < math.sqrt(n):

        if n % a == 0:

            c ,d = b, a + b
            
            x = n % a

            while c <= n:

                if x * c == n:
                    return True

            c,d = d, c + d
        
        a, b = b, a + b


print(czy_iloraz(5))