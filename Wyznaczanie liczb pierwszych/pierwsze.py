import math

def pierwsza(n):

    if n == 2 or n == 3:
        return True

    if n < 2:
        return False

    
    if n % 2 == 0 or n % 3 == 0:
        return False


    a = 5

    while a <= math.sqrt(n):

        if n % a == 0:
            return False

        a += 2

        if n % a == 0:
            return False

        a+=4

    return True







#n = int(input())

for i in range(1000):

    if pierwsza(i):
        print(i)