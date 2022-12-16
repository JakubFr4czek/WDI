
def decToBin(n):

    res = 0
    a = 0

    while n > 0:

        res += (n % 2) * (10 ** a)
        n//=2

        a += 1

    return res


def maska():

    for i in range(2**5):
        print(decToBin(i), i)

maska()