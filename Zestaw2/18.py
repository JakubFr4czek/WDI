
def ciagB(n):
    if n == 0: return 2
    return ciagB(n - 1) + 2 * ciagA(n - 1)

def ciagA(n):

    if n == 0: return 0
    if n == 1: return 1
    return ciagA(n - 1) - ciagB(n - 1) * ciagA(n - 2)

n = int(input())

it = 0

while n == ciagA(it):
    print(ciagB(it))
    it += 1
    n = int(input())