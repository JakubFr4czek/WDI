
def nwd(a,b):


    while b != 0:
        pom = b
        b = a%b
        a = pom

    return a

def nww(a,b):
    return a*b // nwd(a,b)

a = int(input())
b = int(input())
c = int(input())

print(nww(nww(a,b),c))