
import math

def is_prime(n):

    if n < 2: return False

    if n == 2 or n == 3: return True

    if n % 2 == 0 or n % 3 == 0: return False

    a = 5

    while a <= math.sqrt(n):

        if n % a == 0: return False

        a += 2

        if n % a == 0: return False

        a += 4


def sol(n, prawo = False): #n - liczba

    if n == 0: return

    #print(n)
    
    if is_prime(n):
       print(n)

    #ide w lewo
    if prawo == False:
        sol(n // 10, prawo)

    #ide w prawo
    sol( n % 10**(int(math.log10(n))), True)

sol(12345)