a = int(input())
b = int(input())
n = int(input())

integer = a//b

decimal = (a*(10**n)//b)%10**(n)

print(integer,".",decimal, sep = '')