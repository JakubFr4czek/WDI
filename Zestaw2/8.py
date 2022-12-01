n = int(input())
def help(l):
    a = b = 1
    s= 0
    while s <= n:
        s += a
        a, b = b, a+b


    a = b = 1

    while s > n:
        
        s -= a
        if s == n:
            return True


        a,b = b, a+b
    return False

while help(n) == False:
    n+=1
print(n)