n = int(input())

def reverse(a):

    rev = 0

    while a > 0:
        rev *= 10
        rev += a%10
        a=a//10

    return rev

def to_binary(a):

    bin = 2
    
    while a > 0:

        bin*=10

        if(a%2 == 0):
            bin+=0
        else:
            bin+=1

        a//=2

    bin*=10
    bin+=2

    return bin
        


print(to_binary(n))

if n == reverse(n) and to_binary(n) == reverse(to_binary(n)):
    print("SI")
else:
    print("NIE SI")


